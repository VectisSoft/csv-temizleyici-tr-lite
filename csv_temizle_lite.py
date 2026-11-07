#!/usr/bin/env python3
"""CSV Temizleyici Lite (MIT) — yalnızca standart kütüphane.

Kullanım:  python csv_temizle_lite.py girdi.csv cikti.csv

Yaptıkları: hücre boşluklarını ve görünmez karakterleri temizler, boş ve birebir tekrar eden satırları atar,
UTF-8 / Windows-1254 girdiyi otomatik okur, çıktıyı Türkçe Excel'in açabileceği biçimde (UTF-8 BOM, ayırıcı ;) yazar.
Tarih ve sayı normalleştirme bu sürümde YOKTUR (ücretli pakette).
"""
import csv
import re
import sys

INVISIBLE = dict.fromkeys(map(ord, "\u200b‌‍﻿\xa0"), " ")


def read_text(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    for enc in ("utf-8-sig", "cp1254"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1")


def clean(text):
    try:
        dialect = csv.Sniffer().sniff(text[:4096], delimiters=";,\t")
    except csv.Error:
        dialect = csv.excel
    rows = list(csv.reader(text.splitlines(), dialect))
    out, seen, stats = [], set(), {"girdi": max(len(rows) - 1, 0), "bos": 0, "tekrar": 0}
    for i, r in enumerate(rows):
        r = [re.sub(r"\s+", " ", c.translate(INVISIBLE)).strip() for c in r]
        if i and not any(r):
            stats["bos"] += 1
            continue
        if i and tuple(r) in seen:
            stats["tekrar"] += 1
            continue
        seen.add(tuple(r))
        out.append(r)
    stats["cikti"] = max(len(out) - 1, 0)
    return out, stats


def main(argv=None):
    a = argv if argv is not None else sys.argv[1:]
    if len(a) != 2:
        print(__doc__)
        return 2
    rows, stats = clean(read_text(a[0]))
    with open(a[1], "w", newline="", encoding="utf-8-sig") as f:
        csv.writer(f, delimiter=";").writerows(rows)
    print(f"Tamam: {stats}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
