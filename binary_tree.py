# a program that lists the nodes of a random binary tree by nodes at the same depth.
import random

class BTree(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        
    def __repr__(self):
        return "Node Data : %d" % self.data
        
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BTree(value)
            else:
                self.right.insert(value)
                
    def traverse_pre_order(self):
        print self.value
        if self.left:
            self.left.traverse_pre_order()
        if self.right:
            self.right.traverse_pre_order()
            
    def traverse_post_order(self):
        if self.left:
            self.left.traverse_post_order()
        if self.right:
            self.right.traverse_post_order()
        print self.value
            
    def traverse_in_order(self):
        if self.left:
            self.left.traverse_in_order()
        print self.value
        if self.right:
            self.right.traverse_in_order()
        
            
    def depth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return max(left_depth, right_depth) + 1
        
    
    def list_all_at_depth(self, depth):
        if depth == 0:
            print self.value,
        else:
            if self.left:
                self.left.list_all_at_depth(depth-1)
            if self.right:
                self.right.list_all_at_depth(depth-1)
        
        
if __name__=="__main__":
    #can be used to insert random values in testing binary tree.
    '''binary_tree = BTree(random.randrange(100))
    for i in range(9):
        value = random.randrange(100)
        binary_tree.insert(value)
    '''
    
    # creating dummy binary tree with values for testing.
    binary_tree = BTree(8)
    values = [4,12,2,6,10,14,1,3,5,7,9,11,13,15]
    for value in values:
        binary_tree.insert(value)
    
    max_depth = binary_tree.depth()
    
    print 'Binary Tree Nodes Listed Depth Wise'
    for i in range(max_depth):
        binary_tree.list_all_at_depth(i)
        print '-----------------------'
