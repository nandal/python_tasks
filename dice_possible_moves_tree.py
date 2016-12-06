# Imagine you are playing a board game. You roll a 6-faced dice and move forward the same number of spaces that you rolled.
# If the finishing point is “n” spaces away from the starting point, please implement a program that calculates how many 
# possible ways are there to arrive exactly at the finishing point.

# solution using decision tree

import time
import sys


class DiceTreeNode(object):
    def __init__(self, value, parent=None, faces=6):        
        self.children = []
        for i in range(faces):
            self.children.append(None)
        self.value  = value
        self.parent = parent
        
    def __repr__(self):
        return 'Node with value %d' % self.value
        
    def get_full_path(self):
        if self.parent:
            return self.parent.get_full_path() +' -> '+str(self.value)
        else:
            return str(self.value)
         

class DiceTree(object):
    def __init__(self, root, target=610, faces=6):
        self.root = root
        self.target = target
        self.faces = faces
        self.posibilities = 0
        self.posibilities_list = [0,0,0,0,0,0]
        
    def insert(self, parent, value):
        distance = parent.value + value
        #print distance, value
        node = DiceTreeNode(distance, parent, self.faces)
        parent.children[value-1] = node
        if distance == self.target:
            #print node.get_full_path()
            pass
        
        
    def spawn(self, node):
        for i in range(self.faces):
            #time.sleep(0.1)
            value = i+1
            distance = value + node.value
            if distance <= self.target:
                if distance == self.target:
                    self.posibilities += 1
                    self.posibilities_list[0] += 1
                    #print distance, value
                elif distance == self.target - 1:
                    self.posibilities_list[1] += 1
                elif distance == self.target - 2:
                    self.posibilities_list[2] += 1
                elif distance ==  self.target - 3:
                    self.posibilities_list[3] += 1
                elif distance ==  self.target - 4:
                    self.posibilities_list[4] += 1
                elif distance ==  self.target - 5:
                    self.posibilities_list[5] += 1
                self.insert(node, value)
        for child in node.children:
            if child:
                self.spawn(child)
        
    def print_tree(self, node, tab_value=2):
        if node:
            #print '-' * tab_value, node.value
            open('tree.sh', 'a').write('-' * tab_value + str(node.value)+"\n")
            for child in node.children:
                self.print_tree(child, tab_value+2)
        
if __name__=="__main__":
    if len(sys.argv) < 3:
        faces = 6
        distance = 10
    else:
        faces = int(sys.argv[1])
        distance = int(sys.argv[2])
        
    root = DiceTreeNode(0, faces=faces)
    dice_tree = DiceTree(root, distance, faces)
    dice_tree.spawn(dice_tree.root)
    print 'Max Posibilities (',faces,'/',distance,'): ', dice_tree.posibilities
    #dice_tree.print_tree(dice_tree.root, 0)
    for i in range(1, 13):
        root = DiceTreeNode(0, faces=6)
        dice_tree = DiceTree(root, i, 6)
        dice_tree.spawn(dice_tree.root)
        print i, dice_tree.posibilities, dice_tree.posibilities_list

