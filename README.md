# Server Loglarının Təhlil Aləti

Bu layihə server loglarını təhlil edərək uğursuz giriş cəhdlərini aşkar edir və onları məlum təhdid IP-ləri ilə müqayisə edir. Nəticələr müxtəlif formatlarda (JSON, mətn və CSV) saxlanılır.

## Xüsusiyyətlər
- **Uğursuz giriş cəhdlərini** (4xx status kodları) server loglarından çıxarır.
- Loglardakı IP-ləri məlum **təhdid IP-ləri** ilə müqayisə edir.
- Nəticələri aşağıdakı formatlarda saxlayır:
  - JSON formatında strukturlaşdırılmış məlumat üçün.
  - Mətn faylı insan tərəfindən oxuna bilən xülasələr üçün.
  - CSV faylı detallı log məlumatları üçün.

## Fayl Strukturu
- `server_logs.txt`: Təhlil ediləcək server log faylı.
- `index.html`: Məlum təhdid IP-lərini saxlayan HTML faylı.
- Çıxış faylları:
  - `failed_logins.json`: 5-dən çox uğursuz giriş cəhdi olan IP-lər.
  - `threat_ips.json`: Məlum təhdid IP-ləri ilə uyğun gələn IP-lər.
  - `combined_security_data.json`: Hər iki məlumatın birləşdirilmiş JSON faylı.
  - `log_analysis.txt`: Uğursuz giriş cəhdlərinin mətn xülasəsi.
  - `log_analysis.csv`: Təhlil edilmiş bütün log məlumatlarını əks etdirən CSV faylı.

## Necə İstifadə Etmək Olar?
1. Log faylınızı (`server_logs.txt`) və təhdid faylınızı (`index.html`) uyğun yerlərə yerləşdirin.
2. Skripti işə salın:
   ```bash
   python your_script_name.py
Nəticələri output qovluğunda tapın.
Tələblər
Python 3.x
Modullar:
re
json
csv
collections.Counter
Kodun İcmalı
Əsas Funksiyalar
Log Təhlili üçün Regex:

python
Copy code
log_pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(\w+) .*?" (4\d{2})'
Çıxarır:

IP ünvanı
Tarix
HTTP metodu
Status kodu
Təhdid IP-lərinin Uyğunluğu: Log faylındakı IP-ləri index.html-də olan IP-lərlə müqayisə edir.

Çıxış Formatları:

JSON: Strukturlaşdırılmış məlumatların saxlanması üçün.
Mətn: Uğursuz girişlərin xülasəsi üçün.
CSV: Detallı log məlumatlarının saxlanması üçün.
