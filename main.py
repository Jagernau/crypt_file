from classes_crypt import MakeKey, CryptFile
from cryptography.fernet import InvalidToken
from os import path
import click

user_salt: str = input("Введи соль: ")
user_password: str = input("Введи пароль: ")

byte_key = MakeKey(salt=user_salt, password=user_password).key_encode64_bytes

@click.command()
@click.option("-p", "--path_to_dir", type=str, default="/storage/emulated/0/To_cript", help="Путь до папки с файлом")
@click.option("-f", "--file_name", type=str, default="Test_parols.txt", help="Имя файла")
@click.option("-m", "--metod", type=str, help="Метод обработки файла: decrypt, encrypt")
def main(path_to_dir: str, file_name: str, metod: str, key: bytes=byte_key):
    file_path = path.join(path_to_dir, file_name)
    fermet = CryptFile(key)
    try:
        with open(file_path, "rb") as f:
            file = f.read()
    except FileNotFoundError:
        print("Не верное имя файла, \nИли не верный путь")
    else:
        if metod == "decrypt":
            decrypt_file = fermet.decrypt_in_bytes(file)
            while True:
                try:
                    decrypt_file = fermet.decrypt_in_bytes(decrypt_file)
                except InvalidToken:
                    print(decrypt_file.decode("utf-8"))
                    break

        if metod == "encrypt":
            file_to_save = fermet.encrypt_in_bytes(file)
            with open(file_path, "wb") as f:
                f.write(file_to_save)
if __name__ == '__main__':
    main()
