# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# To avoid repeatedly typing character name we can define them with a shortform like "j" and an accent color
define j = Character("Janice",  color="#c8ffc8")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg purple

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show athena tired1

    # Say statements the format goes like "character" "text they speak"
    "Janice" "I like to eat cherry pits"

    # show multiple people
    show athena tired1
    show athena asleep at right  

    # To avoid repeatedly typing character name we can define them with a shortform like "j" and an accent color
    j "Another way for Janice to say I like to eat cherry pits"

    # hide people
    show athena tired1
    hide athena asleep

    # Narrator statements look like this
    "Janice eats a cherry pit"

    # This ends the game.

    return
