# How many characters need to be processed before the first start-of-packet marker is detected?

def checkDuplicates(pointer):
    for char in pointer:
        if pointer.count(char) > 1: return True
    return False

with open("CommunicationSignal.txt", "r") as f:
    pointer = []
    numberOfCharRead = 0
    while True:
        numberOfCharRead += 1
        pointer.append(f.readline(1))
        if len(pointer) == 14 and checkDuplicates(pointer): pointer.pop(0)
        elif len(pointer) == 14 and checkDuplicates(pointer) == False: break

print(f"Chars read : {numberOfCharRead}")