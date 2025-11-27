

username = input("Enter a user:")






if len(username) >12:
    print("Your user cant be 12+ long")
elif not username.find(" ") == -1:
    print("no spaces")
elif not username.isalpha():
    print("no numbers")
else:
    print:(f"welcome {username}")