from weapons import Weapons
from random import randrange
from dinosaur import Dinosaur



robot_list= ['Bender', 'Roberto', 'Donbot']

class Robot:
    def __init__(self, robot_name):
        self.robot_name= robot_name
        self.robot_health= 100
        self.robot_weapon= Weapons()
    

    def attack(self, opponent): #need a function to simulate the attack of the robot
        opponent= Dinosaur(20)
        attack_order= randrange(0,10)
        if attack_order >= 5:
           robo_damage = self.robot_weapon - opponent.dinosaur_health
           return robo_damage
        else: 
            print('Blank Robot attacked but missed, better luck next move.') # I am trying to figure out how to pick a robo or dino to get them to fight
    
first_robot= Robot('Bender')
second_robot= Robot('Roberto')
third_robot= Robot('Donbot')

 
 

# I can't seem to get my objects to work



        