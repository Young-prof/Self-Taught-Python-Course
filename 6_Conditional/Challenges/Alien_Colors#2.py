'''
Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block.
'''
alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
    print("\nYou've just earned 5 points for shooting the alien")
else:
    print("\nYou've just earned 10 points for shooting the target")

if 'yellow' in alien_color:
    print("\nYou've just earned 10 points for shooting an alien")
if 'red' in alien_color:
    print("\nYou've just earned 5 points for shooting an alien")
