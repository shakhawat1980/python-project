
class bikeshop:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("total Bike",self.stock)
    def rentForBike(self,q):
        if q<=0:
            print("Enter the postive value or greater them zero")
        elif q>self.stock:
            print("Enter the value (less then stock)")
        else:
            self.stock=self.stock-q
            print("Total prices",q*100)
            print("Total Bikes",self.stock)
while True:
    obj=bikeshop(100)
    print('''
      1.Display Stocks
      2. Rent a Bike
      3. Exit''')
    a=int(input("Enter the serial number:"))
    print()
    if a==1:
        obj.displayBike()
    elif a==2:
        n=int(input("Enter the Qty:---"))
        obj.rentForBike(n)
    else:
        break

