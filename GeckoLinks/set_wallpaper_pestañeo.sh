#!/bin/bash
# -----------------------------------------------------------------------------
# 🦎 GECKO OS SUBSYSTEM - PESTAÑEO WALLPAPER INJECTOR (NATIVE XFCE)
# -----------------------------------------------------------------------------

# 1. El script descubre dónde está parado y calcula la raíz del proyecto
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# 2. Capturar el nombre del archivo desde la variable de entorno de Python
NOMBRE_ARCHIVO="$GECKOWALL_FILE"

# 3. Construir la ruta absoluta real del wallpaper
WALLPAPER_PATH="${PROJECT_ROOT}/GeckoWall/${NOMBRE_ARCHIVO}"

# Control de Flujo: Validar que la variable no esté vacía y que el archivo exista
if [ -z "$NOMBRE_ARCHIVO" ] || [ ! -f "$WALLPAPER_PATH" ]; then
    echo "❌ Error Subsistema: Archivo no encontrado en: $WALLPAPER_PATH"
    exit 1
fi

echo "🎨 Inyectando fondo de pantalla: $WALLPAPER_PATH"

# 4. Modificar la Matrix de Escritorio de XFCE
PROPIEDADES_XFCE=$(xfconf-query -c xfce4-desktop -p /backdrop -l 2>/dev/null | grep "last-image")

for propiedad in $PROPIEDADES_XFCE; do
    xfconf-query -c xfce4-desktop -p "$propiedad" -s "$WALLPAPER_PATH"
done

exit 0
