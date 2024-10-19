import random

def generate_password(length):
    # Define the character set for the password
    characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-?><:"
    
    # Ensure the password contains at least one character from each category
    password = [
        random.choice("abcdefghijklmnopqrstuvwxyz"),  # lowercase letter
        random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),  # uppercase letter
        random.choice("01234567890"),  # digit
        random.choice("!@#$%^&*()_+=-?><:")  # special character
    ]
    
    # Fill the rest of the password with random characters
    for _ in range(length - 4):
        password.append(random.choice(characters))
    
    # Shuffle the list to avoid the first characters always being in the same character category order
    random.shuffle(password)
    
    # Join the characters into a single string
    return "".join(password)

def main():
    # Get the password length from the user
    while True:
        try:
            passlen = int(input("Enter the length of the password (min 4): "))
            if passlen < 4:
                print("Password length must be at least 4.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    

    password = generate_password(passlen)
    print("Generated Password : ", password)

if __name__ == "__main__":
    main()
