from passlib.context import CryptContext


class Password:
    context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    @classmethod
    def encrypt(cls, plaintext_password):
        return cls.context.hash(plaintext_password)

    @classmethod
    def verify(cls, plaintext_password, hashed_password):
        return cls.context.verify(plaintext_password, hashed_password)
