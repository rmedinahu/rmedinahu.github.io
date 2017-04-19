"""
A BinaryTree class implemented with node/reference technique.
Use for homework 11 apr 19 2017
"""

class BinaryTree:
    
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key),
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key),
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key),

    def bforder(self):
        """This function should be implemented as a generator so that
        main can print the elements like so:
            for i in root.bforder():
                print i,    
        HINT: use python's deque as queue. See DSAP p.330.
        """
        print 'Need to implement. Should return a string containining elements in breadth first traversal order.'

    def build_tree(self, tree, pos, data):
        """ Recursive function to iteratively add left and right
        items to tree. Items are fetched from data. pos is tree index in data
        """
        print 'Tree not built, need to implement.'
                

if __name__ == '__main__':
    data = [0]
    data.extend('guoidpy')  # --> [0, 'g', 'u', 'o', 'i', 'd', 'p', 'y']
    root = BinaryTree(data[1])
    root.build_tree(root, 1, data)

      #############################
      #            g              #
      #        ____|____          #
      #        u       o          #
      #      __|__   __|__        #
      #      i   d   p   y        #
      #############################

    print '\n Pre Order ==>\t ', # --> g u i d o p y
    root.preorder()
    print '\n  In Order ==>\t ', # --> i u d g p o y
    root.inorder()
    print '\nPost Order ==>\t ', # --> i d u p y o g
    root.postorder()
    print '\nBreadth First Order ==>\t ', # --> g u o i d p y
    root.bforder()


