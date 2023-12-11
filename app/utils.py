import bcrypt

def hash(password: str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify(plain_pass, hashed_pass):
    return bcrypt.checkpw(plain_pass.encode(), hashed_pass.encode())
