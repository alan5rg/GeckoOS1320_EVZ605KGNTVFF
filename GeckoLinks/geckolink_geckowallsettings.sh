#!/bin/bash
# -----------------------------------------------------------------------------
# 🦎 LANZADOR MAESTRO XUBUNTU (XFCE) - EDICIÓN GECKÓNICA
# -----------------------------------------------------------------------------
# Centraliza todas las configuraciones vitales: desde el fondo de pantalla 
# hasta las redes neuronales del sistema (y la energía).
# -----------------------------------------------------------------------------

echo "🦎 Iniciando protocolos de configuración Xubuntu..."

# --- MENÚ DE DESPLIEGUE RÁPIDO ---
# Descomentá (sacá el #) la línea que quieras ejecutar.
# Si dejás todo comentado, no pasa nada. Si ponés varios, se abren todos.

echo "🚀 Despegando módulos..."

# 1. 🖼️  ESCRITORIO Y FONDO (Lo visual importante)
# Abre directamente la gestión de fondos, iconos y menú del escritorio.
xfce4-settings-manager --dialog xfce-backdrop-settings   

# 2. 📺  DISPLAY Y GEOMETRÍA (La resolución y escalado)
# Aquí se configura la resolución, frecuencia y disposición de monitores.
# (Para vos, esto es parte vital del "Fondo de Pantalla")
#xfce4-display-settings &

# 3. 🎨  APARIENCIA GENERAL (Temas y Ventanas)
# Cambia el tema de las ventanas (GTK), iconos del sistema y fuentes.
#xfce4-appearance-settings &

# 4. 🌐  REDES Y CONEXIONES (El entorno de red)
# Abre el editor de conexiones (WiFi, Ethernet, VPN, DNS).
# Este es el comando "oculto" más útil para redes en XFCE.
#nm-connection-editor &

# 5. 🔌  ENERGÍA Y BATERÍA (Suspensión y Tapa)
# Configura qué pasa al cerrar la tapa, ahorro de energía y brillo.
#xfce4-power-manager-settings &

# 6. ⌨️  PERIFÉRICOS E INPUT
# Configuración de Teclado (incluye atajos de teclado) y Mouse.
#xfce4-keyboard-settings &
#xfce4-mouse-settings &

# 7. 🎵  SONIDO Y AUDIO
# Configuración de entradas, salidas y eventos de sonido.
#pavucontrol & 
# Nota: Usa 'pavucontrol' (PulseAudio Volume Control) si está instalado, 
# es más completo que el mixer por defecto. Si no, usá:
# xfce4-mixer &

# 8. 🧰  GESTOR COMPLETO (Por si te faltó algo)
# Abre el panel central con TODAS las opciones anteriores y más.
#xfce4-settings-manager &

echo "✅ Todos los sistemas lanzados en segundo plano. ¡A configurar!"   