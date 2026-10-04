import random
char = "sadf!gfjghlyrrewyj@#$@jiumciriq%^&*+-0-=21344354545"
password =""
for i in range(12):
    password += random.choice(char)

print("PASSWORD GENERATED:", password)

