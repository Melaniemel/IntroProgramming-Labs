def main():
    print ("PYTHON GUESSING GAME")
main()

answer = "dog"
guess = ""

while not guess == answer:
    print("I'm thinking of an animal")
    guess = input("What animal am I thinking about?")
    break

if guess == answer:
    print("You win!")
else:
    print ("Wrong! Try Again")


                
