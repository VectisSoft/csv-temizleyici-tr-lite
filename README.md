# CSV Temizleyici Lite — Türkçe Excel için CSV temizleme (MIT)

Tek dosyalık, bağımlılıksız Python aracı. CSV dosyasındaki fazla boşlukları, boş ve tekrar eden satırları temizler; **Türkçe Excel'in doğrudan açtığı biçimde** (UTF-8 BOM, `;` ayırıcı) yazar. Windows-1254 (Türkçe) kodlamalı dosyaları da okur.

## Kullanım
```
python csv_temizle_lite.py girdi.csv cikti.csv
```
Örnek: `ornekler/kirli.csv` → `ornekler/temiz.csv` (sentetik veri).

## Neden?
Türkçe Excel CSV'de noktalı virgül bekler; virgülle ayrılmış veya farklı kodlamalı dosyalar tek sütunda ya da bozuk karakterlerle açılabilir. (Excel'in Veri → Metinden/CSV'den sihirbazı da bunu elle çözer; bu araç aynı işi tek komutla, toplu ve tekrarlanabilir yapar.)

## Sınırlamalar
- Tarih ve sayı normalleştirme yok (aşağıya bakın)
- Düz CSV (`;` `,` veya sekme); .xlsx okumaz; çok büyük dosyalar için tasarlanmadı
- Yalnızca yerelde çalışır, ağ kullanmaz

## Tam sürüm
Tam paket (ücretli, ayrı lisans): tarih sütunlarını `yyyy-aa-gg`'ye, Türkçe sayıları (`1.234,56`) normalleştirme, `--ondalik`/`--ayirici` seçenekleri ve makrosuz **Olay Takip Excel şablonu**. Bağlantı, satış kanalı açıldığında buraya eklenecek.

## Lisans
MIT — bkz. `LICENSE`.
