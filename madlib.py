def promptForWords():
    global n,v,a,p
    n = input("Enter a noun: ")
    v = input("Enter a verb: ")
    a = input("Enter an adjective: ")
    p = input("Enter a place: ")

def makeAndPrintSentence():
    print("Take your", a , n , "and" , v , "it at the" ,p)

def main():
    promptForWords()
    makeAndPrintSentence()

main()

    


