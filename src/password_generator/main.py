from passwordgen import *


password = Password(10,2)
print("Password: "+password.get_password()+ " status: "+ password.get_status())

#pwd = input("Gib dein Passwort ein: ")
#password = Password.create_password(pwd)
#print(password.get_safety())
#print(password.get_password()+"status: "+ password.get_status())
