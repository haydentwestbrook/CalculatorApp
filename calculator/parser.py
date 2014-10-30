from operators import *
import queue as q

def parse(string):
    #Returns the answer to a mathematical
    #expression inputted as a string
    terms = get_terms(string)
    if len(terms) == 1:
        return terms[0]
    #Builds queue containing all terms
    # of the expression
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
        if op == "+":
            term = queue.get()
            answer += term[0]
            if len(term) > 1:
                op = term[1]
        elif op == "-":
            term = queue.get()
            answer -= term[0]
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


def strip_string(string):
    #Strips string of whitespace
    string = string.replace(" ", "")
    string = string.replace("\t", "")
    string = string.replace("\n", "")
    return string