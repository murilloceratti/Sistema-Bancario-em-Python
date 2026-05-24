import hashlib

def hashSenha(senha):

    senha = str(senha)

    senha_bytes = senha.encode('utf-8')
    
    hash_objeto = hashlib.sha256(senha_bytes)
    return hash_objeto.hexdigest()
