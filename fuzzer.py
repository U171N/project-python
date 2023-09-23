import hashlib
import sys
import os
import requests
import random
import string
import socket

def main():
    while True:
        print("""
███████╗██╗   ██╗███████╗███████╗███████╗██████╗
██╔════╝██║   ██║╚══███╔╝╚══███╔╝██╔════╝██╔══██╗
█████╗  ██║   ██║  ███╔╝   ███╔╝ █████╗  ██████╔╝
██╔══╝  ██║   ██║ ███╔╝   ███╔╝  ██╔══╝  ██╔══██╗
██║     ╚██████╔╝███████╗███████╗███████╗██║  ██║
╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
\t Version 1 \t
\t Written By:U171N
\t https://github.com/U171N  \t
              """)
        print("Pilih Menu:")
        print("1- Fuzzing Subdomain")
        print("2- Cari Hidden File")
        print("3- Cari Sensitive Directory")
        print("4- Keluar")
        select = input("Masukan Pilihan :")

        if select == '1':
            FuzzingSubDomain()

        elif select == '2':
            FuzzingHiddenFile()

        elif select == '3':
            FuzzingDirectory()

        elif select == '4':
            sys.exit("Terima kasih sudah menggunakan tools ini")

        else:
            print("Pilihan tidak valid,silahkan pilih menu 1-4")

def FuzzingSubDomain():
    # Mendapatkan path relatif ke file wordlist di dalam folder 'wordlist'
    wordlist_path = os.path.join("worldist", "subdomain.txt")

    # Mengecek apakah file wordlist ada
    if not os.path.isfile(wordlist_path):
        print(f"File '{wordlist_path}' tidak ditemukan")
        return

    # Input target
    target_url = input("Masukan target (contoh: example.com): ")

    # Baca file wordlist dari path relatif
    try:
        with open(wordlist_path, 'r') as file:
            subdomains = file.read().splitlines()
    except FileNotFoundError:
        print(f"File '{wordlist_path}' not found")
        return

    # Main fuzzing
    for subdomain in subdomains:
        url = f"https://{subdomain}.{target_url}"
        try:
            response = requests.get(url)
            if response.status_code != 404:
                print(f"[+] Subdomain ditemukan: {subdomain}")
            else:
                print(f"[-] Subdomain gagal: {subdomain}")  # Menampilkan "failed" jika status 404
        except requests.exceptions.RequestException:
            print(f"[-] Subdomain gagal: {subdomain}")  # Menampilkan "failed" jika ada kesalahan lain

    print("Fuzzing selesai")

    # Main fuzzing
    for subdomain in subdomains:
        url = f"https://{subdomain}.{target_url}"
        try:
            response = requests.get(url)
            if response.status_code != 404:
                print(f"[+] Subdomain ditemukan: {subdomain}")
        except requests.exceptions.RequestException:
            pass

    print("Fuzzing selesai")

def FuzzingHiddenFile():
    # Membangun path absolut ke file wordlist di dalam folder 'wordlist'
    wordlist_path = os.path.join(os.getcwd(), 'worldist', 'hiddenfile.txt')

    target_input = input("Masukkan target input dengan placeholder FUZZ (contoh: https://www.example.com/FUZZ): ")

    try:
        with open(wordlist_path, "rb") as wordlist_file:  # Buka dalam mode biner ("rb")
            wordlist = wordlist_file.read().decode('utf-8').splitlines()  # Dekode sebagai UTF-8

        for word in wordlist:
            fuzzed_input = target_input.replace("FUZZ", word)
            response = requests.get(fuzzed_input)

            if response.status_code == 200:
                print(f"[+] Success - Ditemukan: {fuzzed_input}")
            else:
                print(f"[-] Belum Ditemukan : {fuzzed_input}")

    except FileNotFoundError:
        print(f"File '{wordlist_path}' not found")
    except Exception as e:
        print(f"Error: {str(e)}")

def FuzzingDirectory():
    # Input URL target
    target_url = input("Masukkan URL target (contoh: https://www.example.com/): ")

    # Membaca file wordlist
    wordlist_path = "worldist/directory.txt"
    wordlist = load_wordlist(wordlist_path)

    num_tests = len(wordlist)  # Menggunakan panjang wordlist sebagai jumlah percobaan

    for _ in range(num_tests):
        # Ambil kata acak dari wordlist
        random_word = random.choice(wordlist)

        # Tambahkan garis miring (/) di antara URL target dan kata acak untuk mencari direktori tersembunyi
        new_url = f"{target_url}/{random_word}"

        try:
            response = requests.get(new_url)
            if response.status_code == 200:
                print(f"[+] Direktori ditemukan: {new_url}")
            else:
                print(f"[-] Belum Ditemukan : {new_url}")
        except requests.exceptions.RequestException:
            pass



def load_wordlist(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()
if __name__ == "__main__":
    main()
