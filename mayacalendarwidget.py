#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#mayacalendarwidget.py
# Monkey Python Coding Circus by Alan.RG Systemas & Team Cangurera c.2026
import os, sys
from datetime import date
from qt_compat import (
    QWidget, QTimer, QPainter, QColor, QFont, QPixmap, QApplication,QBrush  )

from operadorcalendaricomaya import OperadorCalendarioMaya

class MayaCalendarWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))

        #Definimos las rutas de los recursos (imágenes de las ruedas)
        self .ResourcesFolder ="Recursos"
        self .ResourcesPath =os .path .join (self .scriptDir ,self .ResourcesFolder )
        self .text_backgrounds_opacity = 137

        # No hace falta instanciar porque usamos classmethods
        # self.operador = OperadorCalendarioMaya()  <-- BORRADO
        
        self.last_day = None
        self.angle_13 = 0
        self.angle_20 = 0
        self.day_number = 4
        self.day_name = "Ajaw"
        self.haab_day = 8
        self.haab_month = "Kumk'u"
        self.baktun = 13
        self.katun = 0
        self.tun = 0
        self.winal = 0
        self.kin = 0
        self.load_default_wheelstheme()
        self.timer = QTimer(self)
        self.timer.timeout.connect(
            self.update_wheels
        )
        self.timer.start(1000)
        self.update_wheels()

    def load_default_wheelstheme(self):
        """ Carga las imágenes de las ruedas desde el directorio de recursos. """        
        self.wheel_13 = QPixmap(os.path.join(self.ResourcesPath,"rueda13.png"))
        self.wheel_20 = QPixmap(os.path.join(self.ResourcesPath,"rueda20.png"))

    def update_wheels(self):
        hoy = date.today()

        if hoy == self.last_day:
            return
        self.last_day = hoy

        # CAMBIO 1: .hoy() no existe, se llama .today()
        # CAMBIO 2: devuelve un objeto EstadoMaya, no un dict
        estado = OperadorCalendarioMaya.today()

        # CAMBIO 3: Acceder con .atributo en vez de ["key"]
        self.day_number = estado.tzolkin_number
        self.day_name = estado.tzolkin_name

        self.haab_day = estado.haab_day
        self.haab_month = estado.haab_month

        self.baktun = estado.baktun
        self.katun = estado.katun
        self.tun = estado.tun
        self.winal = estado.winal  # CAMBIO 4: era "uinal", tu dataclass usa "winal"
        self.kin = estado.kin

        # CAMBIO 5: ya tenés los ángulos calculados en el dataclass
        self.angle_13 = estado.angle_13
        self.angle_20 = estado.angle_20
        self.update()

    def resizeEvent(self, event):
        self.viewport_x = self.width() // 2
        self.viewport_y = self.height() // 2
        super().resizeEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(
            QPainter.Antialiasing
        )

        painter.fillRect(
            self.rect(),
            QColor("#000000")
        )

        cx = self.viewport_x
        cy = self.viewport_y

        self.draw_wheel(
            painter,
            self.wheel_13,
            self.angle_13,
            cx - 320,
            cy
        )

        self.draw_wheel(
            painter,
            self.wheel_20,
            self.angle_20,
            cx + 250,
            cy
        )

        self.display_day_info(
            painter,
            cx,
            cy
        )

    def draw_wheel(self, painter, pixmap, angle, x, y):
        if pixmap.isNull():
            return
        painter.save()
        painter.translate(x, y)
        painter.rotate(angle)
        w = pixmap.width()
        h = pixmap.height()
        painter.drawPixmap(-w // 2, -h // 2, pixmap)
        painter.restore()
    
    ''' Nova Original
    def display_day_info(
            self,
            painter,
            cx,
            cy
        ):

        painter.setPen(
            QColor(255, 255, 255)
        )

        painter.setFont(
            QFont(
                "DejaVu Sans Mono",
                28
            )
        )

        painter.drawText(
            cx + 150,
            cy,
            f"{self.day_number} {self.day_name}"
        )

        painter.setFont(
            QFont(
                "DejaVu Sans Mono",
                16
            )
        )

        painter.drawText(
            40,
            50,
            f"Cuenta Larga: "
            f"{self.baktun}."
            f"{self.katun}."
            f"{self.tun}."
            f"{self.winal}."
            f"{self.kin}"
        )

        painter.drawText(
            40,
            80,
            f"Tzolk'in: "
            f"{self.day_number} "
            f"{self.day_name}"
        )

        painter.drawText(
            40,
            105,
            f"Haab': "
            f"{self.haab_day} "
            f"{self.haab_month}"
        )
    '''

    ''' Leo Floating Texts
    def display_day_info(self, painter, cx, cy):
        painter.setPen(QColor(255, 255, 255))
        
        # --- Configuración para el texto flotante (Día Principal) ---
        font_main = QFont("DejaVu Sans Mono", 28)
        painter.setFont(font_main)
        
        text_main = f"{self.day_number} {self.day_name}"
        
        # 1. Calcular el tamaño real del texto a dibujar
        metrics = painter.fontMetrics()
        text_rect = metrics.boundingRect(text_main)
        text_w = text_rect.width()
        text_h = text_rect.height()
        
        # 2. Definir márgenes desde los bordes del viewport
        margin_right = 40  # Pixeles desde la derecha
        margin_bottom = 40 # Pixeles desde abajo
        
        # 3. Calcular coordenadas X e Y para la esquina inferior derecha
        # X: Ancho total - margen derecho - ancho del texto
        pos_x = self.width() - margin_right - text_w
        
        # Y: Alto total - margen inferior (ajustado por la altura de la fuente para baseline)
        # Nota: drawText usa la baseline, así que restamos un poco más para que visualmente quede pegado
        pos_y = self.height() - margin_bottom 
        
        # 4. Dibujar el texto en la posición calculada
        painter.drawText(pos_x, pos_y, text_main)

        # --- Configuración para los datos secundarios (Izquierda Superior - Sin cambios lógicos) ---
        font_small = QFont("DejaVu Sans Mono", 16)
        painter.setFont(font_small)
        
        # Estos ya están posicionados con coordenadas fijas (40, 50), lo cual está bien para la esquina superior izquierda
        painter.drawText(40, 50, f"Cuenta Larga: {self.baktun}.{self.katun}.{self.tun}.{self.winal}.{self.kin}")
        painter.drawText(40, 80, f"Tzolk'in: {self.day_number} {self.day_name}")
        painter.drawText(40, 105, f"Haab': {self.haab_day} {self.haab_month}")   
    '''

    # Ei2 Overlays
    def display_day_info(self, painter, cx, cy):
        # Set text color to white for all texts
        painter.setPen(QColor(255, 255, 255))
        
        # Define a common padding for the background boxes
        bg_padding = 8
        
        # --- Configuration for floating text (Main Day - Lower Right) ---
        font_main = QFont("DejaVu Sans Mono", 28)
        painter.setFont(font_main)
        
        text_main = f"{self.day_number} {self.day_name}"
        
        # 1. Calculate the real size of the text to be drawn
        metrics_main = painter.fontMetrics()
        text_w_main = metrics_main.horizontalAdvance(text_main)
        text_h_main = metrics_main.height()
        ascent_main = metrics_main.ascent()
        
        # 2. Define margins from the viewport edges
        margin_right = 40  
        margin_bottom = 40 
        
        # 3. Calculate X and Y coordinates for the lower right position
        # The padding is added to the base position.
        pos_x_main = self.width() - margin_right - text_w_main - bg_padding
        pos_y_main = self.height() - margin_bottom 
        
        # Draw background box for main text (semi-transparent black)
        # The box covers the text height and the left/right padding.
        bg_rect_main = metrics_main.boundingRect(text_main).adjusted(-bg_padding, 0, bg_padding, 0)
        # Correct the rect coordinates for drawing position
        bg_rect_main.moveTo(pos_x_main, pos_y_main - ascent_main)
        painter.fillRect(bg_rect_main, QBrush(QColor(0, 0, 0, self.text_backgrounds_opacity))) # 160/255 transparency
        
        # 4. Draw the main text
        painter.drawText(pos_x_main + bg_padding, pos_y_main, text_main)

        # --- Configuration for secondary data (Top Left) ---
        font_small = QFont("DejaVu Sans Mono", 16)
        painter.setFont(font_small)
        metrics_small = painter.fontMetrics()
        ascent_small = metrics_small.ascent()
        text_h_small = metrics_small.height()
        
        # Define left margin for the top-left text block
        margin_left = 40
        
        # Text line 1: Cuenta Larga
        text_small_1 = f"Cuenta Larga: {self.baktun}.{self.katun}.{self.tun}.{self.winal}.{self.kin}"
        text_w_small_1 = metrics_small.horizontalAdvance(text_small_1)
        
        # Position for line 1
        pos_x_small = margin_left
        pos_y_small_1 = 50
        
        # Draw background box for text 1
        bg_rect_small_1 = metrics_small.boundingRect(text_small_1).adjusted(-bg_padding, 0, bg_padding, 0)
        bg_rect_small_1.moveTo(pos_x_small - bg_padding, pos_y_small_1 - ascent_small)
        painter.fillRect(bg_rect_small_1, QBrush(QColor(0, 0, 0, self.text_backgrounds_opacity)))
        
        # Draw text 1
        painter.drawText(pos_x_small, pos_y_small_1, text_small_1)
        
        
        # Text line 2: Tzolk'in
        text_small_2 = f"Tzolk'in: {self.day_number} {self.day_name}"
        text_w_small_2 = metrics_small.horizontalAdvance(text_small_2)
        
        # Position for line 2
        pos_y_small_2 = 80
        
        # Draw background box for text 2
        bg_rect_small_2 = metrics_small.boundingRect(text_small_2).adjusted(-bg_padding, 0, bg_padding, 0)
        bg_rect_small_2.moveTo(pos_x_small - bg_padding, pos_y_small_2 - ascent_small)
        painter.fillRect(bg_rect_small_2, QBrush(QColor(0, 0, 0, 160)))
        
        # Draw text 2
        painter.drawText(pos_x_small, pos_y_small_2, text_small_2)
        
        
        # Text line 3: Haab'
        text_small_3 = f"Haab': {self.haab_day} {self.haab_month}"
        text_w_small_3 = metrics_small.horizontalAdvance(text_small_3)
        
        # Position for line 3
        pos_y_small_3 = 105
        
        # Draw background box for text 3
        bg_rect_small_3 = metrics_small.boundingRect(text_small_3).adjusted(-bg_padding, 0, bg_padding, 0)
        bg_rect_small_3.moveTo(pos_x_small - bg_padding, pos_y_small_3 - ascent_small)
        painter.fillRect(bg_rect_small_3, QBrush(QColor(0, 0, 0, 160)))
        
        # Draw text 3
        painter.drawText(pos_x_small, pos_y_small_3, text_small_3)

if __name__ == "__main__":
    app = QApplication([])
    window = MayaCalendarWidget()
    window.show()
    app.exec_()