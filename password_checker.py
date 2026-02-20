def password_strength(password):
    score=0

    if len(password) >0 or len(password)==8:
        score=score+1
    if len(password) >=12:
        score=score+1

    upper=False
    lower=False
    digit=False
    special=False

    for char in password:
        if char.isupper():
            upper=True
        elif char.islower():
            lower=True
        elif char.isdigit():
            digit= True
        elif not char.isalnum():
            special=True

    if upper:
        score=score+1
    if lower:
        score=score+1
    if digit:
        score=score+1
    if special:
        score=score+1

    if score<3:
        return "Weak Password"
    elif score<5:
        return "Medium"
    elif score<6:
        return "Strong"
    else:
        return "Very Strong"
    
password=input("Enter Password: ")
print("Password Strength:", password_strength(password))

