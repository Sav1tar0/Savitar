 TIP – Travel Itinerary Planner (Console App)

TIP is a simple Python console-based application that helps users manage and organize their travel trips. It allows you to create, update, search, sort, save, and load trip data easily through a menu-driven interface.

Features
Add new trips
View all saved trips
Update existing trips
Search trips by ID, destination, or date
Sort trips by destination, date, or price
Save trips to a file (trips.txt)
Load trips from file
Clear all stored data
Help menu with instructions
Support contact info
Exit system safely
How It Works

The program stores all trip data in a Python list of dictionaries:

trip = {
    "id": "1",
    "destination": "Paris",
    "date": "12-06-2026",
    "duration": 5,
    "price": 1200.0
}

Each menu option performs operations on this list.

  Menu System
1. New trip
2. My trips
3. Update trip
4. Search trip
5. Sort trips
6. Help
7. Save to file
8. Load from file
9. Clear all data
10. Support
0. Exit
  File Storage

Trips are saved in a simple text file:

trips.txt

Format:

id,destination,date,duration,price

Example:

1,Paris,12-06-2026,5,1200.0
 Requirements
Python 3.x

No external libraries required.

 How to Run

Clone the repository and run:

python main.py
 Notes
Console-based UI (no GUI)
Data is stored temporarily in memory unless saved to file
Simple error handling included
Designed for beginner-level Python practice
 Support

If you need help:

Email: gusein366@gmail.com
WhatsApp: (+994)99-800-75-76
 Author

Developed by Huseyn Gahramanov
