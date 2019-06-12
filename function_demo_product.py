a=float(input("Enter price of product 1 = "))
b=float(input("Enter price of product 2 = "))
c=float(input("Enter price of product 3 = "))
def function1(a_,b_,c_) :
    total_amt=a_+b_+c_
    if(total_amt>1000) :
        discount_amt=total_amt*10/100
        final_amt = total_amt-discount_amt
        print("Your Amount : {0} ".format(total_amt))
        print("Discount Amount :{0} ".format(discount_amt))
        print("You have To Pay : {0} ".format(final_amt))
    else :
        print("No Discount ")
        print("You have to Pay : ",total_Amt)

function1(a,b,c)
    
