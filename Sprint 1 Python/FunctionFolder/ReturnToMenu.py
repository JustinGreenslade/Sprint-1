'''
Name: Ashton Dennis
Desc: Function added to team members' programs to maintain the viewing experience established in the main menu
Date: Oct 22, 2024
'''

def ReturnToMenu():
    from os import system, name

    system("cls" if name == "nt" else "clear")
    print("Exiting to main menu...")
    return
