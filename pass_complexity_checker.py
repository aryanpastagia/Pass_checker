import re

def password_complexity_checker(password):
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Check all criteria
    if all([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria]):
        return "Password is strong"
    else:
        feedback = "Password is weak. It should contain:"
        if not length_criteria:
            feedback += "\n- At least 8 characters"
        if not uppercase_criteria:
            feedback += "\n- At least one uppercase letter"
        if not lowercase_criteria:
            feedback += "\n- At least one lowercase letter"
        if not digit_criteria:
            feedback += "\n- At least one digit"
        if not special_char_criteria:
            feedback += "\n- At least one special character"
        return feedback

# Test the function
password = input("Enter a password to check its complexity: ")
print(password_complexity_checker(password))
