person = {
    "lolxd": 'lol xd',
    "hehexd": 'hehe lol xd',
    "nub": 'noob'
}

n = True
while n:
    check = input("Enter pokemon name: ")
    check2 = check.lower()
    print(check2, 'is', person[check2])
    lol = input("Press x to stop searching lol: ")
    if lol == 'x':
        exit()
    else:
        continue

    


