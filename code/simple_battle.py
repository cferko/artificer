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

        plt.ion()        
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.my_plot = self.ax.imshow(self.image_array)
        
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

class Turret:
    
    def __init__(self, location): ## Do we need the battle grid in here?
        self.hp = 10
        self.ac = 15
        self.initiative = 0
        self.location = location
        self.attack_bonus = 2
        self.damage_die = 6
        self.speed = 0
        
        my_sphere = Image.open("sphere_sprite.png")
        my_sphere = my_sphere.resize((64, 64))
        self.image = np.array(my_sphere)
        
    def get_adjacent_enemies(self, enemy_army):
        my_adjacents=[]
        
        for enemy in enemy_army:
            enemy_location = enemy.location
            distance = np.linalg.norm(self.location-enemy_location, ord=np.inf)
            if distance==1:
                my_adjacents.append(enemy)
                
        return my_adjacents
        
    def attack(self, enemy):
        enemy_ac = enemy.ac
        my_roll = np.random.randint(low=1, high=21)
        
        if my_roll + self.attack_bonus > enemy_ac:
            enemy.apply_damage(np.random.randint(low=1, high=self.damage_die))
    
    def apply_damage(self, damage):
        self.hp -= damage
        print "Turret takes", damage, "damage."
        
    def handle_round(self, enemy_army):
        adjacent_enemies = self.get_adjacent_enemies(enemy_army)
        
        if len(adjacent_enemies)==0:
            return
            
        else:
            my_target = np.random.choice(adjacent_enemies)
            self.attack(my_target)
            
class Tyranid:
    
    def __init__(self, location): ## Do we need the battle grid in here?
        self.hp = 10
        self.ac = 15
        self.initiative = 0
        self.location = location
        self.attack_bonus = 2
        self.damage_die = 6
        self.speed = 1

        my_tyr = Image.open("tyranid.png")
        my_tyr = my_tyr.resize((64, 64))
        self.image = np.array(my_tyr)
        
    def get_adjacent_enemies(self, enemy_army):
        my_adjacents=[]
        
        for enemy in enemy_army:
            enemy_location = enemy.location
            distance = np.linalg.norm(self.location-enemy_location, ord=np.inf)
            if distance==1:
                my_adjacents.append(enemy)
                
        return my_adjacents
        
    def attack(self, enemy):
        enemy_ac = enemy.ac
        my_roll = np.random.randint(low=1, high=21)
        
        if my_roll + self.attack_bonus > enemy_ac:
            enemy.apply_damage(np.random.randint(low=1, high=self.damage_die))
    
    def apply_damage(self, damage):
        self.hp -= damage
        print "Tyranid takes", damage, "damage."
        
    def move_closer(self, enemy_army):
        enemy_locations=[]
        enemy_distances = []
        
        for enemy in enemy_army:
            enemy_location = enemy.location
            enemy_locations.append(enemy_location)
            
            distance = np.linalg.norm(self.location-enemy_location, ord=np.inf)
            enemy_distances.append(distance)

            target_square = enemy_locations[np.argmin(enemy_distances)]
            
            my_vector = target_square - self.location
            my_delta = my_vector/np.linalg.norm(my_vector, ord=np.inf)
            self.location = self.location + my_delta
        
        print "Tyranid moves to", self.location        
        
        return                
        
    def handle_round(self, enemy_army):
        adjacent_enemies = self.get_adjacent_enemies(enemy_army)
        
        if len(adjacent_enemies)==0:
            self.move_closer(enemy_army)
            
        else:
            my_target = np.random.choice(adjacent_enemies)
            self.attack(my_target)
            
class Battle:
    def __init__(self, army_one, army_two):
        self.army_one = army_one
        self.army_two = army_two
        self.grid = Grid((8, 8))
        
    def execute_battle(self):
        army_one_size = len([soldier for soldier in self.army_one if soldier.hp>0])        
        army_two_size = len([soldier for soldier in self.army_two if soldier.hp>0])
        
        while army_one_size>0 and army_two_size>0:
            self.perform_round()
            army_one_size = len([soldier for soldier in self.army_one if soldier.hp>0])        
            army_two_size = len([soldier for soldier in self.army_two if soldier.hp>0])            
        
        if army_one_size>0 and army_two_size>0:
            self.perform_round()
            
        elif army_one_size==0 and army_two_size>0:
            print "Army two wins"
            
        elif army_one_size>0 and army_two_size==0:
            print "Army one wins"
            
        elif army_one_size==army_two_size==0:
            print "Tie"
             
    def perform_round(self):
        for soldier in self.army_one:
            soldier.handle_round(self.army_two)
        for soldier in self.army_two:
            soldier.handle_round(self.army_one)

        all_units = self.army_one + self.army_two
        self.grid.update(all_units)
        self.grid.view()

        return            
        
def test():
    turret_loc = np.array((0, 0))
    tyranid_loc = np.array((5, 5))
    army_one = [Turret(turret_loc)]
    army_two = [Tyranid(tyranid_loc)]
    
    my_battle = Battle(army_one, army_two)
    my_battle.execute_battle()
    
test()