# Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?

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

directoryToDelete = list(scannedDirectory)[0]

for entry in scannedDirectory:
    availableSpace = 70000000 - scannedDirectory["/"] + scannedDirectory[entry]
    if scannedDirectory[entry] < scannedDirectory[directoryToDelete] and availableSpace >= 30000000:
        directoryToDelete = entry

print(scannedDirectory[directoryToDelete])
