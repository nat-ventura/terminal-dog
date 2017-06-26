# 6-24-17
# nat
# dog for the terminal

import random

class Dog():
    def __init__(self, name = ""):
        sizes = ["small","medium","large"]
        personalities = {}
        personalities["hyper"] = 0
        personalities["friendly"] = 2
        personalities["chill"] = 3
        personalities["shy"] = 4
        self.name = name
        self.size = random.choice(self.sizes)
        self.personality = random.choice(self.personalities.keys())
        self.sleepy = personalities[self.personality]

    def bark(self):
        barks = ["arf arf", "wuf wuf", "borf borf"]
        for i in range(len(self.sizes)):
            sound = barks[i] + "!"
        return sound

def pick_action(dog, activities):
    for i in range(len(activities)):
        print i, activities[i]
    chosen = False
    while not chosen:
        choice = int(raw_input("what do you want to do? "))
        if choice in range(4):
            if choice == 0:
                pet(dog)
                dog.sleepy += 1
            elif choice == 1:
                walk(dog)
                dog.sleepy += 2
            elif choice == 2:
                hug(dog)
                dog.sleepy += 1
            elif choice == 3:
                feed(dog)
                dog.sleepy += 1
            chosen = True
        else:
            print "please just select one, i have limited capacities."
            continue

def pet(dog):
    print "you pet", dog.name + "\'s", dog.size, "body."
    if dog.personality == "hyper":
        print dog.name, ****
    print Dog.bark(dog)

def walk(dog):
    print "you give", dog.name, "a nice walk."
    print "it's a great time."

def hug(dog):
    print "you give", dog.name, "a little hug."
    print "aww.."

def feed(dog):
    print "you give", dog.name, "some food."
    print "they eat it up."

def main():
    activities = ["pet","walk","hug","feed"]
    print "*pant pant*\n?!!?!"
    name = raw_input("what would you like to call your new friend? ")
    dog = Dog(name)
    bark = Dog.bark(dog)
    print bark
    print "you can do the following activities with", dog.name
    pick_action(dog, activities)
    tired = False
    while not tired:
        print dog.name, "wants to keep hanging out."
        action = pick_action(dog, activities)
        if dog.sleepy >= 12:
            tired = True
    print dog.name, "needs a little alone time now."
    print bark

main()

