def ask_question(question):
    """
    Prompt the user with a question and receive their response.

    Parameters:
    ----------
    question : str
      

    Outputs:
    -------
    str or None
       
       
    Ex.
    --------

    ask_question("Do you prefer A or B?")
    Do you prefer A or B?
    Your answer (A/B): C
    Please answer the question using 'A' or 'B'.
    
    Chatbot Notes
    -----
    If the user enters an invalid response (neither A or B), the function prints
    a message asking the user to provide a valid response and returns None.
    """
    # Print question
    print(question)

    while True:
        answer = input("Your answer (A/B): ") #Prompt the user for input
        if answer == "QUIT": # Check if user wants to quit
            return "QUIT"
        elif answer in ('A', 'B'): # Cehck if answer is A or B
            return answer
        else: # If not A or B, prompt user to input correctly
            print("Please answer the question using 'A' or 'B'.")
         
        
def mbti_analyzer(answers):
    """
    Analyze the user's responses to determine their MBTI personality type.

    Parameters:
    ----------
    answers : list of str
        List containing the user's responses to the MBTI questions.

    Outputs:
    -------
    str
        The user's MBTI personality type.

    Ex.
    --------
    mbti_analyzer(['A', 'B', 'A', 'B'])
    'ENTP'
    """
    
    result = ''
    
    #The enumerate () method adds a counter to an iterable and returns it in the form of an enumerating object.
    for i, answer in enumerate(answers):
        if i == 0:  # First question determines the first letter (E or I)
            if answer == 'A':
                result += 'E'
            else:
                result += 'I'
        elif i == 1:  # Second question determines the second letter (S or N)
            if answer == 'A':
                result += 'S'
            else:
                result += 'N'
        elif i == 2:  # Third question determines the third letter (T or F)
            if answer == 'A':
                result += 'T'
            else:
                result += 'F'
        elif i == 3:  # Fourth question determines the fourth letter (J or P)
            if answer == 'A':
                result += 'J'
            else:
                result += 'P'
    return result


def end_chat():
    """
    End the chat session with a farewell message.

    Parameters
    ----------
    None

    Outputs:
    -------
    str

    Ex.
    --------
    
    end_chat()
    So sorry to see you quit the mini MBTI chatbot right here, I will miss you:(
    Goodbye! Thank you for participating in the mini MBTI project
    The MBTI testing questions are adapting from https://speedmba.online/blog/mbti/
    """
    
    # Print out desired desginated outputs when the function is triggered.
    print("So sorry to see you quit the mini MBTI chatbot right here, I will miss you:(")
    print("Goodbye! Thank you for participating in the mini MBTI project")
    print("The MBTI testing questions are adapting from"
          " https://speedmba.online/blog/mbti/")