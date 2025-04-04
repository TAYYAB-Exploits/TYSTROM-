import os
import webbrowser
from ddos import start_ddos
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    os.system("clear")
    print(Fore.YELLOW + Style.BRIGHT + """
████████╗███████╗████████╗██████╗  ██████╗ ███╗   ███╗
██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗████╗ ████║
███████╗█████╗     ██║   ██████╔╝██║   ██║██╔████╔██║
╚════██║██╔══╝     ██║   ██╔══██╗██║   ██║██║╚██╔╝██║
███████║███████╗   ██║   ██║  ██║╚██████╔╝██║ ╚═╝ ██║
╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝
                TYSTROM
          created by @Tayyabexploits
""")

def menu():
    while True:
        banner()
        print(Fore.GREEN + "1. " + Fore.CYAN + "DDOS Attack")
        print(Fore.GREEN + "2. " + Fore.RED + "YouTube Channel Info")
        print(Fore.GREEN + "3. " + Fore.MAGENTA + "WhatsApp Channel Info")
        print(Fore.GREEN + "4. " + Fore.BLUE + "Telegram Contact Info")
        print(Fore.GREEN + "5. " + Fore.YELLOW + "Exit Program")
        print("\n" + Fore.WHITE + "─"*40)

        choice = input(Fore.CYAN + "\n[?] Select option: ")

        if choice == '1':
            print(Fore.YELLOW + "\n[*] Initializing DDOS Attack Module...")
            start_ddos()
        elif choice == '2':
            print(Fore.YELLOW + "\n[+] YouTube Channel Details:")
            print(Fore.CYAN + "➤ Channel URL: https://www.youtube.com/@Tayyabexploits")
            print(Fore.CYAN + "➤ Subscribers: Open link to check")
        elif choice == '3':
            print(Fore.YELLOW + "\n[+] WhatsApp Channel Details:")
            print(Fore.CYAN + "➤ Channel Link: https://whatsapp.com/channel/0029VanMDac05MUliOn3T52n")
            print(Fore.CYAN + "➤ Join Code: 0029VanMDac05MUliOn3T52n")
        elif choice == '4':
            print(Fore.YELLOW + "\n[+] Telegram Contact Information:")
            print(Fore.CYAN + "➤ Username: @Tayyabexploits")
            print(Fore.CYAN + "➤ Official Channel: https://t.me/TayyabExploits")
            print(Fore.CYAN + "➤ Direct Message: t.me/Tayyabexploits")
        elif choice == '5':
            print(Fore.RED + "\n[!] Shutting down TSTROM... Goodbye!")
            break
        else:
            print(Fore.RED + "\n[!] Invalid selection! Please choose 1-5")

        input(Fore.WHITE + "\n[↲] Press Enter to return to menu...")
        os.system("clear")

if __name__ == "__main__":
    menu()