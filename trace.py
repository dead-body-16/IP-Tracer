import requests
import os

def banner():
    print("\033[1;32m" + "="*40)
    print("      IP TRACER PROFESSIONAL v1.0")
    print("="*40 + "\033[0m")

def trace_ip():
    banner()
    target_ip = input("\n[?] Enter Target IP: ")
    
    try:
        url = f"http://ip-api.com/json/{target_ip}?fields=66846719"
        data = requests.get(url).json()

        if data['status'] == 'success':
            print(f"\n\033[1;34m[+] Information for: {data['query']}\033[0m")
            print(f"[*] Country    : {data.get('country')}")
            print(f"[*] City       : {data.get('city')}")
            print(f"[*] ISP        : {data.get('isp')}")
            print(f"[*] Timezone   : {data.get('timezone')}")
            
            maps_url = f"https://www.google.com/maps?q={data['lat']},{data['lon']}"
            print(f"\n\033[1;33m[!] Google Maps Link: \n{maps_url}\033[0m")
        else:
            print("\033[1;31m[-] Invalid IP Address!\033[0m")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    trace_ip()
