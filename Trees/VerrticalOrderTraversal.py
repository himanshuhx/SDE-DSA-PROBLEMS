#Naive approach 0(width*totalNodes)

def getMinMax(root,min,max,hd):
    if not root:
        return
    if hd<min:
        min = hd
    if hd>max:
        max = hd
    getMinMax(root,min,max,hd-1)
    getMinMax(root,min,max,hd+1)

def printVerticalOrder(node,line_no,hd):
    if not root:
        return
    if hd == line_no:
        print(node.data)
    printVerticalOrder(node.left,line_no,hd-1)
    printVerticalOrder(node.right,line_no,hd+1)

def VerticlOrder(root):
    min = float('inf')
    max = -float('inf')
    getMinMax(root,min,max,0)
    for line_no in range(min,max+1):
        printVerticalOrder(node,line_no,root)

VerticalOrder(root)

# Map Approach 0(n)

def getMap(node,map,hd):
    if not node:
        return
    if hd in map:
        map[hd].append(node.val)
    else:
        map[hd] = [node.val]
    getMap(root.left,map,hd-1)
    getMap(root.right,map,hd+1)

def verticalOrder(root):
    m = dict(list)
    getMap(root,m,0)
    for index,key in enumerate(sorted(m)):
        for value in m[key]:
            print(value)