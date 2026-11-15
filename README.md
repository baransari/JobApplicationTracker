# İş Başvurusu Takip Sistemi

Python ve SQLite kullanılarak hazırlanmış, terminal üzerinden çalışan basit bir iş başvurusu takip uygulaması.

## Özellikler

- İş başvurusu ekleme
- Kayıtlı başvuruları listeleme
- Başvuru durumunu güncelleme
- Boş veya geçersiz başvuru bilgilerini reddetme
- Aynı başvuru kodunun tekrar eklenmesini önleme
- Başvuru kodu bulunamadığında kullanıcıya hata gösterme
- Başvuruları SQLite veritabanında saklama

## Kullanılan teknolojiler

- Python 3
- SQLite (`sqlite3`)
- Python standart kütüphanesi (`dataclasses`, `datetime`, `unittest`)

Harici paket kurulumu gerekmez.

## Projeyi çalıştırma

Proje klasöründe terminal açıp şu komutu çalıştırın:

```bash
python3 main.py
```

Program ilk açıldığında `applications.db` veritabanı dosyası ve gerekli tablo otomatik oluşturulur. Menüden başvuruları görüntüleyebilir, yeni başvuru ekleyebilir, başvuru durumunu güncelleyebilir veya programdan çıkabilirsiniz.

## Başvuru bilgileri

Başvuru tarihi `YYYY-MM-DD` biçiminde girilmelidir. Not alanı isteğe bağlıdır.

Kabul edilen durumlar:

- `applied`
- `interview`
- `offer`
- `rejected`
- `withdrawn`

## Testleri çalıştırma

Proje klasöründe şu komutu çalıştırın:

```bash
python3 -m unittest discover -s tests
```

## Dosyaların görevi

- `main.py`: Programı başlatır ve menü seçimlerini ilgili işlevlere yönlendirir.
- `cli.py`: Kullanıcıdan bilgi alır ve başvuruları terminalde gösterir.
- `models.py`: `JobApplication` veri modelini ve alan kontrollerini içerir.
- `storage.py`: SQLite veritabanını hazırlar; başvuruları ekler, okur ve durumlarını günceller.
- `tests/`: Model ve veritabanı işlevleri için otomatik testleri içerir.
