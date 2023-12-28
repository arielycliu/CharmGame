label tutorial:
    scene bg livingroom

    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Undisclosed name"

    define mc = Character("[name]", color="#4378a9")
    
    claire_unknown "Hey! You!"

    "I scan my surroundings, but there's no one out here except the party attendees, already gathered in a circle by the snack table."

    "In the distance, an owl hoots."

    claire_unknown "Over here!"

    "I look around, but there doesn't seem to be anyone here."

    claire_unknown "Boo!"

    "I turn around."

    show chad laugh
    claire "It's me!"

    show chad delighted
    "Claire gives me a little jazz-hand wave. She's been helping me with the preparations for this party, but to be honest, I thought she'd gone home already."

    "I guess I've been a little zoned out, worrying about this."

    show chad normal
    claire "You've done a good job setting all this up, [name]. Now let's hope that it pays off."

    mc "Yeah, let's hope so. I can't show up to the New Year's Gala without a date. The others would..."

    show chad sad
    claire "Hey, look, don't worry about that now. You've got four people right over there, just waiting to get to know you."