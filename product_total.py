a=float(input("Enter price of product 1 = "))
b=float(input("Enter price of product 2 = "))
c=float(input("Enter price of product 3 = "))
total_Amount = a+b+c
if(total_Amount>1000):
    discount_amt=total_Amount*10/100
    final_amt = total_Amount-discount_amt
    print("Your Amount : {0}".format(total_Amount))
    print("Discount amount : {0}".format(discount_amt))
    print("You have to Pay = {0}".format(final_amt))
else:
    print("No Discount")
    print("Total Amount = {0}".format(total_Amount))

    
