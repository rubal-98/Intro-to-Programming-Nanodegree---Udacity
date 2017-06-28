ques=[[">>Every webpage you look at is written in a language called _____ .",   #this is a list defining all questions. It consists of nested lists!!
       ">>HTML _____ are the building blocks of HTML pages.",
       ">>The visible part of the HTML document is between _____ tag.",
       ">>HTML  _____ consists of several key components."]
      ,[">>HTML also has _____ levels of headings. ",
        ">>The _____ attribute is used to associate an element with a style sheet.",
        ">>Characters surrounding text are displayed half a character's height by _____ tag.",
        ">>CSS stands for _____ Style Sheet ."]
      ,[">>The _____ element is used to contain the content that appears at the top of every page of your website.",
        ">>HTML is similar to _____ , although it is not a strict subset.",
        ">>HTML is a _____ language.",
        ">>The  _____ element defines an arbitrary block of content which can be placed and styled as a single unit."]]

list1=[["html","elements","body","markup"],["six","class","subscript","cascading"],["head","sgml","markup","div"]]  #this is a list defining all answers. It consists of 3 nested lists!!

def replacer(question,ans):
    #two variables ques and ans are passed through this function and ques is returned back to correct function!!!
    unprocess = question.split()
    processed = []
    for word in unprocess:
        if word == "_____":
            processed.append(ans)
        else:
            processed.append(word)
    question = " ".join(processed)
    return question

def correct(question,answer):
    #two variables ques and answer are passed through this function and ques is returned back to correct function!!!
    print ("\nCongratulations! Your answer is correct :D\n")
    ques = replacer(question,answer)
    return ques
def wrong():
    #only a single variable ques is passed through this function and nothing is returned back instead a print statement is executed!!!
    print("\nSorry! Your answer is incorrect :(\n")

def check_answer(question,ansList):
    #this function checks whether the input entered by user is correct or not.It inputs two variables ques and anslist as selected in play func and it prints an output message at the end of the quiz!!
    for index in xrange(0,4):
        while(True):
            ans=raw_input("\ninput value for "+str(index+1)+")_____:  ").lower()
            if ans==ansList[index]:
                question[index] = correct(question[index],ans)
                print_ques(question)
                break
            else:
                wrong()
                print_ques(question)
    print "Congratulations you got all your answers correct!!!!!"

def play(quesList,ansList):
    #it has two variables that are quesList, ansList which are passed as input!! and it calls two functions of which one selects the level and the other function prints the question...
    level = select_level()
    quesList = quesList[level]
    ansList = ansList[level]
    print_ques(quesList)
    check_answer(quesList,ansList)
    cont = raw_input("Do you want to continue? \n Enter y to continue / n to quit").lower()
    if cont=='y':
        play(ques,list1)
    #this is a recursive function which has list ques and list1 as inputs being passed
    else:
        print("thankyou for playing :)")

def select_level():
    #this function selects the level of difficulty and inputs a number based on level and returns level
    print("\nWelcome To The HTML Quiz")
    print("\nEnter the level of difficulty: ")
    level= int(raw_input("Press 1 for Easy || Press 2 for Medium || Press 3 for Difficult:  "))
    print("here begins your level "+str(level)+" quiz \n")
    return level-1

def print_ques(ques):
    #This function prints the question at the particular difficulty selected and has ques as input
    for line in ques:
        print line

play(ques,list1)
#here we input the two lists of ques and ans and doesnot return anything!!
