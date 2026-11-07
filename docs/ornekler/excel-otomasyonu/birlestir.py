"""Klasordeki satis_*.csv dosyalarini birlestirir, Ozet sayfasi (urun bazinda toplam) olan xlsx yazar. Python 3 + openpyxl."""
import csv
import sys
from collections import defaultdict
from pathlib import Path

from openpyxl import Workbook

girdi, cikti = Path(sys.argv[1]), sys.argv[2]
wb = Workbook(); ws = wb.active; ws.title = "Birlesik"
ws.append(["Tarih", "Sube", "Urun", "Adet", "Tutar"])
toplam = defaultdict(lambda: [0, 0.0])
for p in sorted(girdi.glob("satis_*.csv")):
    with open(p, encoding="utf-8-sig", newline="") as f:
        r = csv.reader(f, delimiter=";"); next(r)
        for t, s, u, a, tu in r:
            tu = float(tu.replace(",", ".")); ws.append([t, s, u, int(a), tu])
            toplam[u][0] += int(a); toplam[u][1] += tu
oz = wb.create_sheet("Ozet"); oz.append(["Urun", "Adet", "Tutar"])
for u, (a, tu) in sorted(toplam.items()): oz.append([u, a, round(tu, 2)])
wb.save(cikti)
