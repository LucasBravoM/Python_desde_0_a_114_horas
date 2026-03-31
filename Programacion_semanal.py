import streamlit as st
from fpdf import FPDF
from datetime import datetime, timedelta


# ==========================================
# 1. CONFIGURACIÓN DEL GENERADOR DE PDF
# ==========================================
class MHC_Report(FPDF):
    def header(self):
        self.set_line_width(0.5)
        self.rect(10, 10, 260, 25)
        self.set_font('Arial', 'B', 12)
        self.set_xy(10, 18)
        self.cell(260, 10, "PROGRAMACION SEMANAL DE MATERIALES (ACC)", 0, 0, 'C')

        self.set_font('Arial', '', 8)
        self.set_xy(220, 12)
        self.cell(40, 5, "Código: F-015 A", 0, 1, 'R')
        self.set_xy(220, 17)
        self.cell(40, 5, "Página 1 de 1", 0, 1, 'R')

    def draw_info_header(self, obra, responsable, fecha_semana):
        self.set_font('Arial', '', 9)
        self.set_y(40)
        self.cell(20, 8, "Fecha:", 0)
        self.cell(50, 8, datetime.now().strftime("%d/%m/%Y"), "B")
        self.set_x(120)
        self.cell(15, 8, "Obra:", 0)
        self.cell(50, 8, obra, "B")
        self.ln(10)

        self.cell(25, 8, "Responsable:", 0)
        self.cell(80, 8, responsable.upper(), "B")
        self.set_x(140)
        self.cell(25, 8, "Semana:", 0)
        self.cell(60, 8, fecha_semana, "B")
        self.ln(15)

    def draw_table(self, datos_materiales):
        w = [90, 15, 18, 18, 18, 18, 18, 18, 18, 29]
        self.set_fill_color(240, 240, 240)
        self.set_font('Arial', 'B', 8)
        headers = ["MATERIAL", "UND", "LUN", "MAR", "MIE", "JUE", "VIE", "SAB", "DOM", "TOTAL"]
        for i in range(len(headers)):
            self.cell(w[i], 7, headers[i], 1, 0, 'C', fill=True)
        self.ln()

        self.set_font('Arial', '', 8)
        for fila in datos_materiales:
            self.cell(w[0], 7, fila['nombre'][:50], 1)
            self.cell(w[1], 7, fila['und'], 1, 0, 'C')
            self.cell(w[2], 7, str(fila['L']), 1, 0, 'C')
            self.cell(w[3], 7, str(fila['M']), 1, 0, 'C')
            self.cell(w[4], 7, str(fila['Mi']), 1, 0, 'C')
            self.cell(w[5], 7, str(fila['J']), 1, 0, 'C')
            self.cell(w[6], 7, str(fila['V']), 1, 0, 'C')
            self.cell(w[7], 7, str(fila['S']), 1, 0, 'C')
            self.cell(w[8], 7, str(fila['D']), 1, 0, 'C')
            self.cell(w[9], 7, str(fila['Total']), 1, 0, 'C')
            self.ln()
