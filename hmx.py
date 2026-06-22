#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#hmx.py
# Monkey Python Coding Circus by Alan.RG Systemas & Team Cangurera
'''
21/03/2025 (Edit from same archive .py is only for high python skills) // add extreme full animations & transparencias!
Co-created by NOvaPythonistaPythoniza & MOnkey Python Coding Circus by Alan.R.G. Systemas
'''
import sys, os
os.environ["QT_LOGGING_RULES"] = "qt.qpa.xcb=false"
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGraphicsOpacityEffect,
    QTableWidget, QTableWidgetItem, QMessageBox, QMenu, QMenuBar, QAction, QLabel
)
from PyQt5 import QtGui
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, Qt, QRect, QTimer, QThread, pyqtSignal

from PyQt5.QtGui import QTextOption

class ScrollThread(QThread):
    # Señal para actualizar la posición de la barra de desplazamiento
    update_scroll = pyqtSignal()

    def __init__(self, table):
        super().__init__()
        self.table = table
        self.running = True

    def run(self):
        while self.running:
            self.update_scroll.emit()
            self.msleep(113)  # Esperar 100ms entre actualizaciones del scroll

    def stop(self):
        self.running = False

class MatrixUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HMX - Histories Matrix Xubuntu Beta Testing - Historial de Comandos")
        self.setGeometry(100, 100, 920, 800)
        self.matrix_mode = "xtreme" #Init Mode for Humans Impact

        # Icono de aplicación
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.IconPath = os.path.join(scriptDir, 'icons')   
        self.setWindowIcon(QtGui.QIcon(self.IconPath + os.path.sep + 'histories.png'))

        self.trans_esp()

        # Create the main layout
        self.layout = QVBoxLayout()

        self.initMenuBar()
        self.initUI()
        self.load_history()
        
        # Setting the main layout
        self.setLayout(self.layout)
        
        self.apply_styles("matrix")

        # Iniciar el hilo para el desplazamiento automático
        self.scroll_thread = ScrollThread(self.table)
        self.scroll_thread.update_scroll.connect(self.scroll_table)
        self.scroll_thread.start()

        #self.setup_animations()
        
        #self.terminal_scrub() #bloqueaba la tarminal en el modo demo
        self.init_command() #Inicio MAtrix Xtreme Mode

    def trans_esp(self):
        # Especial UI transparente
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)  # siempre arriba
        self.setAttribute(Qt.WA_TranslucentBackground)  # Fondo transparente
        self.setAttribute(Qt.WA_TransparentForMouseEvents)  # Clicks pasan a través de la parte transparente

        # Hacer que los widgets sean transparentes
        transparent_palette = QtGui.QPalette()
        transparent_palette.setColor(QtGui.QPalette.Base, Qt.transparent)
        transparent_palette.setColor(QtGui.QPalette.Window, Qt.transparent)
        self.setPalette(transparent_palette)

    def initUI(self):
        # Campo de búsqueda
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Buscar en historial...")
        self.search_bar.textChanged.connect(self.filter_commands)
        self.layout.addWidget(self.search_bar)

        # Tabla de historial
        self.table = QTableWidget(self)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        # Formado de tabla
        self.table_mode_formating()
        
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.layout.addWidget(self.table)

        # Campo para escribir comandos manuales
        self.manual_command = QLineEdit(self)
        self.manual_command.setPlaceholderText("Escribí un comando para ejecutarlo directamente...")
        self.manual_command.returnPressed.connect(self.execute_command)
        self.layout.addWidget(self.manual_command)

        # Llena el campo de comandos manuales con la seleccion realizada en la tabla
        self.table.cellClicked.connect(self.fill_command_field)

        # Botón inicio Terminal Basica
        self.init_basic_mode_button = QPushButton("Iniciar Terminal Modo Básico", self)
        self.init_basic_mode_button.clicked.connect(self.init_command_basic_mode)
        self.init_basic_mode_button.setFixedSize(350,50)
        self.init_basic_mode_button.move(int(self.width()/2)-175,int(self.height()/2)-85)

        # Botón inicio Terminal
        self.init_button = QPushButton("Iniciar Terminal Modo Extremo", self)
        self.init_button.clicked.connect(self.init_command)
        self.init_button.setFixedSize(350,50)
        #self.layout.addWidget(self.init_button)
        self.init_button.move(int(self.width()/2)-175,int(self.height()/2)-15)

        # Botón para ejecutar comandos
        self.execute_button = QPushButton("Ejecutar en Terminal", self)
        self.execute_button.clicked.connect(self.execute_command)
        self.execute_button.setFixedSize(350,50)
        self.layout.addWidget(self.execute_button)
        #self.execute_button.move(11,339)
        alto = self.height()
        destino = alto - 61
        self.execute_button.move(11,destino)

    def table_mode_formating(self):
        # Formatea la tabla en funcion del modo
        # matrix_mode eval
        if self.matrix_mode == "basic":
            self.table.setColumnCount(1)
            self.table.verticalHeader().setVisible(False)
            self.table.horizontalHeader().setVisible(True)
            self.table.setHorizontalHeaderLabels(["Histories of Command's"])
            self.table.setSelectionBehavior(QTableWidget.SelectRows)
            #self.table.setColumnWidth(0, 840)  # Ajustar el ancho de la columna
            self.table.horizontalHeader().setStretchLastSection(True)
        elif self.matrix_mode == "xtreme":
            self.table.setRowCount(1)
            self.table.verticalHeader().setVisible(False)
            self.table.horizontalHeader().setVisible(False)
            self.table.setSelectionBehavior(QTableWidget.SelectColumns)
            self.table.horizontalHeader().setStretchLastSection(False)
        else:
            print(f"Modo {self.matrix_mode} no Valido")
            return  # Si el modo no es válido, salir de la función

    def toggle_ui_elements(self, disable: bool):
        """Función genérica para bloquear o desbloquear los elementos de la UI."""
        self.init_basic_mode_button.setVisible(disable)
        self.init_button.setVisible(disable)
        self.search_bar.setEnabled(not disable)
        self.table.setEnabled(not disable)
        self.manual_command.setEnabled(not disable)
        self.execute_button.setEnabled(not disable)

    def terminal_scrub(self):
        """Bloquea los elementos de la interfaz."""
        self.toggle_ui_elements(True)
        self.setup_animations()
        if self.init_button.isVisible():
            self.init_basic_mode_button.move(int(self.width()/2)-175,int(self.height()/2)-85)
            self.init_button.move(int(self.width()/2)-175,int(self.height()/2)-15)

    def init_command(self):
        """Desbloquea los elementos de la interfaz."""
        self.toggle_ui_elements(False)
        self.xtreme()

    def init_command_basic_mode(self):
        """Desbloquea los elementos de la interfaz."""
        self.toggle_ui_elements(False)
        self.basic()

    def fill_command_field(self, row, column):
        # matrix_mode eval
        if self.matrix_mode == "basic":
            command = self.table.item(row, column).text()
        elif self.matrix_mode == "xtreme":
            # Crear una variable para almacenar el comando completo
            command = ""
            # Iterar sobre todas las filas de la columna seleccionada
            for row in range(self.table.rowCount()):
                item = self.table.item(row, column)  # Obtener el item en la fila y columna seleccionada
                if item:  # Verifica si el item existe
                    command += item.text()  # Concatenar el texto de cada celda en la columna
        else:
            return  # Si el modo no es válido, salir de la función        
        # Establecer el comando reconstruido en el campo de texto
        self.manual_command.setText(command)

    def initMenuBar(self):
        # Crear la barra de menú
        menubar = QMenuBar(self)
        
        menuz = QMenu("App", self)
        menum = QMenu("Matrix Mode", self)
        
        ayuda_action = QAction("Ayuda", self)
        ayuda_action.triggered.connect(self.ayuda)

        scrub_action = QAction("Bloquear Terminal", self)
        scrub_action.triggered.connect(self.terminal_scrub)

        quit_action = QAction("Salir", self)
        quit_action.triggered.connect(QApplication.instance().quit)
        
        menuz.addSeparator()
        menuz.addAction(ayuda_action)
        menuz.addAction(scrub_action)
        menuz.addSeparator()
        menuz.addAction(quit_action)
        menubar.addMenu(menuz)
        
        self.xtreme_action = QAction("Extremo", self)
        self.xtreme_action.setCheckable(True)
        self.xtreme_action.setChecked(True)
        self.xtreme_action.triggered.connect(self.xtreme)
        self.basic_action = QAction("Básico", self)
        self.basic_action.setCheckable(True)
        self.basic_action.setChecked(False)
        self.basic_action.triggered.connect(self.basic)

        menum.addAction(self.xtreme_action)
        menum.addAction(self.basic_action)
        menubar.addMenu(menum)
        
        self.layout.addWidget(menubar)

    def basic(self):
        self.matrix_mode = "basic"
        #print(f"#set mode: {self.matrix_mode}")
        self.xtreme_action.setChecked(False)
        self.basic_action.setChecked(True)
        self.reload_and_filter()

    def xtreme(self):
        self.matrix_mode = "xtreme"
        #print(f"#set mode: {self.matrix_mode}")
        self.xtreme_action.setChecked(True)
        self.basic_action.setChecked(False)
        self.reload_and_filter()

    def reload_and_filter(self):
        self.table_mode_formating()
        self.load_history()
        self.filter_commands()
        self.setup_animations()

    def ayuda(self):
        QMessageBox.information(self, "Ayuda", "¿En qué puedo ayudarte yo cuando solo Dios puede ayudarte?")
        return #linea 274
    
    def load_history(self):
        history_file = os.path.expanduser("~/.bash_history")
        if os.path.exists(history_file):
            with open(history_file, "r", encoding="utf-8", errors="ignore") as file:
                self.commands = list(set(file.read().splitlines()))[::-1]  # Elimina duplicados y ordena
        else:
            self.commands = []
        # matrix_mode eval
        if self.matrix_mode == "basic":
            self.populate_table(self.commands)
        elif self.matrix_mode == "xtreme":
            self.populate_table_transposed(self.commands) # Extreme Matrix Mode
        else:
            print(f"Modo {self.matrix_mode} no Valido")
            return  # Si el modo no es válido, salir de la función

    def populate_table(self, command_list):
        self.table.setRowCount(len(command_list))
        for row, command in enumerate(command_list):
            self.table.setItem(row, 0, QTableWidgetItem(command))

    def populate_table_transposed(self, command_list):
        max_length = max(len(command) for command in command_list) + 1 # MAGIA! Encuentra el largo máximo de los comandos para determinar las filas    
        self.table.setColumnCount(len(command_list)) # Establecer el número de columnas como el número de comandos
        self.table.setRowCount(max_length) # Establecer el número de filas como la longitud máxima de los comandos
        # Poblar la tabla con los caracteres transpuestos
        for col, command in enumerate(command_list):
            for row in range(max_length):
                if row < len(command):
                    char = command[row]  # Caracter en la fila correspondiente
                else:
                    char = ''  # Vacío si el comando es más corto que la longitud máxima
                self.table.setItem(row, col, QTableWidgetItem(char))
        # Ajustar el ancho de las columnas para que cada una tenga el ancho de un solo carácter
        for col in range(len(command_list)):
            self.table.setColumnWidth(col, 20)  # Ajustar a un ancho pequeño
        self.table.resizeColumnsToContents()
    
    def filter_commands(self):
        query = self.search_bar.text().strip().lower()
        filtered = [cmd for cmd in self.commands if query in cmd.lower()]
        if len(filtered) == 0: #(MAgia: Quitando un Error Generé una Util Funcion!!!)
            QMessageBox.information(self, "Filtro Extremo", "No es posible encontrar esa cadena de caracteres en la lista de comandos!!!")
        # matrix_mode eval
        if self.matrix_mode == "basic":
            self.populate_table(filtered)
        if self.matrix_mode == "xtreme" and (len(filtered) > 0): # Parte de la MAGIA antes era elif (¿el de la Novela?)
            self.populate_table_transposed(filtered) # Extreme Matrix Mode
        #else:
            #print(f"Modo {self.matrix_mode} no Valido")
            #return  # Si el modo no es válido, salir de la función

    def execute_command(self):
        command = self.manual_command.text().strip()  # Comando manual
        if not command:  # Si no hay comando manual, tomamos el del historial
            selected = self.table.currentRow()
            if selected >= 0:
                command = self.table.item(selected, 0).text()
            else:
                QMessageBox.warning(self, "Atención", "Seleccioná un comando o escribí uno manualmente.")
                return
        
        if command not in self.commands:
            self.commands.insert(0, command)  # Lo agrega al inicio del historial
            self.populate_table(self.commands)

        # Reemplazamos comillas dobles por simples
        command = command.replace('"', "'")
        
        # Ejecutamos el comando en consola limpiandola primero
        #os.system(f'xfce4-terminal --working-directory=$HOME -e "bash -c \\"clear; {command}; exec bash\\""')

        # Ejecutamos el comando en consola no interactiva
        #os.system(f'xfce4-terminal --working-directory=$HOME -e "bash -c \\"{command}; exec bash\\""')
        
        # Ejecutamos el comando en consola interactiva
        #os.system(f'xfce4-terminal --working-directory=$HOME -e "bash -ic \\"clear; {command}; exec bash\\""')
        os.system(f'xfce4-terminal --working-directory=$HOME -e "bash -ic \\"clear; {command}; echo -e \'\\nComando Ejecutado desde HMX32\'; exec bash\\""')

        # Ejecutamos el comando en consola escapando del .bashrc
        #os.system(f'xfce4-terminal --working-directory=$HOME -e "bash --noprofile --norc -c \\"{command}; exec bash\\""')
        
        # Ejecutamos el comando en consola escapando del .bashrc con un flag
        #os.system(f'xfce4-terminal --working-directory=$HOME -e "bash --noprofile --norc -c \\"export APP_RUNNING=true; {command}; exec bash\\""')

    def apply_styles(self, mode):
        """ Aplica hoja de estilos """
        self.current_style = mode  # Guardamos el nombre del estilo aplicado
        styles = {
            "matrix": """
                QWidget {
                    background-color: rgba(0, 0, 0, 0.7);
                    color: #00ff00;
                    font-family: "Courier New", monospace;
                }
                QLabel {
                    font-size: 18px;
                    font-weight: bold;
                    color: #00ff00;
                }
                QLineEdit {
                    background-color: rgba(0, 26, 0, 0.6);
                    border: 2px solid #00ff00;
                    padding: 5px;
                    color: #00ff00;
                    selection-background-color: rgba(0, 51, 0, 0.6);
                }
                QPushButton {
                    background-color: rgba(0, 51, 0, 0.6);
                    color: #00ff00;
                    border: 2px solid #00ff00;
                    padding: 8px;
                    font-size: 16px;
                }
                QPushButton:hover {
                    background-color: rgba(0, 85, 0, 0.6);
                }
                QTextEdit {
                    background-color: rgba(0, 0, 0, 0.7);
                    color: #00ff00;
                    border: 1px solid #00ff00;
                    font-family: "Courier New", monospace;
                }
                QScrollBar:vertical {
                    border: none;
                    background: rgba(0, 0, 0, 0.8);
                    width: 10px;
                }
                QScrollBar::handle:vertical {
                    background: rgba(0, 255, 0, 0.8);
                    min-height: 20px;
                }
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    background: none;
                }
                QMenuBar {
                    background-color: rgba(0, 0, 0, 0.8);
                    color: #00aa00;
                }
                QMenuBar::item {
                    background: transparent;
                }
                QMenuBar::item:selected {
                    background: rgba(0, 51, 0, 0.6);
                    color: #00ff00;
                }
                QMenu {
                    background-color: rgba(0, 26, 0, 0.7);
                    color: #00aa00;
                    selection-background-color: rgba(0, 51, 0, 0.7);
                    border: 1px solid #00ff00;
                }
                QMenu::item:selected {
                    color: #00ff00;
                    background-color: rgba(0, 51, 0, 0.7);
                }
            """,


            "matrix2": """
                QWidget {
                    background-color: #000000;
                    color: #00ff00;
                    font-family: "Courier New", monospace;
                }
                QLabel {
                    font-size: 18px;
                    font-weight: bold;
                    color: #00ff00;
                }
                QLineEdit {
                    background-color: #001a00;
                    border: 2px solid #00ff00;
                    padding: 5px;
                    color: #00ff00;
                    selection-background-color: #003300;
                }
                QPushButton {
                    background-color: #003300;
                    color: #00ff00;
                    border: 2px solid #00ff00;
                    padding: 8px;
                    font-size: 16px;
                }
                QPushButton:hover {
                    background-color: #005500;
                }
                QTextEdit {
                    background-color: #000000;
                    color: #00ff00;
                    border: 1px solid #00ff00;
                    font-family: "Courier New", monospace;
                }
                QScrollBar:vertical {
                    border: none;
                    background: #000000;
                    width: 10px;
                }
                QScrollBar::handle:vertical {
                    background: #00ff00;
                    min-height: 20px;
                }
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    background: none;
                }
                QMenuBar {
                    background-color: black; 
                    color: #00aa00;
                }
                QMenuBar::item {
                    background: transparent;
                }
                QMenuBar::item:selected { 
                    background: #003300;
                    color: #00ff00;
                }
                QMenu {
                    background-color: #001a00;
                    color: #00aa00;
                    selection-background-color: #003300;
                    border: 1px solid #00ff00;
                }
                QMenu::item:selected {
                    color: #00ff00;
                    background-color: #003300;
                }
            """
        }
        self.setStyleSheet(styles.get(mode, styles["matrix"]))

    def setup_animations(self):
        """ Configura los efectos y animaciones """
        if self.matrix_mode == "xtreme": # si pasamos a modo xtreme
            # Fade-in self.manual_command
            self.fade_in()
            # Animación de botón al entrar en escena 
            self.move_button(self.execute_button)
        # Registrar elementos en el event filter
        self.manual_command.installEventFilter(self) # Efecto parpadeo al hacer foco en manual_command
        self.search_bar.installEventFilter(self) # Efecto parpadeo al hacer foco en search_bar
        self.table.installEventFilter(self)  # <-- Agregamos la tabla al eventFilter

    def move_button(self, boton):
        """ Animación de botón """
        self.button_animation = QPropertyAnimation(boton, b"geometry")
        self.button_animation.setDuration(1200)
        self.button_animation.setStartValue(boton.geometry().translated(900, 0))
        self.button_animation.setEndValue(boton.geometry())
        self.button_animation.setEasingCurve(QEasingCurve.OutBounce)
        self.button_animation.start()

    def eventFilter(self, obj, event):
        """ Detecta el foco en los elementos y activa el parpadeo """
        if event.type() == event.FocusIn and obj in {self.manual_command, self.search_bar, self.table}:
            self.blink_effect(obj)
        return super().eventFilter(obj, event)

    def blink_effect(self, widget):
        """ Efecto de parpadeo verde """
        if widget == self.table:
            colors = [
                "color: #00bf00; background-color: #001000; border: 2px solid #001200; selection-background-color: #001a00; selection-color: #00df00;",
                "color: #00ff00; background-color: #001a00; border: 2px solid #001300; selection-background-color: #003300; selection-color: #00ff00;",
                "color: #00bf00; background-color: #001000; border: 2px solid #001200; selection-background-color: #001a00; selection-color: #00df00;",
                "color: #00ff00; background-color: #001a00; border: 2px solid #001300; selection-background-color: #003300; selection-color: #00ff00;"
            ]
            current_style = colors[self.blink_index % len(colors)]
            self.table.setStyleSheet(current_style + " selection-background-color: #003300; selection-color: #00ff00;")    
        else:
            colors = [
                "color: #00bf00; background-color: #001a00; border: 2px solid #00df00;",
                "color: #00ff00; background-color: #003300; border: 2px solid #00ff00;",
                "color: #00bf00; background-color: #001a00; border: 2px solid #00df00;",
                "color: #00ff00; background-color: #003300; border: 2px solid #00ff00;"
            ]
        self.blink_index = 0
        def toggle():
            widget.setStyleSheet(colors[self.blink_index])
            self.blink_index = 1 - self.blink_index
        self.blink_timer = QTimer()
        self.blink_timer.timeout.connect(toggle)
        self.blink_timer.start(50)  # Parpadeo cada 50ms
        QTimer.singleShot(250, self.blink_timer.stop)  # Detener tras 5 parpadeos

    def fade_in(self):
        """Efecto de aparición gradual"""
        self.opacity_effect = QGraphicsOpacityEffect()
        self.manual_command.setGraphicsEffect(self.opacity_effect)
        self.fade_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.fade_animation.setDuration(2000)
        self.fade_animation.setStartValue(0)  # Empieza invisible
        self.fade_animation.setEndValue(1)  # Aparece gradualmente
        self.fade_animation.start()

    def scroll_table(self):
        """ Controla el desplazamiento de la tabla según el modo activo """
        if self.matrix_mode == "basic":
            # Scroll horizontal (loop de derecha a izquierda)
            scroll_bar = self.table.horizontalScrollBar()
        elif self.matrix_mode == "xtreme":
            # Scroll vertical (loop de abajo hacia arriba)
            scroll_bar = self.table.verticalScrollBar()
        else:
            print(f"Modo {self.matrix_mode} no Valido")
            return  # Si el modo no es válido, salir de la función
        direction = -1 # Arriba
        current_value = scroll_bar.value()
        max_value = scroll_bar.maximum()
        # Si llegamos al extremo, volvemos al otro lado
        if current_value == 0:
            scroll_bar.setValue(max_value)
        else:
            scroll_bar.setValue(current_value + direction)

    def closeEvent(self, event):
        # Detener el hilo al cerrar la ventana
        self.scroll_thread.stop()
        self.scroll_thread.wait()
        event.accept()

    def resizeEvent(self, event):
        if self.init_button.isVisible():
            self.init_basic_mode_button.move(int(self.width()/2)-175,int(self.height()/2)-85)
            self.init_button.move(int(self.width()/2)-175,int(self.height()/2)-15)
        event.accept()

if __name__ == "__main__":
    app = QApplication([])
    window = MatrixUI()
    window.show()
    app.exec_()
