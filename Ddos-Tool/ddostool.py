import os
import time
import random
import sys
from datetime import datetime
from termcolor import colored

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_banner():
    banner_text = r'''
 ____  ____              ____      _             _             
|  _ \|  _ \  ___  ___  |  _ \  __| | ___  _ __ (_) ___  _ __  
| | | | | | |/ _ \/ __| | | | |/ _` |/ _ \| '_ \| |/ _ \| '_ \ 
| |_| | |_| |  __/\__ \ | |_| | (_| | (_) | | | | | (_) | | | |
|____/|____/ \___||___/ |____/ \__,_|\___/|_| |_|_|\___/|_| |_|

Author   : HA-MRX
YouTube  : https://www.youtube.com/c/HA-MRX
GitHub   : https://github.com/Ha3MrX
Facebook : https://www.facebook.com/muhamad.jabar222
Version  : 2.3.7 - DDoss Edition
Updated  : {}
    '''.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(colored(banner_text, 'cyan'))
    print(colored("⚡ DDoss MODE: Simulating EPIC UDP FLOOD! Use .exe for MAXIMUM POWER! ⚡", 'yellow', attrs=['bold']))
    print(colored("Download at:https://github.com/Burgersking/Samp-Ddos-Tool-main\n", 'yellow'))

def progress_bar(duration, prefix=""):
    for _ in range(100):
        sys.stdout.write(f"\r{prefix}[{'█' * (_//4)}{' ' * (25-_//4)}] {_}%")
        sys.stdout.flush()
        time.sleep(duration / 100)
    print()

def download_module(module_name):
    print(colored(f"[~] Fetching critical module {module_name}...", 'yellow'))
    progress_bar(1.5, f"Fetching {module_name} ")
    print(colored(f"[✓] Module {module_name} loaded into memory!", 'green'))

def get_user_input():
    print(colored("\n[?] Enter DDoss simulation parameters (or press Enter for defaults):", 'cyan'))
    target_ip = input(colored("Target IP Address [127.0.0.1]: ", 'green')) or "127.0.0.1"
    port = input(colored("Port [7777]: ", 'green')) or "7777"
    threads = input(colored("Number of Threads [10]: ", 'green')) or "10"
    duration = input(colored("Duration (seconds) [30]: ", 'green')) or "30"
    
    try:
        port = int(port)
        threads = int(threads)
        duration = int(duration)
        if port < 1 or port > 65535:
            raise ValueError("Port must be between 1 and 65535")
        if threads < 1:
            raise ValueError("Number of threads must be positive")
        if duration < 1:
            raise ValueError("Duration must be positive")
        return target_ip, port, threads, duration
    except ValueError as e:
        print(colored(f"[!] Invalid input: {e}. Using defaults!", 'red'))
        return "127.0.0.1", 7777, 10, 30

def log_line(i, target_ip, port):
    messages = [
        f"[~] Unleashing packet storm on {target_ip}:{port}...",
        "[~] Overloading buffers with MEGA DATA...",
        "[~] Spawning attack thread {}...",
        "[~] Linking to shadow node {}...",
        "[~] Injecting CHAOTIC headers...",
        "[~] Encrypting payload with SUPER SECURE algorithm...",
        f"[~] Syncing with DDoss server {target_ip}...",
        "[~] Ramping up packet speed to {}ms...",
        "[~] Accessing core pipeline (level {})...",
        f"[~] Flooding {target_ip} with UDP chaos...",
        "[~] Generating RANDOMIZED MAC addresses...",
        "[~] Evading firewall level {}...",
        f"[~] Spoofing route to {target_ip}...",
        "[~] Deploying ULTIMATE DDoss profile {}...",
        "[~] Hiding tracks with proxy matrix...",
        f"[~] Scanning {target_ip} for WEAK ports...",
        "[~] Simulating EPIC ARP flood...",
        "[~] Transmitting GIGABYTES of DDoss packets...",
        "[~] Tweaking TTL for MAXIMUM impact...",
        "[~] Overwriting DNS cache with DDoss data..."
    ]
    msg = random.choice(messages)
    if '{}' in msg:
        msg = msg.format(random.randint(1, 99))
    return colored(f"{i:04d}: {msg}", 'blue')

def run_emulation(target_ip, port, threads, duration):
    modules = [
        "DDoss_core.py",
        "packet_blaster.py",
        "crypto_troll.py",
        "network_jammer.py",
        "proxy_trickster.py"
    ]
    
    print(colored("[*] Initializing DDoss environment for UDP flood...", 'yellow'))
    time.sleep(1)
    
    for module in modules:
        download_module(module)
        time.sleep(0.5)
    
    print(colored(f"\n[*] Launching DDoss UDP FLOOD on {target_ip}:{port} with {threads} threads for {duration} seconds...", 'yellow', attrs=['bold']))
    time.sleep(1)
    
    start_time = time.time()
    i = 1
    while time.time() - start_time < duration:
        print(log_line(i, target_ip, port))
        time.sleep(random.uniform(0.02, 0.06))
        i += 1
        if i > 150:  # Cap logs to keep it snappy
            break
    
    print(colored("\n[!] CRITICAL DDoss FAILURE: UDP FLOOD CORE OVERLOADED!", 'red', attrs=['bold']))
    print(colored("=============================================================", 'red'))
    print(colored("❌ ERROR: DDoss engine melted from EPIC simulation!", 'red', attrs=['bold']))
    print(colored("💡 SOLUTION: Use the SUPERCHARGED .exe for FASTER UDP DDosss!", 'yellow', attrs=['bold']))
    print(colored("Download at: https://github.com/Ha3MrX/udp-simulator/releases", 'yellow'))
    print(colored("=============================================================", 'red'))
    input("\nPress Enter to exit the DDoss...")

def main():
    clear_screen()
    display_banner()
    print(colored("Initializing UDP DDoss Simulator v2.3.7...\n", 'green'))
    time.sleep(2)
    target_ip, port, threads, duration = get_user_input()
    run_emulation(target_ip, port, threads, duration)

if __name__ == "__main__":
    main()
