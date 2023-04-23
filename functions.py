from classes_crypt import CryptFile
from cryptography.fernet import InvalidToken
import sys

def get_decrypt_text(file_path: str, key: bytes) -> bytes | None:
    try:
        with open(file_path, "rb") as f:
            file = f.read()
    except FileNotFoundError:
        print("Не верное имя файла, \nИли не верный путь")
    except IsADirectoryError:
        print("Это дирректория")
    else:
        fermet = CryptFile(key)
        try:
            decrypt_file = fermet.decrypt_in_bytes(file)
        except InvalidToken:
            print("Неверный ключ,\nИли файл не зашифрован")
        else:
            while True:
                try:
                    decrypt_file = fermet.decrypt_in_bytes(decrypt_file)
                except InvalidToken:
                    return decrypt_file


def get_encrypt_text(file_path: str, key: bytes) -> bytes | None:
    try:
        with open(file_path, "rb") as f:
            file = f.read()
    except FileNotFoundError:
        print("Не верное имя файла, \nИли не верный путь")
    except IsADirectoryError:
        print("Это директория")
    else:
        fermet = CryptFile(key)
        try:
            fermet.decrypt_in_bytes(file)
        except InvalidToken:
            print("Не верный предыдущий ключ, \nИли не зашифрованный файл")
        else:
            print("Файл был зашифрован до этого, ключ подходит")
        finally:
            return fermet.encrypt_in_bytes(file)





