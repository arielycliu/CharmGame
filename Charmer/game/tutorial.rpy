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

    show claire smile
    claire "It's me!"

    show claire smile
    "Claire gives me a little jazz-hand wave. She's been helping me with the preparations for this party, but to be honest, I thought she'd gone home already."

    "I guess I've been a little zoned out, worrying about this."

    show claire delighted
    claire "You've done a good job setting all this up, [name]. Now let's hope that it pays off."

    mc "Yeah, let's hope so. I can't show up to the New Year's Gala without a date. The others would..."

    show claire normal
    claire "Hey, look, don't worry about that now. You've got four people right over there, just waiting to get to know you."

    show claire annoyed
    claire "You've got a good chance here. Don't blow it by worrying."

    show claire normal
    claire "Have you hosted anything like this before?"

    menu:
        "Have you hosted anything like this before?"
        "Yep, I know what to do!":
            jump yesknow
            # in order to control the flow of the game, we make the player jump to a certain "label"
        "Not really - have you?":
            jump noidea
    label yesknow:
        show claire delighted2
        claire "Wow, just rearing to go, huh? Well, don't let me stop you then."
        
        show claire delighted
        claire "Remember to save your charm for when you really need it, and have fun out there!"
        
        jump claire_leave
    label noidea:
        show claire delighted2
        claire "Yeah, loads of times!"

        show claire delighted
        claire "Ah, well, it's pretty simple, really."

        claire "Everyone here's looking to find a date before the New Year's Gala, right? And that could be you!"

        show claire delighted2
        claire "So all you've got to do is sweet talk them until they're fighting over you!"

        claire "Haha, only kidding. But I have faith in you, [name]."

        show claire smile
        claire "It's kind of like a bunch of job interviews all at once, if it helps you to think of it that way."

        claire "The really important thing to do here is to make sure that you use your CHARM wisely."

        label charme:
        show screen bars
        
        $ charme = 0
        "I take a look at the top left corner of my screen. I guess she's talking about that magenta bar."

        claire "Yep, that's the one!"

        claire "It's hard work, party hosting, especially if you're trying to get all these people to like you enough to go on a date with you, so you'll want to conserve your energy for when you really need it."

        show claire smile2
        claire "You don't want to run out of CHARM at a pivotal moment, after all."

        show claire smile
        claire "So sometimes, you might want to just make decisions that aren't as CHARMing, rather than ones that endear you to people."

        mc "Yeah, like you're one to talk. I've never seen you scrape the bottom of your CHARM limit, Claire."

        show claire annoyed
        claire "Yeah, and what's that supposed to mean? I'm just more naturally chatty."

        "That's not the problem at all…"

        show claire smile2
        claire "And that's okay! We can't all be performing all the time."

        show claire smile
        claire "You just have to keep them invested."

        jump claire_leave
    
    label claire_leave:
        show claire delighted
        claire "I'll leave you alone to go hit up your targets, then, [name]."

        show claire delighted2
        claire "Best of luck!"

    jump character_intros

