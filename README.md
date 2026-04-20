## 🛡️ HSPY-X Tool v1.1

**HSPY-X** adalah alat investigasi keamanan (Reconnaissance) otomatis yang menggabungkan kekuatan pencarian Google Dorks, infrastruktur Shodan, dan database Exploit-DB lokal dalam satu interface CLI.

## 🚀 Fitur Utama
- **Google Dorking:** Mencari file sensitif (.sql, .env, .php) secara otomatis.
- **Shodan Integration:** Mendeteksi port terbuka, IP, dan layanan pada target.
- **Offline Exploit-DB:** Mencari exploit berdasarkan versi software secara instan dari database lokal.
- **Auto Report:** Hasil scan langsung tersimpan otomatis sebagai file `.txt` di folder Download (Android/Linux/Windows).

📦 Instalasi di Termux
​Buka Termux dan jalankan perintah berikut:

# Update & Setup Storage
pkg update && pkg upgrade -y
termux-setup-storage

# Install Dependency
pkg install git python -y
pip install requests shodan colorama googlesearch-python pandas

# Clone Repository
git clone [https://github.com/USERNAME_KAMU/spy-e-recon.git](https://github.com/USERNAME_KAMU/spy-e-recon.git)
cd spy-e-recon

# Setup API Key
# Edit file config.json dan masukkan Shodan API Key kamu
nano config.json

📖 Cara Penggunaan
​Jalankan tool dengan perintah:
# Scan Domain Target
python main.py -t target.com

# Cari Exploit Berdasarkan Nama Software
python main.py -s "WordPress 6.0"

# Kombinasi Keduanya
python main.py -t target.com -s "Apache 2.4"

📝 Catatan Report
​Hasil laporan akan tersimpan di:
​Android (Termux): /sdcard/Download/recon_target_xxxx.txt
​Linux/Windows: Folder yang sama dengan script.
​⚠️ Disclaimer
​Alat ini dibuat untuk tujuan edukasi dan audit keamanan yang sah. Penggunaan untuk aktivitas ilegal adalah tanggung jawab pengguna sepenuhnya.
