#!/bin/bash

# Script de reparación específica para corrupción "geckolink_ckolink_"
# Elimina la parte corrupta y deja el nombre inmaculado: geckolink_[archivo].sh

echo "Iniciando reparación específica en: $(pwd)"

# Cadena corrupta detectada en tu sistema (18 caracteres)
CORRUPTO="geckolink_ckolink_"
LEN_CORRUPTO=${#CORRUPTO}

for archivo in *.sh; do
    # Salir si no hay archivos .sh
    [ -e "$archivo" ] || break

    # Omitir el propio script
    if [ "$archivo" == "$(basename "$0")" ]; then
        chmod +x "$archivo"
        continue
    fi

    nombre_final="$archivo"

    # 1. DETECCIÓN Y LIMPIEZA ESPECÍFICA
    # Solo actuamos si el archivo empieza EXACTAMENTE con la cadena corrupta conocida
    if [[ "$archivo" == ${CORRUPTO}* ]]; then
        # Extraemos el nombre real quitando los primeros 18 caracteres
        nombre_base="${archivo:$LEN_CORRUPTO}"
        
        # Validación de seguridad: el nombre base no debe estar vacío y debe terminar en .sh
        if [ -n "$nombre_base" ] && [[ "$nombre_base" == *.sh ]]; then
            nombre_final="geckolink_${nombre_base}"
            echo "REPARANDO: '$archivo' -> '$nombre_final'"
        else
            echo "ERROR DE SEGURIDAD: Ignorando '$archivo' (nombre base inválido tras limpieza)."
            continue
        fi
    else
        # Si no está corrupto, lo dejamos tal cual (o solo le damos permisos si ya es geckolink_ limpio)
        if [[ "$archivo" == geckolink_* ]]; then
            echo "OK: '$archivo' (Nombre válido, solo verificando permisos)"
        else
            echo "INFO: '$archivo' (No tiene prefijo geckolink_, se omite en esta reparación)"
            continue
        fi
    fi

    # 2. RENOMBRADO SEGURO
    if [ "$archivo" != "$nombre_final" ]; then
        if [ -e "$nombre_final" ]; then
            echo "CONFLICTO: No se renombra '$archivo' porque ya existe '$nombre_final'"
        else
            mv "$archivo" "$nombre_final"
        fi
    fi

    # 3. ASEGURAR EJECUCIÓN
    chmod +x "$nombre_final"
done

echo "Reparación finalizada. Verifica que los nombres sean ahora geckolink_[nombre].sh"   