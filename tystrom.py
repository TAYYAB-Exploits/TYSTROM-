import os
import webbrowser
from ddos import start_ddos
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    os.system("clear")
    print(Fore.YELLOW + Style.BRIGHT + """
████████╗██╗   ██╗███████╗████████╗██████╗  ██████╗ ███╗   ███╗
╚══██╔══╝██║   ██║██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗████╗ ████║
   ██║   ██║   ██║█████╗     ██║   ██████╔╝██║   ██║██╔████╔██║
   ██║   ██║   ██║██╔══╝     ██║   ██╔═══╝ ██║   ██║██║╚██╔╝██║
   ██║   ╚██████╔╝███████╗   ██║   ██║     ╚██████╔╝██║ ╚═╝ ██║
   ╚═╝    ╚═════╝ ╚══════╝   ╚═╝   ╚═╝      ╚═════╝ ╚═╝     ╚═╝
                TSTROM
          created by @Tayyabexploits
""")

def menu():
    while True:
        banner()
        print(Fore.GREEN + "1. " + Fore.CYAN + "DDOS Attack")
        print(Fore.GREEN + "2. " + Fore.RED + "YouTube Channel")
        print(Fore.GREEN + "3. " + Fore.MAGENTA + "WhatsApp Channel")
        print(Fore.GREEN + "4. " + Fore.BLUE + "Telegram Channel")
        print(Fore.GREEN + "5. " + Fore.YELLOW + "Exit")

        choice = input(Fore.CYAN + "Select option: ")

        if choice == '1':
            print(Fore.YELLOW + "[*] Launching DDOS Attack...")
            start_ddos()
        elif choice == '2':
            print(Fore.YELLOW + "[*] Opening YouTube...")
            webbrowser.open("https://www.youtube.com/@Tayyabexploits", new=2)  # Open in a new tab
        elif choice == '3':
            print(Fore.YELLOW + "[*] Opening WhatsApp...")
            webbrowser.open("https://whatsapp.com/channel/0029VanMDac05MUliOn3T52n", new=2)
        elif choice == '4':
            print(Fore.YELLOW + "[*] Opening Telegram...")
            webbrowser.open("https://t.me/TayyabExploits", new=2)
        elif choice == '5':
            print(Fore.RED + "[!] Exiting TSTROM... Bye!")
            break
        else:
            print(Fore.RED + "[!] Invalid option! Try again.")

        input(Fore.WHITE + "Press Enter to continue...")

if __name__ == "__main__":
    menu()