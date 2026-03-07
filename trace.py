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

def open_socials():
    fb_url = "https://www.facebook.com/nayeemzakir.nishan"
    ig_url = "https://www.instagram.com/boycott_nishan"
    print(f"\n\033[1;33m[1] Open Facebook\n[2] Open Instagram\033[0m")
    choice = input("\n[?] Select (1/2) or Enter to skip: ")
    if choice == '1':
        os.system(f"termux-open-url {fb_url}")
    elif choice == '2':
        os.system(f"termux-open-url {ig_url}")

def trace_ip():
    clear_screen()
    banner()
    target_ip = input("\n\033[1;36m[?] Enter Target IP: \033[0m")
    try:
        url = f"http://ip-api.com/json/{target_ip}?fields=status,country,city,lat,lon,isp,org,timezone,query"
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'success':
            print(f"\n\033[1;34m[+] Result for: {data['query']}\033[0m")
            print("-" * 35)
            print(f"[*] Country : {data.get('country')}")
            print(f"[*] City    : {data.get('city')}")
            print(f"[*] ISP     : {data.get('isp')}")
            print(f"[*] Org     : {data.get('org')}")
            print(f"[*] Time    : {data.get('timezone')}")
            lat, lon = data['lat'], data['lon']
            maps_url = f"https://www.google.com/maps/place/{lat},{lon}"
            print(f"\n\033[1;33m[!] Map: {maps_url}\033[0m")
            print("-" * 35)
            open_socials()
        else:
            print("\033[1;31m[-] Invalid IP!\033[0m")
    except Exception as e:
        print(f"\033[1;31m[-] Error: {e}\033[0m")

if __name__ == "__main__":
    trace_ip()
