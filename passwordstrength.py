import re

def check_password_strength(password):
    
    # Check length
    length_score = min(len(password) // 3, 5)

    # Check if it contains both uppercase and lowercase letters
    upper_lower_score = 2 if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password) else 0

    # Check if it contains numbers
    digit_score = 2 if re.search(r"\d", password) else 0

    # Check if it contains special characters
    special_char_score = 2 if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) else 0

    # Calculate total score
    total_score = length_score + upper_lower_score + digit_score + special_char_score

    # Categorize into levels
    if total_score <= 4:
        strength = "Very Weak"
    elif total_score <= 7:
        strength = "Weak"
    elif total_score <= 10:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength

# Get password input from the user
password = input("Enter your password: ")

# Check password strength
result = check_password_strength(password)

# Display result
print(f"Password Strength: {result}")