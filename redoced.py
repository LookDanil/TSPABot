from cryptography.fernet import Fernet
def redoced():
    def load_key():
        with open('key.key', 'rb') as key_file:
            return key_file.read()

    def decrypt_token(encrypted_token, key):
        fernet = Fernet(key)
        decrypted_token = fernet.decrypt(encrypted_token).decode()
        return decrypted_token

    key = load_key()

    with open('encrypted_token.txt', 'rb') as token_file:
        encrypted_token = token_file.read()

    # Дешифруем токен
    decrypted_token = decrypt_token(encrypted_token, key)
    return decrypted_token