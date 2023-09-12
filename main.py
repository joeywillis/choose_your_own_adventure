def start_game():
    print("In the year 2120, Mikkel, a seasoned space explorer, finds himself on an abandoned space station that orbits a desolate planet. The station is in darkness, save for the occasional flickering lights. The silence is deafening, and a sense of dread permeates the air. Mikkel knows he needs to find a way to escape, but the station holds many secrets...")

    choice = (input("Type '1' to explore the Command Center or '2' to explore the Living Quarters. Type 'help' for assistance. "))

    if choice.lower() == 'help':
            display_help_menu()
            start_game()
    elif choice == "1":
        command_center()
    elif choice == "2":
        living_quarters()
    else:
        invalid_choice()
        start_game()

def invalid_choice():
    print("Invalid choice. Please try again")

def display_help_menu():
    print("Welcome to the Help Menu!")
    print("Here are some tips to help you navigate the game:")
    print("1. At each stage of the game, you will be presented with a narrative and a set of choices.")
    print("2. To make a choice, type the number corresponding to the option you want to choose and press Enter.")
    print("3. If you make an invalid choice, you will be prompted to try again.")
    print("4. Your choices will determine the outcome of the game, so choose wisely!")
    print("5. To access this help menu at any time, type 'help' and press Enter.")
    print("Good luck!")

def command_center():
    print("Mikkel steps into the command center, a room filled with high-tech equipment and large windows that offer a view of the desolate planet below. The place seems to have been abandoned in a hurry, with signs of a struggle evident. Mikkel notices a blinking light on the main console.")
    
    choice = int(input("Type '1' to investigate the blinking light on the console or '2' to search the room for any other clues or exits. "))

    if choice == 1:
        distress_signal()
    elif choice == 2:
        hidden_door()
    else:
        invalid_choice()
        command_center()

def living_quarters():
    print("Mikkel enters the living quarters, where the crew once rested and relaxed. The room is in disarray, with personal belongings scattered everywhere. A strange, metallic smell hangs in the air. Mikkel spots a journal on a table, possibly belonging to a crew member.")

    choice = int(input("Type '1' to read the journal to learn more about what happened or type '2' to continue to explore the room, looking for useful items or exits. "))

    if choice == 1:
        members_journal()
    elif choice == 2:
        explore_room()
    else:
        invalid_choice()
        living_quarters()

def distress_signal():
    print("Mikkel approaches the console, the blinking light casting eerie shadows on the walls. It seems to be a distress signal, looping endlessly. As he listens, a chill runs down his spine - something is very wrong here. Suddenly, the station shudders, as if struck by an unseen force.")

    choice = int(input("Type '1' to try to communicate with the source of the distress signal or type '2' to leave the command center to investigate the cause of the shudder. "))

    if choice == 1:
        abyss_voice()
    elif choice == 2:
        shattered_corridor()
    else:
        invalid_choice()
        living_quarters()

def hidden_door():
    print("Mikkel searches the command center, finding signs of a struggle and remnants of what seems to be a failed evacuation. In the corner of the room, he discovers a hidden door slightly ajar, revealing a dark corridor beyond. A sense of foreboding fills him as he contemplates entering the unknown.")

    choice = int(input("Type '1' to enter the dark corridor to explore further or type '2' to decide against it and return to the main hallway to choose another path. "))

    if choice == 1:
        lab_horrors()
    elif choice == 2:
        main_hallway()
    else:
        invalid_choice()
        hidden_door()

def members_journal():
    print("Mikkel picks up the journal, the pages filled with the frantic scribbles of a crew member who witnessed the downfall of the station. Tales of experiments gone wrong and creatures lurking in the shadows fill the pages. The last entry is unfinished, ending with a chilling scream that seems to echo in Mikkel's mind.")

    choice = int(input("Type '1' to search for the crew member who wrote the journal or type '2' to find a weapon before venturing further into the station. "))

    if choice == 1:
        crew_search()
    elif choice == 2:
        armament()
    else:
        invalid_choice()
        members_journal()

def explore_room():
    print("Mikkel sifts through the belongings scattered across the room, finding personal items that hint at the lives of the crew members who once inhabited the station. In a locker, he finds a laser gun with a few charges left. It might come in handy, considering the dangers that seem to lurk around every corner.")

    choice = int(input("Type '1' to take the laser gun and continue exploring or type '2' to leave the living quarters to investigate other areas of the station. "))

    if choice == 1:
        print("test")
    elif choice == 2:
        print("test2")
    else:
        invalid_choice()
        explore_room()

def abyss_voice():
    print("Mikkel hesitantly reaches out to communicate with the unknown entity sending the distress signal. A voice, distorted and echoing, responds, speaking in riddles and warning of an impending doom. Mikkel feels a presence in the room, watching, waiting...")

    choice = int(input("Type '1' to ask the entity for guidance on how to escape the station or type '2' to end the communication and quickly leave the command center. "))

    if choice == 1:
        entity_guidance()
    elif choice == 2:
        hasty_retreat()
    else:
        invalid_choice()
        abyss_voice()

def shattered_corridor():
    print("Mikkel exits the command center to find the corridor outside shattered and twisted, as if reality itself has been warped. Shadows dance on the walls, and a low growl echoes through the station. Mikkel realizes he is not alone.")

    choice = int(input("Type '1' to follow the growl to confront whatever lurks in the shadows or type '2' to search for a safe place to hide and gather his thoughts. "))

    if choice == 1:
        shadowy_confrontation()
    elif choice == 2:
        respite_moment()
    else:
        invalid_choice()
        shattered_corridor()

def lab_horrors():
    print("Mikkel steps into a dark corridor that leads to a secret laboratory. The room is filled with strange, pulsating machines and vats containing grotesque creatures. It seems the crew were conducting experiments that defy the laws of nature. Mikkel feels a surge of dread as he realizes the extent of the horrors that took place here.")

    choice = int(input("Type '1' to investigate the machines to find out more about the experiments or type '2' to find a way to shut down the laboratory and prevent further horrors."))

    if choice == 1:
        secrets_unveiled()
    elif choice == 2:
        shutdown()
    else:
        invalid_choice()
        lab_horrors()

def main_hallway():
    print("Mikkel decides against venturing into the dark corridor, fearing the unknown horrors that might await him. He returns to the main hallway, a nexus that connects various parts of the station. From here, he can choose a new path, hopefully one that leads to safety.")

    choice = int(input("Type '1' to head to the station's armory to arm himself or type '2' to try to find the station's escape pods to make a quick exit. "))

    if choice == 1:
        armory()
    elif choice == 2:
        escape_pods()
    else:
        invalid_choice()
        main_hallway()

def entity_guidance():
    print("The entity's voice resonates in Mikkel's mind, offering cryptic guidance. It speaks of a hidden sanctuary within the station where Mikkel might find refuge and allies. However, the path is fraught with danger and deceit. Mikkel must decide whether to trust this enigmatic being.")

    choice = int(input("Type '1' to follow the entity's guidance and seek the sanctuary or type '2' to ignore the entity and find your own way. "))

    if choice == 1:
        sanctuary_path()
    elif choice == 2:
        own_path()
    else:
        invalid_choice()
        entity_guidance()

def hasty_retreat():
    print("Mikkel ends the communication abruptly, a sense of urgency overtaking him. The station seems to close in around him, the darkness growing ever more oppressive. He knows he needs to move quickly if he is to escape the looming threat.")

    choice = int(input("Type '1' to follow the entity's guidance and seek the sanctuary or type '2' to ignore the entity and find your own way. "))

    if choice == 1:
        sanctuary_path()
    elif choice == 2:
        own_path()
    else:
        invalid_choice()
        entity_guidance()

def shadowy_confrontation():
    print("Mikkel follows the growl, his heart pounding in his chest. As he turns a corner, he comes face to face with a shadowy creature, a twisted amalgamation of machine and flesh. It's clear that a confrontation is inevitable.")

    choice = int(input("Type '1' to follow the entity's guidance and seek the sanctuary or type '2' to ignore the entity and find your own way. "))

    if choice == 1:
        sanctuary_path()
    elif choice == 2:
        own_path()
    else:
        invalid_choice()
        entity_guidance()

def respite_moment():
    print("Mikkel finds a hidden alcove in the twisted corridor, a brief sanctuary in the midst of chaos. Here, he has a moment to gather his thoughts and plan his next move. But time is of the essence, and he knows he can't stay hidden for long.")

    choice = int(input("Type '1' to follow the entity's guidance and seek the sanctuary or type '2' to ignore the entity and find your own way. "))

    if choice == 1:
        sanctuary_path()
    elif choice == 2:
        own_path()
    else:
        invalid_choice()
        entity_guidance()

def secrets_unveiled():
    print("Mikkel approaches the machines, their pulsating rhythm creating a symphony of dread. As he delves deeper into the data, he uncovers the horrifying truth: the crew were attempting to merge humans with machines, creating abominations that defy the natural order. The experiments went horribly wrong, unleashing the nightmares that now roam the station.")

    choice = int(input("Type '1' to follow the entity's guidance and seek the sanctuary or type '2' to ignore the entity and find your own way. "))

    if choice == 1:
        sanctuary_path()
    elif choice == 2:
        own_path()
    else:
        invalid_choice()
        entity_guidance()

def shutdown():
    print("Determined to prevent further horrors, Mikkel searches for a way to shut down the laboratory. He finds a central control panel that seems to control the power flow to the machines. As he reaches to shut it down, he hears the cries of the creatures in the vats, a symphony of agony and despair.")

    choice = int(input("Type '1' to follow the entity's guidance and seek the sanctuary or type '2' to ignore the entity and find your own way. "))

    if choice == 1:
        sanctuary_path()
    elif choice == 2:
        own_path()
    else:
        invalid_choice()
        entity_guidance()

def armory():
    print("Mikkel makes his way to the armory, a room filled with advanced weaponry and protective gear. As he arms himself, he can feel the weight of the responsibility on his shoulders. The station has become a battlefield, and he must be prepared to fight for his survival.")

    choice = int(input("Type '1' to follow the entity's guidance and seek the sanctuary or type '2' to ignore the entity and find your own way. "))

    if choice == 1:
        sanctuary_path()
    elif choice == 2:
        own_path()
    else:
        invalid_choice()
        entity_guidance()

def escape_pods():
    print("Mikkel rushes to the escape pod bay, hoping to find a quick way out of the nightmare engulfing the station. The bay is in disarray, with many pods damaged or missing. However, a few intact pods offer a glimmer of hope, a chance to escape the horrors and return to tell the tale.")

    choice = int(input("Type '1' to follow the entity's guidance and seek the sanctuary or type '2' to ignore the entity and find your own way. "))

    if choice == 1:
        sanctuary_path()
    elif choice == 2:
        own_path()
    else:
        invalid_choice()
        entity_guidance()

def crew_search():
    print("Driven by a sense of duty and compassion, Mikkel decides to search for the crew member who penned the frantic journal entries. As he ventures deeper into the station, he comes across signs of struggle and remnants of chaos. In a secluded room, he finds the crew member, now transformed into a grotesque creature, a victim of the failed experiments.")

    choice = int(input("Type '1' to follow the entity's guidance and seek the sanctuary or type '2' to ignore the entity and find your own way. "))

    if choice == 1:
        sanctuary_path()
    elif choice == 2:
        own_path()
    else:
        invalid_choice()
        entity_guidance()

def armament():
    print("Understanding the dangers that lurk in the shadows, Mikkel decides to arm himself before venturing further. In a nearby storage room, he finds a cache of weapons left behind in the chaos. As he picks up a laser pistol, he feels a mix of determination and fear, ready to face the horrors that await.")

    choice = int(input("Type '1' to follow the entity's guidance and seek the sanctuary or type '2' to ignore the entity and find your own way. "))

    if choice == 1:
        sanctuary_path()
    elif choice == 2:
        own_path()
    else:
        invalid_choice()
        entity_guidance()

def sanctuary_path():
    print("Mikkel decides to trust the entity and heads towards the sanctuary it spoke of. As he ventures deeper into the station, he encounters areas untouched by the chaos, a beacon of hope amidst the darkness.")

    choice = int(input("Type '1' to explore the sanctuary further or type '2' to leave and find another way. "))

    if choice == 1:
        sanctuary_explore()
    elif choice == 2:
        own_path()
    else:
        invalid_choice()
        sanctuary_path()

def sanctuary_explore():
    print("In the sanctuary, Mikkel finds remnants of a once vibrant community. He discovers resources that might aid him in his journey, but also signs of a tragic end. The sanctuary holds secrets that might be key to understanding the station's downfall.")

    choice = int(input("Type '1' to investigate the secrets of the sanctuary or type '2' to gather resources and leave. "))

    if choice == 1:
        sanctuary_secrets()
    elif choice == 2:
        gather_resources()
    else:
        invalid_choice()
        sanctuary_explore()

def own_path():
    print("Mikkel decides to forge his own path, ignoring the entity's guidance. As he ventures forth, he finds himself facing increasing dangers, but also opportunities to uncover the truth behind the station's downfall.")

    choice = int(input("Type '1' to seek the truth at any cost or type '2' to prioritize finding a way to escape the station. "))

    if choice == 1:
        truth_path()
    elif choice == 2:
        escape_path()
    else:
        invalid_choice()
        own_path()

def sanctuary_secrets():
    print("Mikkel delves into the sanctuary's secrets, uncovering tales of betrayal and a desperate struggle for survival. The knowledge gained here might be the key to stopping the horrors that engulf the station.")

    choice = int(input("Type '1' to use the knowledge to confront the source of the chaos or type '2' to find a way to escape the station with the information. "))

    if choice == 1:
        final_confrontation()
    elif choice == 2:
        escape_with_information()
    else:
        invalid_choice()
        sanctuary_secrets()

def gather_resources():
    print("Mikkel gathers vital resources from the sanctuary, preparing himself for the challenges ahead. Armed with new tools and supplies, he feels a renewed sense of hope.")

    choice = int(input("Type '1' to venture forth to confront the horrors of the station or type '2' to find a way to escape the station with the resources. "))

    if choice == 1:
        final_confrontation()
    elif choice == 2:
        escape_with_resources()
    else:
        invalid_choice()
        gather_resources()

def truth_path():
    print("Determined to uncover the truth, Mikkel delves deeper into the station's mysteries. He discovers logs and recordings that hint at forbidden experiments and a power struggle among the crew.")

    choice = int(input("Type '1' to investigate the lab where the experiments took place or type '2' to confront the station's AI for answers. "))

    if choice == 1:
        secrets_unveiled()
    elif choice == 2:
        ai_confrontation()
    else:
        invalid_choice()
        truth_path()

def escape_path():
    print("Prioritizing his safety, Mikkel decides to find the quickest way out. However, the station's layout is confusing, and dangers lurk around every corner.")

    choice = int(input("Type '1' to head to the escape pods or type '2' to search for a communication room to send a distress signal. "))

    if choice == 1:
        escape_pods()
    elif choice == 2:
        distress_signal()
    else:
        invalid_choice()
        escape_path()

def ai_confrontation():
    print("Mikkel confronts the station's AI, demanding answers. The AI reveals that it had tried to stop the crew's experiments but was overridden. Now, it seeks Mikkel's help to restore order.")

    choice = int(input("Type '1' to help the AI shut down the experiments or type '2' to shut down the AI itself. "))

    if choice == 1:
        shutdown()
    elif choice == 2:
        ai_shutdown()
    else:
        invalid_choice()
        ai_confrontation()

def ai_shutdown():
    print("Believing the AI to be a part of the problem, Mikkel decides to shut it down. However, doing so leaves him without guidance in the treacherous station.")

    choice = int(input("Type '1' to continue searching for the truth or type '2' to find a way to escape the station. "))

    if choice == 1:
        truth_path()
    elif choice == 2:
        escape_path()
    else:
        invalid_choice()
        ai_shutdown()

def final_confrontation():
    print("Mikkel, armed with knowledge and resources, confronts the source of the chaos. A climactic battle ensues, determining the fate of the station and Mikkel himself.")

    choice = int(input("Type '1' to use the knowledge gained to negotiate a truce or type '2' to fight head-on. "))

    if choice == 1:
        negotiated_peace()
    elif choice == 2:
        battle_outcome()
    else:
        invalid_choice()
        final_confrontation()

def escape_with_information():
    print("With the information in hand, Mikkel makes his way to the escape pods. The journey is fraught with danger, but the knowledge he carries could change the fate of the galaxy.")

    choice = int(input("Type '1' to launch an escape pod or type '2' to send the information to a trusted ally before escaping. "))

    if choice == 1:
        successful_escape()
    elif choice == 2:
        send_information()
    else:
        invalid_choice()
        escape_with_information()

def escape_with_resources():
    print("Mikkel, now equipped with vital resources, seeks the quickest way out of the station. Every moment counts as the station's horrors close in on him.")

    choice = int(input("Type '1' to barricade himself and wait for rescue or type '2' to make a daring escape through the station's vents. "))

    if choice == 1:
        await_rescue()
    elif choice == 2:
        vent_escape()
    else:
        invalid_choice()
        escape_with_resources()

def negotiated_peace():
    print("Using the knowledge gained, Mikkel negotiates a truce, bringing peace to the station. The horrors are contained, and Mikkel emerges as a hero.")

def battle_outcome():
    print("A fierce battle ensues. Mikkel, using all his skills and resources, manages to defeat the horrors of the station. However, the victory comes at a cost.")

def successful_escape():
    print("Mikkel launches an escape pod, leaving the horrors of the station behind. As he drifts in space, he reflects on the events and the secrets he uncovered.")

def send_information():
    print("Mikkel sends the vital information to a trusted ally, ensuring that the station's secrets are exposed. With his mission accomplished, he makes his escape, hopeful for a brighter future.")

def await_rescue():
    print("Mikkel barricades himself in a secure room, sending out a distress signal. Days pass before a rescue team arrives, saving him from the station's nightmares.")

def vent_escape():
    print("Mikkel crawls through the station's vents, avoiding the lurking horrors. After what feels like hours, he emerges outside, breathing a sigh of relief as he escapes the station's grasp.")

# start game
start_game()