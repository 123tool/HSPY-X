## 🛡️ HSPY-X Tool v1.1

**HSPY-X** adalah alat investigasi keamanan (Reconnaissance) otomatis yang menggabungkan kekuatan pencarian Google Dorks, infrastruktur Shodan, dan database Exploit-DB lokal dalam satu interface CLI.

## 🚀 Fitur Utama
- **Google Dorking:** Mencari file sensitif (.sql, .env, .php) secara otomatis.
- **Shodan Integration:** Mendeteksi port terbuka, IP, dan layanan pada target.
- **Offline Exploit-DB:** Mencari exploit berdasarkan versi software secara instan dari database lokal.
- **Auto Report:** Hasil scan langsung tersimpan otomatis sebagai file `.txt` di folder Download (Android/Linux/Windows).

## 📦 Instalasi di Termux
​Buka Termux dan jalankan perintah berikut :

## Update & Setup Storage
```bash
pkg update && pkg upgrade -y
termux-setup-storage
```
## Install Dependency
```bash
pkg install git python -y
pip install requests shodan colorama googlesearch-python pandas
```
## Clone Repository
```bash
git clone [https://github.com/123tool/HSPY-X.git]
cd HSPY-X
```
## Setup Sebelum Running
Karena kita nggak upload API Key (demi keamanan), kamu harus buat filenya dulu :
```
cp config.json.example config.json
nano config.json
# Masukkan API Key Shodan kamu di situ, lalu tekan CTRL+X, Y, ENTER untuk save.
```
## Atau Setup API Key Biasa
```bash
Edit file config.json dan masukkan Shodan API Key kamu
```
## 📖 Cara Penggunaan
​Jalankan tool dengan perintah :
## Scan Domain Target
```
python main.py -t target.com
```
## Cari Exploit Berdasarkan Nama Software
```
python main.py -s "WordPress 6.0"
```
## Kombinasi Keduanya
```
python main.py -t target.com -s "Apache 2.4"
```

## 📝 Catatan Report
​Hasil laporan akan tersimpan di Android (Termux) :
```
/sdcard/Download/recon_target_xxxx.txt
​Linux/Windows: Folder yang sama dengan script.
```
## ​⚠️ Disclaimer

**​Alat ini dibuat untuk tujuan edukasi dan audit keamanan yang sah. Penggunaan untuk aktivitas ilegal adalah tanggung jawab pengguna sepenuhnya.**
