# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Goldilocks", color="#FFD700")
define pb = Character("Papa Bear", color="#800000")
define mb = Character("Mama Bear", color="#00FF00")
define lb = Character("Lil Bear", color="#00FFFF")

# Flags
default porridge1 = True
default porridge2 = True

default chair1 = True
default chair2 = True

default bed1 = True
default bed2 = True

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

    # There are multiple ways to play audio. Three channels available:
    # add files to respective folders (music, sound, audio)
    # Accepts string name as parameter
    # Optional parameter
        # fadeout/fadein 1.0 - transitional fade in seconds
        # <from _ to_ loop_>

    # play music "bgm.mp3"
    # play sound "foley.mp3"
    # play audio "va.mp3"

    ################
    # Story begins #
    ################

    "Once upon a time..."

    scene cabin  
    play music "music/LS beginning.mp3" fadeout 0.
    queue music "music/LS middle.mp3"
    show goldilocks neutral with dissolve


    "There was a little girl named Goldilocks."

    hide goldilocks neutral with dissolve

    "She went for a walk in the forest. Pretty soon, she came upon house."

    "She knocked. And when no one answered, she walked right in."

    scene kitchen with dissolve

    "At the table in the kitchen, there were three bowls of porridge."
    "Goldilocks was hungry."

    jump porridge
 
   
label porridge:
    show goldilocks thinking with dissolve

    menu:

        "She was deciding which bowl she wanted to eat."

        "The hot bowl." if porridge1:

            $ porridge1 = False
            show goldilocks hot with dissolve
            g "This porridge is too hot!"
            jump porridge

        "The cold bowl." if porridge2:

            $ porridge2 = False
            show goldilocks cold with dissolve
            g "This porridge is too cold."
            jump porridge

        "The just right bowl":
            show goldilocks gucci with dissolve
            g "Ahhh, this porridge is just right."
            jump livingroom

label livingroom:
    "After she'd eaten the her breakfast, she decided she was feeling a little tired."
    
    scene livingroom with dissolve

    "So, she walked into the living room where she saw three chairs."
    jump chair

label chair:

    show goldilocks thinking with dissolve

    menu:

        "She was deciding which chair to sit on."

        "Not this choice." if chair1:

            $ chair1 = False
            show goldilocks DX with dissolve
            g "That's not right!"
            jump chair

        "Not this choice." if chair2:

            $ chair2 = False
            show goldilocks XP with dissolve
            g "This is definitely wrong."
            jump chair

        "The just right bowl":
            show goldilocks BD with dissolve
            g "Ahhh, this chair is just right."

            hide goldilocks BD with dissolve
            # Crash foley
            "But just as she settled down into the chair to rest, it broke into pieces!"
            jump bedroom

label bedroom:    
    "Goldilocks was very tired by this time, so she went upstairs to the bedroom."
    
    scene bedroom with dissolve

    "There was three beds."
    jump bed

label bed:

    show goldilocks thinking
    with dissolve

    menu:

        "She was deciding which bed to sleep on."

        "Not this choice." if bed1:

            $ bed1 = False
            show goldilocks DX with dissolve
            g "This bed is too hard!"
            jump bed

        "Not this choice." if bed2:

            $ bed2 = False
            show goldilocks XP with dissolve
            g "This bed is too soft."
            jump bed

        "The just right bed":
            show goldilocks BD with dissolve
            g "Ahhh, this bed is just right."
            jump kitchenBear

label kitchenBear:

    #Insert CG of sleeping Goldilocks
    "Goldilocks fell asleep."

    show kitchen with dissolve

    "As she was sleeping, the three bears came home."

    show papa with dissolve
    pb "Somebody toucha my sphaget!"

    show mama with dissolve
    mb "Someone's been eating my porridge."

    show lil bitch with dissolve
    lb "Someone's been eating my porridge and they ate it all up!"

    # Footsteps foley
    jump livingroomBear

label livingroomBear:

    show livingroom with dissolve

    show papa with dissolve
    pb "Someone's been sitting in my chair."

    show mama with dissolve
    mb "Someone's been sitting in my chair too!"

    show lil bitch with dissolve
    lb "Someone's been sitting in my chair and they've broken it to pieces!"

    jump bedroomBear

label bedroomBear:

    show bedroom with dissolve

    "The bears decided to look around some more and when they got upstairs to the bedroom..."

    show papa with dissolve
    pb "Someone's been sleeping in my bed."

    show mama with dissolve
    mb "Someone's been sleeping in my bed too!"

    show lil bitch with dissolve
    lb "Someone's been sleeping in my bed and she's still there!"

    # show cg of sleeping goldilocks with bears over her

    "Just then, Goldilocks woke up and saw the three bears."

    # play music cowboy bebop
    # Show CG of goldilocks running outside of cabin

    g "TASUKETE, ONII-CHAN!!"

    "THE END"
    # This ends the game.

    return
