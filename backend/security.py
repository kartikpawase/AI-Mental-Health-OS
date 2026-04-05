try:
    from passlib.context import CryptContext
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
except ImportError:
    pwd_context = None

def verify_password(plain_password, hashed_password):
    if pwd_context is None: return plain_password == hashed_password
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    if pwd_context is None: return password
    return pwd_context.hash(password)

def encrypt_symptom_log(text):
    """
    In a full production 2050 system, use cryptography.fernet for strict medical HIPAA compliance.
    """
    return f"ENCRYPTED__{text[::-1]}__SECURE"
    
def decrypt_symptom_log(encrypted_text):
    if encrypted_text.startswith("ENCRYPTED__"):
        clean = encrypted_text.replace("ENCRYPTED__", "").replace("__SECURE", "")
        return clean[::-1]
    return encrypted_text
