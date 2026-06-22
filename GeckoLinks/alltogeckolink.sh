#!/bin/bash

# Script simple: Solo añade geckolink_ si falta
# No modifica archivos que ya empiecen con "geckolink_"

echo "Escaneando directorio: $(pwd)"

for archivo in *.sh; do
    # Salir si no hay archivos .sh
    [ -e "$archivo" ] || break

    # Omitir el propio script
    if [ "$archivo" == "$(basename "$0")" ]; then
        chmod +x "$archivo"
        continue
    fi

    # CONDICIÓN CLAVE: Solo procesar si NO empieza con "geckolink_"
    if [[ "$archivo" != geckolink_* ]]; then
        nuevo_nombre="geckolink_${archivo}"
        
        # Verificar conflicto antes de mover
        if [ -e "$nuevo_nombre" ]; then
            echo "SKIP (conflicto): $archivo (ya existe $nuevo_nombre)"
        else
            mv "$archivo" "$nuevo_nombre"
            chmod +x "$nuevo_nombre"
            echo "RENOMBRADO: $archivo -> $nuevo_nombre"
        fi
    else
        # Ignoramos todo lo que ya tenga el prefijo (correcto o corrupto)
        echo "OMITIDO: $archivo (ya contiene prefijo)"
    fi
done

echo "Proceso finalizado. Revisa manualmente los archivos omitidos si es necesario."   