password = "123456789"

if len(password) < 8:
    password = "Weak"
elif len(password) <= 10:
    password = "Medium"
else:
    password = "Strong"

print("Password Strength Is : ", password)