from argon2 import PasswordHasher

ph = PasswordHasher()

def hashSenha(senha):
    return ph.hash(str(senha))

def verificarSenha(hashSalvo, senhaDigitada):
    try:
        return ph.verify(hashSalvo, str(senhaDigitada))
    except:
        return False
