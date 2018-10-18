def main():
    print ("PYTHON GUESSING GAME")
main()

answer = "dog"
guess = ""


while not guess == answer:
    print("I'm thinking of an animal")
    guess = input("What animal am I thinking about?")
    guess = guess.lower()
    
    if guess == answer:
        choice = input("Do you like the animal?  Y for yes and N for no.")
        if choice == "Y":
            print ("I love them too.")
        if choice == "N":
            print("I don't like them either.")
            break
        
    elif guess[0] == "q":
        break

    else:
        print ("Wrong! Try Again")


                
