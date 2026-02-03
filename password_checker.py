import re

def password_strength(pwd):
    score = 0
    tips = []

    if len(pwd) < 8:
        tips.append("Use at least 8 characters")
    else:
        score += 1

    if not re.search("[A-Z]", pwd):
        tips.append("Add an uppercase letter")
    else:
        score += 1

    if not re.search("[a-z]", pwd):
        tips.append("Add a lowercase letter")
    else:
        score += 1

    if not re.search("[0-9]", pwd):
        tips.append("Add a number")
    else:
        score += 1

    if not re.search("[^a-zA-Z0-9]", pwd):
        tips.append("Add a special character")
    else:
        score += 1

    return score, tips


pwd = input("Enter password: ")
score, tips = password_strength(pwd)

print("\nResult:")

if score == 5:
    print("Strong password 👍")
elif score >= 3:
    print("Medium strength password ⚠️")
else:
    print("Weak password ❌")

if tips:
    print("\nSuggestions:")
    for tip in tips:
        print("-", tip)
