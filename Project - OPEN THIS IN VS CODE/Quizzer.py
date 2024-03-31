"""
   ___        _                  
  / _ \ _   _(_)___________ _ __ 
 | | | | | | | |_  /_  / _ \ '__|
 | |_| | |_| | |/ / / /  __/ |   
  \__\_\\__,_|_/___/___\___|_|   
                                 
11 Software Engineering 2024. 
Title art: https://www.patorjk.com/software/taag 
"""

import time
import ast # Gabrielson, 2009 - https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
import os
import random
from datetime import datetime

g_Prompt = '>> '
g_Alpha = ['a', 'b', 'c', 'd', 'e', 'f']
g_Separator = '------------------'

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

    CUSTOMITALIC = '\033[3m'     # Escape sequence from: https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_.28Select_Graphic_Rendition.29_parameters:~:text=3-,Italic,-Not%20widely%20supported
    CUSTOMGRAY = '\033[90m'      # Escape sequence from: https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_.28Select_Graphic_Rendition.29_parameters:~:text=229%2C%E2%80%AF229%2C%E2%80%AF229-,90,-100 
    
def printMenu(p_Info, p_Error): #Main print menu. Everything printed comes from here.
    
    os.system('cls') # Kumaran, 2011 https://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python - Clears the screen using os module for WINDOWS computers.

    # Errors - If an error needs to be shown, it's displayed before everything else.
    if p_Error == 1: # Invalid input
        print(f"{bcolours.FAIL}That's not a possible option.{bcolours.ENDC}\n")

    if p_Error == 2.1: # Input too large
        print(f"{bcolours.FAIL}That's too many questions.{bcolours.ENDC}\n")

    if p_Error == 2.2: # Input too small
        print(f"{bcolours.FAIL}That's not enough questions.{bcolours.ENDC}\n")

    if p_Error == 3.1: # Input over 240 minutes
        print(f"{bcolours.FAIL}Time limit must not exceed 240 minutes{bcolours.ENDC}\n")

    if p_Error == 3.2: # Input too small
        print(f"{bcolours.FAIL}That's not enough time.{bcolours.ENDC}\n")

    if p_Info['Menu'] == 'DirectoryErr_Results': # Shows error when the user hasn't ran the project correctly. 
        print(f"{bcolours.FAIL}{bcolours.BOLD}Quizzer couldn't access the 'Results' or 'Subjects' folder/s!{bcolours.ENDC}\n")
        print(f"Did you follow the download instructions correctly?")
        print(f"""
   1. Download the project from {bcolours.UNDERLINE}https://github.com/Yaveen123/Quizzer/archive/refs/heads/main.zip{bcolours.ENDC} 
   2. Extract the entire folder.
   3. Open VS-Code.
   4. In VS-Code, hold CTRL and hit K+O
   5. Select the "Project" folder. Don't open "Quizzer-main" or any previous folders!
   6. The project should now be opened in VS-Code.
   7. Run 'Quizzer.py' in VS-Code.
""")
        print(f"{bcolours.CUSTOMGRAY}For more information, head to the GitHub Repo at {bcolours.UNDERLINE}https://github.com/Yaveen123/Quizzer{bcolours.ENDC}")
        print(f"{bcolours.CUSTOMGRAY}To try again, please restart Quizzer.{bcolours.ENDC}")

    # Home page and results menus.
    if p_Info['Menu'] == 'Home':                                                                                                  # Home page.
        print(f"{bcolours.CUSTOMGRAY}Hi! Welcome to Quizzer.{bcolours.ENDC}\n") 
        print(f"[1] Take test \n[2] View past result\n")
        print("Select an option by entering a number from above.")

    if p_Info['Menu'] == 'Results_Main': # Results page.                            Takes 'Results' 
        print(f"{bcolours.CUSTOMGRAY}Home > Past results{bcolours.ENDC}\n")

        if len(p_Info['Results']) > 0:
            for p_I in range(len(p_Info['Results'])):                                                                               # Parses the past results and prints each item.   
                print(f"[{p_I + 1}] {p_Info['Results'][p_I][:-3]}")
            print("\nEnter a past test number to view the result.")
        else:
            print(f"{bcolours.CUSTOMITALIC}There's nothing to show here.\n{bcolours.ENDC}")


        print("Enter [e] to go back.")
    
    if p_Info["Menu"] == 'Results_ViewResult': # view a specific result.            Takes: 'Path'
        try: # Tries to open the file. If the program CAN open the file but the information inside it isn't readable, it still raises an error. 
            p_OpenFile = open(getWorkingDirectory() + '/' + p_Info['Path'], 'r')                                                                  # Using specified path, open file.
            p_OpenLog = []
            
            for p_Temp in p_OpenFile:                                                                                                   # Convert file into a list.
                p_OpenLog.append(ast.literal_eval(p_Temp.strip()))                                                                      # Gabrielson, 2009 - The function takes a representation of data and evaluates it into the data type. Link at top of code.
                                                                                                                                        # Here, this means it takes a string representation of a dictionary and converts it into an actual dictionary.

            p_OpenFile.close()

            print(f"{bcolours.CUSTOMGRAY}Home > Past results > {p_OpenLog[0]['Subject']} on {p_OpenLog[0]['Date']}{bcolours.ENDC}") 

            p_K = 0
            for p_I in range(len(p_OpenLog)-1): 
                p_I = p_I + 1
                p_Row = p_OpenLog[p_I] 
                # Print the question.
                if p_Row['SelectedAnswer'] == p_Row['CorrectAnswer']: #If the question is correct, add ✅ else ❌ 
                    p_K += 1
                    print(f"\n{p_I}. ✅ {p_Row['Question']}")
                else:
                    print(f"\n{p_I}. ❌ {p_Row['Question']}") 
                # Print the possible answers that the user could've selected from.
                if p_Row['SelectedAnswer'] != None:
                    if p_Row['SelectedAnswer'] == p_Row['CorrectAnswer']:                                                                    # If the user selected from the correct answer...
                        for p_J in range(len(p_Row['Answers'])):
                            if p_J == p_Row['SelectedAnswer']: 
                                print(f"{bcolours.OKGREEN}   [{g_Alpha[p_J]}] {p_Row['Answers'][p_J]}{bcolours.ENDC}")                       # Print green if correct.
                            else:
                                print(f"   [{g_Alpha[p_J]}] {p_Row['Answers'][p_J]}") 

                        print(f"\n{bcolours.OKGREEN}   Selected: {p_Row['Answers'][p_Row['SelectedAnswer']]}{bcolours.ENDC}")
                        print(f"   Correct: {p_Row['Answers'][p_Row['CorrectAnswer']]}")
                    
                    else:                                                                                                                    # If the user selected the incorrect answer...
                        for p_J in range(len(p_Row['Answers'])):                                                                             # Print all the answers, except this time theres an incorrect answer.
                            if p_J == p_Row['SelectedAnswer']:
                                print(f'{bcolours.FAIL}   [{g_Alpha[p_J]}] {p_Row['Answers'][p_J]}{bcolours.ENDC}') # Print red if incorrect.
                            else:
                                if p_J == p_Row['CorrectAnswer']:
                                    print(f'{bcolours.OKGREEN}   [{g_Alpha[p_J]}] {p_Row['Answers'][p_J]}{bcolours.ENDC}')                   # Print green if correct answer (but user didn't choose it)
                                else:
                                    print(f'   [{g_Alpha[p_J]}] {p_Row['Answers'][p_J]}')

                        print(f'\n{bcolours.FAIL}   Selected: {p_Row['Answers'][p_Row['SelectedAnswer']]}{bcolours.ENDC}')                   # Shows answer user selected (incorrect)
                        print(f'   Correct: {p_Row['Answers'][p_Row['CorrectAnswer']]}')                                                     # Shows the correct answer. 
                else:
                    for p_J in range(len(p_Row['Answers'])):                                                                             # Print all the answers, except this time theres an incorrect answer.
                        if p_J == p_Row['CorrectAnswer']:
                            print(f'{bcolours.OKGREEN}   [{g_Alpha[p_J]}] {p_Row['Answers'][p_J]}{bcolours.ENDC}')                   # Print green if correct answer (but user didn't choose it)
                        else:
                            print(f'   [{g_Alpha[p_J]}] {p_Row['Answers'][p_J]}')

                    print(f'\n{bcolours.FAIL}   No answer selected.{bcolours.ENDC}')                   # Shows answer user selected (incorrect)
                    print(f'   Correct: {p_Row['Answers'][p_Row['CorrectAnswer']]}')  

            print(f"\n{bcolours.CUSTOMGRAY}{g_Separator}")
            print(f"Test on {p_OpenLog[0]['Subject']}:")                                                                                 # Shows subject.

            for p_I in range(len(p_OpenLog[0]['Topics'])):
                print(f'- {p_OpenLog[0]['Topics'][p_I]}')                                                                                # Shows topics.
            
            print(f'{g_Separator}{bcolours.ENDC}')

            print(f'You Scored:   {p_K}/{p_OpenLog[0]['AmtQuestions']} ({str((int(p_K)/int(p_OpenLog[0]['AmtQuestions'])*100))[:4]}%).') # Shows score.
            print(f'Time Taken:   {p_OpenLog[0]['TimeTaken']}m{bcolours.CUSTOMGRAY} out of {p_OpenLog[0]['TimeAllocated']}m.{bcolours.ENDC}') # Shows time taken.

            print(f'{bcolours.CUSTOMGRAY}{g_Separator}{bcolours.ENDC}\n')

            print('Enter [e] to go back.')
            print('Enter [d] to delete test.')
        except:                                                                                                                          # The file either doesn't exist anymore, or the information in the file is damaged. I still offer the option to delete the file. If quizzer can't, an error is shown.
            os.system('cls')
            print(f"{bcolours.CUSTOMGRAY}Home > Past results > {bcolours.FAIL}Error{bcolours.ENDC}\n")
            print(f"Quizzer couldn't read that file.")
            print(f"{bcolours.CUSTOMGRAY}Either the file no longer exists, or the information in the file is damaged.{bcolours.ENDC}\n")
            print(f"Enter [e] to go back.")
            print(f"Enter [d] delete the file.")

    if p_Info['Menu'] == 'Results_DeleteResult': #Delete result.                    Takes: 'Path'
        try:                                                                                                                             # Tries to open the file.
            p_OpenFile = open(getWorkingDirectory() + '/' + p_Info['Path'], 'r')
            p_OpenLog = []
            
            for p_Temp in p_OpenFile:
                p_OpenLog.append(ast.literal_eval(p_Temp.strip()))                                                                       # Gabrielson, 2009 - The function takes a representation of data and evaluates it into the data type. Link at top of code.

            p_OpenFile.close() 
            print(f"{bcolours.CUSTOMGRAY}Home > Past results > {p_OpenLog[0]['Subject']} on {p_OpenLog[0]['Date']} > Deletion{bcolours.ENDC}\n") 
            print('Are you sure you want to delete this?\n')
            print('Enter [e] to go back')
            print(f'Enter {bcolours.FAIL}[d]{bcolours.ENDC} to delete this test.')
        except: # Quizzer can still attempt to delete the file, so I allow that option. If the program cannot remove the file, it shows an error message.
            os.system('cls')
            print(f"{bcolours.CUSTOMGRAY}Home > Past results > Attempt deletion > {bcolours.FAIL}Error{bcolours.ENDC}\n")
            print(f"Quizzer can't read that file. \nWe don't recommend deleting it.\n")
            print(f"{bcolours.CUSTOMGRAY}{bcolours.CUSTOMITALIC}If quizzer isn't able to delete the file, we'll just go back to the past results menu.{bcolours.ENDC}")
            print(f"Enter [e] to go back.")
            print(f"{bcolours.FAIL}Enter [d] to delete file.{bcolours.ENDC}")


    # Test setup 
    if p_Info['Menu'] == 'TestSetup_Main': # Test Selector page.                    Takes: 'Subjects'
        print(f'{bcolours.CUSTOMGRAY}Home > Take a test{bcolours.ENDC}\n')
        print(f'We found {len(p_Info['Subjects'])} subjects.\n')

        for p_I in range(len(p_Info['Subjects'])):                                                                                    # Prints out the list of subjects.
            print(f'  [{p_I +1}] {p_Info['Subjects'][p_I]}')                                                                          # A numeric value is given to each subject to select from. 

        print('\nSelect a subject by entering the corresponding number.') 
        print(f'{bcolours.CUSTOMGRAY}Enter [e] to go back.{bcolours.ENDC}')
    
    if p_Info['Menu'] == 'TestSetup_Topics': # Topics selector page.                Takes: 'Subject', 'Topics', 'ChosenTopics'
        if len(p_Info['Topics']) > 0:
            print(f'{bcolours.CUSTOMGRAY}Home > Take a test > {p_Info['Subject']}{bcolours.ENDC}') 
            print(f'{bcolours.CUSTOMGRAY}Please note that these question sets are AI Generated{bcolours.ENDC}\n')                         # Notifies user that the question sets are primarily AI. 
            print(f"We found {len(p_Info['Topics'])} question sets inside {p_Info['Subject']}")                                         # Shows amt of question sets inside the folder.

            for p_I in range(len(p_Info['Topics'])):                                                                                      # Print each avaliable question set (called 'topic')
                if p_Info['Topics'][p_I] in p_Info['ChosenTopics']:
                    print(f'   [{p_I+1}]  ✅  {p_Info['Topics'][p_I][:-4]}')                                                              # If the user has selected it, print with ✅
                else:
                    print(f'   [{p_I+1}]  ⏺   {p_Info['Topics'][p_I][:-4]}')                                                             # Else print with ⏺
            print(f'\nEnter the corresponding number to add/remove a topic.')
            if len(p_Info['ChosenTopics']) < 1:
                print(f"{bcolours.BOLD}Select at least 1 question set to continue.{bcolours.ENDC}")
            else:
                print("Enter [s] when you're done.")
            print(f'{bcolours.CUSTOMGRAY}Enter [e] to go back.{bcolours.ENDC}')
        else:
            print(f"{bcolours.CUSTOMGRAY}Home > Take a test > {p_Info['Subject']}{bcolours.ENDC}\n\nWe couldn't find any question sets inside {p_Info['Subject']}.\n") 
            print(f'{bcolours.CUSTOMGRAY}Enter [e] to go back.{bcolours.ENDC}')

    if p_Info['Menu'] == 'TestSetup_Questions': # Choose amount of questions.       Takes: 'MaxQuestions'
        print(f'{bcolours.CUSTOMGRAY}Home > Take a test > {p_Info['Subject']} > Questions {bcolours.ENDC}\n')
        if p_Info['CorruptQuestions'] > 0:
            print(f"{bcolours.WARNING}{bcolours.CUSTOMITALIC}{p_Info['CorruptQuestions']} question/s could not be read.\n{bcolours.ENDC}")
        if p_Info['CorruptSets'] > 0:
            print(f"{bcolours.WARNING}{bcolours.CUSTOMITALIC}{p_Info['CorruptSets']} set/s could not be accessed.\n{bcolours.ENDC}")
        
        print('Enter the amount of questions you want in the test.')        
        print(f'{bcolours.CUSTOMGRAY}The max. for your selection is {bcolours.ENDC}{p_Info['MaxQuestions']}.\n')                      # MaxQuestions is determined outside the printmenu.
        print(f'{bcolours.CUSTOMGRAY}Enter [e] to go back.{bcolours.ENDC}')
    
    if p_Info['Menu'] == 'TestSetup_Time': # Choose amount of time to allocate.     Takes 'RecommendedTime' 
        print(f'{bcolours.CUSTOMGRAY}Home > Take a test > {p_Info['Subject']} > Questions > Time{bcolours.ENDC}\n')
        print('Enter the amount of time you want to allocate for your test.')
        print(f'{bcolours.CUSTOMGRAY}We recommend {p_Info['RecommendedTime']} minutes based on your current selection.{bcolours.ENDC}\n') # RecommendedTime is determined outside of the printmenu.
        print(f'{bcolours.CUSTOMGRAY}Enter [e] to go back.{bcolours.ENDC}')
        print('(minutes) ', end='')                                                                                                   # Shows that only an integer (which translates to minutes) is valid.
    
    if p_Info['Menu'] == 'TestSetup_FinalCheck': # Final check before starting.     Takes 'Subject', 'Topics', 'AmtQuestions', 'AmtTime'
        print(f'{bcolours.CUSTOMGRAY}Home > Take a test > {p_Info['Subject']} > Questions > Time > FinalSetps{bcolours.ENDC}\n')
        print(f"{bcolours.CUSTOMGRAY}Just checking, you're about to start a {bcolours.ENDC}{bcolours.BOLD}{p_Info['Subject']}{bcolours.CUSTOMGRAY} test on:{bcolours.ENDC}") # Shows subject
        
        for p_I in range(len(p_Info['Topics'])):                                                                                      # Shows list of topics.
            print(f"{bcolours.BOLD}-  {p_Info['Topics'][p_I][:-4]}{bcolours.ENDC}")
        
        print(f"\nThis test will go for {bcolours.BOLD}{p_Info['AmtTime']} minutes{bcolours.ENDC} and have {bcolours.BOLD}{p_Info['AmtQuestions']} questions.{bcolours.ENDC}") # Shows how long test will go for and how many questions will be in the test.
        
        print('\nEnter [s] to start.')
        print('Enter [e] to go back')


    # Main tests section
    if p_Info['Menu'] == 'Test_Main': # The actual test.                            Takes: 'Subject', 'QuestionNo.', 'AmtQuestions', 'TimeRemaining',  'Question', 'PossibleAnswers', 'SelectedAnswer'
        print(f'{bcolours.CUSTOMGRAY}{p_Info['Subject']} test >{bcolours.ENDC} Question {bcolours.BOLD}{p_Info['QuestionNo.']}/{p_Info['AmtQuestions']}{bcolours.ENDC}')
        print(f'{bcolours.CUSTOMGRAY}{bcolours.BOLD}{p_Info['TimeRemaining']}{bcolours.ENDC}{bcolours.CUSTOMGRAY} minutes remaining.{bcolours.ENDC}') # Shows the time remaining. 

        print(f'\n{p_Info['Question']}') # Shows the question.

        for p_I in range(len(p_Info['PossibleAnswers'])):                                                                            # Shows the possible answers.
            if p_Info['SelectedAnswer'] == None: 
                print(f'   [{g_Alpha[p_I]}] {p_Info['PossibleAnswers'][p_I]}')
            elif p_Info['SelectedAnswer'] == p_I:                                                                                    # Highlights the selected answer if the user has selected anything.
                print(f'{bcolours.OKCYAN}{bcolours.BOLD}-> [{g_Alpha[p_I]}] {p_Info['PossibleAnswers'][p_I]}{bcolours.ENDC}  {bcolours.OKCYAN}{bcolours.CUSTOMITALIC}selected{bcolours.ENDC}')
            else:
                print(f'   [{g_Alpha[p_I]}] {p_Info['PossibleAnswers'][p_I]}')
        
        print('\nEnter the corresponding letter to select your answer.')

        if p_Info['AmtQuestions'] == '1':
            print(f'{bcolours.CUSTOMGRAY}Enter [k] to finish test.{bcolours.ENDC}')
        elif int(p_Info['QuestionNo.']) == 1:                                                                                               # If the user is on the first question, they cannot go back.
            print(f"{bcolours.CUSTOMGRAY}Enter [s] to go forward.")
            print(f'Enter [k] to finish test.{bcolours.ENDC}')
        elif int(p_Info['QuestionNo.']) >= int(p_Info['AmtQuestions']):                                                                        # If the user is on (or somehow further) than the last question, they cannot go forward. 
            print(f'{bcolours.CUSTOMGRAY}Enter [e] to go back.')
            print(f'Enter [k] to finish test.{bcolours.ENDC}')
        else:                                                                                                                        # Show all avaliable options if the user can go forward or back. 
            print(f"{bcolours.CUSTOMGRAY}Enter [s] to go forward.")
            print(f'Enter [e] to go back.')
            print(f'Enter [k] to finish test.{bcolours.ENDC}')

    if p_Info['Menu'] == 'Test_PreExit': # When the user wants to finish the test. Takes: 'AmtQuestions', 'UnansweredQuestions', 'Subject'
        print(f"{bcolours.CUSTOMGRAY}{p_Info['Subject']} Test > {bcolours.ENDC}All questions\n")

        for p_I in range(p_Info['AmtQuestions']):                                                                                    # Creates a menu of all the questions.
            if p_I in p_Info['UnansweredQuestions']:                                                                                 # If the question isn't answered, the question will be marked red. 
                print(f'{bcolours.FAIL}{bcolours.BOLD}[{p_I+1}]{bcolours.ENDC}', end=' ')
            else:
                print(f'[{p_I+1}]', end=' ')
        
        print('')

        for p_I in range(p_Info['AmtQuestions']):
            if p_I in p_Info['UnansweredQuestions']:                                                                                 # If the question isnt answered, a small pointer will appear under the question. 
                print(f'{bcolours.FAIL}{bcolours.BOLD} ^  {bcolours.ENDC}', end='')
            else:
                print(f'    ', end='')

        print(f"\n\nQuestions in {bcolours.FAIL}{bcolours.BOLD}red{bcolours.ENDC} aren't answered.")
        print('Enter any question number to jump to that question.')
        print(f'{bcolours.CUSTOMGRAY}Enter [k] to finish test.')
        print(f'Enter [e] to go back.{bcolours.ENDC}')

    if p_Info['Menu'] == 'Test_End': # End of test by choice.                       Takes 'Subject'
        print(f'{bcolours.CUSTOMGRAY}{p_Info['Subject']}{bcolours.ENDC} > End')
        print(f'\n{bcolours.BOLD}End of test! 🎉{bcolours.ENDC}\n')
        print('Enter [s] to view results.')
        print('Enter [e] to go back to the home screen.')
    
    if p_Info['Menu'] == 'Test_OutOfTime': # End of test due to timelimit.          Takes 'Subject' 
        print(f'{bcolours.CUSTOMGRAY}{p_Info['Subject']}{bcolours.ENDC} > End')
        print(f"\n{bcolours.BOLD}Out of time! ⌚{bcolours.ENDC}\nYour last question wasn't recorded.\n")
        print('Enter [s] to view results.')
        print('Enter [e] to go back to the home screen.')

def checkForErrors(c_Error, c_Input, c_PossibleOptions):                             # Checks if valid input.
    if c_Error == 1:                                                                 # Just a general check if the input is a specified possible option.
        if c_Input.lower() in c_PossibleOptions:
            return 0
        else:
            return 1                                                                 # To print: "That's not a possible option"
    
    if c_Error == 2:
        try:    
            c_Input = int(c_Input)                                                   # Try to convert the input into a int. 
            if c_Input > c_PossibleOptions[0]:                                       # c_PossibleOptions[0] shows the maximum possible input.
                return 2.1                                                           #To print: "That's too many questions."
            elif c_Input < 1:
                return 2.2                                                           #To print: "That's not enough questions."
            else:
                return 0
        except ValueError:                                                           # Jones, 2011 https://stackoverflow.com/questions/8075877/converting-string-to-int-using-try-except-in-python The try/except method allows me to check if the input is an integer without raising an exception. 
            if c_Input in c_PossibleOptions:                                         # Sometimes, menu options like "Enter [b] to go back" will be present as other avaliable options. This bit validates those. 
                return 0
            else:
                return 1                                                             #To print: "That's not a possible option."
    
    if c_Error == 3:
        try:
            c_Input = int(c_Input)                                                   # Try to convert the input into a int. 
            if c_Input > 240:                                                        # The maximum defined time limit is 240 minutes (i.e. 4 hours - insanely long anyway).
                return 3.1                                                           #To print: "Time limit must not exceed 240 minutes"
            elif c_Input < 1: 
                return 3.2                                                           # Try doing a test in 0 minutes or less... "That's not enough time."
            else:
                return 0
        except ValueError:                                                           # Jones, 2011 https://stackoverflow.com/questions/8075877/converting-string-to-int-using-try-except-in-python The try/except method allows me to check if the input is an integer without raising an exception. 
            if c_Input in c_PossibleOptions:                                         # Sometimes, menu options like "Enter [b] to go back" will be present as other avaliable options. This bit validates those. 
                return 0
            else:
                return 1                                                             #To print: "That's not a possible option."

def obtainValidInput(o_PrintMenuInfo, o_ErrorToCheck, o_PossibleInputs): # Prints the menu and checks if the input is valid. The possible inputs MUST be in string.
    o_ErrorCode = None
    while o_ErrorCode != 0:
        printMenu(o_PrintMenuInfo, o_ErrorCode)
        o_Input = input(g_Prompt)
        o_ErrorCode = checkForErrors(o_ErrorToCheck, o_Input, o_PossibleInputs)      # If the input is invalid, then the checkForErrors module will return a value that ISNT 0, and the lopp continues until the input is valid. 
    return o_Input.lower()

def getWorkingDirectory():                                                                                                                               # Very important - if the user hasn't ran the project correctly or tampered with the files, this appears.
    try:                                                                                                                                                 # This makes sure that the program can access the required folders.
        os.listdir(f'{os.getcwd()}/Results')
        os.listdir(f'{os.getcwd()}/Subjects')
        return os.getcwd()
    except: 
        obtainValidInput({'Menu':'DirectoryErr_Results'}, None, [0])                                                                                     # Displays the error message and doesn't allow the user to leave unless they've killed the terminal (so its a proper reset). 

def checkValidQuestion(v_Dict):
    try:
        if type(v_Dict['Question']) == str and type(v_Dict['Answers']) == list and v_Dict['SelectedAnswer'] == None and type(v_Dict['CorrectAnswer']) == int:
            if len(v_Dict['Answers']) == 4 and v_Dict['CorrectAnswer'] < 4:
                return 0
            else:
                return 1
        else:
            return 1
    except:
        return 1


getWorkingDirectory()
g_Menu = [0,0,0,0,0,0,0] 
while True:

    if g_Menu[0] == 2:
        pass
    else:
        g_Menu = [0,0,0,0,0,0,0]                                                                                                                   # Creates items to form a menu. This is done because you cannot assign to a place in a list that hasn't been created yet.
        g_Menu[0] = int(obtainValidInput({'Menu':'Home'}, 1, ['1', '2']))                                                                                    # Home screen.
    

    if g_Menu[0] == 2: # View results screen.
        while g_Menu[0] == 2:
            g_Logs = os.listdir(f'{getWorkingDirectory()}/Results')                                                                                                # Get all the past results.
            g_AllPossibleOptions = ['e']
            for g_I in range(len(g_Logs)): 
                g_AllPossibleOptions.append(str(g_I+1))                                                                                                  # Create all the possible options for the user to input. 

            g_PastResult = obtainValidInput({'Menu':'Results_Main', 'Results':g_Logs}, 1, g_AllPossibleOptions)                                          # Shows the results the user can view.
            if g_PastResult == 'e':                                                                                                                      # If user wants to go back.
                g_Menu[0] = ''
            else:
                g_Menu[1] = 1
                while g_Menu[1] != 0:
                    g_Menu[1] = obtainValidInput({'Menu':'Results_ViewResult', 'Path':f'/results/{g_Logs[int(g_PastResult)-1]}'}, 1, ['e','d'])          # Open a specific result.
                    if g_Menu[1] == 'e':                                                                                                                 # If user wants to go back.
                        g_Menu[1] = 0
                    else:
                        g_Menu[2] = obtainValidInput({'Menu':'Results_DeleteResult', 'Path':f'/results/{g_Logs[int(g_PastResult)-1]}'}, 1, ['e','d'])    # Confirm deletion of a specific result.

                        if g_Menu[2] == 'd':                                                                                                             # User definitely wants to delete this result.
                            try:                                                                                                                         # If the program cannot remove the file, it shows an error message.
                                os.remove(f'{getWorkingDirectory()}/results/{g_Logs[int(g_PastResult)-1]}')                                                        # Deletes the specified result from the results folder. 
                            except:
                                os.system('cls')
                                input("Quizzer wasn't able to delete the file.\n\n[Enter] to go back.")                                                  # Error message when program isn't able to delete the file.
                            g_Menu[2] = 0                                                                                                                # Goes back to the view results main page.
                            g_Menu[1] = 0
                        else:
                            g_Menu[2] = 0                                                                                                                # Goes back to just viewing the results. 
            
    else: 
        while g_Menu[0] != 0 and g_Menu[0] != 2:
            g_AllSubjects = os.listdir(f'{getWorkingDirectory()}/Subjects')
            g_AllPossibleOptions = ['e']
            
            for g_I in range(len(g_AllSubjects)):
                g_AllPossibleOptions.append(str(g_I+1))
            
            g_ChosenSubject = obtainValidInput({'Menu':'TestSetup_Main', 'Subjects':g_AllSubjects}, 1, g_AllPossibleOptions)
            
            if g_ChosenSubject == 'e':
                g_Menu[0] = 0
            else:
                g_Menu[1] = 1
                g_ChosenTopics = []
                while g_Menu[1] != 0:
                    g_Topics = os.listdir(f'{getWorkingDirectory()}/Subjects/{g_AllSubjects[int(g_ChosenSubject)-1]}')

                    g_AllPossibleOptions = ['e','s']

                    for g_I in range(len(g_Topics)):
                        g_AllPossibleOptions.append(str(g_I+1))
                    
                    if len(g_AllPossibleOptions) > 2:
                        while True:

                            g_Input = obtainValidInput({'Menu':'TestSetup_Topics', 'Subject':g_AllSubjects[int(g_ChosenSubject)-1], 'ChosenTopics':g_ChosenTopics, 'Topics':g_Topics}, 1, g_AllPossibleOptions)
                            if g_Input == 's':
                                if len(g_ChosenTopics) > 0:
                                    g_Menu[2] = 1
                                    break
                            elif g_Input == 'e':
                                g_Menu[1] = 0
                                break
                            else:
                                if g_Topics[int(g_Input)-1] in g_ChosenTopics:
                                    g_ChosenTopics.remove(g_Topics[int(g_Input)-1])
                                else:
                                    g_ChosenTopics.append(g_Topics[int(g_Input)-1])
                    
                    else:
                        g_Input = obtainValidInput({'Menu':'TestSetup_Topics', 'Subject':g_AllSubjects[int(g_ChosenSubject)-1], 'ChosenTopics':g_ChosenTopics, 'Topics':g_Topics}, 1, ['e'])
                        g_Menu[1] = 0
                    
                    
                    while g_Menu[2] == 1:
                        print(g_ChosenTopics)
                        g_MaxQuestions = 0
                        g_UnavaliableQuestions = 0
                        g_UnavaliableQuestionSets = 0

                        for g_I in range(len(g_ChosenTopics)):
                            try:
                                g_ReadFile = open(f"{getWorkingDirectory()}/Subjects/{g_AllSubjects[int(g_ChosenSubject)-1]}/{g_ChosenTopics[g_I]}") 
                                
                                for g_J in g_ReadFile.readlines()[1:]: # W3Schools, n.d. https://www.w3schools.com/python/ref_file_readlines.asp returns a list of the file per row. 
                                    if checkValidQuestion(ast.literal_eval(g_J)) == 1:
                                        g_UnavaliableQuestions += 1
                                    else:
                                        g_MaxQuestions += 1
                                g_ReadFile.close()
                            except:
                                g_UnavaliableQuestionSets += 1
                        
                        g_Input = obtainValidInput({'Menu':'TestSetup_Questions', 'MaxQuestions':g_MaxQuestions, 'Subject':g_AllSubjects[int(g_ChosenSubject)-1], 'CorruptSets':g_UnavaliableQuestionSets, 'CorruptQuestions':g_UnavaliableQuestions}, 2, [g_MaxQuestions, 'e'])

                        if g_Input == 'e':
                            g_Menu[2] = 0
                        else:
                            g_Menu[3] = 1
                            g_ChosenAmtQuestions = g_Input

                            while g_Menu[3] != 0:
                                g_RecommendedTime = str(round(int(g_ChosenAmtQuestions)*0.75)) # round() from W3 Schools (n.d.) rounds a float. https://www.w3schools.com/python/ref_func_round.asp 
    	                        
                                g_Input = obtainValidInput({'Menu':'TestSetup_Time', 'RecommendedTime':g_RecommendedTime, 'Subject':g_AllSubjects[int(g_ChosenSubject)-1]}, 3, ['e'])

                                if g_Input == 'e':
                                    g_Menu[3] = 0
                                else:
                                    g_Menu[4] = 1
                                    g_ChosenAmtTime = g_Input

                                    while g_Menu[4] == 1:
                                        g_Input = obtainValidInput({'Menu':'TestSetup_FinalCheck', 'Subject':g_AllSubjects[int(g_ChosenSubject)-1], 'Topics':g_ChosenTopics, 'AmtTime':g_ChosenAmtTime, 'AmtQuestions':g_ChosenAmtQuestions}, 1, ['s', 'e'])

                                        if g_Input == 'e':
                                            g_Menu[4] = 0 
                                        else:
                                            g_test_Questions = []
                                            g_test_QuestionNum = 1
                                            g_Temp = '' 
                                            g_RecursionMax = 0
                                            g_I = 0
                                            g_test_LogName = '' 

                                            while g_I < int(g_ChosenAmtQuestions):
                                                
                                                if g_RecursionMax > 100:
                                                    break

                                                try:
                                                    g_ReadFile = open(f'{getWorkingDirectory()}/Subjects/{g_AllSubjects[int(g_ChosenSubject)-1]}/{random.choice(g_ChosenTopics)}')
                                                    g_Temp = random.choice(g_ReadFile.readlines()[1:])
                                                    if g_Temp not in g_test_Questions and checkValidQuestion(ast.literal_eval(g_Temp)) == 0:
                                                        g_test_Questions.append(g_Temp)
                                                        g_I += 1
                                                    else:
                                                        g_RecursionMax += 1
                                                except:
                                                    break

                                            if len(g_test_Questions) == 0:
                                                os.system('cls')
                                                print(f"{bcolours.CUSTOMITALIC}Failed to generate a question set.{bcolours.ENDC}\n")
                                                print(f"We couldn't retrieve any of the nessesary questions to start the test.")
                                                print(f"{bcolours.CUSTOMGRAY}This may be due to corrupt question data.\n{bcolours.ENDC}")
                                                input(f"[Enter] to go back\n>>")
                                                g_Menu[4] = 0
                                                break
                                            
                                            if g_RecursionMax >= 100:
                                                os.system('cls')
                                                print(f"{bcolours.CUSTOMITALIC}We couldn't retrieve some questions.{bcolours.ENDC}\n")
                                                print(f"You specified {g_ChosenAmtQuestions} questions, however we could only generate a question set with {len(g_test_Questions)} questions.")
                                                print(f"{bcolours.CUSTOMGRAY}This may be due to corrupt question data.\n{bcolours.ENDC}")
                                                input(f"[Enter] to continue\n>>")

                                            g_test_LogName = f'{getWorkingDirectory()}/Results/{g_AllSubjects[int(g_ChosenSubject)-1]} on {str(datetime.today().strftime('%Y-%m-%d'))} ({str(datetime.today().strftime('%H-%M-%S'))}) {g_ChosenAmtTime} minutes {g_ChosenAmtQuestions} questions.txt'
                                            g_test_Log = open(g_test_LogName, 'a')           # 'Diegueus9', 2015, displays date in YYYY-MM-DD form. https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python   
                                            
                                            g_test_Log.write('{' + f"'Subject':'{g_AllSubjects[int(g_ChosenSubject)-1]}','Topics':{g_ChosenTopics}, 'TimeTaken':0, 'TimeAllocated':{g_ChosenAmtTime}, 'Date':'{datetime.today().strftime('%Y-%m-%d %H-%M-%S')}', 'Score':0, 'AmtQuestions':{g_ChosenAmtQuestions}, 'Type':'Test'" + '}' + f'\n')
                                            
                                            for g_I in g_test_Questions:
                                                g_test_Log.write(f"{g_I.strip()}\n")     
                                            
                                            g_test_Log = open(g_test_LogName, 'r')
                                            g_test_Questions = []
                                            for g_I in g_test_Log:
                                                g_test_Questions.append(ast.literal_eval(g_I))                                   
                                            g_test_Log.close()

                                            g_test_StartTime = int(time.time())
                                            g_test_EndTime = g_test_StartTime + (int(g_ChosenAmtTime)*60)
                                            g_test_CurrentTime = round((g_test_EndTime - g_test_StartTime)/60)

                                            while True:
                                                g_Input = obtainValidInput({'Menu':'Test_Main', 'Subject':g_AllSubjects[int(g_ChosenSubject)-1], 'QuestionNo.':g_test_QuestionNum, 'AmtQuestions':g_ChosenAmtQuestions, 'TimeRemaining':round(g_test_CurrentTime), 'Question':g_test_Questions[g_test_QuestionNum]['Question'], 'PossibleAnswers':g_test_Questions[g_test_QuestionNum]['Answers'], 'SelectedAnswer':g_test_Questions[g_test_QuestionNum]['SelectedAnswer']}, 1, ['a','b','c','d','e','s','k'])
                                                g_test_CurrentTime = (g_test_EndTime - int(time.time()))/60

                                                if g_test_CurrentTime < 0:
                                                    break
                                                if g_Input == 'e':
                                                    if g_test_QuestionNum != 1:
                                                        g_test_QuestionNum = g_test_QuestionNum - 1 
                                                elif g_Input == 's':
                                                    if g_test_QuestionNum != int(g_ChosenAmtQuestions):
                                                        g_test_QuestionNum += 1
                                                elif g_Input == 'k':
                                                    break
                                                else:
                                                    g_test_Questions[g_test_QuestionNum]['SelectedAnswer'] = g_Alpha.index(g_Input) # Coventry, 2008 Finds index of given input https://stackoverflow.com/questions/176918/how-to-find-the-index-for-a-given-item-in-a-list

                                            if g_test_CurrentTime < 0:
                                                g_Input = obtainValidInput({'Menu':'Test_OutOfTime', 'Subject':g_AllSubjects[int(g_ChosenSubject)-1]}, 1, ['s', 'e'])
                                            else: 
                                                g_Input = obtainValidInput({'Menu':'Test_End', 'Subject':g_AllSubjects[int(g_ChosenSubject)-1]}, 1, ['s', 'e'])
                                            
                                            g_test_Questions[0]['TimeTaken'] = str(round(int(time.time()) - g_test_StartTime))

                                            try:
                                                open(g_test_LogName, 'w').close() # Parker, 2022 Clears everything in file. https://stackoverflow.com/questions/2769061/how-to-erase-the-file-contents-of-text-file-in-python
                                                
                                                g_ReadFile = open(g_test_LogName, 'a')
                                                for g_I in g_test_Questions:
                                                    g_ReadFile.write(f'{str(g_I)}\n')
                                                
                                                g_ReadFile.close()
                                            except:
                                                print(f"{bcolours.WARNING}Quizzer couldn't save this test.\n{bcolours.CUSTOMGRAY}We couldn't access the created log file.\n")
                                                input('>>')

                                            if g_Input == 's':
                                                g_Menu = [2,0,0,0,0,0,0] 
                                            else:
                                                g_Menu = [0,0,0,0,0,0,0] 