import requests
import os
import time

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print("\033[1;32m")
    print("="*40)
    print("      IP TRACER PRO - NZ NISHAN")
    print("="*40)
    print(" [>] Developer : NZ NISHAN")
    print(" [>] Instagram : boycott_nishan")
    print("="*40)
    print("\033[0m")

def save_to_file(data):
    with open("results.txt", "a") as f:
        f.write(f"\n--- IP Trace Result ---\n")
        f.write(f"IP: {data.get('query')}\nCountry: {data.get('country')}\nCity: {data.get('city')}\nISP: {data.get('isp')}\n")
    print("\033[1;32m[+] Result saved to results.txt\033[0m")

def get_ip_info(target_ip=""):
    try:
        url = f"http://ip-api.com/json/{target_ip}?fields=status,country,city,lat,lon,isp,org,timezone,query"
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'success':
            print(f"\n\033[1;34m[+] Information for: {data['query']}\033[0m")
            print("-" * 35)
            print(f"[*] Country     : {data.get('country')}")
            print(f"[*] City        : {data.get('city')}")
            print(f"[*] ISP         : {data.get('isp')}")
            print(f"[*] Org         : {data.get('org')}")
            print(f"[*] Timezone    : {data.get('timezone')}")
            print("-" * 35)
            choice = input("[?] Save this result? (y/n): ")
            if choice.lower() == 'y':
                save_to_file(data)
        else:
            print("\033[1;31m[-] Invalid IP!\033[0m")
    except Exception as e:
        print(f"\033[1;31m[-] Error: {e}\033[0m")

def main_menu():
    while True:
        clear_screen()
        banner()
        print("1. Trace any public IP")
        print("2. Show your IP info")
        print("3. Follow Developer")
        print("4. Exit")
        
        choice = input("\n[?] Choose an option: ")
        
        if choice == '1':
            ip = input("\n[?] Enter IP to trace: ")
            get_ip_info(ip)
            input("\nPress Enter to continue...")
        elif choice == '2':
            get_ip_info()
            input("\nPress Enter to continue...")
        elif choice == '3':
            print("\n[!] Opening links...")
            os.system("termux-open-url https://www.facebook.com/nayeemzakir.nishan")
            os.system("termux-open-url https://www.instagram.com/boycott_nishan")
        elif choice == '4':
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()