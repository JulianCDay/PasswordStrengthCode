import math

def password_entropy(password):
    # Define character sets
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?`~"
    
    # Initialize entropy
    R = 0
    L = len(password)
    entropy = 0
    
    # Check for the presence of character sets
    has_lowercase = any(char in lowercase_letters for char in password)
    has_uppercase = any(char in uppercase_letters for char in password)
    has_digits = any(char in digits for char in password)
    has_special = any(char in special_characters for char in password)
    
    # Calculate entropy based on character sets
    if has_lowercase:
        R += 26
    if has_uppercase:
        R += 26
    if has_digits:
        R += 10
    if has_special:
        R += 32
    
    # Calculate entropy based on password length
    entropy += math.log2(R) * L
    
    return entropy

# Example usage

password = input("Enter your password: ")
entropy_score = password_entropy(password)

if entropy_score <= 35.0:
    print("Very Weak Password")
elif 35.0 < entropy_score <= 59.0:  # Fix the bitwise AND and add proper comparison
    print("Weak Password")
elif 59.0 < entropy_score <= 119.0:  # Fix the bitwise AND and add proper comparison
    print("Strong Password")
elif entropy_score > 119.0:
    print("Very Strong Password")

print(f"Password Entropy: {entropy_score} bits")