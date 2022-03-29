from passlib.context import CryptContext

context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def encrypt(plaintext_password: str) -> str:
    return context.hash(plaintext_password)


def verify(plaintext_password: str, hashed_password: str) -> bool:
    return context.verify(plaintext_password, hashed_password)
