import secrets
import string

def generate_otp():
    characters = string.ascii_uppercase + string.digits

    
    otp = ''.join(secrets.choice(characters) for _ in range(6))

    return otp


if __name__ == "__main__":
    otp = generate_otp()
    print("Your verification code is:", otp)