from hashlib import md5
from hashlib import sha256
from hashlib import sha512
import hashlib
import sys
import os
import time
import urllib3
import urllib.request
import re
import itertools
import time
import tkinter as tk

from tkinter import filedialog

import secrets
import string


def main():
    while True:
        print("""
    ****************************************************************


██╗  ██╗ █████╗ ███████╗██╗  ██╗██╗███╗   ██╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██║  ██║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝     ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
███████║███████║███████╗███████║██║██╔██╗ ██║██║  ███╗       ██║   ██║   ██║██║   ██║██║     ███████╗
██╔══██║██╔══██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║       ██║   ██║   ██║██║   ██║██║     ╚════██║
██║  ██║██║  ██║███████║██║  ██║██║██║ ╚████║╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝


  	\tPASSWORD CRACKING  AND GENERATE RANDOM PASSWORD \t
  	\tWRITTEN BY : FakhrU'BYTE AKA U171N \t
  	****************************************************************
          """)
        print("SCRIPT PASSWORD CRACKING AND GENERATE RANDOM PASSWORD")
        print('1 - ENCRYPTION USING MD5')
        print('2 - DECRYPT HASH MD5')
        print('3 - ENCRYPTION USING SHA1')
        print('4 - DECRYPT HASH SHA1')
        print('5 - ENCRYPTION USING SHA256')
        print('6 - DECRYPT HASH SHA256')
        print('7 - ENCRYPTION USING SHA512')
        print('8 - DECRYPT HASH SHA512')
        print('9 - GENERATE RANDOM PASSWORD')
        print('10 - Quit')
        select = input("Masukan Pilihan :")

        if select == '1':
            md5encryption()

        elif select == '2':
            md5decrypt()

        elif select == '3':
            sha1encryption()

        elif select == '4':
            crack_sha1()

        elif select == '5':
            sha256encryption()

        elif select == '6':
            crack_sha256()

        elif select == '7':
            sha512encryption()

        elif select == '8':
            sha512_decrypt()

        elif select == '9':
            randompass()

        elif select == '10':
            sys.exit("See You next Time")
        else:
            print("Pilihan tidak valid, silakan pilih angka 1-6.")


def md5encryption():
    string = input("string you want to convert to MD5 >")
    algorithm = hashlib.md5()
    algorithm.update(string.encode())
    encrypted = algorithm.hexdigest()
    print("hasil hashing ke MD5 :", encrypted)
    mainmenu = input("Press [ENTER] to go to main menu.")
    return mainmenu


def md5decrypt():
    # input the MD5 hash to be decrypted
    md5_hash = input("Enter the MD5 hash to be decrypted: ")

    # membuka dialog box untuk memilih file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    # menampilkan path file yang telah dipilih
    print("Path file yang telah dipilih:", file_path)

    # mengubah direktori kerja saat ini ke direktori tempat file tersebut berada
    os.chdir(os.path.dirname(file_path))

    # generate all possible combinations of characters for the password
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+={}[]|\\;:"<>,.?/~`'
    # count = 0
    for password_length in range(1, 100):
        for password in itertools.product(alphabet, repeat=password_length):
            password_str = "".join(password)

            # check if the MD5 hash of the password matches the given hash
            md5_hash_guess = hashlib.md5(password_str.encode()).hexdigest()
            if md5_hash_guess == md5_hash:
                print(
                    f"Hasil Crack: {password_str}")
                return
 # show loading message every 10,000 attempts
            # if count % 10000 == 0:
            #     print("Loading...")
            # count += 1
    print("Hasil Crack tidak ditemukan.")


def sha1encryption():
    string = input("masukan plaintext yang akan diubah ke SHA1 > ")
    algorithm = hashlib.sha1()
    algorithm.update(string.encode())
    encrypted = algorithm.hexdigest()
    print("hasil hashing ke SHA1 :", encrypted)
    mainmenu = input("Tekan [ENTER] untuk kembali ke halaman utama")
    return mainmenu


def crack_sha1():
    # Input the SHA1 hash to be decrypted
    sha1_hash = input("Masukan password yang akan di decrypt: ")

    # Define character set to be used in brute force
    charset = string.ascii_lowercase + string.digits

    # membuka dialog box untuk memilih file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    # menampilkan path file yang telah dipilih
    print("Path file yang telah dipilih:", file_path)

    # mengubah direktori kerja saat ini ke direktori tempat file tersebut berada
    os.chdir(os.path.dirname(file_path))

    # Generate all possible combinations of characters of length 1 to 5
    for length in range(1, 6):
        for guess in itertools.product(charset, repeat=length):
            # Join characters into a string
            guess_str = ''.join(guess)

            # Hash the string using SHA1
            guess_hash = hashlib.sha1(guess_str.encode()).hexdigest()

            # Check if the hash matches the hash we are trying to crack
            if guess_hash == sha1_hash:
                print(
                    f"Hasil Crack: {guess_str}")
                return

    print("Hasil Tidak ditemukan.")
    mainmenu = input("Press [ENTER] to go to main menu.")
    return mainmenu


def sha256encryption():
    select = input("masukan plaintext: ")
    result2 = hashlib.sha256(select.encode())
    print("hasil hashing: ", result2.hexdigest())
    mainmenu = input("Press [ENTER] to go to main menu.")
    return mainmenu


def crack_sha256():
    # input the SHA256 hash to be decrypted
    hash_to_crack = input("Masukan password yang akan di decrypt: ")
    # Define character set to be used in brute force
    charset = string.ascii_letters + string.digits

    # membuka dialog box untuk memilih file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    # menampilkan path file yang telah dipilih
    print("Path file yang telah dipilih:", file_path)

    # mengubah direktori kerja saat ini ke direktori tempat file tersebut berada
    os.chdir(os.path.dirname(file_path))
    # Generate all possible combinations of characters of length 'length'
    for length in range(1, 16):
        for guess in itertools.product(charset, repeat=length):
            # Join characters into a string
            guess_str = ''.join(guess)

            # Hash the string using SHA256
            guess_hash = hashlib.sha256(guess_str.encode()).hexdigest()

            # Check if the hash matches the hash we are trying to crack
            if guess_hash == hash_to_crack:
                print(
                    f"Hasil Crack: {guess_str}")
                return

    print("Password tidak ditemukan.")
    mainmenu = input("Press [ENTER] to go to main menu.")
    return mainmenu


def sha512encryption():
    select = input("masukan plaintext: ")
    result2 = hashlib.sha512(select.encode())
    print("hasil hashing: ", result2.hexdigest())
    mainmenu = input("Press [ENTER] to go to main menu.")
    return mainmenu


def sha512_decrypt():
    # input the sha512 hash to be decrypted
    hash_value = input("Masukan password sha512 yang akan di decrypt: ")

    # membuka dialog box untuk memilih file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    # menampilkan path file yang telah dipilih
    print("Path file yang telah dipilih:", file_path)

    # mengubah direktori kerja saat ini ke direktori tempat file tersebut berada
    os.chdir(os.path.dirname(file_path))

    # define the characters to be used in the brute-force attack (mendefinisikan karakter random yang akan digunakan untuk membuat dictionary brute force)
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+={}[]|\\;:"<>,.?/~`'
    # set the maximum password length to 10 characters
    for length in range(1, 10):
        # generate all possible combinations of characters of length 'length'
        for pwd in itertools.product(chars, repeat=length):
            pwd = ''.join(pwd)
            # Hash the string using SHA512
            hashed_pwd = hashlib.sha512(pwd.encode()).hexdigest()
            # Check if the hash matches the hash we are trying to crack
            if hashed_pwd == hash_value:
                print('Hasil Crack:', pwd)
                return pwd
    print('Hasil Tidak ditemukan.')
    mainmenu = input("Press [ENTER] to go to main menu.")
    return mainmenu


def randompass():
    # mendefinisakan alphabet untuk dibuat random password
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars

    # menentukan panjang password yang akan digenerate
    pwd_length = 12

    pwd = ''
    for i in range(pwd_length):
        pwd += secrets.choice(alphabet)
    print("Hasil Generate Password :", pwd)
    mainmenu = input("Press [ENTER] to go to main menu.")
    return mainmenu


if __name__ == "__main__":
    main()
