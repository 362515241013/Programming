#!/usr/bin/env python
# coding: utf-8

# In[2]:


# นาย วรทัต ศิลป์ชัย 362515241013 EE36241N
username = input("username")
password = input("password")
if username == "EE36241N" and password == "362515241013":
    print("Welcome to Aoys Shop")
    print("-----------Menu-----------")
    print("1. Water 20 THB")
    print("2. Ichitan 20 THB")
    print("3. Lay 10 THB")
    print("4. notbook 12 THB")
    print("5. pepsi 10 THB")
    print("--------------------------")
    ch= int(input("What do you want :"))
    if ch==1:
        price=20
        print("Your order :", "Water", "20 THB")
        How=int(input("How many do you need :"))
        print( "Total :",How*price, "THB")
    elif ch==2:
        price=20
        print("Your order :", "Ichitan", "20THB")
        How=int(input("How many do you need :"))
        print( "Total :",How*price, "THB")
    elif ch==3:
        price=10
        print("Your order :", "Lay", "10 THB") 
        How=int(input("How many do you need :"))
        print( "Total :",How*price, "THB")
    elif ch==4:
        price=7
        print("Your order :", "notbook", "12 THB")
        How=int(input("How many do you need :"))
        print( "Total :",How*price, "THB")
    elif ch==5:
        price=10
        print("Your order :", "pepsi", "10 THB")
        How=int(input("How many do you need :"))
        print( "Total :",How*price, "THB")
    else:
        print("You not order")    
else:
    print("You not member")
print("Thank you")


# In[ ]:




