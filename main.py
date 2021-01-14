
from utils.textprocessing import TextProcessing
import os

'''
THINGS TO DO:

Look for "if conditions".
for each condition I have to check:
if there is && or || I discard it
if there are more than 2 calls I discard it
if there is one call then I check if it is "equal" and it has only one argument, otherwise I discard it
if there is more than one operator (I'm excluding the first operator if it is the first token) I discard it (>= is one single operator)
if there are at most two elements (variable, literal, constaint, null) and one operator (without considering the first token if it is an operator) it's OK otherwise I discard it
I don't consider punctuation (brackets, etc)
'''


def main():
    print("start program")



    java_file=os.path.join(os.getcwd(), "test/code.java")

    t=TextProcessing(java_file)
    t.srcml_process()
    t.remove_comments()
    t.remove_tags()

    print(t.text)


if __name__=="__main__":
    main()