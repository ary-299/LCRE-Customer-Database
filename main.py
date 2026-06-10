import json
import colorama
import time
import math
import os
import sys
import readchar
from prompt_toolkit import prompt

from colorama import Fore, Back, Style, init
script_dir = os.path.dirname(os.path.abspath(__file__))  # Finds the folder of "main.py" and sets variable "script_dir"
data_path = os.path.join(script_dir, "Data.json") #Sets variable "data_path" as the data path (who wouldve thought) -> with help of the "script_dir" variable set above
search_query = None
init()
with open(data_path, "r") as f:
    data = json.load(f)

    os.system('cls' if os.name == 'nt' else 'clear')


print(Fore.CYAN + Style.BRIGHT + "\n\n\nWelcome to the Database of our Company!\n" + Style.RESET_ALL)
time.sleep(0.3)
print(Fore.BLUE + Style.BRIGHT + "Press any Key to start!"+ Style.RESET_ALL)
readchar.readkey()
match_history = []


time.sleep(0.2)
print(Fore.CYAN + "\r Loading ●○○○  ", end="")
time.sleep(0.1)
print("\r Loading ○●○○  ", end="")
time.sleep(0.1)
print("\r Loading ○○●○  ", end="")
time.sleep(0.1)
print("\r Loading ○○○●  ", end="")
time.sleep(0.1)
print("\r Loading ●○○○  ", end="")
time.sleep(0.1)
print("\r Loading ○●○○  ", end="")
time.sleep(0.1)
print("\r Loading ○○●○  ", end="")
time.sleep(0.1)
print("\r Loading ○○○●  ", end="")
time.sleep(0.1)
print("\r Loading ●○○○  ", end="")
time.sleep(0.1)
print("\r Loading ○●○○  ", end="" + Style.RESET_ALL)
time.sleep(0.1)


print(Fore.LIGHTBLUE_EX +"\rOpening.                    ", end="" + Style.RESET_ALL)
time.sleep(0.2)
print(Fore.LIGHTBLUE_EX+"\rOpening..                   ", end="" + Style.RESET_ALL)
time.sleep(0.2)
print(Fore.LIGHTBLUE_EX+"\rOpening...                  ", end="" + Style.RESET_ALL)
time.sleep(0.1)
print(Fore.GREEN+"\rOpened!                  \n\n", end="" + Style.RESET_ALL)
time.sleep(0.3)

if os.name == 'nt':
    import msvcrt
    while msvcrt.kbhit():
        msvcrt.getch()

else:
    import select
    while select.select([sys.stdin], [],[], 0.0)[0]:
        sys.stdin.read(1)

os.system('cls' if os.name == 'nt' else 'clear')


print(Style.BRIGHT + r"""
__        __   _                          _ 
\ \      / /__| | ___ ___  _ __ ___   ___| |
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
  \ V  V /  __/ | (_| (_) | | | | | |  __/_|
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___(_)
""" + Style.RESET_ALL)
time.sleep(0.5)




while True:
    print(Fore.GREEN + """
    ▄▄▀█▄───▄───────▄
    ▀▀▀██──███─────███      
    ░▄██▀░█████░░░█████░░
    ███▀▄███░███░███░███░▄
    ▀█████▀░░░▀███▀░░░▀██▀
    """ + Style.RESET_ALL)                                                                                               #LOOP1
    print("=============== !Main Menu! ===============\n\n" +
        Fore.RED + ">>Read Data: R<<\n\n" 
        + Fore.GREEN + "       >>Add Data: A<<\n\n" 
        + Fore.BLUE + "              >>Edit Data: E<<\n\n" + Style.RESET_ALL 
        + "                    >>Delete Data: D<<\n\n" 
        + Style.RESET_ALL +
        "===========================================\n->made by ary\n\n"
    )
    REA = readchar.readkey()

    if REA == "R" or REA == "r":
        os.system('cls' if os.name == 'nt' else 'clear')                                                                                                            #READ LOGIC
        with open(data_path, "r") as f:
            data = json.load(f)

            print(Fore.RED + Style.BRIGHT + "\n\nRead Data\n\n" + Style.RESET_ALL)
            time.sleep(0.5)
            
            while True:                                                                                                   #LOOP2
                IOI = input(Fore.CYAN + "\n\n1. Search by ID\n2. Search by Information\n3. List all Information from current session\n4. Go back to Menu\n" + Style.RESET_ALL )
                if IOI == "1":                                                                                         #ID SEARCH
                    while True:                                                                                          #LOOP3
                        customer_ID = input(Fore.BLUE +"\nEnter the customers ID: " + Style.RESET_ALL)
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        try:
                            print(
                                "====================================\n" +
                                Fore.CYAN + Style.BRIGHT + "\n" + "Name: " + Style.RESET_ALL + Fore.CYAN + data[customer_ID]["name"] +Style.RESET_ALL+ "\n"+ Fore.GREEN +
                                Style.BRIGHT + "Adress:\n" + Style.RESET_ALL +
                                Fore.GREEN + "   Street:" + data[customer_ID]["adress"]["street"] + "\n" +
                                "   House Number:" + data[customer_ID]["adress"]["house number"] + "\n" +
                                "   City:" + data[customer_ID]["adress"]["city"] + "\n" +
                                Style.RESET_ALL +
                                "\n====================================")
                            match_history.append((customer_ID, data[customer_ID]))
                            break
                        except KeyError:
                            print(Style.BRIGHT + "\nThis ID does not exist! Try again!\n" + Style.RESET_ALL)
            
                elif IOI == "2":                                                                                    #Information Search
                    while True:
                        search_query = input(Fore.CYAN + "\nEnter a name, street, house number or city. Type b to go back\n" + Style.RESET_ALL +"->").lower()
                        if search_query == "b":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
                        else:
                            time.sleep(1)
                            matches = []
                            found_matches = False
                            for customer_ID, details in data.items():  #Realize, what data to look at. Without this line of code, Python wouldnt know what data to use for the future lines
                                name = details["name"].lower()
                                street = details["adress"]["street"].lower()
                                house_num = str(details["adress"]["house number"])
                                city = details["adress"]["city"].lower()
                                if (search_query == customer_ID or          #search itself
                                            search_query in name or
                                            search_query in street or
                                            search_query == house_num or
                                            search_query in city):
                                                
                                                found_matches = True
                                                matches.append((customer_ID, details)) #dumping the matching information into the empty "matches" list to read it out loud later
                                                match_history.append((customer_ID, details)) #dumping the matching information into the empty "match_history" list to read it out if 4 is being entered
                            
                            if found_matches == True:
                                print("\r Searching ●○○○  ", end="")
                                time.sleep(0.1)
                                print("\r Searching ○●○○  ", end="")
                                time.sleep(0.1)
                                print("\r Searching ○○●○  ", end="")
                                time.sleep(0.1)
                                print("\r Searching ○○○●  ", end="")
                                time.sleep(0.1)
                                print("\r Searching ○○●○  ", end="")
                                time.sleep(0.1)
                                print("\r Searching ○●○○  ", end="")
                                time.sleep(0.1)
                                print("\r Searching ●○○○  ", end="")
                                time.sleep(0.1)
                                print("\r Searching ○●○○  ", end="")
                                time.sleep(0.1)
                                print("\r Searching ○○●○  ", end="")
                                time.sleep(0.1)
                                os.system('cls' if os.name == 'nt' else 'clear') 
                                print(Fore.GREEN + Style.BRIGHT + "\r Match found!    \n\n" +Style.RESET_ALL, end="")
                                time.sleep(0.5)
                                print("====================================")
                                for customer_ID, details in matches:
                                    print(Fore.CYAN + Style.BRIGHT + f"\nName: {details['name']}\n" + Style.RESET_ALL)
                                    print(Fore.GREEN + Style.BRIGHT +   "Adress:\n" + Style.RESET_ALL)
                                    print(Fore.GREEN + f"      City: {details['adress']['city']}\n")
                                    print(f"      Street: {details['adress']['street']}\n")
                                    print(f"      House Number: {details['adress']['house number']}\n" + Style.RESET_ALL)
                                    print(Fore.MAGENTA + Style.BRIGHT + f"Customer ID: {customer_ID}\n" + Style.RESET_ALL )
                                    print("=====================================")
                                    time.sleep(0.3)
                                print(Style.BRIGHT + "\n\nPress any key to continue!" +Style.RESET_ALL)
                                readchar.readkey()
                                os.system('cls' if os.name == 'nt' else 'clear')
                                break
                            else:
                                print("\r Searching ●○○○  ", end="")
                                time.sleep(0.1)
                                print("\r Searching ○●○○  ", end="")
                                time.sleep(0.2)
                                print("\r Searching ○○●○  ", end="")
                                time.sleep(0.4)                            
                                print("\r                \n\n", end="")
                                time.sleep(0.01)
                                BOC = input(Style.BRIGHT + "No matches found! Do you want to" + Style.RESET_ALL + Fore.RED + " try again?" +Style.RESET_ALL + Style.BRIGHT + " (Y/N)" + Fore.RED + " \n(An invalid choice will be counted as N)\n"+Style.RESET_ALL + "->")
                                if BOC.lower() == "y":
                                    print("Reloading...")
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    time.sleep(1)
                                    continue
                                elif BOC.lower() == "n":
                                    print("Going back...")
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    time.sleep(1)
                                    break
                                else:
                                    print("Invalid Choice, Going back...")
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    time.sleep(1)
                                    break
                                

                elif IOI == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                    if match_history == []:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(Fore.RED + Style.BRIGHT + "History Empty!" + Style.RESET_ALL + Style.BRIGHT +" Search for Information and then come back!\n" + Style.RESET_ALL)
                        print(Style.BRIGHT + "\nPress any key to continue" + Style.RESET_ALL)
                        readchar.readkey()
                        os.system('cls' if os.name == 'nt' else 'clear')
                    else:
                        print(Style.BRIGHT + "\n\nYour Search Result History:\n\n")
                        print("====================================")
                        for customer_ID, details in match_history:                                                                  #Result history
                            print(Fore.CYAN + Style.BRIGHT + f"\nName: {details['name']}\n" + Style.RESET_ALL)
                            print(Fore.GREEN + Style.BRIGHT + "Adress:\n" + Style.RESET_ALL)
                            print(Fore.GREEN + f"   City: {details['adress']['city']}\n")
                            print(f"   Street: {details['adress']['street']}\n")
                            print(f"   House Number: {details['adress']['house number']}\n" + Style.RESET_ALL)
                            print(Fore.MAGENTA + Style.BRIGHT + f"Customer ID: {customer_ID}\n" + Style.RESET_ALL )
                            print("=====================================\n")
                            time.sleep(0.2)
                    time.sleep(0.5)
                    print(Style.BRIGHT + Fore.RED + "\n\nPress any Key to continue!"+ Style.RESET_ALL)
                    readchar.readkey()
                    os.system('cls' if os.name == 'nt' else 'clear')

                elif IOI == "4":                                                    #esc
                    print("\rGoing back to menu ●○○○", end="")
                    time.sleep(0.1)
                    print("\rGoing back to menu ○●○○", end="")
                    time.sleep(0.1)
                    print("\rGoing back to menu ○○●○", end="")
                    time.sleep(0.1)
                    print("\rGoing back to menu ○○○●", end="")
                    time.sleep(0.1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue


                        
    elif REA == "A" or REA == "a":    
        time.sleep(0.2)                                                                                                        #ADD LOGIC
        with open(data_path, "r") as f:
            data = json.load(f)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.RED + Style.BRIGHT + "\nAdd Data\n" + Style.RESET_ALL)
            AddC = input(Fore.CYAN + "\n\n\nDo you really want to add a new customer? (Y/N)\n\n" + Style.RESET_ALL).lower()
            time.sleep(0.1)

            if AddC == "y":
                while True:    
                    new_name = input(Fore.CYAN + "\n\nEnter the customers Name\n"+ Style.RESET_ALL +"->")
                    if new_name.replace(" ", "").replace("-", "").isalpha():
                        print(Fore.GREEN + Style.BRIGHT + new_name + " ✓" + Style.RESET_ALL)
                        break
                    else: 
                        print(Fore.RED + Style.BRIGHT + new_name + " X" + Style.RESET_ALL)
                        print("\nPlease Enter a Real Name!\n")

                while True:    
                    new_street = input(Fore.CYAN + "\nEnter the customers Street\n" + Style.RESET_ALL +"->")
                    if new_street.replace(" ", "").replace("-", "").replace(".", "").isalpha():
                        print(Fore.GREEN + Style.BRIGHT + new_street + " ✓" + Style.RESET_ALL)
                        break  
                    else:
                        print(Fore.RED + Style.BRIGHT + new_street + " X" + Style.RESET_ALL)
                        print("Please Enter a Real Street!")

                while True:
                    try:
                        new_house_number = int(input(Fore.CYAN + "\nEnter the customers house number\n"+ Style.RESET_ALL+ "->"))
                        print(Fore.GREEN + Style.BRIGHT + str(new_house_number) + " ✓\n" + Style.RESET_ALL)    
                        break  
                    except ValueError: 
                        print(Fore.RED + "\nThat is not a number! Try again!\n" + Style.RESET_ALL)

                while True:    
                    new_city = input(Fore.CYAN + "\nEnter the customers city\n"+Style.RESET_ALL +"->")
                    if new_city.replace(" ", "").replace("-", "").replace(".", "").isalpha():
                        print(Fore.GREEN + Style.BRIGHT + new_city + " ✓\n" + Style.RESET_ALL)
                        break  
                    else:
                        print(Fore.RED + Style.BRIGHT + new_city + " X\n" + Style.RESET_ALL)
                        print(Fore.RED + "\nPlease Enter a Real City!\n" + Style.RESET_ALL)

                print(Fore.RED + "\rLoading.  ", end="")
                time.sleep(0.25)
                print(Fore.BLUE + "\rLoading.. ", end="")
                time.sleep(0.25)
                print(Fore.YELLOW + "\rLoading..." + Style.RESET_ALL)
                time.sleep(0.25)

                All_IDs = []
                for key in data.keys():
                    All_IDs.append(int(key))
                    
                if not All_IDs:
                    new_ID = 1
                else:
                    new_ID = max(All_IDs) + 1     #if json is empty, fallback to ID=1

                data[str(new_ID)] = {
                    "name": new_name,
                    "adress": {
                        "street":new_street,
                        "house number":str(new_house_number),
                        "city":new_city
                    }
                }

                with open(data_path,"w") as f:
                    json.dump(data, f, indent=4)

                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.MAGENTA + Style.BRIGHT + f" ----> Customers new ID: {new_ID}\n\n" + Style.RESET_ALL) 
                time.sleep(0.5)
            else:
                print(Fore.RED + "\nAborted!"+ Style.RESET_ALL+ Style.BRIGHT + " Press any key to go back to menu!\n\n" + Style.RESET_ALL)
                readchar.readkey()
                os.system('cls' if os.name == 'nt' else 'clear')

    elif REA == "E" or REA == "e": 
            time.sleep(1)
            TDE = 0
            while True:    
                if TDE == 999:
                    break
                    
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.BLUE + Style.BRIGHT + "Edit Data\n\n")
                
                user_id_input = input(Fore.BLUE + "\nEnter the customers ID: " + Style.RESET_ALL + Style.BRIGHT + "\nEnter a letter to go back!\n" + Style.RESET_ALL).strip()
                
                if not user_id_input.isdigit():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                    
                customer_ID = user_id_input
                
                with open(data_path, "r") as f:
                    data = json.load(f)
                    
                try:
                    time.sleep(0.1)
                    print("\r Searching ○○●○  ", end="")
                    time.sleep(0.1)
                    print("\r Searching ○●○○  ", end="")
                    time.sleep(0.1)
                    print("\r Searching ●○○○  ", end="")
                    time.sleep(0.1)
                    print("\r Searching ○●○○  ", end="")
                    time.sleep(0.1)
                    print("\r Searching ○○●○  ", end="")
                    time.sleep(0.5)
                    
                    if customer_ID not in data:
                        raise KeyError
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\n====================================\n" +
                    Fore.CYAN + Style.BRIGHT + "\n" + "Name: " + Style.RESET_ALL + Fore.CYAN + data[customer_ID]["name"] + Style.RESET_ALL + "\n" + Fore.GREEN +
                    Style.BRIGHT + "Adress:\n"
                    "   Street:" + Style.RESET_ALL + Fore.GREEN + data[customer_ID]["adress"]["street"] + "\n" + Style.RESET_ALL +
                    Fore.GREEN + Style.BRIGHT + "   House Number:" + Style.RESET_ALL + Fore.GREEN  + data[customer_ID]["adress"]["house number"] + "\n" + Style.RESET_ALL +
                    Fore.GREEN + Style.BRIGHT + "   City:" + Style.RESET_ALL + Fore.GREEN  + data[customer_ID]["adress"]["city"] + "\n"+ Style.RESET_ALL +
                    "\n====================================")
                    
                    YSYN = input(Style.BRIGHT + Fore.RED+ "\n\nAre you sure that you want to edit this data? (Y/N)\n"+ Style.RESET_ALL + Style.BRIGHT + "*everything except for Y and N will be counted as N!\n" + Style.RESET_ALL).lower()
                    
                    if YSYN == "y":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        while True:
                            print("\n====================================\n" +
                            Fore.CYAN + Style.BRIGHT + "\n" + "Name: " + Style.RESET_ALL + Fore.CYAN + data[customer_ID]["name"] + Style.RESET_ALL + "\n" + Fore.GREEN +
                            Style.BRIGHT + "Adress:\n"
                            "   Street:" + Style.RESET_ALL + Fore.GREEN + data[customer_ID]["adress"]["street"] + "\n" + Style.RESET_ALL +
                            Fore.GREEN + Style.BRIGHT + "   House Number:" + Style.RESET_ALL + Fore.GREEN  + data[customer_ID]["adress"]["house number"] + "\n" + Style.RESET_ALL +
                            Fore.GREEN + Style.BRIGHT + "   City:" + Style.RESET_ALL + Fore.GREEN  + data[customer_ID]["adress"]["city"] + "\n"+ Style.RESET_ALL +
                            "\n====================================")
                            print(Fore.RED + Style.BRIGHT + "\n\nWhat do you want to edit?\n"+Style.RESET_ALL+Fore.CYAN+"\n1. Name"+Style.RESET_ALL+Fore.GREEN+"\n2. Street\n3. House Number\n4. City\n\n"+Style.RESET_ALL)
                            NASHC = input("-> ").strip()
                            
                            if NASHC == "1":
                                temp_name = prompt("\nEdit the Name: ", default=data[customer_ID]["name"])
                                if temp_name.replace(" ", "").replace("-", "") .isalpha() == True:
                                    data[customer_ID]["name"] = temp_name
                                    break
                                else:
                                    print(Fore.RED + "\nInvalid Name! Press any Key to continue!\n")
                                    readchar.readkey()
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    continue
                            elif NASHC == "2":
                                temp_street = prompt("\nEdit the Street: "+Style.RESET_ALL, default=data[customer_ID]["adress"]["street"])
                                if temp_street.replace(" ", "").replace("-", "") .isalpha()== True:
                                    data[customer_ID]["adress"]["street"] = temp_street 
                                    break
                                else:
                                    print(Fore.RED + "\nInvalid Street! Press any Key to conitnue\n")
                                    readchar.readkey()
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    continue
                            elif NASHC == "3":
                                try:
                                    temp_HN = int(prompt("\nEdit the House number: ", default=data[customer_ID]["adress"]["house number"]))
                                    data[customer_ID]["adress"]["house_number"] = int(temp_HN)
                                    break
                                except ValueError:
                                    print(Fore.RED + "\nThat is not a number! Press any key to go back!\n" + Style.RESET_ALL)
                                    readchar.readkey()
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    continue
                            elif NASHC == "4":
                                temp_City = prompt("\nEdit the city:" , default=data[customer_ID]["adress"]["city"])
                                if temp_City.replace(" ", "").replace("-", "") .isalpha() == True:
                                    temp_city = data[customer_ID]["adress"]["city"]
                                    break
                                else:
                                    print(Fore.RED + "\nInvalid City! Press any Key to go bacK!\n" + Style.RESET_ALL)
                                    readchar.readkey()
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    continue
                            elif NASHC == "b":
                                time.sleep(0.1)
                                print("\r Going back ●○○○  ", end="")
                                time.sleep(0.1)
                                print("\r Going back ○●○○  ", end="")
                                time.sleep(0.1)
                                print("\r Going back ○○●○  ", end="")
                                os.system('cls' if os.name == 'nt' else 'clear')
                                break
                            else:
                                print("Invalid choice, choose 1-4.")
                                continue

                        with open(data_path, "w") as f:
                            json.dump(data, f, indent=4)
                        print(Fore.GREEN + "\nData successfully updated and saved!" +Style.RESET_ALL)
                        time.sleep(1)
                        
                except KeyError:
                    time.sleep(0.1)
                    print("\r Searching ●○○○  ", end="")
                    time.sleep(0.1)
                    print("\r Searching ○●○○  ", end="")
                    time.sleep(0.1)
                    print("\r Searching ○○●○  ", end="")
                    print(Fore.RED + "\r                                           \n\nID not found!\n" +Style.RESET_ALL,end="")
                    
                    while True:
                        ECYN = input(Style.BRIGHT +"Do you want to search again? (Y/N)\n"+Style.RESET_ALL).lower()
                        if ECYN == "y":
                            print("Try again:")
                            break
                        elif ECYN == "n":
                            TDE = 999
                            print("\rGoing Back.  ", end="")
                            time.sleep(0.1)
                            print("\rGoing Back.. ", end="")
                            time.sleep(0.1)    
                            print("\rGoing Back...", end="")
                            time.sleep(0.3)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
                        else:
                            print(Style.BRIGHT + Fore.RED + "\n\nThat is not a valid answer!" + Style.RESET_ALL)
                            continue
    elif REA == "D" or REA == "d":
        time.sleep(0.2)
        
        with open(data_path, "r") as f:
            data = json.load(f)
            
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + Style.BRIGHT + "Delete Customer Record\n\n" + Style.RESET_ALL)
        
        target_ID = input(Fore.BLUE + "Enter the ID of the customer to delete: " + Style.RESET_ALL).strip()
        
        if target_ID not in data:
            print(Fore.RED + f"\nThe Customer ID {target_ID} does not exist!" + Style.RESET_ALL)
            print("Press any key to go back...")
            readchar.readkey()
            continue
            
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.YELLOW + Style.BRIGHT + "WARNING:" + Style.RESET_ALL)
        print(f"You are about to permanently delete: {Fore.CYAN}{data[target_ID]['name']}{Style.RESET_ALL}")
        
        confirm = input(Fore.RED + "\nAre you absolutely sure? This cannot be undone! (Y/N)\n"+Style.RESET_ALL+Style.BRIGHT+"*any invalid choise will be counted towards N\n\n" + Style.RESET_ALL).lower().strip()
        
        if confirm == "y":
            del data[target_ID]
            
            with open(data_path, "w") as f:
                json.dump(data, f, indent=4)
                
            print(Fore.GREEN + "\nCustomer record successfully deleted!" + Style.RESET_ALL)
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(1.5)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.BLUE + "\nDeletion canceled. Returning to menu..." + Style.RESET_ALL)
            time.sleep(1.5)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        continue