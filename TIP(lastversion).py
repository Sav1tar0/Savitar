import time
import os

trips = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') 


def load(n):
    print("Loading...")
    time.sleep(n)
    print("Done!")
    time.sleep(1)
    clear()

def back_to_menu():
    while True:
        back = input("Press Enter to go back to the main menu...")
        if back == '':
            load(1.2)
            break
        else:
            print("Invalid input! Please press Enter to go back.")

    


#first page(welcome page)
def welcome_page():
    welcome=r'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                    WELCOME TO TIP                    |
|      Take your first step towards your dream trips   |
|                       with TIP ;)                    |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
    print(welcome)  
    next_page = input("Press Enter to continue...")  
    if next_page == '':
        clear()
    else:
        print("Invalid input! Please press Enter to continue.")
        welcome_page()
    load(3)
    

def main_menu():
    print('''
|<<<<<<<<<< Main Menu >>>>>>>>>>|
|<<    1. New trip       ----->>|
|<<    2. My trips       ----->>|
|<<    3. Uptade trip    ----->>|
|<<    4. Search trip    ----->>|
|<<    5. Sort trips     ----->>|
|<<    6. Help           ----->>|
|<<    7. Save to file   ----->>|
|<<    8. Load from file ----->>|
|<<    9. Clear all data ----->>|
|<<   10. Support        ----->>|
|<<    0. Exit           ----->>|
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|
                                     

''')
    
#1
def new_trip():
    try:
        trip = {
            "id": input("Enter trip ID: "),
            "destination": input("Enter destination: "),
            "date": input("Enter date (DD-MM-YYYY): "),
            "duration": int(input("Enter duration (in days): ")),
            "price": float(input("Enter price: "))
        }
        trips.append(trip)
        load(2.5)
        return "Trip added successfully."
        


    except ValueError:
        print("Invalid input! Duration, price must be a number. ")
    



#2
def my_trips():
    load(2) 
    if not trips:
        print("No trips available.")
    else:
        print("{:<10}{:<20}{:<15}{:<10}{:<10}".format("ID", "Destination", "Date", "Duration", "Price"))
        for t in trips:
            print("{:<10}{:<20}{:<15}{:<10}{:<10.2f}".format(t["id"], t["destination"], t["date"], t["duration"], t["price"]))
    
    back_to_menu()
    load(1)



#3
def update_trip():
    load(2)
    trip_id = input("Enter trip ID to update: ")
    for t in trips:
        if t["id"] == trip_id:
            t["destination"] = input("New destination: ")
            t["date"] = input("New date (DD-MM-YYYY): ")
            try:
                t["duration"] = int(input("New duration (in days): "))
                t["price"] = float(input("New price: "))
            except ValueError:
                print("Invalid input! Duration and price must be numbers.")
            load(2)    
            print("Trip updated.")
            return
        else:
            print("Trip not found.") 
        time.sleep(1.5)
        clear()
   
        
#4
def search_trip():
    load(2)
    search_term = input("Enter destination, date or ID to search: ")
    found_trips = [t for t in trips if search_term.lower() in t["destination"].lower() or search_term in t["date"] or search_term in t["id"]]
    if found_trips:
        print("{:<10}{:<20}{:<15}{:<10}{:<10}".format("ID", "Destination", "Date", "Duration", "Price"))
        for t in found_trips:
            print("{:<10}{:<20}{:<15}{:<10}{:<10.2f}".format(t["id"], t["destination"], t["date"], t["duration"], t["price"]))
    back_to_menu()
    load(1.5)
        
#5
def sort_trips():
    load(2)
    sort_by = input("Sort by (destination/date/price): ").lower()
    if sort_by == "destination":
        sorted_trips = sorted(trips, key=lambda x: x["destination"])
    elif sort_by == "date":
        sorted_trips = sorted(trips, key=lambda x: x["date"])
    elif sort_by == "price":
        sorted_trips = sorted(trips, key=lambda x: x["price"])
    else:
        print("Invalid choice! Please try again.")
        return
    load(2)
    print("{:<10}{:<20}{:<15}{:<10}{:<10}".format("ID", "Destination", "Date", "Duration", "Price"))
    for t in sorted_trips:
        print("{:<10}{:<20}{:<15}{:<10}{:<10.2f}".format(t["id"], t["destination"], t["date"], t["duration"], t["price"]))
    back_to_menu()
#6
def help():
    clear()
    print('''
          
^^^^^^^^^^^******************  HELP  *********************^^^^^^^^^^^
/\    1. New trip: Add a new trip to the list.                      /\  
\/    2. My trips: View all your trips.                             \/    
||    3. Update trip: Update the details of an existing trip.       ||
/\    4. Search trip: Search for a trip by destination, date or ID. /\  
\/    5. Sort trips: Sort your trips by destination, date or price. \/
||    6. Help: View this help message.                              ||
/\    7. Save to file: Save your trips to a file.                   /\ 
\/    8. Load from file: Load trips from a file.                    \/ 
||    9. Clear all data: Clear all trips from the list.             || 
/\    10. Support: Get support information.                         /\      
\/    11. Exit: Exit the program.                                   \/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
                                               
''')
    back_to_menu()
    time.sleep(2)
    

#7
def save_to_file():
    load(2)
    with open("trips.txt", "w") as file:
        for trip in trips:
            file.write(f"{trip['id']},{trip['destination']},{trip['date']},{trip['duration']},{trip['price']}\n")
    print("Trips saved to file.")
    time.sleep(2)
    clear()

#8
def load_from_file():
    load(4)
    global trips
    try:
        with open("trips.txt", "r") as file:
            trips = []
            for line in file:
                id, destination, date, duration, price = line.strip().split(",")
                trips.append({
                    "id": id,
                    "destination": destination,
                    "date": date,
                    "duration": int(duration),
                    "price": float(price)
                })
        print("Trips loaded from file.")
    except FileNotFoundError:
        print("File not found. Please save trips first.")
    time.sleep(2)
    clear()

#9
def clear_all_data():
    global trips
    trips = []
    print("All data cleared.")
    time.sleep(2)
    clear()

#10
def support():
    load(0.7)
    print('''
*******************           | SUPPORT |        ***********************
$                                                                      $       
$   |  If you have any questions or need help, please contact us:  |   $
$                                                                      $                                           
$  Email:                                                              $
$     gusein366@gmail.com                                              $
$                                                                      $
$  Whatsapp:                                                           $                                                       
$     (+994)99-800-75-76                                               $
$                                                                      $                               
************************************************************************



''')

#0
def exit(): 
    print("Exiting the program. Goodbye!")
    time.sleep(2)
    clear()
    os._exit(0)  









def main():
    welcome_page()
    while True:
        main_menu()
        try:
            choice = input("Enter your choice: ")
            if choice == '1':
                new_trip()
                time.sleep(2)
                clear()

                
            elif choice == '2':
                my_trips()
                
                


            elif choice == '3':
                update_trip()

           

            elif choice == '4':     
                search_trip()            


            elif choice == '5':
                sort_trips()
            

            elif choice == '6':
                help()
            

            elif choice == '7':
                save_to_file()
            

            elif choice == '8':
                load_from_file()
            

            elif choice == '9':    
                clear_all_data()
            

            elif choice == '10':
                support()
                
            
            elif choice == '0':
                exit()
            
            else:
                print("Invalid choice! Please try again.")
                time.sleep(1)
                clear()

        except Exception as e:
            print("An error occurred:", str(e))


print(main())


