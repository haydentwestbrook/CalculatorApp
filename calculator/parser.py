from operators import *


def parse(string):

    """
    Takes in a string of math operations and returns the solution
    """

    i, found = 0, False
    while i < len(string):
        if string[i] == "(":
            found = True
            j = i + 1
            while j < len(string) and string[j] != ")":
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
            float(string)
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