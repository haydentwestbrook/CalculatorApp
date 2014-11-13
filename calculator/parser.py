from operators import *
import queue as q

'''
def parse2(string):
    #Returns the answer to a mathematical
    #expression inputed as a string
    terms = get_terms(string)
    if len(terms) == 1:
        return terms[0]
    #Builds queue containing all terms
    #of the expression
    queue = q.Queue()
    queue.put(terms)
    while len(terms) > 1:
        terms = get_terms(terms[2])
        queue.put(terms)
    term = queue.get()
    answer = term[0]
    op = term[1]
    #Evaluates the expression as values are 
    #removed from the queue
    while not queue.empty():
        if op == "*":
            start = term[0]
            term_string = ""
            while op == "*" and not queue.empty():
                term = queue.get()
                term_string += str(term[0])
                if len(term) > 1:
                    op = term[1]
                    term_string += op
                else:
                    op = None
            answer += start * parse(term_string)
        elif op == "+":
            term = queue.get()
            answer = add(answer, term[0])
            if len(term) > 1:
                op = term[1]
        elif op == "-":
            term = queue.get()
            answer = subtract(answer, term[0])
            if len(term) > 1:
                op = term[1]
    return answer
        
    
def get_terms(string):
    #Returns a tuple with an int of the first
    #number, the operator, and the remainder 
    #of the expression string
    if not isinstance(string, str):
        raise TypeError()
    if not len(string) > 0:
        return None
    i = 0
    while True:
        if string[0] == "-":
            i += 1
        try:
            int(string[i])
            i += 1
        except:
            break
    a = int(string[0: i])
    if i >= len(string) - 1:
        return [a]
    op = string[i]
    if op == "/" and string[i+1] == "//":
        op = "//"
    if i+1 > len(string) - 1:
        return [a]
    b = string[i+1: len(string)]
    return (int(a), op, b)
'''

def parse(string):
    while "*" in string or "/" in string:
        i, found = 0, False
        while i < len(string):
            if string[i] == "*" or string[i] == "/":
                found = True
                break
            i += 1
        if found:
            num1 = get_number(string, i, "b")
            num2 = get_number(string, i, "f")
            if string[i] == "*":
                string = string[0:i-len(num1)] + str(float(num1) * float(num2)) + string[i+len(num2)+1:len(string)]
            elif string[i] == "/":
                string = string[0:i-len(num1)] + str(float(num1) / float(num2)) + string[i+len(num2)+1:len(string)]
    while True:
        try:
            float(string)
            break
        except:
            pass
        i, found = 0, False
        while i < len(string):
            if string[i] == "+" or string[i] == "-":
                found = True
                break
            i += 1
        if found:
            num1 = get_number(string, i, "b")
            num2 = get_number(string, i, "f")
            if string[i] == "+":
                string = string[0:i-len(num1)] + str(float(num1) + float(num2)) + string[i+len(num2)+1:len(string)]
            elif string[i] == "-":
                string = string[0:i-len(num1)] + str(float(num1) - float(num2)) + string[i+len(num2)+1:len(string)]
    return string


def get_number(string, i, mode="f"):
    if mode == "f":
        number = ""
        i += 1
        if string[i] == "~":
            number += string[i]
            i += 1
        while i < len(string):
            try:
                if string[i] == ".":
                    number += string[i]
                else:
                    float(string[i])
                    number += string[i]
                i += 1
            except:
                break
    if mode == "b":
        number = ""
        i -= 1
        while i >= 0:
            try:
                if string[i] == ".":
                    number += string[i]
                else:
                    float(string[i])
                    number += string[i]
                i -= 1
            except:
                break
        if i >= 0 and string[i] == "~":
            number += string[i]
        number = number[::-1]
    return number


def strip_string(string):
    #Strips string of whitespace
    string = string.replace(" ", "")
    string = string.replace("\t", "")
    string = string.replace("\n", "")
    return string