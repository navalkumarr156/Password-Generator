import random, string

length = int(input("Enter passord lenght: "))

chars = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(chars) for i in range(length))


with open("password.txt", "a") as f:
  a = "-"
  f.write(f"{a} {password}\n")

print("Your password: ", password)