#!/bin/bash
# -----------------------------------------------------------------
# Launcher de Configuración Xubuntu (XFCE) - Team Cangurera Style
# -----------------------------------------------------------------

echo "🦎 Iniciando componentes de Xubuntu..."

# Opción A: Abre el Administrador de Configuración General completo
xfce4-settings-manager &

# --- BONUS TRACKS (Por si querés lanzar paneles específicos sueltos) ---
# Descomentá (sacale el #) al que quieras usar si preferís ir directo:

# xfce4-display-settings &      # Configuración de Pantalla/Monitores
# xfce4-mouse-settings &        # Configuración de Mouse y Touchpad
# xfce4-keyboard-settings &     # Configuración de Teclado y Atajos
# xfce4-appearance-settings &   # Apariencia (Temas, Iconos, Tipografías)

echo "🚀 Componentes lanzados en segundo plano."