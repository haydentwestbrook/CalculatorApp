from operators import *
import flask
import trig
import logs
import exceptions


def parse(string):

    """
    Takes in a string of math operations and returns the solution
    """

    try:
        functions = ["sin", "cos", "tan", "sec", "csc", "cot", "ln", "log"]
        for function in functions:
            while function in string:
                i = 0
                while i < len(string) - 3:
                    if string[i:i+3] == function:
                        j = 0
                        while string[j] != ")" and j < len(string):
                            j += 1
                        input_string = string[i+4:j]
                        if function == "sin":
                            input_string = trig.sin(float(parse(input_string)))
                        if function == "cos":
                            input_string = trig.cos(float(parse(input_string)))
                        if function == "tan":
                            input_string = trig.tan(float(parse(input_string)))
                        if function == "sec":
                            input_string = trig.sec(float(parse(input_string)))
                        if function == "csc":
                            input_string = trig.csc(float(parse(input_string)))
                        if function == "cot":
                            input_string = trig.cot(float(parse(input_string)))
                        if function == "log":
                            input_string = logs.log(float(parse(input_string)))
                        string = string[0:i] + str(input_string) + string[j+1:len(string)]
                    if string[i:i+2] == function:
                        j = 0
                        while string[j] != ")" and j < len(string):
                            j += 1
                        input_string = logs.ln(float(parse(string[i+3:j])))
                        string = string[0:i] + str(input_string) + string[j+1:len(string)]
                    i += 1

        while "(" in string:
            i, found = 0, False
            while i < len(string):
                if string[i] == "(":
                    found = True
                    j, n = i + 1, 0
                    while j < len(string):
                        if string[j] == "(":
                            n += 1
                        if string[j] == ")" and n == 0:
                            break
                        if string[j] == ")":
                            n -= 1
                        j += 1
                    new_string = string[i+1: j]
                    break
                i += 1
            if found:
                string = string[0:i] + parse(new_string) + string[j+1:len(string)]

            while "^" in string:
                i, found = 0, False
                while i < len(string):
                    if string[i] == "^":
                        found = True
                        break
                    i += 1
                if found:
                    num1 = get_number(string, i, "b")
                    num2 = get_number(string, i, "f")
                    string = string[0:i-len(num1)] + str(float(num1) ** float(num2)) + string[i+len(num2)+1:len(string)]

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
                string = str(float(string))
                if float(string) == float(int(float(string))):
                    string = string[0:len(string)-2]
                break
            except:
                pass
            i, found = 0, False
            while i < len(string):
                if string[i] == "+" or (string[i] == "-" and (i != 0 and not (string[i-1] == "+" or string[i-1] == "-" or
                                                                              string[i-1] == "*" or string[i-1] == "/"))):
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
    except:
        raise exceptions.InputError("Input is in an invalid format.")


def get_number(string, i, mode="f"):
    if mode == "f":
        number = ""
        i += 1
        if i < len(string) and string[i] == "-":
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
        if string[i] == "-" and (i == 0 or (string[i-1] == "+" or string[i-1] == "-" or
                                            string[i-1] == "*" or string[i-1] == "/")):
            number += string[i]
        number = number[::-1]
    if number == "":
        number = "0"
    return number


def strip_string(string):
    """
    Strips string of whitespace
    """
    string = string.replace(" ", "")
    string = string.replace("\t", "")
    string = string.replace("\n", "")
    return string

def printer(equation):
    flask.flash("The equation, " + equation + ", equals:")
    flask.flash(parse(strip_string(equation)))
