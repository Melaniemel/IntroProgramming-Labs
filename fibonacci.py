#A Fibonacci number is a sequence of numbers where each successive number
#is the sum of the previous two. The classic Fibonacci sequence begins:
#1, 1, 2, 3, 5, 8, 13, .... Write a program that computes the nth Fibonacci
#number where n is a value input by the user.
#For example, if n = 6, then the result is 8.

#Start with a function that you later call outside of the function

def main():
    n = int(input("Enter the value for n: "))
    current, previous = 1,1
    for i in range (n-2):
        current,previous = current + previous, current

    print()
    print("Answer is", current)

main()

