#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# GeckoOSmain.py
# Monkey Python Coding Circus by Alan.RG Systemas & Team Cangurera c.2026

import sys
from PyQt5.QtWidgets import QApplication

# GeckoOS DistroCodeNAme
from GeckoOS1320EVZ605KGNTVFF import GeckoLauncker

import qdarkstyle
from qdarkstyle import DarkPalette

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(DarkPalette))

    estilo_gecko = """
        QWidget { background-color: #19232d; }
        QLabel, QPushButton, QComboBox, QCheckBox, QTabBar::tab, QGroupBox {
            font-family: "Ubuntu", sans-serif;
            font-weight: bold;
            font-size: 12px;
            color: #00ff88;
        }
    """
    
    # El Principio de la Navegación
    GeckoOS = GeckoLauncker()
    # Lo Maquillamos para salir a Escena
    GeckoOS.setStyleSheet(estilo_gecko)
    # Gecko Sale al Escenario
    GeckoOS.show()

    sys.exit(app.exec_())