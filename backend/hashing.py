from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


def Hash(password: str):
    return pwd_ctx.hash(password)


def Verify(plain_password, hashed_password):
    return pwd_ctx.verify(plain_password, hashed_password)
