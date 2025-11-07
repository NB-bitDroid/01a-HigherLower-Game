#while True:
#    user_in = input("enter a number: ")
#    if not user_in.isnumeric():
#        print("make sure it's an int")
#    #print(f"you entered {user_in})
    
while True:
   try:
      user_in = int(input("enter a number: "))
   except ValueError:
      print("that wasn't right!")
   print(user_in)
        