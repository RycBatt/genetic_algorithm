


import random
import string


class Agent:
        
    def __init__(self, target_lenght):

        self.alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"
        self.lenght = target_lenght
        self.string = ''.join(random.choice(self.alphabet) for _ in range(target_lenght))
        self.fitness = -1
        
    def __str__(self):
        return ('String: ' + str(self.string) + ' Fitness: ' + str(self.fitness))


