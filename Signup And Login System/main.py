from replit import db
from getpass import getpass

Users = []
Dictionary = {}

try:
  Users = db["Users"]
except KeyError:
  db["Users"] = []
try:
  Dictionary = db["Accounts"]
except KeyError:
  db["Accounts"] = {}


def SignUp():
  while True:
    User = input("Username:  ")
    if User in Users:
      print("\nError: Username exists\n")
      continue
    else:
      break
  Passcode = getpass("Passcode:  ")
  Users.append(User)
  db["Users"] = Users
  Dictionary.update({User: Passcode})
  db["Accounts"] = Dictionary


def SignIn():
  while True:
    User = input("Username:  ")
    if User in Users:
      break
    else:
      print("\nError: Username Does Not exists\n")
      continue
  Passcode = getpass("Passcode:  ")
  if Dictionary[User] == Passcode:
    print(f"Welcome {User}")


print("""
Welcome to Dashtiss's Signin/SignUp System using replit db

1: Signup
2: SignIn
""")
while True:
  try:
    choice = int(input("Choice:  "))
  except ValueError:
    print("\nError Not a valid choice\n")
    continue
  else:
    break
if choice == 1:
  SignUp()
elif choice == 2:
  SignIn()
