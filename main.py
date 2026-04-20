import json
import argparse
import os
from datetime import datetime
from colorama import Fore, Style, init
from modules.shodan_mod import scan_shodan
from modules.dorker import run_dorks
from modules.edb_search import search_exploit

init(autoreset=True)

# Lokasi penyimpanan default di Termux (Folder Download HP)
# Kalau di Windows/Linux, dia akan simpan di folder yang sama dengan script
OUTPUT_DIR = "/sdcard/Download/" if os.path.exists("/sdcard/Download/") else "./"

BANNER = f"""
{Fore.RED}███████╗██████╗ ██╗   ██╗      ███████╗
{Fore.RED}██╔════╝██╔══██╗╚██╗ ██╔╝      ██╔════╝
{Fore.WHITE}███████╗██████╔╝ ╚████╔╝ █████╗█████╗  
{Fore.WHITE}╚════██║██╔═══╝   ╚██╔╝  ╚════╝██╔══╝  
{Fore.BLUE}███████║██║        ██║         ███████╗
{Fore.BLUE}╚══════╝╚═╝        ╚═╝         ╚══════╝
{Fore.YELLOW}        RECON TOOL v1.1 - by SPY-E
"""

def save_to_file(content, filename):
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="SPY-E Advanced Recon Tool")
    parser.add_argument("-t", "--target", help="Target Domain")
    parser.add_argument("-s", "--software", help="Software name to find exploits")
    args = parser.parse_args()

    if not args.target and not args.software:
        parser.print_help()
        return

    config = { "shodan_api": "ISI_API_KEY_MU" } # Sebaiknya baca dari config.json
    
    report_content = f"RECON REPORT - {datetime.now()}\n"
    report_content += "="*30 + "\n"

    if args.target:
        print(f"{Fore.CYAN}[*] Scanning Target: {args.target}")
        # Logika Dorking
        dork_results = run_dorks(args.target) # Pastikan modul return string
        report_content += f"\n[GOOGLE DORK RESULTS]\n{dork_results}\n"
        
        # Logika Shodan
        shodan_results = scan_shodan(f"hostname:{args.target}", config['shodan_api'])
        report_content += f"\n[SHODAN RESULTS]\n{shodan_results}\n"

    if args.software:
        print(f"{Fore.CYAN}[*] Searching Exploits for: {args.software}")
        edb_results = search_exploit(args.software)
        report_content += f"\n[EXPLOIT-DB RESULTS]\n{edb_results}\n"

    # Simpan File
    filename = f"recon_{args.target or 'software'}_{datetime.now().strftime('%H%M%S')}.txt"
    path = save_to_file(report_content, filename)
    
    print("\n" + "="*50)
    print(f"{Fore.GREEN}[SUCCESS] Laporan tersimpan di: {path}")
    print(f"{Fore.YELLOW}[INFO] Cek File Manager HP kamu di folder 'Download'")

if __name__ == "__main__":
    main()
