import shodan
from colorama import Fore

def scan_shodan(query, api_key):
    try:
        api = shodan.Shodan(api_key)
        results = api.search(query)
        print(f"{Fore.CYAN}[*] Total found on Shodan: {results['total']}")
        for result in results['matches']:
            print(f"{Fore.GREEN}[+] IP: {result['ip_str']} | Port: {result['port']} | Org: {result['org']}")
    except Exception as e:
        print(f"{Fore.RED}[!] Shodan Error: {e}")
