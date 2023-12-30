label may:
    scene bg sittingroom
    "My legs are starting to feel tired after all this standing around and socializing."

    "Maybe I should sit down for a while on the couch."

    "I head to the living room, only to find someone already there."

    "It looks like they're playing some game on a console."

    "I plop down on the couch beside them."

    mc "What are you playing?"

    show may surprised
    may_unknown "It's a game called OLO. Do you want to play?"

    menu:
        may_unknown "It's a game called OLO. Do you want to play?"
        "Sure I'm down. You'd have to teach me though.":
            show may laugh
            may_unknown "Oh, it's a bit complicated to learn."
            show may smile
            may_unknown "You should come over to my house and I could teach you."
            mc "Sounds good, I look forward to it."
        "Nah I'm good.":
            $ may_approval -= 8
            if may_approval <= 0:
                jump may_leaves
            show may sad
            may_unknown "Aww... you're no fun."
    
    show may normal
    may_unknown "Do you play any video games?"

    mc "Not really, I play a bit of NCat from time to time though."

    show may suprised
    may_unknown "Wait you play NCat? I've written some of the code on there, I worked as a game developer there for a while."

    if charm >= 10:
        menu:
            "Wait you play NCat? I've written some of the code on there, I worked as a game developer there for a while."
            "Wow, that's impressive! (-10 charm)":
                $ may_approval -= 0
                show may laugh
                may_unknown "Thank you, thank you!"
            "Oh cool":
                $ may_approval -= 5
                if may_approval <= 0:
                    jump may_leaves
                show may normal
                may_unknown "..."
            "I've noticed some bugs in the code...":
                $ may_approval -= 10
                if may_approval <= 0:
                    jump may_leaves
                show may sweat
                may_unknown "I'm not responsible for all of the code, in reality my impact was pretty small."
                may_unknown "If it was my error that caused your bug then I'm sorry about that."
    else:
        menu:
            "Wait you play NCat? I've written some of the code on there, I worked as a game developer there for a while."
            "Oh cool":
                $ may_approval -= 5
                if may_approval <= 0:
                    jump may_leaves
                show may normal
                may_unknown "..."
            "I've noticed some bugs in the code...":
                $ may_approval -= 10
                if may_approval <= 0:
                    jump may_leaves
                show may sweat
                may_unknown "I'm not responsible for all of the code, in reality my impact was pretty small."
                may_unknown "If it was my error that caused your bug then I'm sorry about that."
    
    show may smile1
    may "My name is May by the way, how do you know Claire?"

    mc "Oh we're childhood friends, we were in the same class throughout elementary school."

    show may laugh
    may "Ah, so you've known each other for a long time. Claire's always been a bit of a troublemaker, hasn't she?"

    mc "You don't need to tell me twice. She's always kept things interesting...like that time she smothered glue all over my chair..."

    show may surprised
    may "That sounds pretty traumatic."



label may_leaves:
    scene bg sittingroom
    show may sweat
    may "Uh..."

    show may normal
    may "I'm sorry to say this but I don't want to waste your time..."
    
    show may smile2
    may "I don't think we're going to be a good fit."

    show may smile1
    may "I think we're looking for different things."

    show may smirk
    may "I wish you all the best. Good luck."

    hide may smirk

    pause(0.5)
    jump athena
