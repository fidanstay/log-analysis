import re
import json
import csv
from collections import Counter

# Fayl adları
log_file = 'c:\\Users\\Admin\\Desktop\\lab1\\server_logs.txt'
threat_file = 'c:\\Users\\Admin\\Desktop\\lab1\\index.html'

# 4xx status kodları üçün regex
log_pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(\w+) .*?" (4\d{2})'

# Təhdid IP-lərini HTML-dən oxumaq
with open(threat_file, 'r') as tf:
    threat_ips = re.findall(r'<td>(\d+\.\d+\.\d+\.\d+)</td>', tf.read())

# Log analiz və uğursuz girişlərin sayılması
failed_attempts = Counter()
log_entries = []

with open(log_file, 'r') as lf:
    for line in lf:
        match = re.search(log_pattern, line)
        if match:
            ip, date, method, status = match.groups()
            log_entries.append({'IP': ip, 'Date': date, 'Method': method, 'Status': status})
            failed_attempts[ip] += 1

# 5-dən çox uğursuz giriş edən IP-lər
failed_logins = {ip: count for ip, count in failed_attempts.items() if count > 5}

# Təhdid IP-ləri ilə uyğun gələnlər
matched_threat_ips = [entry['IP'] for entry in log_entries if entry['IP'] in threat_ips]

# JSON fayllarını yazmaq
json.dump(failed_logins, open('failed_logins.json', 'w'), indent=4)
json.dump(matched_threat_ips, open('threat_ips.json', 'w'), indent=4)

# Combined təhlükəsizlik məlumatlarını birləşdirmək
combined_data = {
    "failed_logins": failed_logins,
    "threat_ips": matched_threat_ips
}
with open('combined_security_data.json', 'w') as f:
    json.dump(combined_data, f, indent=4)

# Mətn faylına yazmaq
with open('log_analysis.txt', 'w') as f:
    for ip, count in failed_logins.items():
        f.write(f"{ip} - {count} uğursuz giriş cəhdi\n")

# CSV faylı
with open('log_analysis.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['IP', 'Date', 'Method', 'Status'])
    writer.writeheader()
    writer.writerows(log_entries)

print("Log təhlili tamamlandı.")
