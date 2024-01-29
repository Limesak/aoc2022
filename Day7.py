# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

def ChangeDirectoryCommand(currentPath, destDir):
    if destDir == "..":
        currentPath.pop()
    elif destDir == "/":
        currentPath.append('/')
    else:
        currentPath.append(destDir + '/')

def ListCommand(inputFile, currentPath, scannedDirs):
    dirSize = 0
    currentLine = [""]
    strPath = ''.join(currentPath)
    while currentLine[0] != "$" and len(inputFile) > 0:
        poppedLine = inputFile.pop(0)
        currentLine = poppedLine.strip().split(" ")
        if currentLine[0].isdigit():
            dirSize += int(currentLine[0])
        elif currentLine[0] == "dir":
            scannedDirectory[strPath + currentLine[1] + '/'] = 0
        else:
            inputFile.insert(0, poppedLine)
    scannedDirs[strPath] = dirSize
    
    for entry in scannedDirectory:
        if entry in strPath and entry != strPath:
            scannedDirectory[entry] += dirSize

currentDirectoryPath = []
scannedDirectory = {"/": 0}

with open("FileSystem.txt", "r") as f:
    f = f.readlines()
    while len(f) > 0:
        line = f.pop(0).strip().split(' ')
        if line[1] == "cd":
            ChangeDirectoryCommand(currentDirectoryPath, line[2])
        elif line[1] == "ls":
            ListCommand(f, currentDirectoryPath, scannedDirectory)

totalSizes = 0

for entry in scannedDirectory:
    if scannedDirectory[entry] < 100000:
        totalSizes += scannedDirectory[entry]

print(totalSizes)
