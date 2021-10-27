from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes='bcrypt', deprecated='auto')


class Hash:
    @staticmethod
    def encrypt(password: str):
        return pwd_ctx.hash(password)

    @staticmethod
    def verify(hashed_password, plain_password):
        return pwd_ctx.verify(plain_password, hashed_password)
