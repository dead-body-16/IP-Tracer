import requests
import os
import time
import socket

# Colors
G = '\033[1;32m' # Green
R = '\033[1;31m' # Red
B = '\033[1;34m' # Blue
Y = '\033[1;33m' # Yellow
W = '\033[0m'    # White

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(f"{G}")
    print("="*45)
    print("      IP TRACER & PORT SCANNER - PRO")
    print("="*45)
    print(f" [>] Developer : NZ NISHAN")
    print(f" [>] Instagram : boycott_nishan")
    print("="*45)
    print(f"{W}")

def save_to_file(data):
    with open("results.txt", "a") as f:
        f.write(f"\n--- IP Trace Result ---\n")
        f.write(f"IP: {data.get('query')}\nCountry: {data.get('country')}\nCity: {data.get('city')}\nISP: {data.get('isp')}\n")
    print(f"{G}[+] Result saved to results.txt{W}")

def get_ip_info(target_ip=""):
    try:
        url = f"http://ip-api.com/json/{target_ip}?fields=status,country,city,lat,lon,isp,org,timezone,query"
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'success':
            print(f"\n{B}[+] Information for: {data['query']}{W}")
            print("-" * 35)
            print(f"[*] Country     : {data.get('country')}")
            print(f"[*] City        : {data.get('city')}")
            print(f"[*] ISP         : {data.get('isp')}")
            print(f"[*] Org         : {data.get('org')}")
            print(f"[*] Timezone    : {data.get('timezone')}")
            print("-" * 35)
            choice = input(f"{Y}[?] Save this result? (y/n): {W}")
            if choice.lower() == 'y':
                save_to_file(data)
        else:
            print(f"{R}[-] Invalid IP!{W}")
    except Exception as e:
        print(f"{R}[-] Error: {e}{W}")

def port_scanner():
    target = input(f"\n{Y}[?] Enter IP or Domain to Scan: {W}")
    print(f"{B}[*] Scanning started on: {target}{W}")
    print(f"{Y}[!] Please wait, checking common ports...{W}")
    
    # Common ports for reconnaissance
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 3389, 8080]
    
    try:
        found_ports = 0
        for port in common_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1) # Timeout for faster scanning
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"{G}[+] Port {port} is OPEN{W}")
                found_ports += 1
            s.close()
        
        if found_ports == 0:
            print(f"{R}[!] No common ports are open on this target.{W}")
        else:
            print(f"\n{G}[+] Scanning complete. Found {found_ports} open ports.{W}")
            
    except Exception as e:
        print(f"{R}[!] Error: {e}{W}")

def main_menu():
    while True:
        clear_screen()
        banner()
        print(f"{G}1. Trace any public IP")
        print(f"2. Show your IP info")
        print(f"3. Port Scanner (Beta)")
        print(f"4. Follow Developer")
        print(f"5. Exit{W}")

        choice = input(f"\n{Y}[?] Choose an option: {W}")

        if choice == '1':
            ip = input(f"\n{Y}[?] Enter IP to trace: {W}")
            get_ip_info(ip)
            input(f"\n{B}Press Enter to continue...{W}")
        elif choice == '2':
            get_ip_info()
            input(f"\n{B}Press Enter to continue...{W}")
        elif choice == '3':
            port_scanner()
            input(f"\n{B}Press Enter to continue...{W}")
        elif choice == '4':
            print(f"\n{B}[!] Opening links...{W}")
            os.system("termux-open-url https://www.facebook.com/nayeemzakir.nishan")
            os.system("termux-open-url https://www.instagram.com/boycott_nishan")
        elif choice == '5':
            print(f"\n{R}Goodbye, Nishan Bhai!{W}")
            break
        else:
            print(f"{R}Invalid choice!{W}")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()