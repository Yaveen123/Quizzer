import time
import ast # Gabrielson, 2009 - https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
import os

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

g_Prompt = '>> '
g_Alpha = ['a', 'b', 'c', 'd', 'e', 'f']
g_Separator = '------------------'


 
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
    
    if p_Info["Menu"] == 'Results_ViewResult':
        p_OpenFile = open(os.getcwd() + '/' + p_Info['Path'], 'r')
        p_OpenLog = []
        
        for p_Temp in p_OpenFile:
            p_OpenLog.append(ast.literal_eval(p_Temp.strip())) # Gabrielson, 2009 - The function takes a representation of data and evaluates it into the data type. 

        p_OpenFile.close()

        print(f"{bcolours.CUSTOMGRAY}Home > Past results > {p_OpenLog[0]['Subject']} on {p_OpenLog[0]['Date']}{bcolours.ENDC}") 

        for p_I in range(len(p_OpenLog)-1): 
            p_I = p_I + 1
            p_Row = p_OpenLog[p_I] 

            if p_Row['SelectedAnswer'] == p_Row['CorrectAnswer']:
                print(f"\n{p_I}. ✅ {p_Row['Question']}")
            else:
                print(f"\n{p_I}. ❌ {p_Row['Question']}") 

            if p_Row['SelectedAnswer'] == p_Row['CorrectAnswer']: 
                for p_J in range(len(p_Row['Answers'])):
                    if p_J == p_Row['SelectedAnswer']:
                        print(f'{bcolours.OKGREEN}   [{g_Alpha[p_J]}] {p_Row['Answers'][p_J]}{bcolours.ENDC}')
                    else:
                        print(f'   [{g_Alpha[p_J]}] {p_Row['Answers'][p_J]}')

                print(f'\n{bcolours.OKGREEN}   Selected: {p_Row['Answers'][p_Row['SelectedAnswer']]}{bcolours.ENDC}')
                print(f'   Correct: {p_Row['Answers'][p_Row['CorrectAnswer']]}')
            
            else:
                for p_J in range(len(p_Row['Answers'])):
                    if p_J == p_Row['SelectedAnswer']:
                        print(f'{bcolours.FAIL}   [{g_Alpha[p_J]}] {p_Row['Answers'][p_J]}{bcolours.ENDC}')
                    else:
                        if p_J == p_Row['CorrectAnswer']:
                            print(f'{bcolours.OKGREEN}   [{g_Alpha[p_J]}] {p_Row['Answers'][p_J]}{bcolours.ENDC}')
                        else:
                            print(f'   [{g_Alpha[p_J]}] {p_Row['Answers'][p_J]}')

                print(f'\n{bcolours.FAIL}   Selected: {p_Row['Answers'][p_Row['SelectedAnswer']]}{bcolours.ENDC}')
                print(f'   Correct: {p_Row['Answers'][p_Row['CorrectAnswer']]}')

            print(f"\n{bcolours.CUSTOMGRAY}{g_Separator}")
            print(f"Test on {p_OpenLog[0]['Subject']}:")

            for p_I in range(len(p_OpenLog[0]['Topics'])):
                print(f'- {p_OpenLog[0]['Topics'][p_I]}')
            
            print(f'{g_Separator}{bcolours.ENDC}')

            print(f'You Scored:   {p_OpenLog[0]['Score']}/{p_OpenLog[0]['AmtQuestions']} ({str((int(p_OpenLog[0]['Score'])/int(p_OpenLog[0]['AmtQuestions'])*100))[:4]}%).')
            print(f'Time Taken:   {p_OpenLog[0]['TimeTaken']}m{bcolours.CUSTOMGRAY} out of {p_OpenLog[0]['TimeAllocated']}m.{bcolours.ENDC}')

            print(f'{bcolours.CUSTOMGRAY}{g_Separator}{bcolours.ENDC}\n')

            print('Enter [e] to go back.')
            print('Enter [d] to delete test.')

    if p_Info['Menu'] == 'Results_DeleteResult':
        p_OpenFile = open(os.getcwd() + '/' + p_Info['Path'], 'r')
        p_OpenLog = []
        
        for p_Temp in p_OpenFile:
            p_OpenLog.append(ast.literal_eval(p_Temp.strip())) # Gabrielson, 2009 - The function takes a representation of data and evaluates it into the data type. 

        p_OpenFile.close() 
        print(f"{bcolours.CUSTOMGRAY}Home > Past results > {p_OpenLog[0]['Subject']} on {p_OpenLog[0]['Date']} > Deletion{bcolours.ENDC}\n") 
        print('Are you sure you want to delete this test?\n')
        print('Enter [e] to go back')
        print(f'Enter {bcolours.FAIL}[d]{bcolours.ENDC} to delete this test.')

    if p_Info['Menu'] == 'TestSetup_Main':
        print(f'{bcolours.CUSTOMGRAY}Home > Take a test{bcolours.ENDC}\n')
        print(f'We found {len(p_Info['Subjects'])} subjects.\n')

        for p_I in range(len(p_Info['Subjects'])):
            print(f'  [{p_I +1}] {p_Info['Subjects'][p_I]}')

        print('\nSelect a subject by entering the corresponding number.')
        print(f'{bcolours.CUSTOMGRAY}Enter [e] to go back.{bcolours.ENDC}')
    
    if p_Info['Menu'] == 'TestSetup_Topics':
        print(f'{bcolours.CUSTOMGRAY}Home > Take a test > {p_Info['Subject']}{bcolours.ENDC}')
        print(f'{bcolours.CUSTOMGRAY}Please note that these question sets are AI Generated{bcolours.ENDC}\n')
        print(f"We found {len(p_Info['Topics'])} question sets inside {p_Info['Subject']}\n")
        
        for p_I in range(len(p_Info['Topics'])):
            if p_Info['Topics'][p_I][:-4] in p_Info['ChosenTopics']:
                print(f'   [{p_I+1}]  ✅  {p_Info['Topics'][p_I][:-4]}')
            else:
                print(f'   [{p_I+1}]  ⏺   {p_Info['Topics'][p_I][:-4]}')
        print(f'\nEnter the corresponding number to add/remove a topic.')
        print("Enter [s] when you're done.")
        print(f'{bcolours.CUSTOMGRAY}Enter [e] to go back.{bcolours.ENDC}')
    
    if p_Info['Menu'] == 'TestSetup_Questions':
        print(f'{bcolours.CUSTOMGRAY}Home > Take a test > {p_Info['Subject']} > Questions {bcolours.ENDC}\n')
        print('Enter the amount of questions you want in the test.')
        print(f'{bcolours.CUSTOMGRAY}The max. for your selection is {bcolours.ENDC}{p_Info['MaxQuestions']}.\n')
        print(f'{bcolours.CUSTOMGRAY}Enter [e] to go back.{bcolours.ENDC}')
    
    if p_Info['Menu'] == 'TestSetup_Time':
        print(f'{bcolours.CUSTOMGRAY}Home > Take a test > {p_Info['Subject']} > Questions > Time{bcolours.ENDC}\n')
        print('Enter the amount of time you want to allocate for your test.')
        print(f'{bcolours.CUSTOMGRAY}We recommend {p_Info['RecommendedTime']} minutes based on your current selection.{bcolours.ENDC}\n')
        print(f'{bcolours.CUSTOMGRAY}Enter [e] to go back.{bcolours.ENDC}')
        print('(minutes) ', end='')
    
    if p_Info['Menu'] == 'TestSetup_FinalCheck':
        print(f'{bcolours.CUSTOMGRAY}{bcolours.ENDC}')
    









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

# View a result
"""
printMenu({'Menu':'Results_ViewResult', 'Path':'Results/Maths on 2-03-2024 (14.59.21) 5 minutes 4 questions copy.txt'}, 2.1)
"""

#Delete a result
"""
printMenu({'Menu':'Results_DeleteResult', 'Path':'Results/Maths on 2-03-2024 (14.59.21) 5 minutes 4 questions copy.txt'}, 1)
"""

# Test - Setup Main
"""
g_Subjects = os.listdir(os.getcwd()+'/Subjects')
printMenu({'Menu':'TestSetup_Main', 'Subjects':g_Subjects}, 2.1)
"""


# Test - Setup Topics
g_ChosenSubject = 'Math'
g_ChosenTopics = ['Addition']
"""
g_Topics = os.listdir(os.getcwd() + '/Subjects/' + g_ChosenSubject)
printMenu({'Menu':'TestSetup_Topics', 'Subject':g_ChosenSubject,'Topics':g_Topics, 'ChosenTopics':g_ChosenTopics}, 2.2)
"""



#Test - Setup Questions
"""
printMenu({'Menu':'TestSetup_Questions', 'Subject':g_ChosenSubject, 'MaxQuestions':50},1)
"""

#Test - Setup Time
"""
printMenu({'Menu':'TestSetup_Time', 'Subject':g_ChosenSubject, 'RecommendedTime':70}, 2)
"""

#Test - Final Checks

"""
"""

printMenu({'Menu':'TestSetup_Time', ''})

input(g_Prompt)
