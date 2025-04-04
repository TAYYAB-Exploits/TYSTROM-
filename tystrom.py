# tystrom.py
import os
import webbrowser
from ddos import start_ddos
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    os.system("clear")
    print(Fore.RED + Style.BRIGHT + """
████████╗██╗   ██╗███████╗████████╗██████╗  ██████╗ ███╗   ███╗
╚══██╔══╝██║   ██║██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗████╗ ████║
   ██║   ██║   ██║███████╗   ██║   ██████╔╝██║   ██║██╔████╔██║
   ██║   ██║   ██║╚════██║   ██║   ██╔═══╝ ██║   ██║██║╚██╔╝██║
   ██║   ╚██████╔╝███████║   ██║   ██║     ╚██████╔╝██║ ╚═╝ ██║
   ╚═╝    ╚═════╝ ╚══════╝   ╚═╝   ╚═╝      ╚═════╝ ╚═╝     ╚═╝
    """)
    print(Fore.CYAN + "         > Created By: @TayyabExploits")
    print(Fore.YELLOW + "         > Tool Name: TYSTROM")
    print(Fore.GREEN + "         > Educational Purpose Only")
    print(Fore.MAGENTA + "         > Developer: ChatGPT x @TayyabExploits
")

def menu():
    while True:
        banner()
        print(Fore.GREEN + "1. DDOS Attack")
        print("2. YOUTUBE Channel")
        print("3. WHATSAPP Channel")
        print("4. TELEGRAM Channel")
        print("5. Exit
")

        choice = input(Fore.CYAN + "Select option: ")
        
        if choice == '1':
            start_ddos()
        elif choice == '2':
            webbrowser.open("https://www.youtube.com/@Tayyabexploits")
        elif choice == '3':
            webbrowser.open("https://whatsapp.com/channel/0029VanMDac05MUliOn3T52n")
        elif choice == '4':
            webbrowser.open("https://t.me/TayyabExploits")
        elif choice == '5':
            print(Fore.RED + "
[!] Exiting TYSTROM... Bye!")
            break
        else:
            print(Fore.RED + "[!] Invalid option! Try again.")
            input("Press Enter...")

if __name__ == "__main__":
    menu()
