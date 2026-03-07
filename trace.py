import requests
import os
import time

def clear_screen():
    # Termux ba Linux er jonno screen clear
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    # Updated Banner with New Developer Name
    print("\033[1;32m") # Green Color
    print("""
    ██████╗ ███████╗ █████╗ ██████╗     ██████╗  ██████╗ ██████╗ ██╗   ██╗
    ██╔══██╗██╔════╝██╔══██╗██╔══██╗    ██╔══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝
    ██║  ██║█████╗  ███████║██║  ██║    ██████╔╝██║   ██║██║  ██║ ╚████╔╝ 
    ██║  ██║██╔══╝  ██╔══██║██║  ██║    ██╔══██╗██║   ██║██║  ██║  ╚██╔╝  
    ██████╔╝███████╗██║  ██║██████╔╝    ██████╔╝╚██████╔╝██████╔╝   ██║   
    ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝     ╚═════╝  ╚═════╝ ╚═════╝    ╚═╝   
    """)
    print("="*65)
    print(" [>] Tool Name  : IP-Tracer-Pro")
    print(" [>] Developer  : NZ NISHAN")
    print(" [>] Instagram  : boycott_nishan")
    print(" [>] Facebook   : https://www.facebook.com/nayeemzakir.nishan")
    print("="*65)
    print("\033[0m")

def open_socials():
    # Social media links
    fb_url = "https://www.facebook.com/nayeemzakir.nishan"
    ig_url = "https://www.instagram.com/boycott_nishan"
    
    print(f"\n\033[1;33m[1] Open Facebook Profile")
    print(f"[2] Open Instagram Profile\033[0m")
    
    choice = input("\n[?] Select an option to follow (1/2) or press Enter to skip: ")
    
    if choice == '1':
        print("\033[1;32m[!] Opening Facebook...\033[0m")
        time.sleep(1)
        os.system(f"termux-open-url {fb_url}")
    elif choice == '2':
        print("\033[1;32m[!] Opening Instagram...\033[0m")
        time.sleep(1)
        os.system(f"termux-open-url {ig_url}")

def trace_ip():
    clear_screen()
    banner()
    
    target_ip = input("\n\033[1;36m[?] Enter Target IP (Leave blank for your IP): \033[0m")
    
    try:
        # API request
        url = f"http://ip-api.com/json/{target_ip}?fields=status,message,country,regionName,city,zip,lat,lon,timezone,isp,org,query"
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'success':
            print(f"\n\033[1;34m[+] Information for: {data['query']}\033[0m")
            print("-" * 35)
            print(f"[*] Country     : {data.get('country')}")
            print(f"[*] Region      : {data.get('regionName')}")
            print(f"[*] City        : {data.get('city')}")
            print(f"[*] ISP         : {data.get('isp')}")
            print(f"[*] Organization : {data.get('org')}")
            print
