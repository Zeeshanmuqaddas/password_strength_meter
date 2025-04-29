import re

def check_password_strength(password):
    """
    Check the strength of a password and return a score and feedback.
    
    Criteria:
    - Length (8+ chars)
    - Contains uppercase letters
    - Contains lowercase letters
    - Contains numbers
    - Contains special characters
    - Not a common password
    """
    
    # Common weak passwords to check against
    common_passwords = [
        'password', '123456', '12345678', '1234', 'qwerty', 
        'letmein', 'admin', 'welcome', 'monkey', 'sunshine'
    ]
    
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    # Check for special characters
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    # Check against common passwords
    if password.lower() in common_passwords:
        score = 0
        feedback.append("This password is too common and easily guessable.")
    
    # Determine strength level
    if score == 0:
        strength = "Very Weak"
    elif score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"
    
    return {
        'score': score,
        'strength': strength,
        'feedback': feedback
    }

def main():
    print("Password Strength Meter")
    print("-----------------------")
    
    while True:
        password = input("\nEnter a password to check (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            break
            
        result = check_password_strength(password)
        
        print(f"\nPassword Strength: {result['strength']} ({result['score']}/5)")
        
        if result['feedback']:
            print("\nSuggestions to improve:")
            for suggestion in result['feedback']:
                print(f"- {suggestion}")
        
        print("\nScoring Criteria:")
        print("- At least 8 characters")
        print("- Contains uppercase letters")
        print("- Contains lowercase letters")
        print("- Contains numbers")
        print("- Contains special characters")
        print("- Not a common password")

if __name__ == "__main__":
    main()