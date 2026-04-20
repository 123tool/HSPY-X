import os
import sys
import json
import argparse
from datetime import datetime
from colorama import Fore, Style, init

# Import modul dari folder modules/
try:
    from modules.shodan_mod import scan_shodan
    from modules.dorker import run_dorks
    from modules.edb_search import search_exploit
except ImportError as e:
    print(f"[!] Error: Modul tidak ditemukan. Pastikan folder modules/ lengkap. {e}")
    sys.exit(1)

init(autoreset=True)

# Tentukan folder output (Termux friendly)
OUTPUT_DIR = "/sdcard/Download/" if os.path.exists("/sdcard/Download/") else "./"

BANNER = f"""
{Fore.RED}      .---.      .---.      .---.
{Fore.RED}     (  v  )    (  v  )    (  v  )
{Fore.WHITE}      \   /      \   /      \   /
{Fore.WHITE}       ' '        ' '        ' '
{Fore.BLUE}  _    _  _____  _____ __     __      __   __
{Fore.BLUE} | |  | |/ ____||  __ \\ \   / /      \ \ / /
{Fore.BLUE} | |__| | (___  | |__) |\ \_/ / ______ \ V / 
{Fore.WHITE} |  __  |\___ \ |  ___/  \   / |______| > <  
{Fore.RED} | |  | |____) || |       | |          / . \ 
{Fore.RED} |_|  |_|_____/ |_|       |_|         /_/ \_\\
                                                        
{Fore.YELLOW}     [ MULTI-ENGINE RECONNAISSANCE SYSTEM v1.1 ]
{Fore.YELLOW}           [ Dorks | Shodan | Exploit-DB ]
"""

def check_config():
    """Fungsi pengecekan API Key agar aman sebelum eksekusi"""
    if not os.path.exists('config.json'):
        print(f"{Fore.RED}[!] Error: File config.json tidak ditemukan!")
        print(f"{Fore.YELLOW}[*] Silakan copy config.json.example menjadi config.json dan isi API Key kamu.")
        # Kita buatkan template otomatis kalau file belum ada
        template = {"shodan_api": "ISI_API_KEY_DISINI"}
        with open('config.json.example', 'w') as f:
            json.dump(template, f, indent=4)
        sys.exit(1)

def load_config():
    with open('config.json') as f:
        return json.load(f)

def save_to_file(content, filename):
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath

def main():
    check_config() # <-- Dijalankan paling pertama!
    print(BANNER)
    
    parser = argparse.ArgumentParser(description="HSPY-X: Advanced Recon Tool")
    parser.add_argument("-t", "--target", help="Target Domain (e.g. example.com)")
    parser.add_argument("-s", "--software", help="Software name to find exploits")
    args = parser.parse_args()

    if not args.target and not args.software:
        parser.print_help()
        return

    config = load_config()
    report_content = f"HSPY-X RECON REPORT - {datetime.now()}\n"
    report_content += "="*40 + "\n"

    # --- Eksekusi Google Dorking ---
    if args.target:
        print(f"{Fore.CYAN}[*] Scanning Target: {args.target}")
        dork_results = run_dorks(args.target)
        report_content += f"\n[GOOGLE DORK RESULTS]\n{dork_results}\n"
        
        # --- Eksekusi Shodan ---
        print(f"{Fore.CYAN}[*] Checking Shodan Infrastructure...")
        shodan_results = scan_shodan(f"hostname:{args.target}", config['shodan_api'])
        report_content += f"\n[SHODAN RESULTS]\n{shodan_results}\n"

    # --- Eksekusi Exploit-DB ---
    if args.software:
        print(f"{Fore.CYAN}[*] Searching Exploits for: {args.software}")
        edb_results = search_exploit(args.software)
        report_content += f"\n[EXPLOIT-DB RESULTS]\n{edb_results}\n"

    # --- Simpan Laporan ---
    file_target = args.target if args.target else "software_search"
    filename = f"hspyx_{file_target.replace('.', '_')}_{datetime.now().strftime('%H%M')}.txt"
    path = save_to_file(report_content, filename)
    
    print("\n" + "="*50)
    print(f"{Fore.GREEN}[SUCCESS] Laporan tersimpan di: {path}")

if __name__ == "__main__":
    main()
