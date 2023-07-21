import csv
from os import remove, write

class User():
    def __init__(self, name, residence):
        self.name= name
        self.residence= residence
    

    def __str__(self):
        return self.name + ", " + self.residence


  
def meny(): # Main meny of choices
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('|                        WELCOME                                  |')
    print('|         1. Create user & save user to Guest List & csv-file.    |')
    print('|         2. Load saved users                                     |')
    print('|         3. Delete user                                          |')
    print('|         4. End program                                          |')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

  

guest_list = [] # Gust list
while True:
    meny()
    choice = int(input("Please enter the nr of your choice: "))

    
    if choice == 1: #Create user
        print("Adding a new guest in guest book")
        print()
        add_guest = input("Please enter your first name?: ")
        x=add_guest.isalpha()
        if x==True:
            pass
        my_residence= input("What is your residence?: ")
        print()
        y=my_residence.isalpha()
        if y==True:
            pass
        if x and y==True:
            print(f"Hello {add_guest} from {my_residence}! You are added to the down below guest list!")
            print()
            new_guest= User(add_guest, my_residence)    
            guest_list.append(new_guest)
            print("The following list of guests: ")
            print("~~~~~~~~~~~~~~~~~~~~~~~")

            for i, item in enumerate(guest_list):      
                print("{}. {}".format(i+ 1, item))
            print("~~~~~~~~~~~~~~~~~~~~~~~")
            print()

        else:
            print(u"\u001b[2J")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("You need to add at least one letter in both your: \n--name\n and your\n --residence \nPlease fill out the required fields again!")    
            print()
            print("Press enter to go back to main meny and select 1. Create user again:")
            input()
            print(u"\u001b[2J") 

        if len(guest_list)> 0:
            with open ('guest_list.csv', 'w', newline='', encoding='utf8') as csvfile:
                writer=csv.writer(csvfile)
                writer.writerow(guest_list[0]. __dict__.keys())
                for guest in guest_list:
                    writer.writerow(guest. __dict__.values())
            print("Also find the guest list in the created file 'quest_list.csv' ")
            print("=========================================================")
            print()
            print("If you want to continue please make a choice in the meny!\n", end="")
        if len(guest_list)==0:
                print("No new users have been created!")       

 
    if choice == 2:
        # Load users
        with open ('guest_list.csv', newline='', encoding='utf8') as csvfile:
                reader=csv.reader(csvfile)
                guest_list=[]
                for row in reader:
                    guest_list.append(User(row[0], row[1]))
                guest_list=guest_list[1:] 
                print('Yor have loaded the saved users.\n')
                print("The following list of guests: ")
                print("~~~~~~~~~~~~~~~~~~~~~~~")

        for i, item in enumerate(guest_list):      
            print("{}. {}".format(i + 1, item))
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        print("Press enter to go back to menu!")
        input()
        print(u"\u001b[2J") 
 
    if choice == 3: # Delete user
        print()
        for i, item in enumerate(guest_list):      
            print("{}. {}".format(i + 1, item))
        print("Enter the number of the user do you want to delete?")
        x=int(input())
        guest_list.pop(x-1)
        if len(guest_list)> 0:
            with open ('guest_list.csv', 'w', newline='', encoding='utf8') as csvfile:
                writer=csv.writer(csvfile)
                writer.writerow(guest_list[0]. __dict__.keys())
                for guest in guest_list:
                    writer.writerow(guest. __dict__.values())
            print("User have been removed and the updated list can be seen in the file'quest_list.csv' ")
            print("=======================================")
            print("Press enter to go back to menu!")
            input()

    if choice == 4:
        print("The program will be shut down!")
        break
