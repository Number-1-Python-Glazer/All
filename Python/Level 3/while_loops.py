
name = input("Enter your name")

while name == "":
    print("You didnt enter anything")
    input("Enter your name")

print(f"    hello {name}")

age = int(input("Enter your name"))

while age < 0:
    print("Age cant be negative")
    age = int(input("Enter your age"))
    
print(f"You are {age} years old")

food = input("Enter a food you like (q tjo quit)")
while not food == "q":
    print(f"You like your {food}")
    food = input("Enter another food you like (q to quit)")
print("bye")
 
movie = input("Enter a movie you like (q to quit)")

while not movie == "q":
    print(f"You like {movie}!")
    movie = input("Another one (q to get out)")
print("bye")

num = int(input("Enter a number between 1 through 10"))

while num < 1 or num >10:
    print(f"{num}is not valid")
    num = int(input("Number between 1 and 10 again "))
print(f"Your number is{num}")

