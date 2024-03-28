# Welcome to Quizzer!
> Software Engineering Task 1 - 2024 

Quizzer - a simple system that allows you to mix different questions from multiple question sets! 
Why? Because real world exams often test different topics at one time, but current pre-test/quiz systems often only tackle one topic at a time.  

# Getting started. 🚀
1. Download the [project](https://github.com/Yaveen123/Quizzer/tree/main/Project) folder and extract the contents.
2. Open the project folder **in VS-Code.**
3. Run 'Quizzer.py' **in VS-Code.**

### System requirements.
- **VS Code** or other IDE with [ANSI Escape Sequences](https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_.28Select_Graphic_Rendition.29_parameters) enabled.
- **Python 3.12** or higher.
- **Windows** 10 (v22H2+) or 11.

# Creating your own question sets.
## Question sets
This is an example question set:
`Addition.txt`
```py
{'Subject':'Maths','Topic':'Addition'}
{'Question':'What is 2 + 3', 'Answers':['10','5','22', '12'], 'SelectedAnswer':None, 'CorrectAnswer':2}
{'Question': 'What is 1 + 2', 'Answers': ['3', '5', '7', '1'], 'SelectedAnswer': None, 'CorrectAnswer': 0}
``` 
Simply put this file into any folder in the `Subjects` folder. 


### How does it work?
- Each row of a question set is a [dictionary](https://www.w3schools.com/python/python_dictionaries.asp). 
- The **first row** of the your question set always shows the `subject` and the `topic`.  
```py
{
  'Subject':'Maths',
  'Topic':'Addition'
}
```

- Every other row represents a question, like so:
```py
{
  'Question':'What is 2 + 3',        # Given question.
  'Answers':['10','5','22', '12'],   # List of possible answers.
  'SelectedAnswer':None,             # Always should be set to None.
  'CorrectAnswer':2                  # Index of the correct answer.
}
```



## File system
Inside the `Subjects` folder, you can create your own folder, and place your question sets inside :D 

Every subject is stored in the `Subjects` folder. In each subject, a `.txt` file holds a question set. 

```
Subjects/
├─ Math/
│  ├─ Addition.txt
│  ├─ Multiplication.txt/
├─ English/
│  ├─ Spelling.txt/
```

When setting up a test, the subjects and topics will be shown through the filename, for example: 
![image 3](https://github.com/Yaveen123/Quizzer/assets/94953863/7f010a9c-17ca-4eb8-88ed-25feb81e19d9)




