# Find possible ways in a Dice Game
# using efficient approach instead of Decision Tree

import sys

def find_possible_ways_dice_game(faces, distance):
    pre_values = [0 for x in range(faces)]
    cur_values = [0 for x in range(faces)]
    
    for i in range(1, distance+1):
        if i <= faces:
            if i == 1:
                cur_values[0] = 1
            elif i > 1:
                cur_values[0] = pre_values[0]*2
        else:
            cur_values[0] = sum(pre_values)
        for j in range(1, faces):
            cur_values[j] = pre_values[j-1]
        for k in range(faces):
            pre_values[k] = cur_values[k]
        
    return cur_values[0]
            
        
if __name__=="__main__":
    if len(sys.argv) >= 3:
        try:
            faces = int(sys.argv[1].strip())
            distance = int(sys.argv[2].strip())
            possible_moves = find_possible_ways_dice_game(faces, distance)
            print 'Possible moves for Distance',distance,'with',faces,'faces dice: ', possible_moves
        except:
            print 'Kindly provide integer values as arguments'
    else:
        print 'Kindly provide integer values as arguments for faces of dice and total distance.'
