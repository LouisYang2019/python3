#ex43 Basic Object-Oriented Analysis and Design
from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print('This sence is not yet configured.')
        print('Subclass it and implement enter()')
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.sence_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #be sure to print out the last_scene
        current_scene.enter()

class Death(Scene):

    quips = [
        'You died. You kinda suck at this.',
        'You Mon would be proud...if she were smarter.',
        'Such a luser.',
        "I have a small puppy that's better at this. ",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
        The Gothons of Planet Percal #25 have invaded your ship and
        destroyed your entire crew. You are the last surviving
        member and your last mission is to get the neutron destruct
        bomb from the Weapons Armory,put it in the bridge, and
        blow the ship up after getting into an escape pod.

        You're running down the central corridor to the Weapons
        Armory when a Gothon jumps out, red scaly skin, dark grimy
        teeth, and evil clown costume flowing around his hate
        filled body. He's blocking the door to the Armory and
        about to pull a weapon to blast you.
        """))

        action = input('> ')
        if action == 'shoot!':
            print (dedent("""
            Quick on the draw you yank out your blast and fire
            it at the Gotton. His clown costume is flowing and
            moving around his body, which throws off your aim.
            Your laser hits his costume but misses him 
            """))


        pass

class LaserWeaponArmory(Scene):
    def enter(self):
        pass

class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass
