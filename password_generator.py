import random
import string

def generate_password(length, include_chars):
    chars = ''
    if 'uppercase' in include_chars:
        chars += string.ascii_uppercase
    if 'lowercase' in include_chars:
        chars += string.ascii_lowercase
    if 'digits' in include_chars:
        chars += string.digits
    if 'special' in include_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    print("This is an open source password generator made by an")
    print("indepedent developer that is still learning python.")
    length = int(input("Enter the length of the password: "))
    
    include_chars = []
    while True:
        print("\nChoose character types to include:")
        print("1. Uppercase letters")
        print("2. Lowercase letters")
        print("3. Digits")
        print("4. Special characters")
        print("5. Generate Password")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            include_chars.append('uppercase')
        elif choice == '2':
            include_chars.append('lowercase')
        elif choice == '3':
            include_chars.append('digits')
        elif choice == '4':
            include_chars.append('special')
        elif choice == '5':
            if len(include_chars) == 0:
                print("Please select at least one character type.")
            else:
                password = generate_password(length, include_chars)
                print(f"Your generated password is: {password}")
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
