import threading 
import random 
import time

freechairs = 3                                                          #I designed the code so the varibales (cusomters, freechairs, length of waitign room) can be easily changed even by someone who has no knowledge of python
waiting_room = []                                           
threads = []
waiting_room_size = 15

def enters_shop():                      
    print("Customer " + threading.current_thread().getName() + " has entered the shop!")
    if freechairs > 0:                                                  #check if there is a free chair and print outcome 
        print("There is a free chair.")
    else:
        print("All chairs are full.")
    
    inside_barber_shop(customer)

def inside_barber_shop(customer):                       
    global freechairs                                                   #delcare freechairs as a global variable

    if freechairs < 1:                                                  #check to see if there is a freechair
        
        if len(waiting_room) < waiting_room_size:                       #if there is an empty seat in the waiting room add the customer to the list
            waiting_room.append(threading.current_thread().getName())

            print("Customer "+ threading.current_thread().getName() + " has been added to the waiting room.")
            print("The waiting room consists of " + str(waiting_room))
        
        else:                                                           #if not the customer must leave
            print("The waiting room is full and customer " + threading.current_thread().getName() + " must leave")
    
    else:
        haircut(customer)                                               #give the customer a haircut
    
def haircut(customer):
    global freechairs

    freechairs -= 1                                                     #once the customer goes for their haircut, mark the seat as used
    print("Customer " + str(customer) + " is getting their haircut")
    haircut_length = random.randint(5, 10)                              #the haircut will take a random amount of time, the thread will sleep
    time.sleep(haircut_length)
    
    print("Customer " + str(customer) + " is finished getting their haircut")

    if len(waiting_room) == 0:                                          #the barber then checks the length of the waiting room,if empty, the barber sleeps
        freechairs += 1                                                 #and the seat becomes free
        print("The waiting room is empty")              
    

    else:
        print((str(waiting_room)) + " are left in the waiting room")
        print("The barber will now take " + waiting_room[0])


        if len(waiting_room) > 0:                                       #if there is someone in the waiting room

            haircut(waiting_room.pop(0))                                #trim the cusomter who has been waiting the longest and remove them from the waitng room


        else:
            print("There are no more customers")                        #this is triggered when the program has completed 


#main body of code 
cusomters = random.randint(40, 50)                                      #produces a range of customers
print("Amount of customers: " + str(cusomters))                               
for customer in range(0, cusomters):
    time_between_cusomters = random.randint(0, 4)                       #random intreval between customers entering the shop
    time.sleep(time_between_cusomters)                                  #sleep for time 
    print("\n")                                                         #make the output seperated per customer for readability purposes
    customer = threading.Thread(target=enters_shop, name=customer)      #start the thread, named customer and target set to the start of the barber shop
    customer.start()                                                    #start each thread
    threads.append(customer)                                            

for thread in threads:
    thread.join()                                                       #wait for each thread to finish
