productNames = [ "Ultrasonic range finder"
               , "Servo motor"
               , "Servo controller"
               , "Microcontroller Board"
               , "Laser range finder"
               , "Lithium polymer battery"
               ]
productPrices = [ 2.50, 14.99, 44.95, 34.95, 149.99, 8.99 ]

productQuantities = [ 4, 10, 5, 7, 2, 8 ]

def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(products)):
        if product[i].quantity > 0:
            print()
            print(str(i)+")",product[i].name, "$", product[i].price)
    
def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit": break
        prodId = int(vals[0])
        count = int(vals[1])
        if product[prodId].quantity >= count:
            if cash >= product[prodId].price * count:
                product[prodId].quantity -= count
                cash -= product[prodId].price * count
                print("You purchased", count, product[prodId].name+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:print("Sorry, you cannot afford that product.")
            else:print("Sorry, we are sold out of", product[prodId].name)
main()

class Product:
    def __init__ (self, name, price, quantity):
        self.name =""
        self.price =""
        self.quantity = ""

productNames = Product()


   
            
        
