# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# default charm = 0

# To avoid repeatedly typing character name we can define them with a shortform like "j" and an accent color
define j = Character("Janice",  color="#e460de")

# we can also define other things like transitions, now we can use with slowerdissolve to quickly get a slower dissolve transition
define slowerdissolve = Dissolve(2.0)

# we can also redefine an image's tag to a shortform like logo, now we can use "show logo"
image logo = "janice logo.png"


# The game starts here.


# label charm:
#     show bg temple
#     show screen bars
    
#     show may normal
#     j "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sit amet ligula quam. Phasellus vel erat sed lacus feugiat faucibus. Donec sodales, eros vitae vehicula dapibus, enim elit eleifend risus, eget sagittis est risus id diam. Curabitur maximus libero lacus, nec varius ex ultricies ut. Maecenas id posuere erat. Pellentesque lacinia lacus quis massa tempor, a dapibus eros semper."

#     $ charm = 0
#     j "Test Charm at 0"
#     $ charm = 10
#     j "Test Charm at 10"
#     $ charm = 50
#     j "Test Charm at 50"
#     $ charm = 75
#     j "Test Charm at 75"
#     $ charm = 99
#     j "Test Charm at 99"
#     $ charm = 100
#     j "Test Charm at 100"

#     hide may normal


label intro:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show bg purple
    with fade

    # show keyword just adds the image on top of everything else or swaps out the older version of that image
    # scene keyword removes everything on the screen, then adds the image

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show athena tired1

    # Say statements the format goes like "character" "text they speak"
    "Janice" "I like to eat cherry pits"

    # show multiple people
    show athena tired2
    show chad angry at right  

    # if there is already an image with the same tag e.g, athena, the new image replaces the old one
    # to prevent that from happening we can do "show athena tired1 as athena2 at right"

    # To avoid repeatedly typing character name we can define them with a shortform like "j" and an accent color
    j "Another way for Janice to say I like to eat cherry pits"

    # hide people
    show athena asleep
    hide chad angry

    # add a random pause
    pause 0.5

    # Narrator statements look like this
    "Janice eats a cherry pit"

# label keyword -> dictates the window name
label choices:
    # create a flag to keep track of the decision the user makes
    default flag = False

    # This is how to add a choice
    # choices are introduced with the menu keyword
    menu:
        "Optional dialogue that appears under menu, like: \"Make a choice\""
        "Choice 1":
            jump choice1
            # in order to control the flow of the game, we make the player jump to a certain "label"
        "Choice 2":
            jump choice2
    label choice1:
        "You picked choice 1"
        # update flag
        # dollar sign is a way to signal that the code is python code, basically we are just updating the flag we created in line 61
        $ flag = True
        jump choice_end
    label choice2:
        "You picked choice 2"
        jump choice_end
    
    label choice_end:
        "No matter if you picked 2 or 1 you should see this text"

        # this if statement tests the flag
        if flag:
            "You triggered the flag by picking choice 1, you should see this text if you picked choice 1"

    # This ends the game.
label input:
    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Guy Shy"

    show athena asleep
    j "To display a variable, write it in square brackets. Isn't that right, [name]?"
 
    # you can also create a character with a user given input like so
    define n = Character("[name]")
    n "Now you're speaking"
    return


# use shift-R to reload the game and see ur changes
# use d to make changes right there in the game -> ur changes are saved to the script