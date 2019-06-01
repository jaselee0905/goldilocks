# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Goldilocks", color="#FFD700")
define pb = Character("Papa Bear", color="#800000")
define mb = Character("Mama Bear", color="#00FF00")
define bb = Character("Lil Bear", color="#00FFFF")

# Flags
default porridge1 = True
default porridge2 = True

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    "Once upon a time..."

    scene cabin    
    show goldilocks neutral
    with dissolve

    "There was a little girl named Goldilocks. She went for a walk in the forest. Pretty soon, she came upon house."

    "She knocked. And when no one answered, she walked right in."

    scene kitchen
    "At the table in the kitchen, there were three bowls of porridge."
    "Goldilocks was hungry."

    jump porridge
 
   
label porridge:
    show goldilocks sad
    with dissolve

    menu:

        "She was deciding which bowl she wanted to eat."

        "The hot bowl." if porridge1:

            $ porridge1 = False
            show goldilocks DX
            g "This porridge is too hot!"
            jump porridge

        "The cold bowl." if porridge2:

            $ porridge2 = False
            show goldilocks XP
            g "This porridge is too cold."
            jump porridge

        "The just right bowl":
            show goldilocks BD
            g "Ahhh, this porridge is just right."
            jump livingroom

label livingroom:
    "After she'd eaten the her breakfast, she decided she was feeling a little tired."
    
    # This ends the game.

    return
