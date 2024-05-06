def isValidInput(input):
    checkLower = 0
    checkUpper = 0
    checkNumb = 0
    if len(input) < 5 or len(input) > 10:
        return 1
    else:
        for char in input:
            if char.isupper():
                checkUpper = 1
            if char.islower():
                checkLower = 1
            if char.isdigit():
                checkNumb = 1
        if (checkLower == 0):
            return 2
        if (checkUpper == 0):
            return 3
        if (checkNumb == 0):
            return 4
        if (checkLower == checkUpper == checkNumb):
            return 0

def isValidEmail(email):
    checkA = 0
    checkOther = 0
    Aidx = 0
    for i in range(len(email)):
        if (email[i] == '@' and i != 0):
            checkA = 1
            Aidx = i
    for i in range(Aidx, len(email)):
        if (email[i] == '.' and email[i - 1] != '@' and email[-1] != '.'):
            checkOther = 1
    if (checkA == checkOther == 1):
        return 1
    else:
        return 0

# while True:
#     s = input()
#     print(isValidEmail(s))