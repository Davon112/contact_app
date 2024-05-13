





# Main Menu Index
add_contact = "1" 
edit_contact = "2"
delete_contact = "3"
search_contact = "4"
display_contact = "5"
export_contact = "6"
quit = "8"

# Variable Index
contact_dict = {"785-845-7351": {"Name": "Davon Manuel", "Email": "davon.manuel@gmail.com", "Phone Number": "785-845-7351", "Category": "Work" }}
print(contact_dict)
print(contact_dict.items())
print(contact_dict.keys())

app_user = input("\nHello! Please enter your name: ")
#This is the main menu
def main ():
    import re   
    print("\n                     "+ app_user)
    print("         How would you like to manage your contacts")        
        #If you change this you will need to change the main menu index
    print("\n     TASK MENU:")
    print("            1)    Add new contact")
    print("            2)    Edit contact")
    print("            3)    Delete contact")
    print("            4)    Search")
    print("            5)    Display contacts")
    print("            6)    Export contact")
    print("            8)    Quit")
    menu1 = (input(f"\n{add_contact}, {edit_contact}, {delete_contact}, {search_contact}, {display_contact}, {export_contact}, {quit}: ")) #DONT CHANGE NAME MENU1
    while True:
        if menu1 == quit:
            print("Keep connected")
            exit()
            break
        else:
            if menu1 == add_contact:
                while True:
                    user_input = input("Press enter to continue, type 'quit' to exit ")
                    if user_input == "quit":
                        break
                    else:
                        print(contact_dict)
                        while True:
                            name = input("First & Last Name: ")
                            regex_name = re.search(r"^[A-Z][a-z]+\s[A-Z][a-z]+$", name)
                            if regex_name == None:
                                print("\nOnly use characters a-z")
                            else:
                                break
                        while True:    
                            add_email = input("Email: ")
                            regex_email = re.search(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", add_email)
                            if regex_email == None:
                                print("\nInvalid Response. Ex: name123@gmail.com")
                            else:
                                break
                        
                        while True:
                            add_phone = input("Phone Number: ###-###-#### ")
                            regex_phone = re.search(r"\d{3}-\d{3}-\d{4}", add_phone)
                            if regex_phone == None:
                                print("\nPlease only use 1-9 and use ###-###-#### format")
                            else:
                                break
                            
                        add_category = input("Friend, Family, or Work?: ")
                        full_contact = {"Name": {name}, "Email": {add_email}, "Phone Number": {add_phone}, "Category": {add_category}}
                        contact_dict[add_phone] = full_contact
                        print(contact_dict)
            elif menu1 == edit_contact:
                while True:
                    print(contact_dict.keys())
                    user_input2 = input(f"Which contact would you like to edit? type 'quit' to exit: ")
                    if user_input2 == "quit":
                        print("Back to menu")
                        break
                    else:
                        print(f"{contact_dict[user_input2]}: What would you like to edit?")
                        edit_input = input("Name, Email, Number, Category?: ").lower()
                        if edit_input == "name":
                            new_name = input("Insert Name: ")
                            new_name_regex = re.search(r"^[A-Z][a-z]+\s[A-Z][a-z]+$", new_name)
                            if new_name_regex == None:
                                print("\nOnly use characters a-z")
                            else:
                                contact_dict[user_input2].update({"Name": new_name})
                                print(contact_dict)
                                repeat = input("Return to menu? y or n: ").lower()                                 
                        elif edit_input == "email":
                            new_email = input("Insert Email: ")
                            regex_new_email = re.search(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", new_email)
                            if regex_new_email == None:
                                print("\nInvalid Response. Ex: name123@gmail.com")
                            else:
                                contact_dict[user_input2].update({"Email": new_email})
                                print(contact_dict)                                                            
                        elif edit_input == "number":
                            new_number = input("Insert Number: ")
                            regex_new_phone = re.search(r"\d{3}-\d{3}-\d{4}", new_number)
                            if regex_new_phone == None:
                                print("\nPlease only use 1-9 and use ###-###-#### format")
                            else:
                                contact_dict[user_input2].update({"Phone Number": new_number})
                                print(contact_dict)                                                            
                        elif edit_input == "category":
                                new_category = input("Friend, Family Work, etc?: ")
                                contact_dict[user_input2].update({"Category": new_category})
                                print(contact_dict)
            elif menu1 == delete_contact:
                print(contact_dict.keys())
                contact_delete = input("Which contact would you like to delete?")
                if contact_delete in contact_dict:
                    contact_dict.pop(contact_delete)
                else:
                    print("Not a valid contact")    
            elif menu1 == search_contact:
                search_input = input("Enter Number of Contact: ")
                if search_input in contact_dict:
                    print(contact_dict[search_input])
                else:
                    print("Not a valid contact")   
            elif menu1 == display_contact:
                print(contact_dict.keys())
            elif menu1 == export_contact:
                with open("contact_app.txt", "w") as file:
                    for number, info in contact_dict.items():
                        file.write(f"{number}:\n")
                        for communication_type, more_info in info.items():
                            file.write(f"-{communication_type}: {more_info}\n")
        repeat = input("Return to menu? y or n: ").lower()
        if repeat == "y":
                main()
        else:
                exit()
main()