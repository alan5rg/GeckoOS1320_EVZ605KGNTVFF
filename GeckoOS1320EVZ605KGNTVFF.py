#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#GeckoOS1320.EVZX.XX.py
revision = "[EVZ605KGNTVFF]" #.21062026.00:47 ANOTHER DAY OF CONSCIOUSNESS /// Enfoque del Chamahán Nahual Gecko
# Monkey Python Coding Circus by Alan.RG Systemas & Team Cangurera c.2026
# Mackeniguem ash Gecko OS to transform any Computer into an Gecko System TM
"""
TODO locals al 22/06/26 00:50. (FF) FILA FILTRADA : EN GITHUB COMO HUELLA DE GECKO EN EL CIBERESPACIO 🦎✨
     locals al 21/06/26 20:23. (no FF) No entiendo esa notacion de tiempo pero paso poco. [Esto se puede automatizar. se debe automatizar... ]
"""
# --------------------------------------------------------------------------------------------------------------------------
# --- RESTO DEL CODIGO (MENOS LAS PUTEADAS QUE NO SEAN LOGICAS, CONSCIENTES Y/O FROFEZADAS Y PROFETIZADAS CON INTENCION) ---
# --------------------------------------------------------------------------------------------------------------------------
import sys 
import os 
cleanconsole =lambda :os .system ('cls'if os .name =='nt'else 'clear')
import json 
import re 
import subprocess 
import shutil
from datetime import date, timedelta    

#For Cognitive Evolution 20/06/2026 19:10 UTC-3
from datetime import datetime, timedelta
import psutil
from collections import defaultdict

#Clean Old Consoles... The New Era is Comming...
cleanconsole ()
from qt_compat import (
    QApplication, QMainWindow, QListWidget, QListWidgetItem,
    QSizePolicy, QVBoxLayout, QGroupBox, QLabel, QMenu, QAction,
    QColorDialog, QFileDialog, QTabWidget, QInputDialog, QMessageBox,
    QWidget, QHBoxLayout, QGridLayout, QSlider, QComboBox, QPushButton,
    QCheckBox, QButtonGroup, QScrollArea, QLineEdit,
    Qt, QSize, QPoint, QTimer, QUrl, QEvent,
    QtGui, QColor, QIcon, QPixmap, QFont, QKeySequence,
    QMediaPlayer, QMediaContent, QPainter, QThread, pyqtSignal, QMutex, QMutexLocker,
    get_qt_version
)
# MIT DarkStyle
import qdarkstyle 
from qdarkstyle import load_stylesheet ,DarkPalette 
from qdarkstyle import LightPalette
# Team Cangurera & Monkey Python Coding Circus - 2026   
from precisionslider import PrecisionSliderH 
from mayacalendarwidget import MayaCalendarWidget

geckoappversion ="13/20 — Tzolkin Edition"
verFisicaGeckonica = True
print(f"[Gecko OS...] Corriendo en {get_qt_version()}")

posicionPestanasGecko =QTabWidget .South 

def get_version (easter_egg =False ):
    if not easter_egg :
        return f"Geckolauncker {geckoappversion}"

    G ="\033[38;5;46m"
    Y ="\033[38;5;226m"
    Z ="\033[94m"
    A ="\033[38;5;214m"
    C ="\033[38;5;51m"
    D ="\033[38;5;240m"
    R ="\033[0m"
    NAVIGATOR ="\033[92m"
    PLEYADIAN ="\033[94m"
    TRIDACTIL ="\033[90m"
    NAVZONES ="\033[96m"
    SYSTEMS ="\033[93m"
    EI2TEAM ="\033[95m"
    LLAMITATEAM ="\033[93m"
    NOVATEAM ="\033[96m"

    return f"""
        {G}
                                                    
                            __           {Z}____{G}
                           /'_)       {Z}__|_'_ |{G}{Y}__{G}
                    .-^^^-/ /        {Z}|    ___|{G}  {Y}|{G}
                __/        /         {Z}|__{G}{Y}|   ____|{G}
               <__.|_|--|_|             {Y}|___'_|{G}

                {G}GECKO OS{G}                {Z}PYT{G}{Y}HON{G} 
                {G}LAUNCKER MINIMAL{G}  {PLEYADIAN}[{geckoappversion}]{G} 
                {C}Core == Cuore by Team Cangurera{R}
                {A}ET MUTAGENICO COMPATIBLE CON PYLAND{R}
                {G}🦎Geckonismo™{R} {C}🦎Geckoniano™{R} {Y}🦎Geckónico™{R}
                {PLEYADIAN}Artefacto 1997 // Berazategui // 2184{R}

                {G}Modular{R} • {A}Minimalista{R} • {C}Geckoniano{R} • {Y}Pleyadiano{R}
                {G}by Monkey Python Coding Circus & AlanRG Systemas{R}
        {R}
~\\\\Gecko OS> Please Enter Your Intention...
    """

# WhatchGeckoTotal by Aetheris // Implementación Llamita Encendida en la WWW
class WatchGeckoTotal(QThread):
    """
    WatchGeckoTotal EVZ6: Guardián de intenciones propias.
    Solo monitorea PIDs lanzados desde GeckoLAuncker durante esta sesión.
    Ley: Si no lo lancé yo, no es mi problema.
    """
    alerta = pyqtSignal(str, str)

    def __init__(self, launcher):
        super().__init__()
        self.launcher = launcher
        self.running = True
        self.pids_vigilados = {} # {pid: {"nombre": str, "cpu_alertado": float}}
        self.lock = QMutex() # Thread-safe

    def registrar_pid(self, pid, nombre):
        """Llamar desde ejecutar_lanzador cuando lanzás algo."""
        with QMutexLocker(self.lock):
            self.pids_vigilados[pid] = {"nombre": nombre, "cpu_alertado": 0}

    def run(self):
        while self.running:
            self.chequear_hijos()
            self.msleep(3000) # Cada 3s

    def chequear_hijos(self):
        """
        Solo chequea procesos hijos de GeckoLAuncker.
        Si CPU > 25% y no fue alertado, salta.
        """
        with QMutexLocker(self.lock):
            pids_muertos = []

            for pid, data in self.pids_vigilados.items():
                try:
                    p = psutil.Process(pid)
                    cpu = p.cpu_percent(interval=0.1) # Medición real

                    # Umbral 25% - solo vampiros serios
                    if cpu > 25.0:
                        cpu_anterior = data["cpu_alertado"]

                        # Alerta solo si subió 10% desde última vez
                        if cpu > cpu_anterior + 10:
                            msg = (f"🦎 Hijo en divergencia\n\n"
                                   f"'{data['nombre']}' consume {cpu:.0f}% CPU.\n"
                                   f"PID: {pid}\n\n¿Mutar proceso?")
                            self.alerta.emit("WatchGeckoTotal", msg)
                            self.pids_vigilados[pid]["cpu_alertado"] = cpu

                except psutil.NoSuchProcess:
                    # El proceso murió, sacarlo de la lista
                    pids_muertos.append(pid)
                except psutil.AccessDenied:
                    # No tenemos permiso, sacarlo igual
                    pids_muertos.append(pid)

            # Limpiar muertos
            for pid in pids_muertos:
                del self.pids_vigilados[pid]

    # SPSG (Super Poderosa Salida Geckónica)
    def stop(self):
        self.running = False
        # Si el hilo está en msleep, no podemos simplemente esperar.
        # En Qt, no hay un "interrupt" directo para sleep, pero podemos 
        # cerrar el hilo abruptamente si es necesario para un cierre limpio.
        if self.isRunning():
            self.terminate() # Fuerza la salida inmediata del hilo
            self.wait()      # Asegura que los recursos se limpien

# Clases ini EVZX
class GeckoList (QListWidget ):
    def __init__ (self ,parent_launcher ):
        super ().__init__ ()
        self .launcher =parent_launcher 
        '''
        print("\n🧬 GeckoList INIT")
        print("   id:", id(self))
        '''
        self .setAcceptDrops (True )
        self .setDragDropMode (QListWidget .InternalMove )

        self .setMinimumSize (1 ,1 )
        self .setUniformItemSizes (True )

    def contextMenuEvent (self ,event ):
        global_pos =event .globalPos ()
        self .launcher .mostrar_menu_contextual (global_pos ,self )
        event .accept ()

    def dragEnterEvent (self ,event ):
        if event .mimeData ().hasUrls ():
            event .acceptProposedAction ()
            self .launcher .play_sfx ('dialog-information.oga')

            self .setProperty ("dragActive",True )
            self .style ().unpolish (self )
            self .style ().polish (self )
        else :
            super ().dragEnterEvent (event )

    def dragLeaveEvent (self ,event ):
        self .setProperty ("dragActive",False )
        self .style ().unpolish (self )
        self .style ().polish (self )
        super ().dragLeaveEvent (event )

    def dropEvent (self ,event ):
        self .setProperty ("dragActive",False )
        self .style ().unpolish (self )
        self .style ().polish (self )

        if event .mimeData ().hasUrls ():
            for url in event .mimeData ().urls ():
                ruta =url .toLocalFile ()
                if os .path .isfile (ruta ):
                    nombre =os .path .basename (ruta )
                    self .launcher .agregar_item_lista (self ,nombre ,ruta ,usar_consola =False )
            self .launcher .guardar_lanzadores ()
            self .launcher .play_sfx ('device-added.oga')
            event .acceptProposedAction ()
        else :
            super ().dropEvent (event )

# Refactor de Ei2 (mucho menos glitcheado pero con bugs y pockerrores por atrapar y testear!!!)
class PanelMutagenico (QWidget ):
    def __init__ (self, launcher):
        super ().__init__ ()
        self .launcher = launcher 
        self .snapshot = json.loads(json.dumps(launcher.config))
        self. maximo_left_container = 350
        # El Team Cangurera eliminó las fluctuaciones estocásticas.
        self .init_ui ()

    def init_ui (self ):
        main = QHBoxLayout (self )
        main .setSpacing (13 )

        # --- CONTENEDOR DE CONTROLES (IZQUIERDA) ---
        self.left_container = QWidget()
        self.left_container.setMaximumWidth(self.maximo_left_container)
        
        left = QVBoxLayout(self.left_container)
        left.setSpacing(13)
        left.setContentsMargins(0, 0, 0, 0)

        left .addWidget (QLabel ("🧭 Rombo de los Vientos"))
        grid = QGridLayout ()
        grid .setSpacing (5 )

        self .grupo_rombo = QButtonGroup (self )
        self .grupo_rombo .setExclusive (True )
        self .botones_rombo = {}

        pos = [
            ("↑ Norte", QTabWidget .North, 0, 1),
            ("← Oeste", QTabWidget .West, 1, 0),
            ("→ Este", QTabWidget .East, 1, 2),
            ("↓ Sur", QTabWidget .South, 2, 1)
        ]
        for txt, val, row, col in pos :
            btn = QPushButton (txt)
            btn .setCheckable (True)
            self .grupo_rombo .addButton (btn, val)
            self .botones_rombo [val] = btn 
            btn .clicked .connect (lambda _, v = val: self .mutar_posicion (v))
            grid .addWidget (btn, row, col)
        left .addLayout (grid)

        self .etiquetas_slider = {}
        for label, attr, minv, maxv, default in [
            ("Alto de GeckoTab", "s_tab", 137, 470, self .launcher .tamanio_geckotable .width ()),
            ("Lado de SQuareIcon", "s_icon", 37, 256, 86),
            ("Tamaño Texto", "s_texto", 8, 37, self .launcher .font_geckotable)
        ]:
            slider = PrecisionSliderH (self, orientation = Qt .Horizontal)
            slider .setMinimumHeight (45)
            slider .setRange (minv, maxv)
            slider .setValue (default)
            slider .valueChanged .connect (self .mutar_geometria)
            setattr (self, attr, slider)
            etiqueta = QLabel (f"{label}: {slider.value()}")
            self .etiquetas_slider [attr] = etiqueta 
            left .addWidget (etiqueta)
            left .addWidget (slider)

        left .addWidget (QLabel ("🎨 GeckoLAunker Icons Themes"))
        self .combo_tema = QComboBox ()
        self .actualizar_temas ()
        self .combo_tema .currentTextChanged .connect (self .mutar_tema)
        left .addWidget (self .combo_tema)

        # 🖼️ Selector de Wallpapers dedicados de Gecko OS
        left .addWidget (QLabel ("🖼️ GeckoWall Systems Selector"))
        self .combo_wallpaper = QComboBox ()
        self .actualizar_wallpapers_disponibles ()
        self .combo_wallpaper .currentTextChanged .connect (self .mutar_wallpaper_manual)
        left .addWidget (self .combo_wallpaper)

        self .chk_sonido = QCheckBox ("🔊 Sonidos Geckónicos")
        self .chk_sonido .setChecked (self .launcher .geckosounds)
        self .chk_sonido .toggled .connect (self .mutar_sonido)
        left .addWidget (self .chk_sonido)

        # ⚡ BOTÓN NATIVO GECKOLINK: Conmutador del Compositor del Sistema
        self.btn_toggle_transp = QPushButton("⚡ [Toggle TranspGeckonic]")
        self.btn_toggle_transp.setStyleSheet("""
            QPushButton {
                background-color: #050505;
                color: #00ff88;
                border: 2px solid #00ff88;
                border-radius: 5px;
                padding: 6px;
                font-family: monospace;
                font-weight: bold;
            }
            QPushButton:pressed {
                background-color: #00ff88;
                color: #000000;
            }
        """)
        self.btn_toggle_transp.clicked.connect(self.disparar_transparencia_geckolink)
        left.addWidget(self.btn_toggle_transp)

        h = QHBoxLayout ()
        h .addWidget (QPushButton ("¿GotoInitThem?>>>", clicked = self .ir_al_pasado))
        h .addWidget (QPushButton ("<<<¿Reset?Geckónic", clicked = self .reset_geckonico))
        left .addLayout (h)

        left.addStretch()
        main.addWidget(self.left_container)

        # --- CONTENEDOR DE PREVIEWS (DERECHA) ---
        right_container = QWidget()
        right_layout = QVBoxLayout(right_container)
        right_layout.setSpacing(13)
        right_layout.setContentsMargins(0, 0, 0, 0)

        # 🖼️ El preview del Wallpaper vivo, acoplado arriba de las pestañas
        wallpaper_group = QGroupBox("🖼️ GeckoWall Real-Time View (Preview)")
        w_layout = QVBoxLayout()
        self.wallpaper_preview_lbl = QLabel("Esperando Inicialización...")
        self.wallpaper_preview_lbl.setFixedSize(510, 287)
        self.wallpaper_preview_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wallpaper_preview_lbl.setStyleSheet("""
            background-color: #050505; 
            border: 2px dashed #00ff88; 
            border-radius: 6px; 
            color: #00ff88;
            font-family: monospace;
        """)
        w_layout.addWidget(self.wallpaper_preview_lbl, alignment=Qt.AlignmentFlag.AlignCenter)
        wallpaper_group.setLayout(w_layout)
        right_layout.addWidget(wallpaper_group)

        # --- CAJA DE GRUPO PREVIEW MUTAGENICO DE GECKO ---
        preview_group = QGroupBox ("👁️ GeckoTab de Muestra (Preview)")
        p_layout = QVBoxLayout ()
        self .preview = QListWidget ()
        self .preview .setViewMode (QListWidget .IconMode )
        self .preview .setFixedSize (510, 200) 
        self .preview .setSpacing (self .launcher .espacing_geckotabs)
        self .preview .setStyleSheet ("""
            QListWidget { background: #000000; border: 3px solid #00ff88; border-radius: 10px; }
        """)
        p_layout .addWidget (self .preview, alignment = Qt .AlignmentFlag .AlignCenter)
        preview_group .setLayout (p_layout)
        
        right_layout.addWidget(preview_group)
        main.addWidget(right_container)

        # Inicialización de flujos y visores locales
        self .despertar_panel ()
        self .actualizar_preview ()
        self .actualizar_render_miniatura (self.combo_wallpaper.currentText())

    def despertar_panel (self ):
        m = self .launcher .config .get ("estado_mutagenico", {})
        self .s_tab .setValue (m .get ("tamanio_geckotable",[137, 83])[0])
        self .s_icon .setValue (m .get ("geckoiconsize",[86, 86])[0])
        self .s_texto .setValue (m .get ("font_geckotable", 17))

        tema_actual = m .get ("IconThemeFolder", "default")
        idx = self .combo_tema .findText (tema_actual)
        if idx >= 0 :
            self .combo_tema .setCurrentIndex (idx)

        self .chk_sonido .setChecked (m .get ("geckosounds", False))
        pos_raw = m .get ("tab_position", QTabWidget .South)
        if isinstance (pos_raw, str):
            pos_actual = getattr (QTabWidget, pos_raw .split (".")[-1], QTabWidget .South)
        else :
            pos_actual = pos_raw 
        self .pintar_rombo_activo (pos_actual)

    def actualizar_preview (self ):
        self .preview .clear ()
        item = QListWidgetItem ("Brave")
        icon_path = os .path .join (self .launcher .IconPath, "brave.png")
        if os .path .exists (icon_path ):
            item .setIcon (QIcon (icon_path ))
        else :
            item .setIcon (QIcon .fromTheme ("applications-internet"))
        item .setTextAlignment (Qt .AlignmentFlag .AlignCenter)
        item .setSizeHint (self .launcher .tamanio_geckotable)
        item .setBackground (QColor ("#037730"))
        self .preview .addItem (item)
        self .preview .setIconSize (self .launcher .geckoiconsize)
        self .preview .setGridSize (self .launcher .tamanio_geckotable)
        font = self .preview .font ()
        font .setPointSize (self .launcher .font_geckotable)
        self .preview .setFont (font)

    def actualizar_wallpapers_disponibles(self):
        path = os.path.join(self.launcher.scriptDir, "GeckoWall")
        if os.path.exists(path):
            archivos = [f for f in os.listdir(path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            self.combo_wallpaper.clear()
            self.combo_wallpaper.addItems(archivos)

    def actualizar_render_miniatura(self, nombre_archivo):
        if not nombre_archivo:
            self.wallpaper_preview_lbl.setText("🖼— Matrix Vacía")
            return
        ruta = os.path.join(self.launcher.scriptDir, "GeckoWall", nombre_archivo)
        if os.path.exists(ruta):
            pixmap = QPixmap(ruta)
            scaled = pixmap.scaled(self.wallpaper_preview_lbl.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
            self.wallpaper_preview_lbl.setPixmap(scaled)
        else:
            self.wallpaper_preview_lbl.clear()
            self.wallpaper_preview_lbl.setText(f"❌ Desconectado: {nombre_archivo}")

    def disparar_transparencia_geckolink(self):
        """ Invoca el enlace nativo usando la referencia de ruta cruda y limpia """
        # Tomamos la referencia pura del sistema de archivos sin comillas extras
        ruta_script = os.path.join(self.launcher.scriptDir, "GeckoLinks", "geckolink_toggleTransp.sh")
        
        item_virtual = QListWidgetItem()
        item_virtual.setData(Qt.UserRole, {
            "ruta": ruta_script,  # Referencia limpia para que os.path.exists(ruta) de TRUE
            "nombre": "geckolink_toggleTransp",
            "consola": False,
            "huevo": False,
            "categoria_origen": "Mutageno_Compositor_Trigger"
        })
        
        # Disparo directo al Popen maestro sin interferir con el validador
        self.launcher.ejecutar_lanzador(item_virtual)

    def mutar_geometria (self ):
        tab_w = self .s_tab .value ()
        icon_s = min (self .s_icon .value (), int (tab_w *0.78 ))
        text_s = self .s_texto .value ()

        self .etiquetas_slider ["s_tab"].setText (f"Alto de GeckoTab: {tab_w}")
        self .etiquetas_slider ["s_icon"].setText (f"Lado de SQuareIcon: {icon_s}")
        self .etiquetas_slider ["s_texto"].setText (f"Tamaño Texto: {text_s}")

        self .launcher .tamanio_geckotable = QSize (tab_w, int (tab_w *0.62 ))
        self .launcher .geckoiconsize = QSize (icon_s, icon_s)
        self .launcher .font_geckotable = text_s 

        self.aplicar_mutacion()

    def mutar_posicion (self, pos ):
        self .launcher .tabs .setTabPosition (pos)
        self.aplicar_mutacion()
        self .pintar_rombo_activo (pos)

    def pintar_rombo_activo (self, pos_actual ):
        for val, btn in self .botones_rombo .items ():
            texto_base = btn .text ().lstrip ("✓ ")
            if val == pos_actual :
                btn .setText (f"✓ {texto_base}")
                btn .setChecked (True)
            else :
                btn .setText (texto_base)
                btn .setChecked (False)

    def mutar_tema (self, tema ):
        if not tema:
            return
        self .launcher .IconThemeFolder = tema 

        self.launcher.IconPath = os.path.join(self.launcher.scriptDir, "ThemeIcons", tema)
        self.launcher.refrescar_iconos_barra_inferior()       

        nombre_homonimo = f"{tema}.wall.png"
        
        self.combo_wallpaper.blockSignals(True)
        idx = self.combo_wallpaper.findText(nombre_homonimo)
        if idx >= 0:
            self.combo_wallpaper.setCurrentIndex(idx)
            self.actualizar_render_miniatura(nombre_homonimo)
            self.inyectar_wallpaper_sistema(nombre_homonimo)
        self.combo_wallpaper.blockSignals(False)

        self.aplicar_mutacion()

    def mutar_wallpaper_manual(self, archivo_wallpaper):
        if not archivo_wallpaper:
            return
        self.actualizar_render_miniatura(archivo_wallpaper)
        self.inyectar_wallpaper_sistema(archivo_wallpaper)

    def inyectar_wallpaper_sistema(self, nombre_archivo):
        """
        Envía la ruta limpia del script al motor para pasar el validador,
        e inyecta el nombre del archivo en el entorno para el proceso Bash.
        """
        # 1. Ruta cruda y limpia para que os.path.exists(ruta_script) dé TRUE
        ruta_script = os.path.join(self.launcher.scriptDir, "GeckoLinks", "set_wallpaper_pestañeo.sh")
        
        # 2. Inyectamos la variable directamente en el entorno vivo del sistema operativo.
        # El subproceso Popen heredará este entorno automáticamente al nacer.
        os.environ["GECKOWALL_FILE"] = nombre_archivo
        
        item_virtual = QListWidgetItem()
        item_virtual.setData(Qt.UserRole, {
            "ruta": ruta_script, # Pura, limpia y sin comillas extras para tu motor madre
            "nombre": "set_wallpaper_pestañeo",
            "consola": False,
            "huevo": False,
            "categoria_origen": "Mutageno_Wall_Injected"
        })
        
        # Al ejecutar, pasará el control de seguridad y heredará la variable perfectamente
        self.launcher.ejecutar_lanzador(item_virtual)

    def mutar_sonido(self, estado):
        self.launcher.geckosounds = bool(estado)
        self.aplicar_mutacion()
    
    def ir_al_pasado(self):
        config_pasada = self.snapshot["estado_mutagenico"]
        self.launcher.tamanio_geckotable = QSize(*config_pasada["tamanio_geckotable"])
        self.launcher.geckoiconsize = QSize(*config_pasada["geckoiconsize"])
        self.launcher.font_geckotable = config_pasada["font_geckotable"]
        self.despertar_panel()
        self.aplicar_mutacion()

    def reset_geckonico(self):
        self.launcher.tamanio_geckotable = QSize(137, 83)
        self.launcher.geckoiconsize = QSize(55, 55)
        self.launcher.font_geckotable = 13 
        self.launcher.geckosounds = False 
        self.launcher.colapsar_realidad()
        self.combo_tema.setCurrentIndex(0) if self.combo_tema.count() > 0 else None
        self.aplicar_mutacion()

    def actualizar_temas(self):
        path = os.path.join(self.launcher.scriptDir, "ThemeIcons")
        if os.path.exists(path):
            temas = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
            self.combo_tema.clear()
            self.combo_tema.addItems(temas)

    def aplicar_mutacion(self):
        self.actualizar_preview()
        self.launcher.colapsar_realidad()
        if hasattr(self.launcher, 'guardar_lanzadores'):
            self.launcher.guardar_lanzadores()

# la barra que cambio el "Search & Launch" para siempre
class GeckoSearchBar(QLineEdit):
    def __init__(self, launcher):
        super().__init__()
        self.launcher = launcher
        self.setPlaceholderText("Susurrale una runa al vacío...")
        self.setStyleSheet("""
            QLineEdit {
                background: transparent;
                border: 1px solid #333;
                color: #00ff88;
                padding: 5px;
            }
            QLineEdit:focus { border: 1px solid #ffffff; }
        """)
        self.textChanged.connect(self.launcher.invocar_oraculo)

    def keyPressEvent(self, event):
        # Si el usuario presiona ESC, limpiamos y devolvemos la calma
        if event.key() == Qt.Key_Escape:
            self.clear()
        super().keyPressEvent(event)

# Parte Fundamental Iniciatica de Gecko OS EvolZXX
class GeckoLauncker (QMainWindow ):
    def __init__ (self ):
        super ().__init__ ()
        self.scriptDir = os.path.dirname (os.path.realpath(__file__ ))
        self.offset = None 
        self.setWindowTitle(f"🦎 Gecko OS {geckoappversion} {revision}")

        # VAriables para el Panel Mutagénico Geckonista Geckónico
        self.tamanio_geckotable = (QSize(226 ,137 ))
        self.font_geckotable = 17
        self.espacing_geckotabs = 15
        # Para configurar condiciones especificas matriciales ejemplo [3:4]
        # primero hacer un checkbox con variable para pasarla a False
        # self.automatic_adjust_geckotaps = True
        # if self.automatic_adjust_geckotaps == True:
        #    se habilitan campos desplegables para ingresar [X:X]
        # En nuestro ejemplo
        # self.columnas = 3
        # self.filas = 4

        self.IconThemeFolder = "ThemeIcons"
        self.IconThemePath = os .path .join (self .scriptDir ,self .IconThemeFolder )
        self.geckoiconsize = (QSize(86 ,86 ))
        self.geckosounds = False 
        self.geckorefresh = 13
        self.altura_mododock = 200
        self.botones_inferiores = []

        self.IconPath = os.path.join (self.scriptDir ,'Icons')
        icon_file = os.path.join (self.IconPath ,'appicon.png')
        if os.path.exists(icon_file ):
            self.setWindowIcon(QtGui.QIcon(icon_file ))

        # Nuevo GeckoDock's Mode TM (no funcional evaluar propuestas de Leo)            
        self.gecko_dock_activo = False  # Puedes cambiar esto a False para "desconectar"   

        self.player = QMediaPlayer ()

        # EvALUAR Enviar variable al mutagenico para que decida si mostrar el panel o no, o incluso qué opciones mostrar. El muta puede ser un filtro de realidad dentro del panel.
        # Colocar el boton cerrar app antes del frameless. 
        #self .setWindowFlags (Qt .FramelessWindowHint )

        '''
        self.transparent_palette = QtGui.QPalette()
        self.transparent_palette.setColor(QtGui.QPalette.Base, Qt.transparent)
        self.transparent_palette.setColor(QtGui.QPalette.Window, Qt.transparent)
        self.setPalette(self.transparent_palette)
        '''

        #self .config_file =os .path .expanduser ("~/.config/gecko_lanzadoresv3x4.json")
        self .config_file =os .path .expanduser ("~/.config/geckoos.json")

        self .config ={
        "version":geckoappversion ,
        "fondo_launcher":"#0a0a0a",
        "categorias":{
        "🦎 GeckoLAuncker":{
        "items":[],
        "tema":{
        "color_texto":"#00ff88",
        "color_fondo_lista":"#000000",
        "color_fondo_item_activo":"#00ff88",
        "color_texto_item_activo":"#000000"
        }
        }
        },
        "estado_mutagenico":{
        "tamanio_geckotable":[226 ,137 ],
        "geckoiconsize":[86 ,86 ],
        "font_geckotable":17 ,
        "tab_position":QTabWidget .South ,
        "IconThemeFolder":"default",
        "geckosounds":False 
        }
        }

        # original old ok EVZ6
        self .cargar_lanzadores ()

        # Evaluar esta limpieza de estilos
        self .setup_styles ()

        # Original ui Gecko OS
        self .init_ui ()
        
        # NUEVO: Panel de Intenciones Frecuentes
        # CREAR PESTAÑA NORMAL CON FAA
        self.crear_pestana_intenciones_frecuentes()

        # NUEVO: WatchGeckoTotal
        self.watchdog = WatchGeckoTotal(self)
        self.watchdog.alerta.connect(self.mostrar_alerta_geckonica)
        self.watchdog.start()

        '''
        self.tabs.setStyleSheet("QTabWidget::pane { background: transparent; border: none; }")
        self.tabs.setAttribute(Qt.WA_TranslucentBackground)

        # Aplicar transparencia a los widgets dentro de las pestañas
        for i in range(self.tabs.count()):
            self.tabs.widget(i).setAttribute(Qt.WA_TranslucentBackground)
            self.tabs.widget(i).setPalette(self.transparent_palette)
        '''

        self.resize_timer = QTimer(self)
        self.resize_timer.setSingleShot(True)
        self.resize_timer.timeout.connect(self.ejecutar_consolidacion)

        # ahhh carga config guardada !!! jajajajja
        self .setStyleSheet (f"QMainWindow {{ background: {self.config.get('fondo_launcher', '#0a0a0a')}; }}")
        
        print (get_version (easter_egg =True ))

        self.foco_en_el_oraculo()

    def foco_en_el_oraculo(self):
        # ----------------------------------------------------------------------------------------------------------------------
        self.campo_oraculo = self.geckoSearch # La Fuente de la Verdad Ultima
        # Foco Inicial en el Oraculo... si moves el mouse sigue... si haces click en narnia sigue...
        # ACTIVACIÓN del campo sagrado doble vía:
        # --- SOLUCIÓN DE UNA LÍNEA by LEO [Team Cangurera]---
        [w.setFocusPolicy(Qt.NoFocus) for w in self.findChildren(QWidget) if w != self.campo_oraculo]
        # --- El Doble en Recursividad Fractal de foco al Oraculo Sagrado por si lo anterior falla por algun Glitch Multiversal
        # --- APLICACIÓN ROBUSTA DE NO-FOCO (Recursiva real)
        # Usamos un bucle explícito para asegurar profundidad máxima en Linux
        for widget in self.findChildren(QWidget):
            if widget != self.campo_oraculo:
                widget.setFocusPolicy(Qt.NoFocus)
        # --- Asegurar que el Oráculo tenga foco fuerte (aunque ya la tenga por defecto, es buena práctica explícita).
        self.campo_oraculo.setFocusPolicy(Qt.StrongFocus)
        # ----------------------------------------------------------------------------------------------------------------------
        # Foco Inicial (se mantendrá por los siglos de los siglos mientras el sol siga naciendo cada día)
        self.campo_oraculo.setFocus()
       
    def setup_styles (self ):
        """ Hojas de estilo unificadas de tu suite cyberpunk """
        base_style ="""
            QPushButton {
            background: transparent;
            border: 1px solid #00ff88;
            border-radius: 4px;
        }
        QPushButton:hover {
            background: #00ff88;
            color: #000;
        }
        QPushButton:pressed {
            background: #00cc6a;
        }
            QListWidget::item:selected {
                background: #00ff88; /* Verde Geckonico */
                color:#000;
                border-left: 3px solid #ffffff;
                font-weight: bold;
            }
            QListWidget::item:hover {
                background: #00ff88; /* Verde Geckonico*/
                color: #000;
                border-left: 3px solid #00ff00;
            }
            QTabWidget::tab {
                font-weight: bold;
            }   
            QTabWidget::pane {
                font-weight: bold;
                border: 2px solid #00ff88;
                background: rgba(0, 0, 0, 0.85);
            }
            QTabBar::tab {
                background: #111;
                color: #00ff88;
                padding: 10px;
                border: 1px solid #333;
                font-weight: bold;
            }
            QTabBar::tab:selected {
                background: #00ff88;
                color: #000;
                font-weight: bold;
            }
        """
        self .list_style_normal =f"QListWidget {{ background: #000; color: #00ff88; border: 2px solid #00ff88; font-family: 'Courier New', monospace; font-size: {self.font_geckotable}px; }} {base_style}"
        self .list_style_active =f"QListWidget {{ background: #000; color: #00ff88; border: 2px solid #ffffff; font-family: 'Courier New', monospace; font-size: {self.font_geckotable}px; }} {base_style}"

    def aplicar_estilo_lista (self ,lista_widget ,nombre_tab ):
        #tema_tab =self .config ["categorias"][nombre_tab ].get ("tema",{})

        categoria = self.config.get("categorias", {}).get(nombre_tab, {})
        tema_tab = categoria.get("tema", {})

        color_texto =tema_tab .get ("color_texto","#00ff88")
        color_fondo =tema_tab .get ("color_fondo_lista","#000000")
        color_fondo_activo =tema_tab .get ("color_fondo_item_activo","#00ff88")
        color_texto_activo =tema_tab .get ("color_texto_item_activo","#000000")

        estilo =f"""
            QListWidget {{
                background: {color_fondo};
                color: {color_texto};
                border: 2px solid #00ff88;
                font-family: 'Courier New', monospace;
                font-size: {self.font_geckotable}px;
            }}
            QListWidget::item:selected {{
                background: {color_fondo_activo};
                color: {color_texto_activo};
                border-left: 3px solid #ffffff;
                font-weight: bold;
            }}
            QListWidget::item:hover {{
                background: {color_fondo_activo};
                color: {color_texto_activo};
                border-left: 3px solid #00ff00;
            }}
        """
        estilo +="""
            QListWidget[dragActive="true"] {
                border: 2px solid #ffffff;
            }
        """
        lista_widget .setStyleSheet (estilo )

    def init_ui (self ):
        """Inicializa el contenedor de GeckoTabs y tu primera lista """

        self .launcker_conteiner =QGroupBox ()
        self .launcker_layout =QVBoxLayout ()
        self .launcker_layout .setContentsMargins (0 ,0 ,0 ,0 )
        self .launcker_conteiner .setLayout (self .launcker_layout )

        self .tabs =QTabWidget (self )

        m =self .config .get ("estado_mutagenico",{})
        self .tamanio_geckotable =QSize (*m .get ("tamanio_geckotable",[226 ,137 ]))
        self .geckoiconsize =QSize (*m .get ("geckoiconsize",[86 ,86 ]))
        self .font_geckotable =m .get ("font_geckotable",17 )
        self .IconThemeFolder =m .get ("IconThemeFolder","default")
        self .IconPath =os .path .join (self .IconThemePath ,self .IconThemeFolder )

        # Logica de Inicio de las QtabWidgets: Pestaneas
        tab_pos_raw =m .get ("tab_position",self .config .get ("posicion_tabs",QTabWidget .South ))
        tab_pos =getattr (QTabWidget ,tab_pos_raw .split (".")[-1 ],QTabWidget .South )if isinstance (tab_pos_raw ,str )else tab_pos_raw 
        self .tabs .setTabPosition (tab_pos )
        self .tabs .setMovable (True )
        self .tabs .setTabsClosable (True )
        self .tabs .tabCloseRequested .connect (self .eliminar_categoria )
        self .tabs .currentChanged .connect (self .cambiar_lista_activa )
        self .tabs .tabBar ().tabMoved .connect (self .reordenar_categorias_dict )
        self .tabs .clear ()

        for nombre_tab ,data_tab in self .config ["categorias"].items ():
            lista_widget =self .crear_pestana (nombre_tab )
            for data in data_tab .get ("items",[]):
                self .agregar_item_lista (lista_widget ,data ["nombre"],data ["ruta"],data ["consola"],sync_config =False )

        if self .tabs .count ()>0 :
            self .lista =self .tabs .widget (0 )
            self .tabs .setCurrentIndex (0 )
        else :
            '''
            self .lista =self .crear_pestana ("Inicio 🦎")
            self .config ["categorias"]["Inicio 🦎"]=[]
            '''
            # Primero creá la entrada en SHEISON con estructura completa
            self.config["categorias"]["Inicio 🦎"] = {
                "items": [],
                "tema": {
                    "color_texto": "#00ff88",
                    "color_fondo_lista": "#000000",
                    "color_fondo_item_activo": "#00ff88", 
                    "color_texto_item_activo": "#000000"
                }
            }
            # Recién después creá la pestaña visual
            self.lista = self.crear_pestana("Inicio 🦎")

        self .launcker_layout .addWidget (self .tabs )

        #aca estaba la barra de Gecko y se fue a abstraerse
        self.init_barra_geckonica()

        self .panel_mutagenico =PanelMutagenico (self )
        self .tabs .addTab (self .panel_mutagenico ,"🧬 MUTAGÉNICO")

        self .setCentralWidget (self .launcker_conteiner )
    
    def init_barra_geckonica (self):
        # ------------------------------------------------------
        # --- Barra con Buscador Geckonico de Runas + botones:
        # ------------------------------------------------------
        barra_inferior = QHBoxLayout()
        barra_inferior.setContentsMargins(5, 0, 5, 5)

        #label_version = QLabel(f"🦎 🦎 Gecko OS Launcker Minimal {geckoappversion}")
        self.geckoSearch =GeckoSearchBar(self)
        self.geckoSearch.setFocus()
        self.geckoSearch.returnPressed.connect(self.ejecutar_item_en_foco)
        barra_inferior.addWidget(self.geckoSearch)
        barra_inferior.addStretch() # Empuja los botones a la derecha

        # Geckonic Introdución
        barra_inferior.addWidget (QLabel (f"🦎 Gecko OS Minimal LAuncker"),alignment =Qt .AlignRight )

        # Botón Modo Dock
        icon_dock = QIcon(os.path.join(self.IconPath, "dock.png"))
        self.btn_dock_mode = QPushButton(icon_dock, "")
        self.btn_dock_mode.setToolTip("Geckonic Dock Mode")
        self.btn_dock_mode.setFixedSize(32, 32)
        self.btn_dock_mode.setIconSize(QSize(24, 24))
        self.btn_dock_mode.clicked.connect(self.activar_modo_dock)
        self.botones_inferiores.append((self.btn_dock_mode, "dock"))
        barra_inferior.addWidget(self.btn_dock_mode)

        # Botón Toggle de Solapas
        icon_tab = QIcon(os.path.join(self.IconPath, "tabs.png")) 
        self.btn_toggle_tabs = QPushButton(icon_tab, "")
        self.btn_toggle_tabs.setToolTip("Pestaneas ON/oFF")
        self.btn_toggle_tabs.setFixedSize(32, 32)
        self.btn_toggle_tabs.setIconSize(QSize(24, 24))
        self.btn_toggle_tabs.clicked.connect(self.toggle_solapas)
        self.botones_inferiores.append((self.btn_toggle_tabs, "tabs"))
        barra_inferior.addWidget(self.btn_toggle_tabs)

        # Botón Calendario Maya       
        icon_maya = QIcon(os.path.join(self.IconPath,"mayacalendar.png"))
        self.btn_maya = QPushButton(icon_maya, "")
        self.btn_maya.setToolTip("Ruedas Calendaricas Cosmológicas Mayas")
        self.btn_maya.setFixedSize(32, 32)
        self.btn_maya.setIconSize(QSize(24, 24))
        self.btn_maya.clicked.connect(lambda: self.toggle_geckonico("🗿 TZOLKIN", MayaCalendarWidget))
        self.botones_inferiores.append((self.btn_maya, "mayacalendar"))
        barra_inferior.addWidget(self.btn_maya)                

        # Botón Config
        icon_config = QIcon(os.path.join(self.IconPath, "config.png"))
        self.btn_config = QPushButton(icon_config, "")
        self.btn_config.setToolTip("Bunny Kpop Panel Mutagénico")
        self.btn_config.setFixedSize(32, 32)
        self.btn_config.setIconSize(QSize(24, 24))
        self.btn_config.clicked.connect(lambda: self.toggle_geckonico("🧬 MUTAGÉNICO", PanelMutagenico))
        self.botones_inferiores.append((self.btn_config, "config"))
        barra_inferior.addWidget(self.btn_config)

        # Botón Salir
        icon_salir = QIcon(os.path.join(self.IconPath, "salir.png"))
        self.btn_salir = QPushButton(icon_salir, "")
        self.btn_salir.setToolTip("Salir del GeckoLAuncker")
        self.btn_salir.setFixedSize(32, 32)
        self.btn_salir.setIconSize(QSize(24, 24))
        self.btn_salir.clicked.connect(self.close)
        self.botones_inferiores.append((self.btn_salir, "salir"))
        barra_inferior.addWidget(self.btn_salir)

        self.launcker_layout.addLayout(barra_inferior)

    def play_sfx (self ,nombre_archivo ):
        """
        Funcion La Voz de Gecko Unificada, este metodo (que para mi es una funcion por "su funcion dentro de GeckoLAunker")
        es el centro del Sonido... el primer if lo explica todo, el PEPIF Primordial...
        """
        if not self .geckosounds :
            return 

        ruta_abs =os .path .abspath (os .path .join ("/usr/share/sounds/freedesktop/stereo/",nombre_archivo ))
        if os .path .isfile (ruta_abs ):
            self .player .setMedia (QMediaContent (QUrl .fromLocalFile (ruta_abs )))
            self .player .play ()
        else :
            print (f"🦎 SFX no encontrado: {ruta_abs}")

    # --- Geckonización     
    def anclar_multiverso(self):
        # Usamos availableGeometry para ignorar la barra de tareas real del OS
        # y no quedar ocultos detrás de ella.
        geom = QApplication.primaryScreen().availableGeometry()
        
        # Posicionamiento: Centrado horizontal, abajo vertical
        x = (geom.width() - self.width()) // 2
        y = geom.height() - self.height()
        
        self.move(x, y)
    ''' original ok v ant
    def activar_modo_dock(self):
        """
        Modo Dock: Secuencia de liberación de memoria y despliegue espacial.
        """
        # Buscamos el índice del Mutagénico
        index_mutagenico = -1
        for i in range(self.tabs.count()):
            if self.tabs.tabText(i) == "🧬 MUTAGÉNICO":
                index_mutagenico = i
                break
        # 1. Si existe, lo cerramos en el siguiente ciclo para limpiar el layout
        if index_mutagenico != -1:
            self.tabs.removeTab(index_mutagenico)

        # Ocultación de la TabBar (Si está visible, la ocultamos)
        tab_bar = self.tabs.tabBar()
        if tab_bar.isVisible():
            tab_bar.setVisible(False)
        
        # Programamos el redimensionamiento para que ocurra 
        # inmediatamente después de que el layout se haya reacomodado
        QTimer.singleShot(0, self.redimensionado_en_grieta_temporal)
    '''
    def activar_modo_dock(self):
        """
        Toggle: Activa o desactiva el Modos GeckoDock's System TM 
        El verdadero poder está en moveEvent, no aquí.
        """

        """
        Modo Dock Original: Secuencia de liberación de memoria y despliegue espacial.
        """
        print(f"🦎 [DOCK MODE ORIGINAL]: Colapsando en Campo Gravitatorio Gecko {geckoappversion}")
        # Buscamos el índice del Mutagénico
        index_mutagenico = -1
        for i in range(self.tabs.count()):
            if self.tabs.tabText(i) == "🧬 MUTAGÉNICO":
                index_mutagenico = i
                break
        # 1. Si existe, lo cerramos en el siguiente ciclo para limpiar el layout
        if index_mutagenico != -1:
            self.tabs.removeTab(index_mutagenico)

        # Opcional (no se siente natural) Ocultación de la TabBar (Si está visible, la ocultamos)
        #tab_bar = self.tabs.tabBar()
        #if tab_bar.isVisible():
        #    tab_bar.setVisible(False)
        
        # Programamos el redimensionamiento para que ocurra 
        # inmediatamente después de que el layout se haya reacomodado
        QTimer.singleShot(0, self.redimensionado_en_grieta_temporal) #COMENTADO POR NUEVOS MODOS GECKODOCK'S TM

        # --- Leo Se adiere a las paredes del Tiempo Blando ---
        # Alternar el estado (True/False)
        #nuevo_estado = not self.config.get('modo_dock', {}).get('activo', False)
        
        nuevo_estado = self.gecko_dock_activo
        # Actualizar el estado en el diccionario
        if 'modo_dock' not in self.config:
            self.config['modo_dock'] = {}
        self.config['modo_dock']['activo'] = nuevo_estado
        
        # Opcional: Cambiar el icono del botón para dar feedback  [ROTO, SE ME ROMPIO]
        # icono = QIcon(os.path.join(self.IconPath, "dock_active.png")) if nuevo_estado else icon_dock
        # self.btn_dock_mode.setIcon(icono)
        
        # --- AUDITORÍA 1: El Toggle ---
        estado_texto = "ACTIVADO 🟢" if nuevo_estado else "DESACTIVADO 🔴"
        print(f"🦎 [MODES GECKODOCK'S]: El sistema nervioso está {estado_texto}")
        

        # Guardar el estado del toggle
        self.guardar_config_en_json()   
    
    def redimensionado_en_grieta_temporal(self):
        pantalla = self.screen().availableGeometry()
        nuevo_ancho = pantalla.width()
        nueva_altura = self.altura_mododock
        self.resize(nuevo_ancho, nueva_altura)
        self.move(pantalla.left(), pantalla.bottom() - nueva_altura)
        self.asegurar_limites()

    def toggle_geckonico(self, titulo_tab, clase_widget):
        """
        El Motor de Estado Único de Pestaneas Gecko OS by Ei2 - Team Cangurera
        Crea, Enfoca o Cierra cualquier panel basado en su identidad.
        """
        index = -1
        for i in range(self.tabs.count()):
            if self.tabs.tabText(i) == titulo_tab:
                index = i
                break
        
        # 1. Ya está abierta y activa: CERRAR
        if index != -1 and self.tabs.currentIndex() == index:
            self.tabs.removeTab(index)
            self.play_sfx('window-close.oga')
            
        # 2. Existe pero no está activa: ENFOCAR
        elif index != -1:
            self.tabs.setCurrentIndex(index)
            self.play_sfx('dialog-information.oga')
            
        # 3. No existe: CREAR
        else:
            nuevo_widget = clase_widget(self)
            self.tabs.addTab(nuevo_widget, titulo_tab)
            self.tabs.setCurrentIndex(self.tabs.count() - 1)
            self.play_sfx('window-new.oga')
    
    # original funcional sin modo GeckoDock's
    ''' 
    def ejecutar_consolidacion(self):
        """
        Este método es el único que realiza cambios de posición.
        Al ser llamado por el timer, garantizamos que el resize terminó.
        """
        widget = self.tabs.currentWidget()
        if isinstance(widget, GeckoList):
            widget.setResizeMode(QListWidget.Adjust)
            QTimer.singleShot(37, lambda: widget.resize(widget.size()))
            #QTimer.singleShot(37, lambda: GeckoList.setResizeMode(QListWidget.Adjust))
            #QTimer.singleShot(37, lambda: widget.setResizeMode(QListWidget.Fixed))
        
        # Ahora, cuando esto corre, el OS ya terminó de redimensionar.
        self.asegurar_limites()
    '''
    # para modo GeckoDock's
    def ejecutar_consolidacion(self):
        """
        CEREBRO DE CONSOLIDACIÓN GECKÓNICA.
        Se ejecuta automáticamente cuando el usuario termina de redimensionar (timer).
        
        Flujo:
        1. Ajusta internos de GeckoList (tu lógica original).
        2. Asegura límites de pantalla.
        3. [NUEVO] Si Modo Dock está ACTIVO: Detecta intención, imanta al borde y guarda en el Grimorio.
        """
        # --- 1. Lógica Original: Ajuste de GeckoList ---
        widget = self.tabs.currentWidget()
        if isinstance(widget, GeckoList):
            widget.setResizeMode(QListWidget.Adjust)
            # Pequeño delay para permitir que el layout se asiente antes de forzar resize
            QTimer.singleShot(37, lambda: widget.resize(widget.size()))

        # --- 2. Lógica Original: Seguridad de Límites ---
        # Evita que la ventana quede fuera de la pantalla visible
        self.asegurar_limites()

        # --- 3. NUEVO: Lógica de Imantación Geckónica (Solo si Modo Dock está ON) ---
        if self.config.get('modo_dock', {}).get('activo', False):
            #self._procesar_imantacion_dock()
            print("Hasta acá llegaste Leo en modo MAgneto Glitcheado!!!")

    def _procesar_imantacion_dock(self):
        """
        Sub-rutina de Consolidación: Detecta la intención de anclaje basada en la geometría final.
        Calcula el borde más cercano según el tamaño y 'pega' la ventana.
        """
        pantalla = QApplication.primaryScreen()
        area = pantalla.availableGeometry()
        geo = self.geometry()
        
        ancho, alto = geo.width(), geo.height()
        x, y = geo.x(), geo.y()
        
        # Umbrales de Intención (85% de la pantalla sugiere un dock)
        umbral_ancho = area.width() * 0.85
        umbral_alto = area.height() * 0.85
        
        modo_detectado = None
        nueva_x, nueva_y = x, y

        # --- DETECCIÓN DE INTENCIÓN ---
        
        # CASO A: Horizontal (Inferior o Superior)
        if ancho >= umbral_ancho:
            dist_abajo = abs((area.bottom() - alto) - y)
            dist_arriba = abs(area.top() - y)
            
            if dist_abajo < dist_arriba:
                modo_detectado = 'inferior'
                nueva_y = int(area.bottom()) - alto
            else:
                modo_detectado = 'superior'
                nueva_y = int(area.top())

        # CASO B: Vertical (Izquierda o Derecha)
        elif alto >= umbral_alto:
            dist_izq = abs(area.left() - x)
            dist_der = abs((area.right() - ancho) - x)
            
            if dist_izq < dist_der:
                modo_detectado = 'izquierda'
                nueva_x = int(area.left())
            else:
                modo_detectado = 'derecha'
                nueva_x = int(area.right()) - ancho

        # --- EJECUCIÓN DEL ANCLAJE ---
        if modo_detectado:
            # 1. Actualizar Estado en el Grimorio
            self.config['modo_dock']['modo'] = modo_detectado
            self.config['modo_dock']['ancho'] = ancho
            self.config['modo_dock']['alto'] = alto
            
            # 2. Mover (Imantar) a la posición exacta
            self.move(int(nueva_x), int(nueva_y))
            
            # 3. Guardado Silencioso en JSON
            self.guardar_config_en_json()
            
            print(f"🦎 [DOCK CONSOLIDADO]: Anclado a [{modo_detectado.upper()}] | {ancho}x{alto}")
        else:
            # Si redimensionó pero no alcanzó umbrales de dock, solo guarda tamaño
            self.config['modo_dock']['ancho'] = ancho
            self.config['modo_dock']['alto'] = alto
            self.guardar_config_en_json()
            print(f"🦎 [TAMAÑO ACTUALIZADO]: {ancho}x{alto} (Sin anclaje específico)")   
 
    def asegurar_limites(self):
        pantalla = self.screen().availableGeometry()
        geo = self.frameGeometry()
        
        # Si el sistema reporta que el área disponible es igual a la pantalla
        # y sabes que tienes una barra de tareas, forzamos un margen seguro.
        # Esto es lo que estabas buscando: autonomía frente a la desinformación del OS.
        margen_seguro = 68 #evaluar de donde sale este valor para medirlo por software dinamicamente!!!
        
        limite_inferior = pantalla.bottom() - self.height()
        
        # Si detectamos que estamos muy cerca del borde total (posible error de lectura)
        if abs(pantalla.bottom() - pantalla.height()) < 10: 
            limite_inferior -= margen_seguro

        if geo.bottom() > pantalla.bottom():
            self.move(geo.x(), limite_inferior)

    def colapsar_realidad (self ):
        """Arkano Supremo - Colapso de la Realidad Geckónica
        Intención: Cuando la Nave muta, el colapso no solo repinta la UI.
        Cristaliza el estado físico actual en self.config["estado_mutagenico"].
        La UI es el reflejo. El dic es la realidad. El colapso sincroniza ambos.
        Función: Se llama después de cualquier mutación. Garantiza que json = UI.
        """
        for i in range (self .tabs .count ()):
            widget =self .tabs .widget (i )
            if isinstance (widget ,GeckoList ):
                widget .setGridSize (self .tamanio_geckotable )
                widget .setIconSize (self .geckoiconsize )

                self .aplicar_estilo_lista (widget ,self .tabs .tabText (i ))

                for j in range (widget .count ()):
                    item =widget .item (j )
                    if item :
                        data =item .data (Qt .UserRole )

                        _ ,icono_nuevo =self .geckonizar_nombre_e_icono (data ["nombre"])
                        if icono_nuevo :
                            item .setIcon (icono_nuevo )

                        item .setSizeHint (self .tamanio_geckotable )
        self .update ()
        self .repaint ()

        self .config ["estado_mutagenico"]={
        "tamanio_geckotable":[self .tamanio_geckotable .width (),self .tamanio_geckotable .height ()],
        "geckoiconsize":[self .geckoiconsize .width (),self .geckoiconsize .height ()],
        "font_geckotable":self .font_geckotable ,

        "tab_position":int (self .tabs .tabPosition ()),
        "IconThemeFolder":self .IconThemeFolder ,
        "geckosounds":self .geckosounds ,
        }

    def invocar_oraculo(self, query):
        """
        El Oráculo: Recibe la intención (query) y sincroniza la realidad (UI).
        """
        if not query:
            return

        query = query.lower()
        mejor_match = None
        target_tab_index = -1
        
        # 1. El Oráculo recorre las categorías buscando la verdad
        for i in range(self.tabs.count()):
            widget = self.tabs.widget(i)
            if isinstance(widget, GeckoList):
                for j in range(widget.count()):
                    item = widget.item(j)
                    data = item.data(Qt.UserRole)
                    if data and query in data["nombre"].lower():
                        # Encontró un match
                        mejor_match = item
                        target_tab_index = i
                        break
            if mejor_match: break

        # 2. Si hay coincidencia, la Nave se desplaza hacia ella
        if mejor_match and target_tab_index != -1:
            self.tabs.setCurrentIndex(target_tab_index)
            lista_activa = self.tabs.widget(target_tab_index)
            lista_activa.setCurrentItem(mejor_match)
            lista_activa.scrollToItem(mejor_match)
            self.play_sfx('dialog-information.oga') # Feedback sutil

    def refrescar_iconos_barra_inferior(self):
        """Actualización masiva de la barra inferior."""
        for btn, nombre_icono in self.botones_inferiores:
            ruta = os.path.join(self.IconPath, f"{nombre_icono}.png")
            btn.setIcon(QIcon(ruta))

    def toggle_solapas(self):
        """
        Refactor Toggle de Solapas - Método Vulkano Mejorado con Sincronización Visual
        By Ei2 - Team Cangurera
        """
        tab_bar = self.tabs.tabBar()
        tab_bar.setVisible(not tab_bar.isVisible())
        
        # Team Cangurera Position Paranoic
        self.asegurar_limites()

        # Data: "Sincronización inmediata para evitar el salto visual"
        self.ejecutar_consolidacion()

    # --- Inicia la Maquina de Estados Geckonicos
    def crear_pestana (self ,nombre_categoria ):
        """ Fábrica para clonar exactamente tu lista con geometría fija sagrada """
        nueva_lista = GeckoList(self)

        nueva_lista.setViewMode(QListWidget.IconMode )
        nueva_lista.setIconSize(self.geckoiconsize )
        nueva_lista.setGridSize(self.tamanio_geckotable )
        nueva_lista.setSpacing(self.espacing_geckotabs)
        nueva_lista.setUniformItemSizes(True)
        
        #nueva_lista .setResizeMode (QListWidget .Fixed ) #Deprecated by Ei2 Spatial Optimization
        # CAMBIO CLAVE: Usa 'Adjust' para que los elementos se 
        # auto-organicen sin que tengas que forzarlos después.
        nueva_lista.setResizeMode(QListWidget.Adjust)
        nueva_lista.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        nueva_lista.setAcceptDrops(True)
        nueva_lista.setDragDropMode(QListWidget .InternalMove)

        '''
        # Para configurar condiciones especificas matriciales ejemplo [3:4]
        # self.columnas = 3
        # self.filas = 4
        ancho_minimo = (self.columnas * self.tamanio_geckotable.width()) + ((self.columnas - 1) * self.espacing_geckotabs) + 5
        alto_minimo  = (self.filas * self.tamanio_geckotable.height()) + ((self.filas - 1) * self.espacing_geckotabs) + 5
        nueva_lista.setMinimumSize(ancho_minimo, alto_minimo)
        '''        
        nueva_lista.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff )
        nueva_lista.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff )

        self .aplicar_estilo_lista (nueva_lista ,nombre_categoria )

        ruta_hmx =os .path .join (self .scriptDir ,"hmx.py")
        if os .path .exists (ruta_hmx ):
            huevo =QListWidgetItem ("🐣\n\nhmx.py")
            huevo .setData (Qt .UserRole ,{"nombre":"hmx.py","ruta":ruta_hmx ,"consola":False ,"huevo":True })
            huevo .setSizeHint (self .tamanio_geckotable )
            nueva_lista .addItem (huevo )

        # en 1492 LINEAS EL CHAMAN LLEGA A LA ILUMINACION!!!
        #nueva_lista .itemDoubleClicked .connect (self .ejecutar_lanzador )
        nueva_lista .itemClicked .connect (self .ejecutar_lanzador )
        nueva_lista .model ().rowsMoved .connect (lambda :self .sincronizar_orden_lista (nueva_lista ))

        self .tabs .addTab (nueva_lista ,nombre_categoria )
        self .tabs .setCurrentWidget (nueva_lista )

        nueva_lista .viewport ().setContextMenuPolicy (Qt .CustomContextMenu )
        nueva_lista .viewport ().customContextMenuRequested .connect (
        lambda pos ,lw =nueva_lista :self ._on_context_menu_viewport (
        lw .viewport ().mapToGlobal (pos ),lw 
        )
        )

        return nueva_lista 

    def cambiar_lista_activa (self ,index ):
        """
        🦎✨ El Team Cangurera ha logrado que la burocracia de los layouts se lea como un haiku de precisión cuántica. 
        Redirecciona la variable global self.lista a la pestaña enfocada
        y realiza un auto ordenamiento inteligente, aun más que muchos OS ilógicos
        """
        widget_actual =self .tabs .widget (index )
        if widget_actual is None :
            return 

        if isinstance (widget_actual ,GeckoList ):
            self .lista =widget_actual 
            # Refrescar Geometría
            # Como ya estás dentro del widget actual, lo llamas directo:
            widget_actual.setResizeMode(QListWidget.Adjust)
            # Esperar a que la UI se asiente y forzar recálculo + volver a fijo (Leo - Team Cangurera)
            # Data y Spok a coro: -  Ilógico sería hacerlo sincrónico - Spok levantó una ceja, Data sonrrió
            # "Esto es clave para que los iconos se reorganicen al tamaño actual y luego se bloqueen hasta
            #  nuevos cambios en la estructura del plano de material de la geometria espacio-tiempo"
            QTimer.singleShot(37, lambda: widget_actual.resize(widget_actual.size())) # <--- LA LÍNEA MÁGICA
            #QTimer.singleShot(37, lambda: widget_actual.setResizeMode(QListWidget.Fixed)) # Bloquea de nuevo

        else :
            self .lista =None 

    def reordenar_categorias_dict (self ,from_index ,to_index ):
        """ Mantiene self.config['categorias'] en el mismo orden que las tabs """
        items =list (self .config ["categorias"].items ())
        item =items .pop (from_index )
        items .insert (to_index ,item )
        self .config ["categorias"]=dict (items )
        self .guardar_lanzadores ()

    def correccion_geckonica_gravedad (self ,index ):
        """
        Neurona de Lógica de Matriz (Index-Based).
        Ignora píxeles, usa la posición lógica en la grilla de 3 columnas.
        """
        global posicionPestanasGecko 

        columna =index %3 
        fila =index //3 

        if posicionPestanasGecko in (QTabWidget .North ,QTabWidget .South ):
            return (columna ,fila )

        else :
            return (fila ,columna )

    def sincronizar_orden_lista (self ,lista_widget ):
        global verFisicaGeckonica 

        lista_widget .blockSignals (True )
        lista_widget .model ().blockSignals (True )
        self .setUpdatesEnabled (False )

        try :
            nombre_tab =self .tabs .tabText (self .tabs .indexOf (lista_widget ))

            items_data =[]
            for i in range (lista_widget .count ()):
                data =lista_widget .item (i ).data (Qt .UserRole )
                if data and not data .get ("huevo"):
                    items_data .append (data )

            lista_widget .clear ()

            ruta_hmx =os .path .join (self .scriptDir ,"hmx.py")
            if os .path .exists (ruta_hmx ):
                huevo =QListWidgetItem ("🐣\n\nhmx.py")
                huevo .setData (Qt .UserRole ,{"nombre":"hmx.py","ruta":ruta_hmx ,"consola":False ,"huevo":True })
                huevo .setSizeHint (self .tamanio_geckotable )
                lista_widget .addItem (huevo )

            for data in items_data :
                self .agregar_item_lista (lista_widget ,data ["nombre"],data ["ruta"],data ["consola"],sync_config =False )

            lista_widget .setSizePolicy (QSizePolicy .Expanding ,QSizePolicy .Expanding )

            self .config ["categorias"][nombre_tab ]["items"]=items_data 
            self .guardar_lanzadores ()
            self .aplicar_estilo_lista (lista_widget ,nombre_tab )

            lista_widget .setMinimumSize (0 ,0 )
            lista_widget .setSizePolicy (QSizePolicy .Expanding ,QSizePolicy .Expanding )

        except Exception as e :
            print (f"❌ Error en la sincronización: {e}")

        finally :
            lista_widget .blockSignals (False )
            lista_widget .model ().blockSignals (False )
            self .setUpdatesEnabled (True )

    def agregar_item_lista (self ,lista_target ,nombre ,ruta ,usar_consola =False ,sync_config =True ):
        icono_visual ="💻"if usar_consola else "⚙"

        nombre_visible ,icono =self .geckonizar_nombre_e_icono (nombre )

        item =QListWidgetItem (nombre_visible )

        if icono is not None :
            item .setIcon (icono )
        else :
            emoji ="💻"if usar_consola else "⚙"
            item .setText (f"{emoji}\n\n{nombre_visible}")

        item .setData (Qt .UserRole ,{"nombre":nombre ,"ruta":ruta ,"consola":usar_consola })
        item .setTextAlignment (Qt .AlignCenter )
        item .setSizeHint (self .tamanio_geckotable )
        lista_target .addItem (item )

        if sync_config :
            nombre_tab =self .tabs .tabText (self .tabs .indexOf (lista_target ))
            if nombre_tab in self .config ["categorias"]:
                self .config ["categorias"][nombre_tab ]["items"].append ({"nombre":nombre ,"ruta":ruta ,"consola":usar_consola })

    def geckonizar_nombre_e_icono (self ,nombre_archivo ):
        base =nombre_archivo 

        if base .startswith ("geckolink_")and base .endswith (".sh"):
            base =base [len ("geckolink_"):-3 ]

        nombre_visible =(
        base 
        .replace ("_"," ")
        .replace ("-"," ")
        .title ()
        )

        ruta_icono =os .path .join (
        self .IconPath ,
        f"{base.lower()}.png"
        )

        icono =(
        QtGui .QIcon (ruta_icono )
        if os .path .exists (ruta_icono )
        else None 
        )

        return nombre_visible ,icono 

    def ejecutar_item_en_foco(self):
        item = self.lista.currentItem()

        if item:
            self.ejecutar_lanzador(item)

    # -------------------------------------------------------------------------------
    # --- WORKING ARROUN COGNITION GECKO OS SYSTEM TM
    # New 20/06/2026 for Cognitive Geckonic NAvigation System TM
    def ejecutar_lanzador(self, item):
        data = item.data(Qt.UserRole)
        ruta = data["ruta"]
        nombre = data.get("nombre", os.path.basename(ruta))

        if not os.path.exists(ruta):
            QMessageBox.warning(self, "🦎 Error", f"No existe: {ruta}")
            return

        try:
            os.chmod(ruta, 0o755)
        except PermissionError:
            pass

        # === LAUNCH ===
        proceso = None
        if data.get("consola"):
            terminal = shutil.which("xfce4-terminal") or shutil.which("x-terminal-emulator") or "xterm"
            proceso = subprocess.Popen([terminal, "-e", f"bash -c '{ruta}; exec bash'"])
            self.play_sfx('complete.oga')
        elif data.get("huevo"):
            proceso = subprocess.Popen([sys.executable, os.path.abspath(ruta)],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            proceso = subprocess.Popen([ruta], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # === REGISTRAR EN WATCHGECKO ===
        if proceso and hasattr(self, 'watchdog'):
            self.watchdog.registrar_pid(proceso.pid, nombre)

        # === TELEMETRÍA EN EL GRIMORIO (EvolZ06 - Sin fantasmas) ===
        data = item.data(Qt.UserRole)
        # Prioridad absoluta: Si el item conoce su origen, el origen es la verdad.
        # Si no, caemos en la pestaña actual (para items normales).
        nombre_cat = data.get("categoria_origen", self.tabs.tabText(self.tabs.currentIndex()))
        
        categoria = self.config["categorias"].get(nombre_cat)
        if categoria:
            stats = categoria.setdefault("stats", {})
            stats[ruta] = stats.get(ruta, 0) + 1
            self.guardar_lanzadores()
            
            # Refresco neuronal: Si la lista de intenciones existe, la obligamos a actualizarse
            if hasattr(self, 'lista_intenciones'):
                QTimer.singleShot(50, self.actualizar_intenciones_frecuentes)


        # === ACTUALIZAR PANEL INTENCIONES ===
        if hasattr(self, 'lista_intenciones'):
            QTimer.singleShot(50, self.actualizar_intenciones_frecuentes)

    def crear_pestana_intenciones_frecuentes(self):
        """
        EVZ6: No es clase. Es pestaña normal.
        Usa GeckoList = mismo widget, mismo menú derecho, mismo todo.
        Solo cambia el contenido: se llena del Sheison, no de items[]
        """
        lista = self.crear_pestana("🔥 Intenciones Frecuentes")
        self.lista_intenciones = lista # Guardar referencia
        
        # ESTA LÍNEA MATA EL MENÚ CONTEXTUAL PARA LOS CLONES
        lista.setContextMenuPolicy(Qt.NoContextMenu)  # ← UNA LÍNEA
        
        self.actualizar_intenciones_frecuentes()

    def actualizar_intenciones_frecuentes(self):
        """
        Clona TOP 13 desde el Grimorio.
        Usa GeckoList normal = menú derecho funciona automático.
        """
        if not hasattr(self, 'lista_intenciones'):
            return

        self.lista_intenciones.clear()
        eventos_globales = defaultdict(lambda: {"faa": 0, "nombre": "", "ruta": "", "categoria": ""})

        # Leer Sheison del Grimorio
        for nombre_tab, data_tab in self.config["categorias"].items():
            if nombre_tab == "🔥 Intenciones Frecuentes": # No contarse a sí misma
                continue

            stats = data_tab.get("stats", {})
            items = data_tab.get("items", [])
            mapa_items = {item["ruta"]: item for item in items}

            for ruta, conteo in stats.items():
                eventos_globales[ruta]["faa"] += conteo
                eventos_globales[ruta]["ruta"] = ruta
                eventos_globales[ruta]["categoria"] = nombre_tab

                if ruta in mapa_items:
                    eventos_globales[ruta]["nombre"] = mapa_items[ruta]["nombre"]
                    eventos_globales[ruta]["consola"] = mapa_items[ruta].get("consola", False)
                else:
                    eventos_globales[ruta]["nombre"] = os.path.basename(ruta)
                    eventos_globales[ruta]["consola"] = False

        # TOP 13 por FAA
        top = sorted(eventos_globales.items(),
                    key=lambda x: x[1]["faa"],
                    reverse=True)[:13]

        for ruta, data in top:
            if data["faa"] < 1:
                continue

            nombre = data["nombre"]
            faa = data["faa"]
            cat = data["categoria"]

            nombre_visible, icono = self.geckonizar_nombre_e_icono(nombre)
            item = QListWidgetItem(f"[X:{faa}]{nombre_visible}")
            item.setToolTip(f"Ejecuciones: {faa}\nCategoría original: {cat}\nRuta: {ruta}")
            item.setData(Qt.UserRole, {
                "ruta": ruta,
                "nombre": nombre,
                "consola": data.get("consola", False),
                "categoria_origen": cat 
            })

            tema_original = self.config["categorias"][cat].get("tema", {})
            if "color_fondo_item_activo" in tema_original:
                item.setBackground(QColor(tema_original["color_fondo_item_activo"]))
            if "color_texto_item_activo" in tema_original:
                item.setForeground(QColor(tema_original["color_texto_item_activo"]))


            if icono:
                item.setIcon(icono)
            else:
                item.setIcon(QIcon.fromTheme("applications-other"))

            item.setSizeHint(self.tamanio_geckotable)
            item.setTextAlignment(Qt.AlignCenter)
            self.lista_intenciones.addItem(item)
    
    def mostrar_alerta_geckonica(self, titulo, mensaje):
        """Interpelación Arkano-Minimalista."""
        reply = QMessageBox.question(self, titulo, mensaje,
                                    QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.No)
        if reply == QMessageBox.Yes:
            print(f"[WATCHGECKO] Usuario aceptó mutar. Acción manual requerida.")
    # -------------------------------------------------------------------------------

    # --- menu en Geckotabs ---
    def mostrar_menu_contextual (self ,pos_global ,lista_origen =None ):
        '''
        print("🔥 ORIGEN:", id(lista_origen), "SELF.LISTA:", id(self.lista))
        
        print("\n🧠 MENU REQUEST")
        print("   lista_origen:", lista_origen)
        print("   self.lista actual:", self.lista)
        print("   match:", lista_origen is self.lista)
        print("   type(lista_origen):", type(lista_origen))
        
        print("🔥 TAB ACTUAL:", self.tabs.currentIndex())
        print("🔥 WIDGET CURRENT:", self.tabs.currentWidget())
        print("🔥 lista_origen:", lista_origen)
        '''
        lista_activa =lista_origen or self .lista 
        if not lista_activa :return 
        pos_local =lista_activa .viewport ().mapFromGlobal (pos_global )
        item =lista_activa .itemAt (pos_local )

        menu =QMenu (None )
        # EVALUAR PORQUE SE CARGABA ACA O ELIMINAR SI HEREDA ESTILOS
        #menu .setStyleSheet (qdarkstyle .load_stylesheet (DarkPalette ))

        if item :
            data =item .data (Qt .UserRole )
            toggle_txt ="Desactivar Consola"if data ["consola"]else "Activar Consola"
            act_consola =QAction (toggle_txt ,self )
            act_consola .triggered .connect (lambda :self .toggle_consola (item ))
            menu .addAction (act_consola )

            menu_pintar =QMenu ("🎨 Tunear TabletasGecko",self )

            act_txt =QAction ("Color del texto",self )
            act_txt .triggered .connect (lambda :self .pintame (lista_activa ,"texto"))
            menu_pintar .addAction (act_txt )

            act_bg =QAction ("Color de fondo de lista",self )
            act_bg .triggered .connect (lambda :self .pintame (lista_activa ,"fondo"))
            menu_pintar .addAction (act_bg )

            menu_pintar .addSeparator ()

            act_sel =QAction ("Color de fondo al seleccionar",self )
            act_sel .triggered .connect (lambda :self .pintame (lista_activa ,"seleccion"))
            menu_pintar .addAction (act_sel )

            act_sel_txt =QAction ("Color de texto al seleccionar",self )
            act_sel_txt .triggered .connect (lambda :self .pintame (lista_activa ,"texto_seleccion"))
            menu_pintar .addAction (act_sel_txt )

            menu .addMenu (menu_pintar )

            menu .addSeparator ()
            act_eliminar =QAction ("❌ Eliminar Lanzador",self )
            act_eliminar .triggered .connect (lambda :self .eliminar_lanzador (item ))
            menu .addAction (act_eliminar )

        else :
            act_nuevo =QAction ("➕ Agregar archivo manualmente",self )
            act_nuevo .triggered .connect (self .agregar_manual )
            menu .addAction (act_nuevo )

            menu .addSeparator ()
            act_nueva_tab =QAction ("📁 Crear Nueva Categoría / Pestaña",self )
            act_nueva_tab .triggered .connect (self .agregar_categoria_dialog )
            menu .addAction (act_nueva_tab )

            if self .tabs .count ()>1 :
                act_borrar_tab =QAction ("🗑️ Eliminar esta Pestaña Actual",self )
                act_borrar_tab .triggered .connect (self .eliminar_pestana_actual )
                menu .addAction (act_borrar_tab )

        if menu .actions ():

            self .play_sfx ('bell.oga')
            menu .exec_ (pos_global )
        else :
            print ("⚠️ Menú sin acciones!")

    def toggle_consola (self ,item ):
        data =item .data (Qt .UserRole )
        data ["consola"]=not data ["consola"]
        item .setData (Qt .UserRole ,data )
        icono_visual ="💻"if data ["consola"]else "⚙️"
        item .setText (f"{icono_visual}\n\n{data['nombre']}")

        nombre_tab =self .tabs .tabText (self .tabs .currentIndex ())
        for script in self .config ["categorias"][nombre_tab ]["items"]:
            if script ["ruta"]==data ["ruta"]:
                script ["consola"]=data ["consola"]
                break 
        self .guardar_lanzadores ()

    def eliminar_lanzador (self ,item ):
        if not self .lista :return 
        data =item .data (Qt .UserRole )
        nombre_tab =self .tabs .tabText (self .tabs .currentIndex ())

        if nombre_tab in self .config ["categorias"]:
            self .config ["categorias"][nombre_tab ]["items"]=[
            d for d in self .config ["categorias"][nombre_tab ]["items"]if d ["ruta"]!=data ["ruta"]
            ]
        self .lista .takeItem (self .lista .row (item ))
        self .guardar_lanzadores ()

    def agregar_manual (self ):
        if not self .lista :return 
        ruta ,_ =QFileDialog .getOpenFileName (self ,"Seleccionar Script",os .path .expanduser ("~"))
        if ruta :
            nombre =os .path .basename (ruta )
            self .agregar_item_lista (self .lista ,nombre ,ruta ,usar_consola =False )
            self .guardar_lanzadores ()

    def agregar_categoria_dialog (self ):
        nombre ,ok =QInputDialog .getText (self ,"🦎 Nueva Categoría","Nombre de las GeckoTab:")
        if ok and nombre .strip ():
            nombre =nombre .strip ()
            self .config ["categorias"][nombre ]={"items":[],"tema":{"color_texto":"#00ff88","color_fondo_lista":"#000000","color_fondo_item_activo":"#00ff88","color_texto_item_activo":"#000000"}}
            self .crear_pestana (nombre )
            self .guardar_lanzadores ()

    def eliminar_pestana_actual (self ):
        index_actual =self .tabs .currentIndex ()
        if index_actual ==-1 :
            return 
        lista_actual =self .tabs .widget (index_actual )
        if isinstance (lista_actual ,QListWidget )and lista_actual .count ()>0 :
            boton_clickeado =QMessageBox .question (
            self ,"⚠️ Confirmación",
            "Esta pestaña tiene elementos dentro. ¿Deseas eliminarla por completo?",
            QMessageBox .Yes |QMessageBox .No ,QMessageBox .No 
            )
            if boton_clickeado ==QMessageBox .No :
                return 

        nombre_tab =self .tabs .tabText (index_actual )
        if nombre_tab in self .config ["categorias"]:
            del self .config ["categorias"][nombre_tab ]
        self .tabs .removeTab (index_actual )
        self .guardar_lanzadores ()

    def eliminar_categoria (self ,index ):
        self .tabs .setCurrentIndex (index )
        self .eliminar_pestana_actual ()

    def pintame (self ,lista_widget ,tipo_pintura ):
        if not isinstance (lista_widget ,GeckoList ):
            return False 

        nombre_tab =self .tabs .tabText (self .tabs .indexOf (lista_widget ))
        tema_tab =self .config ["categorias"][nombre_tab ]["tema"]

        mapa_claves ={
        'texto':'color_texto',
        'fondo':'color_fondo_lista',
        'seleccion':'color_fondo_item_activo',
        'texto_seleccion':'color_texto_item_activo'
        }

        clave =mapa_claves [tipo_pintura ]
        color_inicial =QColor (tema_tab .get (clave ,"#00ff88"))

        titulo ={
        'texto':"Texto de esta TabletaGecko",
        'fondo':"Fondo de esta TabletaGecko",
        'seleccion':"Fondo al seleccionar en esta Tableta",
        'texto_seleccion':"Texto al seleccionar en esta Tableta"
        }

        color_nuevo =QColorDialog .getColor (color_inicial ,self ,f"🦎 {titulo[tipo_pintura]}")
        if not color_nuevo .isValid ():
            return False 

        tema_temp =tema_tab .copy ()
        tema_temp [clave ]=color_nuevo .name ()

        if tema_temp ['color_texto']==tema_temp ['color_fondo_lista']:
            QMessageBox .warning (self ,"🦎 Ojo","Texto y fondo no pueden ser iguales en esta tableta.")
            return False 
        if tema_temp ['color_texto_item_activo']==tema_temp ['color_fondo_item_activo']:
            QMessageBox .warning (self ,"🦎 Ojo","Texto y fondo de selección no pueden ser iguales en esta tableta.")
            return False 

        self .config ["categorias"][nombre_tab ]["tema"][clave ]=color_nuevo .name ()

        self .aplicar_estilo_lista (lista_widget ,nombre_tab )
        self .guardar_lanzadores ()
        return True 

    # Funciones Guardame Originales con Metodos Funcionales  
    def guardar_lanzadores (self ):
        """ Ahora es trivial: solo guarda el dict que ya tenemos en memoria """
        with open (self .config_file ,'w',encoding ='utf-8')as f :
            json .dump (self .config ,f ,indent =4 ,ensure_ascii =False )
    
    def cargar_lanzadores (self ):
        if os .path .exists (self .config_file ):
            try :
                with open (self .config_file ,'r',encoding ='utf-8')as f :
                    config_cargada =json .load (f )

                if "categorias"in config_cargada :
                    for nombre_tab ,data in config_cargada ["categorias"].items ():

                        if isinstance (data ,list ):
                            config_cargada ["categorias"][nombre_tab ]={
                            "items":data ,
                            "tema":{
                            "color_texto":"#00ff88",
                            "color_fondo_lista":"#000000",
                            "color_fondo_item_activo":"#00ff88",
                            "color_texto_item_activo":"#000000"
                            }
                            }

                def merge_dicts (base ,nuevo ):
                    for k ,v in nuevo .items ():
                        if k in base and isinstance (base [k ],dict )and isinstance (v ,dict ):
                            merge_dicts (base [k ],v )
                        else :
                            base [k ]=v 
                merge_dicts (self .config ,config_cargada )

            except Exception as e :
                print (f"Error cargando config: {e}. Usando defaults.")
  
    # --- Eventos capturados por GeckoLAuncker para funcionalidades globales
    def event(self, event):
        # Detectamos cuando la ventana cambia de estado (maximizar, minimizar, restaurar)
        if event.type() == QEvent.WindowStateChange:
            # Usamos un pequeño timer (0ms) para que el cálculo corra 
            # EN EL PRÓXIMO CICLO del evento, cuando el SO ya terminó de ajustar.
            QTimer.singleShot(0, self.asegurar_limites)
            
        # Detectamos si la ventana fue movida por el usuario
        if event.type() == QEvent.Move:
            # Opcional: Si quieres que sea imposible moverla fuera de límites
            self.asegurar_limites()
            
        return super().event(event)

    def mousePressEvent (self ,event ):
        if event .button ()==Qt .LeftButton :
            self .offset =event .globalPosition ().toPoint ()-self .frameGeometry ().topLeft ()

    def mouseMoveEvent (self ,event ):
        if event .buttons ()==Qt .LeftButton and self .offset is not None :
            self .move (event .globalPosition ().toPoint ()-self .offset )

    def resizeEvent(self, event):
        """
        El resizeEvent solo marca el inicio de la inestabilidad.
        No ejecutamos lógica pesada aquí, solo iniciamos el temporizador.
        """
        super().resizeEvent(event)

        """
        Si estamos en modo dock, guardar el nuevo tamaño.
        if self.config.get('modo_dock', {}).get('activo', False):
            self.config['modo_dock']['ancho'] = self.width()
            self.config['modo_dock']['alto'] = self.height()
            self.guardar_config_en_json()
        """
        """
        Solo guarda la nueva geometría si estamos en un modo Dock activo.
        No mueve, solo recuerda.
        """
        super().resizeEvent(event)
        
        if self.gecko_dock_activo:
            if self.config.get('modo_dock', {}).get('activo', False):
                modo = self.config['modo_dock'].get('modo_actual')
                if modo:
                    geo = self.geometry()
                    self._guardar_geometria_dock(modo, int(geo.x()), int(geo.y()), int(geo.width()), int(geo.height()))
                    # Opcional: Print silencioso o solo guardar
                    print(f"💾 [MEMORIA ACTUALIZADA]: {modo} -> {geo.width()}x{geo.height()}")

        # Spock: "Esperamos a que el sistema se asiente."
        # Si el usuario sigue redimensionando, el timer se reinicia y 
        # nunca se ejecuta hasta que el usuario suelte el ratón.
        self.resize_timer.stop() 
        self.resize_timer.start(self.geckorefresh)

    # nuevo metodo para memorizar posicion en GeckoDock Mode
    def _guardar_geometria_dock(self, modo, x, y, w, h):
        """
        Helper minimalista para guardar en el Grimorio sin repetir código.
        """
        if 'modo_dock' not in self.config:
            self.config['modo_dock'] = {}
            
        # Clave dinámica: geometria_INF, geometria_SUP, etc.
        clave_geo = f'geometria_{modo}'
        
        self.config['modo_dock'][clave_geo] = {
            'x': x,
            'y': y,
            'w': w,
            'h': h
        }
        self.guardar_config_en_json()

    def focusInEvent(self, event):
        # Esto ocurre justo cuando la ventana recupera el foco
        super().focusInEvent(event)
        
        # Aquí puedes disparar tu lógica de "despertar"
        # Por ejemplo: refrescar el calendario o el F.A.A.
        print("🦎 La ventana ha recuperado el foco. Sincronizando entorno...")
        self.foco_en_el_oraculo()
        # Si quieres que la barra de búsqueda siempre sea la protagonista:
        # self.geckoSearch.setFocus()
        
        # Puedes reproducir un sfx sutil si el GeckoOS está despierto
        # self.play_sfx('startup.oga')
    
    def moveEvent(self, event):
        """
        GEOLOCALIZACIÓN GECKÓNICA EN TIEMPO REAL.
        Si el Modo Dock está ACTIVO y la ventana toca un borde, 
        se imanta automáticamente y RESTAURA la última geometría guardada.
        """
        if not self.gecko_dock_activo:
            super().moveEvent(event)
            return

        # --- SALIDA TEMPRANA: Si está maximizado, no hacer nada ---
        if self.isMaximized(): # no funciona se cuelga igual!!!
            super().moveEvent(event)
            return
        
        # 1. Verificar interruptor
        if not self.config.get('modo_dock', {}).get('activo', False):
            super().moveEvent(event)
            return

        # 2. Obtener datos limpios (todo convertido a int para evitar errores)
        pantalla = QApplication.primaryScreen()
        area = pantalla.availableGeometry()
        
        # Coordenadas actuales de la ventana
        geo = self.geometry()
        x = int(geo.x())
        y = int(geo.y())
        w = int(geo.width())
        h = int(geo.height())
        
        # Límites de pantalla (todo a int)
        screen_left = int(area.left())
        screen_right = int(area.right())
        screen_top = int(area.top())
        screen_bottom = int(area.bottom())
        
        # Margen de activación (pixeles de cercanía)
        margen = 30 
        
        modo_detectado = None
        geo_guardada = None

        # --- DETECCIÓN DE BORDES (AUTO-DOCK) ---
        
        # 1. BORDE INFERIOR
        if abs((screen_bottom - h) - y) <= margen:
            modo_detectado = 'INF'
            # Recuperar geometría guardada para este modo
            geo_guardada = self.config.get('modo_dock', {}).get('geometria_INF')
            
        # 2. BORDE SUPERIOR
        elif abs(screen_top - y) <= margen:
            modo_detectado = 'SUP'
            geo_guardada = self.config.get('modo_dock', {}).get('geometria_SUP')
            
        # 3. BORDE IZQUIERDO
        elif abs(screen_left - x) <= margen:
            modo_detectado = 'IZQ'
            geo_guardada = self.config.get('modo_dock', {}).get('geometria_IZQ')
            
        # 4. BORDE DERECHO
        elif abs((screen_right - w) - x) <= margen:
            modo_detectado = 'DER'
            geo_guardada = self.config.get('modo_dock', {}).get('geometria_DER')

        # --- EJECUCIÓN DEL SALTO CUÁNTICO ---
        if modo_detectado and geo_guardada:
            # ¡Autodock Detectado! Aplicar geometría histórica
            self.move(int(geo_guardada['x']), int(geo_guardada['y']))
            self.resize(int(geo_guardada['w']), int(geo_guardada['h']))
            print(f"🦎 [AUTODOCK DETECTADO]: [{modo_detectado}] -> Recuperando geometría guardada.")
            
            # Actualizar estado actual en el diccionario (para saber dónde estamos)
            self.config['modo_dock']['modo_actual'] = modo_detectado
            
        elif modo_detectado and not geo_guardada:
            # Primer vez que toca este borde: Guardar geometría ACTUAL como referencia futura
            self._guardar_geometria_dock(modo_detectado, x, y, w, h)
            print(f"🦎 [PRIMER CONTACTO]: [{modo_detectado}] -> Guardando geometría inicial.")
            self.config['modo_dock']['modo_actual'] = modo_detectado

        super().moveEvent(event)   

    # Nueva Version del Asistente Memóptico de Pegosidad Gecko-Screen
    def guardar_config_en_json(self):
        """
        Guardado Silencioso: Escribe el estado actual del diccionario en el Grimorio.
        Crea claves orgánicamente si no existen. Sin ruido, solo persistencia.
        """
        # --- AUDITORÍA 3: El Guardado Silencioso ---
        # Descomenta la siguiente línea si quieres ver CADA vez que guarda (puede ser mucho ruido)
        # print(f"💾 [GRIMORIO]: Escribiendo estado en {os.path.basename(self.config_file)}...")
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                # indent=4 mantiene el Grimorio legible para inspección manual si fuera necesario
                json.dump(self.config, f, indent=4, ensure_ascii=False)
        except IOError:
            # Silencio absoluto incluso en error (o log mínimo si es crítico)
            print(f"🦎 [ERROR CRÍTICO]: No se pudo escribir en el Grimorio: {e}")
            pass    
            
    # --- Princio y Fin del Geckonismo de la Aplicación
    def showEvent(self, event):
        super().showEvent(event)
        # Forzamos la posición cada vez que se muestra
        self.anclar_multiverso()

    def closeEvent (self ,event ):
        self .guardar_lanzadores ()

        # Al cerrar, detener watchdog de forma segura.
        if hasattr(self, 'watchdog'):
            self.watchdog.stop()

        event .accept ()


if __name__ =='__main__':
    app =QApplication (sys .argv )
    app .setStyleSheet (qdarkstyle .load_stylesheet (DarkPalette ))
    #app .setStyleSheet (qdarkstyle .load_stylesheet (LightPalette ))
    launcher =GeckoLauncker ()
    # Unificación de estilos: La única verdad es el string final
    estilo_gecko = """
        QWidget { background-color: #19232d; }
        QLabel, QPushButton, QComboBox, QCheckBox, QTabBar::tab, QGroupBox {
            font-family: "Ubuntu", sans-serif;
            font-weight: bold;
            font-size: 12px;
            color: #00ff88;
        }
    """
    launcher.setStyleSheet(estilo_gecko)
    launcher .show ()
    sys .exit (app .exec_ ())