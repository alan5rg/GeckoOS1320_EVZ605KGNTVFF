#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# qt_compat.py - MUTAGÉNICO INTERDIMENSIONAL v5.0 GECKOSTABLE
# Soporta PyQt5, PyQt6 y PySide6 con la misma API
# Monkey Python Coding Circus by Alan.RG Systemas & Team Cangurera c.2026

QT_LIB = None
QtWidgets = QtCore = QtGui = QtMultimedia = None

# Intentamos en orden: PyQt6 -> PySide6 -> PyQt5
for lib in ["PyQt6", "PySide6", "PyQt5"]:
    try:
        if lib == "PyQt6":
            from PyQt6 import QtWidgets, QtCore, QtGui, QtMultimedia
        elif lib == "PySide6":
            from PySide6 import QtWidgets, QtCore, QtGui, QtMultimedia
        else:
            from PyQt5 import QtWidgets, QtCore, QtGui, QtMultimedia
        QT_LIB = lib
        break
    except ImportError:
        continue

if QT_LIB is None:
    raise ImportError(
        "GECKO PANIC: No se encontró PyQt5, PyQt6 ni PySide6.\n"
        "Instalá uno: pip install PyQt5"
    )

# --- PARCHES DE COMPATIBILIDAD INTERDIMENSIONAL ---

# PyQt6: exec_ -> exec
if QT_LIB == "PyQt6":
    QtCore.QEventLoop.exec_ = QtCore.QEventLoop.exec
    QtWidgets.QApplication.exec_ = QtWidgets.QApplication.exec
    # PyQt6 movió enums: Qt.ScrollBarAsNeeded -> Qt.ScrollBarPolicy.ScrollBarAsNeeded
    if not hasattr(QtCore.Qt, 'ScrollBarAsNeeded'):
        QtCore.Qt.ScrollBarAsNeeded = QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded
        QtCore.Qt.ScrollBarAlwaysOff = QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff

# PySide6: pyqtSignal -> Signal
if QT_LIB == "PySide6":
    QtCore.pyqtSignal = QtCore.Signal
    QtCore.pyqtSlot = QtCore.Slot
    # PySide6 también cambió enums
    if not hasattr(QtCore.Qt, 'ScrollBarAsNeeded'):
        QtCore.Qt.ScrollBarAsNeeded = QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded
        QtCore.Qt.ScrollBarAlwaysOff = QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff

# --- RE-EXPORTS PARA EL VALLESIANO ---

# QtWidgets
QApplication = QtWidgets.QApplication
QMainWindow = QtWidgets.QMainWindow
QWidget = QtWidgets.QWidget
QListWidget = QtWidgets.QListWidget
QListWidgetItem = QtWidgets.QListWidgetItem
QSizePolicy = QtWidgets.QSizePolicy
QVBoxLayout = QtWidgets.QVBoxLayout
QHBoxLayout = QtWidgets.QHBoxLayout
QGridLayout = QtWidgets.QGridLayout
QGroupBox = QtWidgets.QGroupBox
QLabel = QtWidgets.QLabel
QMenu = QtWidgets.QMenu
QAction = QtWidgets.QAction
QColorDialog = QtWidgets.QColorDialog
QFileDialog = QtWidgets.QFileDialog
QTabWidget = QtWidgets.QTabWidget
QInputDialog = QtWidgets.QInputDialog
QMessageBox = QtWidgets.QMessageBox
QSlider = QtWidgets.QSlider
QComboBox = QtWidgets.QComboBox
QPushButton = QtWidgets.QPushButton
QCheckBox = QtWidgets.QCheckBox
QButtonGroup = QtWidgets.QButtonGroup
QScrollArea = QtWidgets.QScrollArea
QLineEdit = QtWidgets.QLineEdit 

# QtCore
Qt = QtCore.Qt
QSize = QtCore.QSize
QPoint = QtCore.QPoint
QTimer = QtCore.QTimer
QUrl = QtCore.QUrl
QEvent = QtCore.QEvent
QThread = QtCore.QThread
pyqtSignal = QtCore.pyqtSignal
QMutex = QtCore.QMutex
QMutexLocker = QtCore.QMutexLocker


# QtGui - Exportamos el módulo entero para QtGui.QIcon, etc
QtGui = QtGui
QPainter = QtGui.QPainter
QBrush = QtGui.QBrush
QColor = QtGui.QColor
QIcon = QtGui.QIcon
QPixmap = QtGui.QPixmap
QFont = QtGui.QFont
QKeySequence = QtGui.QKeySequence

# QtMultimedia - Para sonidos pleyadianos
QMediaPlayer = QtMultimedia.QMediaPlayer
QMediaContent = QtMultimedia.QMediaContent

def get_qt_version():
    return QT_LIB

print(f"[MUTAGENICO COMPATIBLE] Corriendo en {QT_LIB} - Túnel cuántico estable")