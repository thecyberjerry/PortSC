import socket
import threading
import pyfiglet
from colorama import Fore
banner = pyfiglet.figlet_format("PortSC")
print(banner)
def scann():
    with open('list.txt', 'r') as file:
        var = file.read()
        ports = var.splitlines()
    f = [int(i) for i in ports]
    var2 = input(Fore.BLUE + "\nEnter Your Target: " + Fore.RESET )
    host = socket.gethostbyname(var2)
    print(Fore.YELLOW + f'\nIP Address of the target: {host}' + Fore.YELLOW)
    for port in list(f):
        target = socket.gethostbyname(var2)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        result = s.connect_ex((target, port))
        if result == 0:
            print(Fore.WHITE + '\n{} is open at Port: {}'.format(var2, port) + Fore.RESET)
        s.close()

    return 'Finished!!'

with open('readme.md','r') as file2:
    var2 = file2.read()
    print (Fore.GREEN + var2 + Fore.RESET)
thread = threading.Thread(target=scann)
thread.start()


