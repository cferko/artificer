import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from IPython import display
import time

class Grid:
    
    def __init__(self, size):
        self.size = size
        self.length = size[0]
        self.width = size[1]
        self.image_array = np.zeros((self.length*64, self.width*64, 4), dtype='uint8')
#
#        plt.ion()        
#        self.fig = plt.figure()
#        self.ax = self.fig.add_subplot(111)
#        self.my_plot = self.ax.imshow(self.image_array)
        
    def update(self, unit_list):
        self.image_array = np.zeros((self.length*64, self.width*64, 4), dtype='uint8')

        for unit in unit_list:
            this_image = unit.image
            this_location = unit.location
            
            this_x = this_location[0]
            this_y = this_location[1]

            self.image_array[this_x*64:(this_x+1)*64, this_y*64:(this_y+1)*64] = this_image
            
    def view(self):
        self.my_plot.set_data(self.image_array)
        self.fig.canvas.draw()
        print "viewing"
        
class Mover:
    
    def __init__(self, location, update_rule, grid_shape):
        self.location = location
        self.speed = 1

        my_tyr = Image.open("../images/tyranid.png")
        my_tyr = my_tyr.resize((64, 64))
        self.image = np.array(my_tyr)
        self.update_rule = update_rule
        self.grid_shape = grid_shape
        
    def get_step(self, target_square):
        """Should we ask them to implement this as a challenge?
        """
        my_vector = target_square - self.location
        my_delta = my_vector/np.linalg.norm(my_vector, ord=np.inf)      
        
        return my_delta

    def handle_round(self):
        my_location = self.location
        my_delta = self.update_rule(my_location)
        
        proposed_location = self.location + my_delta
        
        if np.linalg.norm(my_delta, ord=np.inf)<=1 and is_allowed(proposed_location, self.grid_shape):
            self.location = proposed_location
            
        else:
            print "Your update function returned an invalid move", proposed_location
            pass           

def is_allowed(location, grid_size):
    return all([0 <= location[i] <= grid_size[i] for i in range(2)])
           
class Search:
    def __init__(self, monster, princess, grid_shape):
        self.monster = monster
        self.princess = princess
        self.grid = Grid(grid_shape)
        self.time = 0
        self.allowed_locs = [[i, j] for i in range(10) for j in range(10)]
 
    def execute(self):
        while not np.array_equal(self.monster.location, self.princess.location):
            self.monster.handle_round()
#            print "Monster: ", self.monster.location

            if not np.array_equal(self.monster.location, self.princess.location):
                self.princess.handle_round()
#                print "Princess: ", self.princess.location
                
            self.time+=1
#
#        print "Princess found after time ", self.time

        return            

def random_update(my_location):
    proposed_move = np.random.choice([-1, 0, 1], 2)
    while not is_allowed(proposed_move+my_location, (2,2)):
        proposed_move = np.random.choice([1,-1], 2)
        
    return proposed_move

def stand_still(my_location):
    return np.zeros((2))        
        
def test():
    monster_loc = np.random.choice(range(2), 2)
    princess_loc =  np.random.choice(range(2), 2)
    grid_shape = (2, 2)
    
    while np.array_equal(princess_loc, monster_loc):
        princess_loc =  np.random.choice(range(2), 2)
        
    monster = Mover(monster_loc, random_update, grid_shape)
    princess = Mover(princess_loc, stand_still, grid_shape)
    
    my_search = Search(monster, princess, grid_shape)
    my_search.execute()
    final_time = my_search.time
    return final_time
    
def test2():
    monster_loc = np.random.choice(range(2), 2)
    princess_loc =  np.random.choice(range(2), 2)
    grid_shape = (2, 2)
    
    while np.array_equal(princess_loc, monster_loc):
        princess_loc =  np.random.choice(range(2), 2)
        
    monster = Mover(monster_loc, random_update, grid_shape)
    princess = Mover(princess_loc, random_update, grid_shape)
    
    my_search = Search(monster, princess, grid_shape)
    my_search.execute()
    final_time = my_search.time
    return final_time
    
still_times=[]
move_times=[]    
for i in range(100):
    still_times.append(test())
    move_times.append(test2())
    
print np.mean(still_times)
print np.mean(move_times)