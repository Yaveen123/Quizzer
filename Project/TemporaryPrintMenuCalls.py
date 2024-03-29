
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
# Delete a result
"""
printMenu({'Menu':'Results_DeleteResult', 'Path':'Results/Maths on 2-03-2024 (14.59.21) 5 minutes 4 questions copy.txt'}, 1)
"""
# TestSetup - Setup Main
"""
g_Subjects = os.listdir(os.getcwd()+'/Subjects')
printMenu({'Menu':'TestSetup_Main', 'Subjects':g_Subjects}, 2.1)
"""
# TestSetup - Setup Topics
g_ChosenSubject = 'Math'
g_ChosenTopics = ['Addition','Multiplication']
"""
g_Topics = os.listdir(os.getcwd() + '/Subjects/' + g_ChosenSubject)
printMenu({'Menu':'TestSetup_Topics', 'Subject':g_ChosenSubject,'Topics':g_Topics, 'ChosenTopics':g_ChosenTopics}, 2.2)
"""
#TestSetup - Setup Questions
"""
printMenu({'Menu':'TestSetup_Questions', 'Subject':g_ChosenSubject, 'MaxQuestions':50},1)
"""
#TestSetup - Setup Time
"""
printMenu({'Menu':'TestSetup_Time', 'Subject':g_ChosenSubject, 'RecommendedTime':70}, 2)
"""
#TestSetup - Final Checks
"""
printMenu({'Menu':'TestSetup_FinalCheck', 'Subject':g_ChosenSubject, 'Topics':g_ChosenTopics, 'AmtQuestions':30, 'AmtTime':20}, None)
"""
#Test - Main
"""
printMenu({
    'Menu':'Test_Main', 
    'Subject':g_ChosenSubject, 
    'QuestionNo.':2,
    'AmtQuestions':len(g_ChosenTopics)+3, 
    'TimeRemaining':20, 
    'Question':'Whats 1+1', 
    'PossibleAnswers':['10','2','22', '12'], 
    'SelectedAnswer':2
    }, 1)
"""
#Test - PreExit
"""
printMenu({
    'Menu':'Test_PreExit', 
    'AmtQuestions':10, 
    'UnansweredQuestions':[0,3], 
    'Subject':g_ChosenSubject
    }, 1)
"""
#End Test - End
"""
printMenu({'Menu':'Test_End', 'Subject':g_ChosenSubject}, 1)
"""
#End Test - Out of time
"""
printMenu({'Menu':'Test_OutOfTime', 'Subject':g_ChosenSubject}, 1)
"""

