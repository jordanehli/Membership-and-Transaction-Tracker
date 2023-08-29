#Author: Jordan Ehlinger
#Assignment Number & Name: HW2 Audiobooks
#Due Date: N/A
#Program Description: Collects membership and transaction information and outputs a summary of the transaction


##NAMED CONSTANTS
#declare the tax rate
tax_rate=0.0825


##INPUT COLLECTION
#request customer's name
customer_name=input("What is your name? ")

#request the amount of books they would like to purchase
number_of_books_purchased=int(input("How many books would you like to buy? "))

#request current membership type
membership_input=input("What kind of member are you? (Press R for Regular or P for Premium): ")

#convert membership response and ask for membership upgrade
if membership_input == "R" or membership_input == "r":
    membership_type="Regular Customer"
    upgrade_request=input("Would you like to upgrade to a premium membership for a fee of $4.95? (Y for Yes or N for No): ")
#fulfill upgrade request by applying membership fee and upgrading the membership type
    if upgrade_request=="Y" or upgrade_request=="y":
        membership_fee=4.95
        membership_type="Premium Member"
    else:
        membership_fee=0
else:
    membership_type="Premium Member"
    membership_fee=0
    upgrade_request="n/a"


##CALCULATIONS    
#calculate number of free books earned
if membership_type=="Regular Customer":
    if number_of_books_purchased<8:
        free_books=0
    elif number_of_books_purchased<=12:
        free_books=1
    else:
        free_books=2
else:
    if number_of_books_purchased<6:
        free_books=0
    elif number_of_books_purchased<=9:
        free_books=1
    else:
        free_books=2

#calculate total books received
total_books=number_of_books_purchased + free_books

#calculate subtotal
if membership_type=="Regular Customer":
    subtotal=number_of_books_purchased*9.95
else:
    subtotal=number_of_books_purchased*8.49

#calculate tax
tax=tax_rate*subtotal 

#calculate price of total sale
total_sale=subtotal+tax+membership_fee


##DISPLAY OUTPUTS
#product summary header
print("\n------Product Summary------")

#display customer name
print("Customer Name: ",customer_name,sep='')

#display if customer has membership or not
print("Customer Type: ",membership_type,sep='')

#display total number of books received
print("Total Books: ",total_books,sep='')

#display subtotal price
print("Subtotal: $",format(subtotal,'.2f'),sep='')

#display thank you message for membership upgrade
if upgrade_request=="Y" or upgrade_request=="y":
    print("Thank you for upgrading to a premium membership!")
    print("Membership Fee: $4.95")
elif upgrade_request=="n/a":
    print("Thank you for being a valued member of gBooks!")
else:
    print("Thank you for shopping with us! You can upgrade your membership at any time.")

#display sales tax
print("Sales Tax: $",format(tax,'.2f'),sep='')

#display price of total sale
print("Total: $",format(total_sale,'.2f'),sep='')
