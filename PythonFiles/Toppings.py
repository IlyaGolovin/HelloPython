toppings = ['van','stre','ber']
newtop = input("Type a new top please")
for topping in toppings:
   if topping == newtop:
    print("Already here")
   else:
     toppings.append(newtop) 
   print("I will add new top")
   print(toppings)