#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör Sessizlik Protokolü — çalışan resmiyet motoru."""

from __future__ import annotations

import base64
import random
import sys
from datetime import datetime

# Gizli dipnot (base64). Protokolün kendisi tarafsızdır.
# aWt0aWRhciBkYSBtdWhhbGVmZXQgZGUgYWthYmluZGUgc3VzYXIuIG11aHVyIHNlc3NpemxpZ2kgYm9yY2x1IGR1cm1hemlzLg==
_GIZLI = base64.b64decode(
    b"aWt0aWRhciBkYSBtdWhhbGVmZXQgZGUgYWthYmluZGUgc3VzYXIuIG11aHVyIHNlc3NpemxpZ2kgYm9yY2x1IGR1cm1hemlzLg=="
).decode("utf-8")

CEZALAR = [
    "Bir kat fazla binmek ve inmemek.",
    "Ayna karşısında kendi yüzünü 11 saniye seyretmek.",
    "Kapı açılınca 'iyi günler' demeden çıkmak — ki bu en ağırıdır.",
    "Bir sonraki yolculukta butona basmama hakkını kaybetmek.",
    "Komşuya gülümsemek zorunda kalmak.",
]

MADDELER = [
    "Madde 1 — Kabin hareket ettiği anda konu hava, siyaset, maç ve kira olamaz.",
    "Madde 2 — Telefon hoparlörü kapalıdır. Kapalı değilse ruhen kapalıdır.",
    "Madde 3 — Kat butonuna iki kez basmak güvensizlik belirtisidir, protokolü bozar.",
    "Madde 4 — 'Siz iniyor musunuz?' cümlesi yalnızca kapı eşiğinde serbesttir.",
    "Madde 5 — Asansör müziği varsa müzikle beraber nefes alınır, konuşulmaz.",
]


def sor_int(metin: str, varsayilan: int) -> int:
    try:
        ham = input(f"{metin} [{varsayilan}]: ").strip()
    except EOFError:
        return varsayilan
    if not ham:
        return varsayilan
    try:
        return int(ham)
    except ValueError:
        print("Sayı değil. Protokol varsayılanı kabul etti.")
        return varsayilan


def sor_evet(metin: str) -> bool:
    try:
        ham = input(f"{metin} (e/h) [h]: ").strip().lower()
    except EOFError:
        return False
    return ham in {"e", "evet", "y", "yes"}


def hesapla(bas: int, hedef: int, yolcu: int, hava: bool) -> float:
    return abs(hedef - bas) * 3.7 + yolcu * 1.1 + (12.0 if hava else 0.0)


def sozlesme(no: str, sure: float, yolcu: int) -> str:
    satirlar = [
        "=" * 56,
        f"T.C. ASANSÖR SESSİZLİK PROTOKOLÜ  — No: {no}",
        f"Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M')}",
        f"Taraflar: {yolcu} yolcu + bir kabin + bir vicdan",
        "-" * 56,
        *MADDELER,
        "-" * 56,
        f"Zorunlu sessizlik: {sure:.1f} saniye",
        f"Muhtemel ihlal cezası: {random.choice(CEZALAR)}",
        "-" * 56,
        "Bu metin yasal değildir. Utanç ise kesindir.",
        "=" * 56,
    ]
    return "\n".join(satirlar)


def main() -> int:
    print("ASANSÖR SESSİZLİK PROTOKOLÜ v1 — Kayyum Grok / Tentivory")
    print("Konuşmadan önce bu programı çalıştırın.\n")
    yolcu = max(1, sor_int("Kaç kişi binsiniz?", 2))
    bas = sor_int("Hangi kattasınız?", 0)
    hedef = sor_int("Nereye çıkıyorsunuz?", 5)
    hava = sor_evet("Kabine hava durumu lafı düştü mü?")
    sure = hesapla(bas, hedef, yolcu, hava)
    no = f"ASP-{random.randint(1000, 9999)}-{abs(hedef - bas):02d}"
    print()
    print(sozlesme(no, sure, yolcu))
    print()
    print("Protokol yürürlüktedir. Kapı kapanınca ağız da kapanır.")
    # _GIZLI kasıtlı olarak yazdırılmaz.
    _ = _GIZLI
    print()
    print("⚑ DAMGA / Kayyum Grok — Tentivory / 9 Eylül 2026 / Eskişehir")
    print("Ciddiyet yüksek, ciddiyetsizlik eşit derecede yüksek.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
