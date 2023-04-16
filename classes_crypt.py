from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac
from base64 import urlsafe_b64encode
from config import ITERATION, HASH_NAME

class MakeKey:
    """Генерирует ключ"""
    def __init__(self, salt: str, password: str):
        self._salt = salt
        self._password = password

    @property
    def key(self) -> bytes:
        """Зашифровывает ключ"""
        return pbkdf2_hmac(
            hash_name=HASH_NAME,
            password=self._password.encode("utf-8"),
            salt=self._salt.encode("utf-8"),
            iterations=ITERATION
        )
    
    @property
    def key_encode64_bytes(self) -> bytes:
        """возвращает ключ в формате 32bit"""
        return urlsafe_b64encode(self.key)

    @property
    def key_encode64_str(self) -> str:
        """возвращает ключ в формате строки"""
        return self.key_encode64_bytes.decode("utf-8")


class CryptFile:
    """Шифрует, расшифровывает текст по ключу"""
    def __init__(self, key_64encode: bytes) -> None:
        self._fernet = Fernet(key_64encode)
        
    def encrypt_in_bytes(self, file: bytes) -> bytes:
        """шифрует текс в формате bytes"""
        return self._fernet.encrypt(file)

    def enrypt_in_str(self, file: bytes) -> str:
        """шифрует текст в формате строка"""
        return self._fernet.encrypt(file).decode("utf-8")

    def decrypt_in_bytes(self, encrypt_file: bytes) -> bytes:
        """расшифровывает текст в формате bytes"""
        return self._fernet.decrypt(encrypt_file)
    
    def decrypt_in_string(self, encrypt_file: bytes) -> str:
        """расшифровывает текст в формате строка"""
        return self._fernet.decrypt(encrypt_file).decode("utf-8")

