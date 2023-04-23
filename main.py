from classes_crypt import MakeKey
from os import path
import click
from config import DEFAULT_DIR, DEFAULT_NAME
from functions import get_decrypt_text, get_encrypt_text


user_salt: str = input("Введи соль: ")
user_password: str = input("Введи пароль: ")

byte_key = MakeKey(salt=user_salt, password=user_password).key_encode64_bytes

@click.command()
@click.option("-p", "--path_to_dir", type=str, default=DEFAULT_DIR, help="Путь до папки с файлом")
@click.option("-f", "--file_name", type=str, default=DEFAULT_NAME, help="Имя файла")
@click.option("-m", "--metod", type=str, help="Метод обработки файла: decrypt, encrypt")
def main(path_to_dir: str, file_name: str, metod: str, key: bytes=byte_key):
    file_path = path.join(path_to_dir, file_name)

    if metod == "decrypt":
        byte_decrypt_text = get_decrypt_text(file_path, key)
        if byte_decrypt_text is not None:
            print(byte_decrypt_text.decode("utf-8"))
        else:
            print("Не раскодируется")

    if metod == "encrypt":
        byte_encrypt_text = get_encrypt_text(file_path, key)
        if byte_encrypt_text is not None:
            with open(file_path, "wb") as f:
                f.write(byte_encrypt_text)
            print("Успешно закодированно и переписанно")
        else:
            print("Не кодируется")

    if metod == "append":
        pass

if __name__ == '__main__':
    main()
