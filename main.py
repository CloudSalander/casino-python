"""
TO-DO:
- Input validation
- Add constant values
"""
players = {}
option = input()

def enterCasino(input):
    if input[0] in players:
        print(input[0]+ " is already in the casino")
    else:
        players[input[0]] = 0

def leaveCasino(input):
    if input[0] in players:
        print(input[0]+" has won "+str(players[input[0]]))
        players.pop(input[0])
    else:
        print(input[0]+" is not in the casino")

def useOption(option):
    input = option.split()
    if "enters" in input[1]:
        enterCasino(input)
    elif "leaves" in input[1]:
        leaveCasino(input)

while option != "" :
    useOption(option)
    option = input()

print(players)