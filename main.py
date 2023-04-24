from classes_crypt import MakeKey, CryptBytes
from os import path
import click
from config import DEFAULT_DIR, DEFAULT_NAME
from functions import get_file_bytes



@click.command()
@click.option("-p", "--path_to_dir", type=str, default=DEFAULT_DIR, help="Путь до папки с файлом")
@click.option("-f", "--file_name", type=str, default=DEFAULT_NAME, help="Имя файла")
@click.option("-m", "--metod", type=str, help="Метод обработки файла: decrypt, encrypt")
def main(path_to_dir: str, file_name: str, metod: str):
    file = get_file_bytes(path_to_dir, file_name)
    if file is not None:
        user_salt: str = input("Введи соль: ")
        user_password: str = input("Введи пароль: ")
        key = MakeKey(salt=user_salt, password=user_password).key_encode64_bytes

        if metod == "decrypt":
            fernet = CryptBytes(key)
            byte_decrypt_text = fernet.get_decrypt_file(file)
            if byte_decrypt_text is not None:
                print(byte_decrypt_text.decode("utf-8"))
            else:
                print("Не раскодируется")

        if metod == "encrypt":
            fernet = CryptBytes(key)
            byte_encrypt_text = fernet.get_encrypt_file(file)
            if byte_encrypt_text is not None:
                with open(path.join(path_to_dir, file_name), "wb") as f:
                    f.write(byte_encrypt_text)
                print("Успешно закодированно и переписанно")
            else:
                print("Не кодируется")

        if metod == "append":
            pass


    else:
        print("Файл не открывается")
    
    
if __name__ == '__main__':
    main()
