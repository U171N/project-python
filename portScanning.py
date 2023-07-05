import socket
import sys
import os


def main():

    while True:
        print("""

 █████╗  ██████╗ █████╗ ██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔══██╗██╔════╝██╔══██╗██║ ██╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
███████║██║     ███████║█████╔╝        ██║   ██║   ██║██║   ██║██║     ███████╗
██╔══██║██║     ██╔══██║██╔═██╗        ██║   ██║   ██║██║   ██║██║     ╚════██║
██║  ██║╚██████╗██║  ██║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
\t Version 1 \t
\tWRITTEN BY: U171N\t
\thttps://github.com/U171N\t
              """)
        print("Pilih Menu:")
        print("1 - SubDomain Enumerate")
        print("2- Port Scanning")
        print("3 - Quit")
        select = input("Masukan Pilihan :")
        if select == '1':
            domain = input("masukan domain yang akan di enumerate: ")
            subdomains = []
            file_path = os.path.join(os.path.dirname(
                __file__), "package/subdomains.txt")

            with open(file_path, "r") as f:
                for line in f:
                    subdomains.append(line.strip())

            # dns server ini bisa diubah sesuai keinginan (disini menggunakan dari google)
            dns_server = "8.8.8.8"
            record_type = "A"  # dns record disini bisa diubah sesuai keinginan

            for subdomain in subdomains:
                ip = SubDomainEnum(subdomain=subdomain, domain=domain,
                                   dns_server=dns_server, record_type=record_type)
                if ip:
                    print(subdomain + "." + domain + "-->" + ip)
                else:
                    print(subdomain + "." + domain + "--> Tidak ditemukan")
            mainmenu = input("Press [ENTER] to go to main menu.")
        # Return mainmenu to the beginning of the loop if the user presses enter
            if not mainmenu:
                continue

        elif select == '2':
            open_ports = PortScanning()
            if open_ports:
                print("Port yang terbuka antara lain:")
                for port in open_ports:
                    print(port)
            else:
                print("Tidak ada port yang terbuka")

        elif select == '3':
            print("Keluar dari program")
            sys.exit()

        else:
            print("Pilihan tidak valid")


def SubDomainEnum(subdomain, domain, dns_server="8.8.8.8", record_type="A"):
    try:
        ip = socket.getaddrinfo(subdomain + "." + domain,
                                None, socket.AF_INET)[0][4][0]
        return ip
    except (socket.error, IndexError):
        return ''


def PortScanning():
    target = input("Masukan alamat IP target: ")
    min_port = int(input("Masukan minimal port: "))
    max_port = int(input("Masukan maksimal port: "))

    open_ports = []
    for port in range(min_port, max_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    mainmenu = input("Press [ENTER] to go to main menu.")
    return open_ports, mainmenu

   # return mainmenu


if __name__ == '__main__':
    main()
