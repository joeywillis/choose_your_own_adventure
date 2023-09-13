def start_game():
    print(" \n In the year 2120, Mikkel, a seasoned space explorer, finds himself on an abandoned space station that orbits a desolate planet.")
    print("The station is in darkness, save for the occasional flickering lights.")
    print("The silence is deafening, and a sense of dread permeates the air.")
    print("Mikkel knows he needs to find a way to escape, but the station holds many secrets...")

    choice = (input(" \n Type '1' to explore the control room or '2' to explore the Living Quarters. Type 'help' for assistance. "))

    if choice.lower() == 'help':
            display_help_menu()
            start_game()
    elif choice == "1":
        explore_control_room() # Path 1 
    elif choice == "2":
        docking_bay() # Path 2 
    else:
        invalid_choice()
        start_game()

def replay():
    replay = input("\n Do you want to replay the story and try for a different endings? Type 'y' to replay or 'n' to quit. ")

    if replay.lower() == 'y':
        start_game()
    elif replay.lower() == 'n':
        quit()
    else:
        quit()


# Error handling 
def invalid_choice():
    print("Invalid choice. Please try again")

# Help menu
def display_help_menu():
    print("Welcome to the Help Menu!")
    print("Here are some tips to help you navigate the game:")
    print("1. At each stage of the game, you will be presented with a narrative and a set of choices.")
    print("2. To make a choice, type the number corresponding to the option you want to choose and press Enter.")
    print("3. If you make an invalid choice, you will be prompted to try again.")
    print("4. Your choices will determine the outcome of the game, so choose wisely!")
    print("5. To access this help menu at any time, type 'help' and press Enter.")
    print("Good luck!")


# Story path 1

def explore_control_room():
    print("\n Mikkel decides to head to the control room first, hoping to find some clues about the station's current state.")
    print("As he navigates through the dark corridors, he comes across two doors.")
    print("One leads to the control room, while the other leads to what seems like a laboratory.")
    
    choice = int(input("\n Type '1' to go into the control room or '2' to enter the laboratory. "))

    if choice == 1:
        enter_control_room()
    elif choice == 2:
        enter_lab()
    else:
        invalid_choice()
        explore_control_room()

# Path 1.1 

def enter_control_room():
    print("\n Inside, Mikkel finds a functioning terminal.")
    print("It reveals that the station was abandoned due to a catastrophic event, but there might be a functioning escape pod in the docking bay.")
    print("Mikkel decides to head there.")

    choice = int(input("\n Type '1' to attempt to launch the pod or '2' to search for manuals. "))

    if choice == 1:
        attempt_pod()
    elif choice == 2:
        search_manuals()
    else:
        invalid_choice()
        enter_control_room()

def attempt_pod():
    print(" \n Mikkel reaches the docking bay and finds a lone escape pod.")
    print("It's old and covered in dust, but it seems functional.")
    print("He must decide whether to attempt to launch it immediately or search for manuals to ensure a safe launch.")

    ending_04()

def search_manuals():
    print("\n Mikkel decides to search for manuals first.")
    print("In the process, he discovers a hidden compartment with valuable resources and information about the station's history.")
    print("This knowledge gives him an edge in his escape attempt.")

    ending_01()

# Path 1.2 

def enter_lab():
    print("\n Mikkel finds remnants of strange experiments.")
    print("He also finds a logbook that hints at the existence of a hidden safe room within the station.")
    print("Curious, Mikkel decides to find this safe room.")

    choice = int(input("\n Type '1' to find the safe room or '2' to continue exploring. "))

    if choice == 1:
        safe_room()
    elif choice == 2:
        explore()
    else:
        invalid_choice()
        enter_lab()

def safe_room():
    print("\n Mikkel manages to locate the safe room, which is a haven stocked with supplies and a distress beacon.")
    print("He can choose to settle here and send a distress signal or continue exploring the station.")

    ending_02()

def explore():
    print("\n Mikkel decides to continue exploring the station.")
    print("He stumbles upon a garden with plants that have adapted to the station's environment.")
    print("Here, he meets a lone scientist who has been maintaining the garden. Together, they formulate a plan to revitalize the station.")

    ending_01()



# Path 2

def docking_bay():
    print("\n Believing that time is of the essence, Mikkel decides to head straight to the docking bay, bypassing the control room and laboratory.")

    choice = int(input("\n Type '1' to look for a functional escape pod or type '2' to search for supplies "))

    if choice == 1:
        escape_pod()
    elif choice == 2:
        search_supplies()
    else:
        invalid_choice()
        docking_bay()

def escape_pod():
    print("\n Mikkel finds a working escape pod.")
    print("However, it has room for only one person, and the launch sequence is complicated.")
    print("Mikkel has to decide whether to launch immediately or try to find more information to ensure a safe escape.")

    choice = int(input("\n Type '1' to launch immediately or type '2' to find more information. "))

    if choice == 1:
        launch_immediately()
    elif choice == 2:
        find_info()
    else:
        invalid_choice()
        escape_pod()

def search_supplies():
    print("\n Before attempting to escape, Mikkel decides to search for supplies that might help him survive on the desolate planet below, if necessary.")
    print("In his search, he stumbles upon a group of survivors who have been hiding in the station.")

    choice = int(input("\n Type '1' to join survivors or type '2' to venture out alone. "))

    if choice == 1:
        join_survivors()
    elif choice == 2:
        venture_alone()
    else:
        invalid_choice()
        search_supplies()

def launch_immediately():
    print("\n Mikkel decides to take a chance and launches the pod.")
    print("He successfully escapes the station but finds himself drifting in space, with the desolate planet as his only company.")

    ending_03()

def find_info():
    print("\n Mikkel decides to find more information first.")
    print("In his search, he discovers a control room with a map showing a network of safe havens on the planet below.")
    print("This gives him hope for a new beginning.")

    ending_03()

def join_survivors():
    print("\n Mikkel joins the group of survivors.")
    print("Together, they work to repair the station and make it habitable again, forming a small but resilient community.")

    ending_01()

def venture_alone():
    print("\n Mikkel decides to venture alone, using the supplies he found to survive on the desolate planet.")
    print("Over time, he adapts to the harsh environment and starts a new life, with the hope of one day restoring the planet to its former glory.")

    ending_03()


# Endings

def ending_01():
    print("\n  Mikkel successfully revitalizes the station with the help of the scientist and the survivors, turning it into a flourishing oasis in space.")
    replay()

def ending_02():
    print("\n Mikkel sends a distress signal from the safe room, leading to a rescue mission that brings him back to Earth, where he shares the tales of the abandoned station.")
    replay() 

def ending_03():
    print("\n Mikkel starts a new life on the desolate planet, using his knowledge and resources to create a haven where life can thrive once again.")
    replay()

def ending_04():
    print("\n Mikkel's attempt to escape fails tragically, leaving him lost in the vastness of space, a silent witness to the mysteries of the universe.")
    replay()

    
start_game()