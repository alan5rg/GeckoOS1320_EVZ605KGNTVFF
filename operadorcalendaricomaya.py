#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🦎 Operador Calendárico Maya
Gecko OS 13/20 — Tzolkin Edition

Transforma una fecha gregoriana en un estado cosmológico maya.

Ancla:
    GMT Correlation = 584283

Propiedades:
✓ Determinístico
✓ Sin estado persistente
✓ Recalculable desde cero
✓ Basado en aritmética modular
✓ Independiente de la interfaz gráfica
✓ Compatible con las ruedas calendaricas existentes

La cosmología se recalcula cada amanecer.

Compilado en tiempo real
y en el tiempo blando.
"""
import sys, os
from dataclasses import dataclass
import datetime


@dataclass(frozen=True)
class EstadoMaya:
    fecha_gregoriana: str
    julian_day: int
    delta_days: int

    baktun: int
    katun: int
    tun: int
    winal: int
    kin: int

    tzolkin_number: int
    tzolkin_name: str
    tzolkin_index: int

    haab_day: int
    haab_month: str
    haab_index: int

    night_lord: int

    @property
    def long_count(self):
        return (
            self.baktun,
            self.katun,
            self.tun,
            self.winal,
            self.kin
        )

    @property
    def long_count_str(self):
        return (
            f"{self.baktun}."
            f"{self.katun}."
            f"{self.tun}."
            f"{self.winal}."
            f"{self.kin}"
        )

    @property
    def tzolkin_str(self):
        return f"{self.tzolkin_number} {self.tzolkin_name}"

    @property
    def haab_str(self):
        return f"{self.haab_day} {self.haab_month}"

    @property
    def night_lord_str(self):
        return f"G{self.night_lord}"

    @property
    def angle_13(self):
        paso = 360.0 / 13.0
        return -(paso * (self.tzolkin_number - 1))

    @property
    def angle_20(self):
        paso = 360.0 / 20.0
        return paso * self.tzolkin_index


class OperadorCalendarioMaya:

    GMT_CORRELATION = 584283

    TZOLKIN_NAMES = [
        "Imix",
        "Ik'",
        "Ak'b'al",
        "K'an",
        "Chikchan",
        "Kimi",
        "Manik'",
        "Lamat",
        "Muluk",
        "Ok",
        "Chuwen",
        "Eb'",
        "B'en",
        "Ix",
        "Men",
        "K'ib'",
        "Kaban",
        "Etz'nab'",
        "Kawak",
        "Ajaw"
    ]

    HAAB_MONTHS = [
        "Pop",
        "Wo",
        "Sip",
        "Sotz'",
        "Sek",
        "Xul",
        "Yaxk'in",
        "Mol",
        "Ch'en",
        "Yax",
        "Sak'",
        "Keh",
        "Mak",
        "K'ank'in",
        "Muwan",
        "Pax",
        "K'ayab",
        "Kumk'u",
        "Wayeb'"
    ]

    # =====================================================
    # Día Juliano
    # =====================================================

    @staticmethod
    def gregorian_to_jd(fecha):

        a = (14 - fecha.month) // 12
        y = fecha.year + 4800 - a
        m = fecha.month + 12 * a - 3

        return (
            fecha.day
            + ((153 * m + 2) // 5)
            + (365 * y)
            + (y // 4)
            - (y // 100)
            + (y // 400)
            - 32045
        )

    # =====================================================
    # Cuenta Larga
    # =====================================================

    @staticmethod
    def long_count(delta):

        d = delta

        baktun = d // 144000
        d %= 144000

        katun = d // 7200
        d %= 7200

        tun = d // 360
        d %= 360

        winal = d // 20
        kin = d % 20

        return (
            baktun,
            katun,
            tun,
            winal,
            kin
        )

    # =====================================================
    # Tzolk'in
    # =====================================================

    @classmethod
    def tzolkin(cls, delta):

        number = ((delta + 3) % 13) + 1

        index = (delta + 19) % 20

        name = cls.TZOLKIN_NAMES[index]

        return (
            number,
            name,
            index
        )

    # =====================================================
    # Haab'
    # =====================================================

    @classmethod
    def haab(cls, delta):

        #
        # 0.0.0.0.0 = 8 Kumk'u
        #
        offset = 17 * 20 + 8

        posicion = (delta + offset) % 365

        if posicion >= 360:
            dia = posicion - 360
            return (
                dia,
                "Wayeb'",
                posicion
            )

        mes = posicion // 20
        dia = posicion % 20

        return (
            dia,
            cls.HAAB_MONTHS[mes],
            posicion
        )

    # =====================================================
    # Señor de la Noche
    # =====================================================

    @staticmethod
    def night_lord(delta):

        #
        # Ajuste para:
        # 18/06/2026 -> G4
        #
        return ((delta + 3) % 9) + 1

    # =====================================================
    # Constructor de estado
    # =====================================================

    @classmethod
    def from_date(cls, fecha):

        jd = cls.gregorian_to_jd(fecha)

        delta = jd - cls.GMT_CORRELATION

        baktun, katun, tun, winal, kin = (
            cls.long_count(delta)
        )

        tz_num, tz_name, tz_index = (
            cls.tzolkin(delta)
        )

        haab_day, haab_month, haab_index = (
            cls.haab(delta)
        )

        night = cls.night_lord(delta)

        return EstadoMaya(
            fecha_gregoriana=fecha.isoformat(),
            julian_day=jd,
            delta_days=delta,

            baktun=baktun,
            katun=katun,
            tun=tun,
            winal=winal,
            kin=kin,

            tzolkin_number=tz_num,
            tzolkin_name=tz_name,
            tzolkin_index=tz_index,

            haab_day=haab_day,
            haab_month=haab_month,
            haab_index=haab_index,

            night_lord=night
        )

    @classmethod
    def today(cls):
        return cls.from_date(
            datetime.date.today()
        )


if __name__ == "__main__":

    maya = OperadorCalendarioMaya.today()

    print("🦎 Gecko OS 13/20 — Tzolkin Edition")
    print("-----------------------------------")
    print("Fecha Gregoriana :", maya.fecha_gregoriana)
    print("Julian Day       :", maya.julian_day)
    print("Delta Days       :", maya.delta_days)
    print("Cuenta Larga     :", maya.long_count_str)
    print("Tzolk'in         :", maya.tzolkin_str)
    print("Haab'            :", maya.haab_str)
    print("Señor Noche      :", maya.night_lord_str)
    print("Ángulo rueda 13  :", maya.angle_13)
    print("Ángulo rueda 20  :", maya.angle_20)