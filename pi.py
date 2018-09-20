import math

def main():

    n = int(input("Number of terms:"))
    total = 0
    sgn = 1   
    for i in range(1, 2*n, 2):
        total = total + sgn * 4.0/i
        sgn = -sgn 

    print("The approximate value is:", total)
    print("Difference:", math.pi - total)

main()
        
