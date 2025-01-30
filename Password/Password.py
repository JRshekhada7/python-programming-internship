import random
import string

class PasswordGenerator:
    def __init__(self, length):
        self.length = length

    def generate_password(self):
        if self.length < 4:
            return "Password length must be at least 4 characters!"

        # Combining different character sets
        characters = string.ascii_letters + string.digits + string.punctuation

        
        password = (
            random.choice(string.ascii_uppercase) +  # At least 1 uppercase
            random.choice(string.ascii_lowercase) +  # At least 1 lowercase
            random.choice(string.digits) +           # At least 1 digit
            random.choice(string.punctuation)        # At least 1 special character
        )

       
        password += ''.join(random.choices(characters, k=self.length - 4))

        
        password = ''.join(random.sample(password, len(password)))

        return password



def main():
    print(" Random Password Generator ")
    
    
    try:
        length = int(input("Enter the desired password length: "))
        generator = PasswordGenerator(length)
        password = generator.generate_password()
        print("\n Your Secure Password: ", password)
    except ValueError:
        print(" Please enter a valid number!")

# Running the program
if __name__ == "__main__":
    main()
