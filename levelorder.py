#Given an array of unique elements, construct a Binary Search Tree and print the Level Order of the tree.

#Input Format

#First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - number of nodes in the BST. The next line contains N unique integers - value of the nodes.

#Constraints

#For each test case, print the Level Order of the Binary Search Tree, separate each level by newline. Separate the output of different test cases with an extra newline.

#code

class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,ele):
    if(root==None):
        return node(ele)
    elif(root.data>ele):
        root.left=insert(root.left,ele)
    elif(root.data<ele):
        root.right=insert(root.right,ele)
    return root
def levelorder(root):
    if(root==None):
        return
    q=[]
    q.append(root)
    null=node(None)
    q.append(null)
    while(len(q)!=1):
        curr=q[0]
        q.pop(0)
        if(curr!=null):
            print(curr.data,end=" ")
            if(curr.left!=None):
                q.append(curr.left)
            if(curr.right!=None):
                q.append(curr.right)
        else:
            q.append(null)
            print()
         
for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    root=None
    for i in a:
        root=insert(root,i)
    levelorder(root)
    print() 
    print()
    
    

        
