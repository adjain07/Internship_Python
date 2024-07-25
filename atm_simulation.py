name = input("plz enter your name :")
print("Hello",name)

message = """"
How may i help you .

please select any of them option,
type 1 >>>>>> CHECK BALANCE.
type 2 >>>>>> DEPOSIT.
type 3 >>>>>> WITHDRAWL.
"""
print(message)
task = int(input("plz enter your option :"))
avilable_amount = 10000

if task >=1 and task <=3:
    print('welcome to you in virtual bank program')

    if task == 1:
     print("your avilable amount is : ",avilable_amount,'INR')
     print("thank you for visiting !")
    elif task == 2:
        deposite_amount = int(input("please enter deposite amount : "))
        if deposite_amount >0:
          available_amount = avilable_amount + deposite_amount
          print("you have successfully deposited your amount :",deposite_amount)
          print('your available amount is : ',available_amount,'INR')
        else:
            print("please enter valid amount!")




    else:
        withdraw_amount = int(input ("please enter withdraw amount : "))
        if withdraw_amount <= avilable_amount:
            avilable_amount -= withdraw_amount
            print('You have succussfully withdrawl your amount: ' ,withdraw_amount)
            print( 'Your available amount is : ', avilable_amount,' INR')
        else:
            print("you dont have sufficient amount in your account!")
            print('Your available amount is : ' ,avilable_amount,' INR')
else:
    print("Sorry, you are not select valid option")
    print("thank you for visiting!")