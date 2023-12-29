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

    show claire smile2: 
        zoom 0.75
        xpos 0.20
    claire "It's me!"

    show claire smile: 
        zoom 0.75
        xpos 0.20
    "Claire gives me a little jazz-hand wave. She's been helping me with the preparations for this party, but to be honest, I thought she'd gone home already."

    "I guess I've been a little zoned out, worrying about this."

    show claire delighted: 
        zoom 0.75
        xpos 0.20
    claire "You've done a good job setting all this up, [name]. Now let's hope that it pays off."

    mc "Yeah, let's hope so. I can't show up to the New Year's Gala without a date. The others would..."

    show claire sad: 
        zoom 0.75
        xpos 0.20
    claire "Hey, look, don't worry about that now. You've got four people right over there, just waiting to get to know you."

    jump character_intros

