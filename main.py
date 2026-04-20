import json
import argparse
from colorama import Fore, Style, init
from modules.shodan_mod import scan_shodan
from modules.dorker.py import run_dorks # Note: Perbaiki typo path jika perlu
from modules.edb_search import search_exploit

init(autoreset=True)

BANNER = f"""
{Fore.RED}███████╗██████╗ ██╗   ██╗      ███████╗
{Fore.RED}██╔════╝██╔══██╗╚██╗ ██╔╝      ██╔════╝
{Fore.WHITE}███████╗██████╔╝ ╚████╔╝ █████╗█████╗  
{Fore.WHITE}╚════██║██╔═══╝   ╚██╔╝  ╚════╝██╔══╝  
{Fore.BLUE}███████║██║        ██║         ███████╗
{Fore.BLUE}╚══════╝╚═╝        ╚═╝         ╚══════╝
{Fore.YELLOW}        RECON TOOL v1 - by SPY-E
"""

def load_config():
    with open('config.json') as f:
        return json.load(f)

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="SPY-E Advanced Recon Tool")
    parser.add_argument("-t", "--target", help="Target Domain (e.g. example.com)")
    parser.add_argument("-s", "--software", help="Software name to find exploits")
    args = parser.parse_args()

    config = load_config()

    if args.target:
        # 1. Jalankan Google Dorking
        run_dorks(args.target)
        # 2. Jalankan Shodan (Cari IP terkait target via query)
        print("\n" + "="*50)
        scan_shodan(f"hostname:{args.target}", config['shodan_api'])

    if args.software:
        # 3. Cari Exploit Lokal
        print("\n" + "="*50)
        search_exploit(args.software)

if __name__ == "__main__":
    main()
