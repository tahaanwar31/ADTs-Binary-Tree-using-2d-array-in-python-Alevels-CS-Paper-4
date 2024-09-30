#DECLARE ArrayNodes:ARRAY[0:19,0:2] OF INTEGER
#DECLARE RootPointer,FreeNode:INTEGER
global ArrayNodes
global RootPointer
global FreeNode
ArrayNodes=[[0]*3 for x in range(20)]
RootPointer=-1
FreeNode=0
def AddNode():
    global ArrayNodes
    global RootPointer
    global FreeNode
    NodeData=int(input("Please enter the data you want to add: "))
    if RootPointer>19:
        print("BInary Tree is full")
    else:
        ArrayNodes[FreeNode][0]=-1
        ArrayNodes[FreeNode][1]=NodeData
        ArrayNodes[FreeNode][2]=-1
        if RootPointer==-1:
            RootPointer=0
        else:
            placed=False
            CurrentPointer=RootPointer
            while placed==False:
                if NodeData<ArrayNodes[CurrentPointer][1]:
                    if ArrayNodes[CurrentPointer][0]==-1:
                        ArrayNodes[CurrentPointer][0]=FreeNode
                        placed=True
                    else:
                        CurrentPointer=ArrayNodes[CurrentPointer][0]
                else:
                    if ArrayNodes[CurrentPointer][2]==-1:
                        ArrayNodes[CurrentPointer][2]=FreeNode
                        placed=True
                    else:
                        CurrentPointer=ArrayNodes[CurrentPointer][2]
        FreeNode=FreeNode+1
def FindItem(SearchItem):
    CurrentPointer=RootPointer
    while CurrentPointer!=-1 and ArrayNodes[CurrentPointer][1]!=SearchItem:
        if SearchItem<ArrayNodes[CurrentPointer][1]:
            CurrentPointer=ArrayNodes[CurrentPointer][0]
        else:
            CurrentPointer=ArrayNodes[CurrentPointer][2]
    print(CurrentPointer)

