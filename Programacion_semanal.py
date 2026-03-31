import streamlit as st
from fpdf import FPDF
from datetime import datetime, timedelta
import pandas as pd

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="MHC - Programación de Materiales", layout="wide")


class MHC_PDF(FPDF):
    def header(self):
        # Marco del encabezado
        self.set_line_width(0.5)
        self.rect(10, 10, 260, 25)

        # Título principal
        self.set_font('Arial', 'B', 14)
        self.set_xy(10, 15)
        self.cell(260, 10, "PROGRAMACION SEMANAL DE MATERIALES (ACC)", 0, 0, 'C')

        # Códigos laterales
        self.set_font('Arial', '', 8)
        self.set_xy(230, 12)
        self.cell(35, 5, "Código: F-015 A", 0, 1, 'R')
        self.set_xy(230, 17)
        self.cell(35, 5, "Página 1 de 1", 0, 1, 'R')

    def footer(self):
        self.set_y(-30)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Generado el {datetime.now().strftime("%d/%m/%Y %H:%M")}', 0, 0, 'C')


# --- LÓGICA DE FECHAS (VIERNES PARA LA PRÓXIMA SEMANA) ---
hoy = datetime.now()
# Calculamos el próximo lunes
dias_al_lunes = (7 - hoy.weekday()) % 7
if dias_al_lunes == 0: dias_al_lunes = 7  # Si hoy es lunes, programamos la siguiente
lunes_prox = hoy + timedelta(days=dias_al_lunes)
domingo_prox = lunes_prox + timedelta(days=6)
rango_semana = f"{lunes_prox.day} al {domingo_prox.strftime('%d de %B de %Y')}"

# --- INTERFAZ DE USUARIO (STREAMLIT) ---
st.title("🚜 Sistema de Programación - MHC")
st.info(f"📅 Solicitud para la **Semana del {rango_semana}**")

col1, col2 = st.columns(2)
with col1:
    obra = st.selectbox("Seleccione la Obra", ["CMOP", "MHC NORTE", "MHC SUR", "BOGOTÁ TUBE"])
    responsable = st.text_input("Nombre del Ingeniero Responsable")
with col2:
    codigo_obra = st.text_input("Código de la Obra", value=obra)
    fecha_hoy = st.date_input("Fecha de Solicitud", hoy)

# Lista de los 18 insumos (puedes editar los nombres aquí)
insumos = [
    "ASFALTO NORMALIZADO 60-70", "ASFALTO CAUCHO", "GAS LICUADO DE PETROLEO",
    "ACEITE QUEMADO", "CEMENTO GRIS CONCRETERO A GRANEL", "ACPM PARA PLANTA",
    "PIEDRA RAJON DE 12\" - 8\" - CANTERA (TON)", "ARENA DE RIO (70% NAT - 30% TRIT)",
    "ARENA LAVADA TRITURADA PASA 3/8\"", "GRAVA TRITURADA PASA 1\"",
    "ADITIVO SIKAMENT PH 7000", "SOLUCION DE UREA AL 32.5 (I)"
]

st.subheader("📝 Detalle de Materiales")
st.write("Ingrese las cantidades para los días necesarios:")

datos_finales = []

for item in insumos:
    with st.expander(f"➕ {item}"):
        c1, c2, c3, c4, c5, c6, c7, c8 = st.columns([2, 1, 1, 1, 1, 1, 1, 1])
        unidad = c1.text_input("Unidad", value="KG", key=f"u_{item}")
        l = c2.number_input("Lun", key=f"l_{item}", step=0.1)
        m = c3.number_input("Mar", key=f"m_{item}", step=0.1)
        mi = c4.number_input("Mie", key=f"mi_{item}", step=0.1)
        j = c5.number_input("Jue", key=f"j_{item}", step=0.1)
        v = c6.number_input("Vie", key=f"v_{item}", step=0.1)
        s = c7.number_input("Sab", key=f"s_{item}", step=0.1)