import re
from entropy import calculate_entropy

COMMON_PASSWORDS =["123456", "password", "qwerty", "admin", "welcome"]

def check_strength(password):

    score = 100
    issues = []

    if password.lower() in COMMON_PASSWORDS:
        score -= 60
        issues.append("Password is too common.")

    if len(password) < 8:
        score -= 30
        issues.append("Password is too short.")

    if not re.search(r'[A-Z]', password):
        score -= 10
        issues.append("Password should contain at least one uppercase letter.")

    if not re.search(r'[a-z]', password):
        score -= 10
        issues.append("Password should contain at least one lowercase letter.")

    if not re.search(r'[0-9]', password):
        score -= 10
        issues.append("Password should contain at least one digit.")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score -= 10
        issues.append("Password should contain at least one special character.")

    entropy = calculate_entropy(password)

    if entropy <3 :
        score -= 20
        issues.append("Password entropy is too low.")

    if score >=80:
        level = "STRONG"
    elif score >=50:
        level = "MEDIUM"
    else:
        level = "WEAK"

    return{
        "score": score,
        "level": level,
        "issues": issues,
        "entropy": entropy
    }