import random

def filestart():
    open("BookingList.txt", "a").close()
    choice()
# ^ Starts each file and ensures they all exist (if they don't exist they are made here)

def stafflogin():
    print(f"Welcome to the staff login page. If you wish to access the customer portal, please input 'customer' in the next available input / text slot.\n"
          f"Please note that you will NOT be able to access any shortcuts when typing in your password, it will only work through your login.")
    while True:
        login = input("Enter your login name: ").lower()
        password = input("Enter your password: ")
        if login in Actions_map:
            Actions_map[login]()
            break
        elif not login or not password:
            print("Please ensure that you are providing an input.")
            break
    filestart()

def search_booking(search_type):
    value = input(f"Enter the {search_type.lower()} to search: ").lower()
    search = f"{search_type}: {value}"
    try:
        with open("BookingList.txt","r") as file: 
            lines=file.readlines()
            for number, line in enumerate(lines):
                if search in line:
                    print(f"{search} exists in your booking list.")
                    print(f"Line Number: {number}")
                    print(f"Line Content: {line}")
                    print("Surrounding lines:")
                    print("".join(lines[max(0,number-4):number+5]))
                    return True
                else:
                    print(f"{search} does not exist in our booking records.")
                    return False
    except FileNotFoundError:
        print("Booking file not found. Reloading files now. You will have to login again, we apologise for any inconveniences.")
        filestart()

def completedlogin():
    while True:
        controls=input("\nWelcome to the staff portal.\nA) View booking list\nB) Search for stalls\nC) See whether invoices have been paid\nD) Return to customer menu\nE) Quit the program\nSelect an option: ").lower()
        if controls == "a" or controls == "view booking list":
            try:
                with open("BookingList.txt","r") as file: content=file.read()
                if content.strip():
                    print(content)
                else:
                    print("No bookings found.")
            except FileNotFoundError:
                print("Booking file not found. Reloading files now.")
                filestart()
        elif controls in ("b","c") or controls in ("search for stalls", "see whether invoices have been payed or not"): 
            search_menu()
        elif controls == "d" or controls == "return to customer menu":
            print("You are now being redirected to the customer menu.")
            UserDetails()
        elif controls == "e" or controls == "quit":
             quitchoice = input("Are you sure you want to quit?").lower()
            if quitchoice == "yes" or "y":
                quit()
            else:
                print("You will now be returned to the staff menu.")
                completedlogin()
        else: 
            print("Please select one of the listed options of either 'a', 'b', 'c', 'd' or 'e'.")




def search_menu():
    types = {"booking number": "Booking Number", "stall": "Stall Name", "stall name": "Stall Name", "vendor": "Vendor Name", "vendor name": "Vendor Name"}
    while True:
        search = input("Do you want to search by stall name, vendor name or booking number? ").lower()
        if search not in types:
            print("Please enter booking number, stall name or vendor name.")
            continue
        if search_booking(types[search]):
            return
        print("The search component failed to load. You will now be returned to the main menu, and we apologise for any inconveniences.")
        return

def choice():
    while True:
        userchoice = input(f"Welcome to the official staff and booking portal for the Glastonbury Festival of Contemporary Performing Arts - 2026.\n"
                           f"Do you want to access the staff login page or instead access the customer page? ").lower()
        if userchoice == "staff" or userchoice == "staff login" or userchoice == "staff page":
            print("You will now be redirected to the staff page.")
            stafflogin()
        elif userchoice == "customer" or userchoice == "customer page":
            print("You will now be redirected to the customer page.")
            UserDetails()
        elif userchoice in Actions_map:
            Actions_map[userchoice]()
        else:
            print("Please enter a valid option of either 'staff' / 'staff login' or 'customer' / 'customer page' respectively.")

def UserDetails():
    print(f"Welcome to the booking component of the booking and staff portal for the Glastonbury Festival of Contemporary Performing Arts - 2026.\n"   
    f"If at any point you want to restart the booking process, please just type 'restart' into the next available input slot. In a similar fashion, if at any point you want to quit, just type 'quit' into the next available input.\n"   
    f"If at any point you instead want to either go straight to the staff menu or return back to the portal choice menu, please just type 'staff' or 'choice' accordingly into the next available input slot.\n"   
    f"We will now begin the booking process, please follow any instructions provided and answer all of the questions below:")
    while True:
        name = input("Enter your full name (excluding middle names): ")
        if not name:
            print("Please ensure that you are providing an input.")
        elif name in Actions_map:
            Actions_map[name]()
        elif len(name.split()) <= 1 or len(name.split()) > 2:
            print("Please ensure that you are providing your first and last name, excluding any middle names.")
        else:
            break
    while True:
        age = input("Enter your age in whole numbers (do not round up): ")
        if age in Actions_map:
            Actions_map[age]()
        elif not age:
            print("Please ensure that you have provided an input and try again.")
        else:
            try:
                age = int(age)
                if age < 18:
                    print("You need to be over 18 to fill out this form. Please give this form to someone over the age of 18.")
                    quit()
                else:
                    break
            except ValueError:
                print("Please ensure that you have enterred your age in whole numbers, e.g. '19'.")
                
    contact1, contact2, booking_number = UserContacts()
    booking_number, stall_name = StallName(booking_number)
    deposit = Deposit()
    size_a = StallSize()
    duration_a = BookingDuration()
    banner_b = PromotionalBanner()
    invoice_number = InvoiceNumber()
    final_cost = stallcost(size_a, duration_a, invoice_number, banner_b)
    invoice, invoice_paid, reciept = FinalInvoice(name, contact1, contact2, stall_name, deposit, booking_number, invoice_number, size_a, duration_a, banner_b, final_cost)
    return name, age


def UserContacts():
    while True:
        contact1 = input("Please enter your correct phone number (including the 0 at the beginning) with no spaces: ")
        contact1a = "0" in contact1
        if len(contact1) != 11 or contact1a == False:
            print("Your phone number is incorrect. Please ensure that you have included a 0 at the beginning of your phone number, and that you haven't accidentally inputted an additional number which is not part of your phone number")
        else:
            break
    while True:
        contact2 = input("Please enter your email: ")
        contact2a = "@" in contact2
        if contact2 in Actions_map:
            Actions_map[contact2]()
        elif len(contact2) <= 8 or contact2a == False or len(contact2.split()) !=1:
            print("Your email address is incorrect. Please ensure that you have typed out your email correctly and that you have included the full domain name (e.g. ___@gmail.com), or that you are only providing your email, and try again.")
        else:
            break
    while True:
        booking_number = random.randint(1, 100000000)
        with open("BookingList.txt", "r") as file:
            content = file.read()
            booking_number2 = str(booking_number)
            while booking_number2 in content:
                if booking_number == 100000000:
                    booking_number = 1
                else:
                    booking_number = booking_number + 1
            else:
                break
    return contact1, contact2, booking_number


def StallName(booking_number):
    while True:
        stall_name = input("Enter your desired stall name: ")
        if stall_name in Actions_map:
            Actions_map[stall_name]()
        elif not stall_name:
            print("Please ensure that you are providing an input and try again.")
        elif len(stall_name.split()) >= 9:
            print("Please enter a name that isn't greater than 8 words in total.")
        else:
            with open("BookingList.txt", "r") as f2:
                content = f2.read()
                if stall_name in content:
                    while stall_name in content:
                        print("This stall name is already taken. Please enter an unused stall name: ")
                else:
                    break
    return booking_number, stall_name

def Deposit():
    while True:
        deposit = input("Enter your deposit (in GBP / £): ")
        if deposit in Actions_map:
            Actions_map[deposit]()
        elif not deposit:
            print("Please ensure that you are providing an input and try again.")
        else:
            try:
                deposit = float(deposit)
                if deposit < 25.0:
                    print("A deposit of atleast £25.00 is required")
                else:
                    print("Deposit Successful.")
                    break
            except ValueError:
                print(
                    "Your deposit has not been processed. Please ensure that your deposit is in numerical form WITHOUT any additional symbols or characters (i.e. currency symbols, etc).")
    return deposit

def StallSize():
    size_a = 0
    size_choices = {"small": 200, "medium": 400, "large": 600}
    while True:
        size = input("Enter the desired size of your stall (small / medium / large): ").lower()
        if size in Actions_map:
            Actions_map[size]()
        elif not size:
            print("Please ensure that you are providing an input.")
        elif len(size.split()) > 1:
            print("Please ensure that you are only providing one stall size (if you are, please ensure that no other words are included).")
        else:
            if size in size_choices:
                size_a = size_choices[size]
                break
            else:
                print("Please enter a valid size of your stall: ")
    return size_a

def BookingDuration():
    duration_a = 0
    duration_choices = {"1": 1, "1 day": 1, "2": 2, "2 days": 2, "3": 3, "3 days": 3, "4": 4, "4 days": 4, "5": 5, "5 days": 5, "6": 6, "6 days": 6}
    while True:
        duration = input("Enter the desired duration of your booking (in days) between 1 and 6: ")
        if duration in Actions_map:
            Actions_map[duration]()
        elif len(duration) <= 0:
            print("Please enter a valid duration in full days.")
        else:
            if duration in duration_choices:
                duration_a = duration_choices[duration]
                break
            else:
                print("Please enter a valid duration of your booking (in days) between 1 and 6 days: ")
    return duration_a

def PromotionalBanner():
    banner_b = False
    # ^ Sets banner as being false to start off with to prevent banner being set as true in case the remainder of the subroutine doesn't work as intended for whatever reason
    while True:
        banner = input("Do you wish to include a promotional banner in order to reduce your cost by 10%? (Yes/No) ").lower()
        if banner in Actions_map:
            Actions_map[banner]()
        elif not banner:
            print("Please ensure that you are providing an input and try again.")
        elif banner == "yes" or banner == "y":
            print(f"Thank you, your discount will be applied during checkout.")
            banner_b = True
            break
        elif banner == "no" or banner == "n":
            print(f"Thank you, you will not have any discount applied.")
            banner_b = False
            break
        else:
            print("Please enter a valid option of yes or no.")
    return banner_b

def stallcost(size_a, duration_a, banner_b, deposit):
    final_cost = size_a * duration_a
    final_cost -= deposit
    if banner_b == True:
        final_cost -= final_cost * 0.1
        # Applies banner discount of 10% of total cost
    
    if final_cost < 0:
        print("Your total cost has failed to calculate. We apologise for the inconvenience, however you will need to complete your booking once again.")
        quit
    return final_cost

def InvoiceNumber():
    invoice_number = random.randint(1, 100000000)
    with open("BookingList.txt", "r") as f2:
        content = f2.read()
        invoice_number2 = str(invoice_number)
        while invoice_number2 in content:
            if invoice_number >= 100000000:
                invoice_number = 1
            else:
                invoice_number += 1
    return invoice_number

def FinalInvoice(name, contact1, contact2, stall_name, deposit, booking_number, invoice_number, size_a, duration_a,banner_b, final_cost):
    invoice_paid = False
    invoice = (f"\n---INVOICE---\nInvoice for {name}\n:" 
    f"\nDetails:\n"
    f"Vendor Name: {stall_name}\n"    
    f"Deposit: {deposit}\n"    
    f"Booking Number: {booking_number}\n"   
    f"Invoice Number: {invoice_number}\n"  
    f"\nThe following costs have been applied:\n"    
    f"Stall Size: +£{size_a}\n"  
    f"Stall Duration: {size_a} x {duration_a}\n"    
    f"Promotional Banner Discount Applicable: {banner_b}\n"    
    f"=============\n" 
    f"Total Cost of Stall:\n"    
    f"£{final_cost}\n")
    print(invoice)
    # ^ Shows user invoice and sets the invoice paid to false by default
    reciept = (f"\nVendor Name: {name}\n"
    f"Vendor Phone Number: {contact1}\n"
    f"Vendor Email Address: {contact2}\n"
    f"Stall Name: {stall_name}\n"
    f"Booking Number: {booking_number}\n"
    f"Deposit: {deposit}\n"
    f"Banner (Y/N): {banner_b}\n"
    f"Invoice Paid (Y/N): {invoice_paid}\n")
    try:
        with open("BookingList.txt", "a") as file:
            file.write(reciept)
            # ^ Stores invoice and receipt, receipt is written to booking file to prevent useless bloating of information in the primary list
        print("Data stored successfully. Please await further instructions. ")

    except FileNotFoundError:
        print("Files could not be loaded properly. We apologise for this, however you will need to re-complete your booking.")
        filestart()
        # ^ If files are not found, which should've been caught earlier unless they were unexpectedly deleted (still shouldn't have happened as they'd just be created now) or a bug was found
    while True:
        restart = input("Would you like wish to make a separate booking for a new stall? ").lower()
        if restart == "yes" or restart == "y":
            UserDetails()
        elif restart == "no" or restart == "n":
            while True:
                choice = input("Do you wish to access the staff portal or quit the program? ")
                if choice in Actions_map:
                    Actions_map[choice]()
                else:
                    print("Please enter a valid option of either 'staff' / 'staff portal' or 'quit' / 'restart' accordingly.")
        else:    
            print("Please input a valid option of 'yes' or 'no'.")
    return invoice, invoice_paid, reciept

Actions_map = {"restart": UserDetails, "choice": choice, "quit": quit, "staff": stafflogin, "staff portal": stafflogin, "customer": UserDetails, "quit the program": quit}
 # ^ Fixes need for multiple unnecessary if elif statememnts following every input

filestart()
# ^ Starts the entire program by verifying / creating files (depending on whether they exist on the machine they are being ran on nor not,
# "filestart" subroutine also calls next subroutine, which calls the subroutine after that, etc
