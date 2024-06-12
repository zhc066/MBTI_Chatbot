# NOTE: test_functions successfully pass the pytest with command: 
# zhc066@dsmlp-jupyter-zhc066:~/MyProjectFolder$ pytest -s

import pytest
import string
from io import StringIO
from functions import mbti_analyzer, ask_question, end_chat

def test_mbti_analyzer():
    """
    Test the mbti_analyzer() function.
    
    NO INPUTS OR OUTPUTS, test pass silently

    Assertion test for different combinaton of answers, and test the correct outputs.

    """
    # Test for if the function is callable
    assert callable(end_chat)
    
    # Different combination of the answers
    answers_A = ["A", "A", "A", "A"]
    answers_B = ["B", "B", "B", "B"]
    answers_C = ["A", "B", "A", "B"]
    answers_D = ["B", "A", "B", "A"]
    
    # Assert for expected MBTI types
    assert mbti_analyzer(answers_A) == "ESTJ"
    assert mbti_analyzer(answers_B) == "INFP"
    assert mbti_analyzer(answers_C) == "ENTP"
    assert mbti_analyzer(answers_D) == "ISFJ"
    
def test_ask_question():
    """
    Test the ask_question() function.
    
    NO INPUTS OR OUTPUTS, test pass silently
    
    Ensure function correctly prompts the user with a question and computes
    different types of user responses.
    
    Notes, we only need to test the three inputs types: 'A', 'B', and 'QUIT" 
    since these three types have the actual meaning to the function, and their 
    return value will be evalued by the mbti_analyzer.
    """
    # Test for if the function is callable
    assert callable(ask_question)
    answer_A = 'A'
    answer_B = 'B'
    answer_quit = 'QUIT'

    # Test A and B inputs
    assert ask_question("Type 'A' to test function") == answer_A
    assert ask_question("Type 'B' to test function") == answer_B

    # Test QUIT command
    assert ask_question("Type 'QUIT' to test function") == answer_quit



def test_end_chat():
    """
    Test the end_chat() function.
    
    NO INPUTS OR OUTPUTS, test pass silently
    
    Ensure end_chat function prints out correct type.
    """
    
    # Test for if the function is callable
    assert callable(end_chat)
    
    # OUTSIDE SOURCE: With statement ensures closing resources right after processing them. 
    # https://www.geeksforgeeks.org/stringio-module-in-python/
    # Initiate a StringIO object, as captured_output.
    # Basically, binds the StringIO object with the new defined captured_output
    with StringIO() as output:
        
        # Execute function
        end_chat()
        
        # OUTSIDE SOURCE: StringIO.getvalue(): returns the entire content of the file.
        # https://www.geeksforgeeks.org/with-statement-in-python/
        # Get the captured output message
        actual_output = output.getvalue()

    # Assert type string
    assert isinstance(actual_output, str)