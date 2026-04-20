from googlesearch import search
from colorama import Fore

def run_dorks(domain):
    dorks = [
        f"site:{domain} filetype:sql",
        f"site:{domain} filetype:env",
        f"site:{domain} inurl:admin"
    ]
    print(f"{Fore.CYAN}[*] Running Google Dorks for {domain}...")
    for dork in dorks:
        try:
            for url in search(dork, num_results=5):
                print(f"{Fore.YELLOW}[!] Potentially sensitive: {url}")
        except Exception as e:
            print(f"{Fore.RED}[!] Google Error (Possible Rate Limit): {e}")
            break
