import pandas as pd
from colorama import Fore

def search_exploit(software_name):
    try:
        df = pd.read_csv('data/exploits.csv')
        results = df[df['description'].str.contains(software_name, case=False, na=False)]
        if not results.empty:
            print(f"{Fore.GREEN}[+] Found {len(results)} exploits for {software_name}:")
            for index, row in results.head(10).iterrows():
                print(f"    - ID: {row['id']} | {row['description']}")
        else:
            print(f"{Fore.YELLOW}[-] No local exploits found for {software_name}.")
    except Exception as e:
        print(f"{Fore.RED}[!] Exploit-DB Search Error: {e}")
