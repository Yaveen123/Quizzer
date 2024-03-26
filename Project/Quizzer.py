import time
import os

g_Prompt = '>> '

class bcolours: # 'joeld', 2008. Coloured text - https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal 
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    CUSTOMGRAY = '\033[90m'
 
def printMenu(p_Info, p_Error):
    
    os.system('cls') # Kumaran, 2011 https://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python - Clears the screen using os module for WINDOWS computers.

    if p_Error == 1:
        print(f"{bcolours.FAIL}That's not a possible option.{bcolours.ENDC}\n")

    if p_Error == 2.1:
        print(f"{bcolours.FAIL}That's too many questions.{bcolours.ENDC}\n")

    if p_Error == 2.2:
        print(f"{bcolours.FAIL}That's not enough questions.{bcolours.ENDC}\n")

    if p_Error == 3.1:
        print(f"{bcolours.FAIL}Time limit must not exceed 1000 minutes{bcolours.ENDC}\n")

    if p_Error == 3.2:
        print(f"{bcolours.FAIL}That's not enough time.{bcolours.ENDC}\n")



    if p_Info['Menu'] == 'Home':
        print(f"{bcolours.CUSTOMGRAY}Hi! Welcome to Quizzer.{bcolours.ENDC}\n") 
        print(f"[1] Take test \n[2] View past result\n")
        print("Select an option by entering a number from above.")

    if p_Info['Menu'] == 'Results_Main':
        print(f"{bcolours.CUSTOMGRAY}Home > Past results{bcolours.ENDC}\n")

        for p_I in range(len(p_Info['Results'])):
            print(f"[{p_I + 1}] {p_Info['Results'][p_I][:-3]}")
        
        print("\nEnter a past test number to view the result.")
        print("Enter [e] to go back.")



# Print the home page.
""" 
p_Info = {'Menu':'Home'}
p_Error = None
printMenu(p_Info, p_Error)
"""

# Print the results page.
"""
g_Temp = os.listdir(os.getcwd() + '/results')
printMenu({'Menu':'Results_Main', 'Results':g_Temp}, 1) 
"""





input(g_Prompt)