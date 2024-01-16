import os,time
listOfEmail = []
def prettyPrint():
 os.system("clear")
 print("listOfEmail")
 print()
 #for index in range(len(listOfEmail)):
   #print(f"{index}:{listOfEmail[index]}")
 counter = 1
 for email in listOfEmail:
   print(f"{counter}: {email}")
   counter += 1
 time.sleep(1)
  
def spam(max):
  for i in range(0,max):
    print(f"""Email{i+1}
Dear{listOfEmail[1]}
ipsum lorem ipsum ipsum loren ipsum loren.
regards

Menon """)
    time.sleep(1)
    os.system("clear")





    
 #os.system("clear")
 #print("listOfEmail")
 #print()
 #for index in range(len(listOfEmail)):
   #print(f"{index}: {listOfEmail[index]}")

 #time.sleep(1)
while True:
  print("Spammer Inc")
  menu = input("1. Add Email. \n 2. Remove Email \n 3. View Emails \n 4. Get Spamming \n > ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu == "2":
    email = input("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint()
    #if email in listOfEmail:
       #listOfEmail.view(email)
  elif menu == "4":
    spam(10)
      #if email in ListOfEmail :
        #ListOfEmail.spamming(email)
    #prettyPrint()
  time.sleep(7)
  os.system("clear")

    
      
    



#import os, time
#listOfFood = []

#def prettyPrint():
  #os.system("clear") 
  #print("listofFood") 
  #print()
  #counter = 1 
  #for order in listOfFood: 
    #print(f"{counter}: {order}") 
    #counter += 1 
  #time.sleep(1)
#while True:
  #print("Yummy Food Restaurant")
  #menu = input("1. Order food\n2: Delete order\n3. Leave a review\n4. Delivery\n> ")
  #if menu == "1":
    #order = input("order > ")
    #listOfFood.append(order)
  #elif menu =="2":
    #order = input ("delete order> ")
    #if order in listOfFood:
      #listOfFood.remove(order)
  #elif menu == "3": 
    #prettyPrint() 
  #time.sleep(1)
  #os.system("clear")

  
      