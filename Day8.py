# Consider your map; how many trees are visible from outside the grid?

def CheckAround(subList, currentElement):
    if all(int(i) < int(currentElement) for i in subList):
        return True
    else: False

def FindVisibleTreesInLine(line, lines, columns):
    treesToAdd = 0
    for treeIndex in range(len(line)):
        columnOfTree = columns[treeIndex]
        leftOfTree = line[:treeIndex]
        rightOfTree = line[treeIndex + 1:]
        topOfTree = list(columnOfTree)[:lines.index(line)]
        subOfTree = list(columnOfTree)[lines.index(line) + 1:]
        if treeIndex == 0 or treeIndex == len(line) - 1:
            treesToAdd += 1
        elif CheckAround(leftOfTree, line[treeIndex]) or CheckAround(rightOfTree, line[treeIndex]) or CheckAround(topOfTree, line[treeIndex]) or CheckAround(subOfTree, line[treeIndex]):
            treesToAdd += 1
    return treesToAdd

treeLines = []
visibleTreesTotal = 0

with open("Forest.txt") as f:
    lines = f.readlines()
    while len(lines) > 0:
        newTreeLine = lines.pop(0)
        treeLines.append(list(newTreeLine.strip()))

treeColumns = list(zip(*treeLines))

for treeLine in treeLines:
    if treeLines.index(treeLine) == 0 or treeLines.index(treeLine) == -1:
        visibleTreesTotal += len(treeLine)
    else:
        visibleTreesTotal += FindVisibleTreesInLine(treeLine, treeLines, treeColumns)

print(f"There are {visibleTreesTotal} trees visible")