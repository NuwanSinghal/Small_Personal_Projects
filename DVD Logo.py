import sys, random, time
import bext

Width, Height = bext.size()

Width -= 1

Number_of_Logos = 1
Pause_Amount = 0.2
Colours = ['red','green','blue','cyan']

Up_Right = 'ur'
Up_Left = 'ul'
Down_Right = 'dr'
Down_Left = 'dl'
Directions = (Up_Left, Up_Right, Down_Left, Down_Right)

Colour = 'colour'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    bext.clear()

    logos = []
    for i in range(Number_of_Logos):
        logos.append({Colour: random.choice(Colours),
            X: random.randint(1, Width - 4),
            Y: random.randint(1, Height - 4),
            DIR: random.choice(Directions)})
        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1

    cornerBounces = 0

    while True:
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print('  ', end='')

            originalDirection = logo[DIR]

            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = Down_Right
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == Height - 1:
                logo[DIR] = Up_Right
                cornerBounces += 1
            elif logo[X] == Width - 3 and logo[Y] == 0:
                logo[DIR] = Down_Left
                cornerBounces += 1
            elif logo[X] == Width -3 and logo[Y] == Height - 1:
                logo[DIR] = Up_Left
                cornerBounces += 1

            elif logo[X] == 0 and logo[DIR] == Up_Left:
                logo[DIR] = Up_Right
            elif logo[X] == 0 and logo[DIR] == Down_Left:
                logo[DIR] = Down_Right

            elif logo[Y] == 0 and logo[DIR] == Up_Left:
                logo[DIR] = Down_Left
            elif logo[Y] == 0 and logo[DIR] == Up_Right:
                logo[DIR] = Down_Right

            elif logo[X] == Width - 3 and logo[DIR] == Up_Right:
                logo[DIR] = Up_Left
            elif logo[X] == Width - 3 and logo[DIR] == Down_Right:
                logo[DIR] = Down_Left

            elif logo[Y] == Height - 1 and logo[DIR] == Down_Left:
                logo[DIR] = Up_Left
            elif logo[Y] == Height - 1 and logo[DIR] == Down_Right:
                logo[DIR] = Up_Right

            if logo[DIR] != originalDirection:
                logo[Colour] = random.choice(Colours)

            if logo[DIR] == Up_Right:
                logo[X] += 2
                logo[Y] -= 1
            if logo[DIR] == Up_Left:
                logo[X] -= 2
                logo[Y] -= 1
            if logo[DIR] == Down_Right:
                logo[X] += 2
                logo[Y] += 1
            if logo[DIR] == Down_Left:
                logo[X] -= 2
                logo[Y] += 1

            bext.goto(5,0)
            bext.fg('white')
            print(f"Corner Bounces: {cornerBounces}")

            for logo in logos:
                bext.goto(logo[X], logo[Y])
                bext.fg(logo[Colour])
                print('DVD', end='')

            bext.goto(0,0)

            sys.stdout.flush()
            time.sleep(Pause_Amount)

if __name__ == '__main__':
    main()