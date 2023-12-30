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
            show may smile2
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

    show may surprised
    may_unknown "Wait you play NCat? I've written some of the code on there, I worked as a game developer there for a while."

    if charm >= 10:
        menu:
            "Wait you play NCat? I've written some of the code on there, I worked as a game developer there for a while."
            "Wow, that's impressive! (-10 charm)":
                
                $ charm_start = charm
                while charm > charm_start - 5:
                    $ charm -= 1
                    pause(0.0001)

                $ may_approval -= 0
                show may laugh
                may_unknown "Thank you, thank you!"
            "Oh cool":
                $ may_approval -= 5
                if may_approval <= 0:
                    jump may_leaves
                show may normal
                may_unknown "Thanks"
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

    mc "What about you? How did you and Claire meet?"

    show may smile1
    may "We actually met at a gaming convention a few years back. We bonded over our love for coding and, of course, video games."

    may "When she mentioned that she has a good looking friend looking for a date, I had to come and see them for myself."

    if charm >= 15:
        menu:
            "I think you're the good looking one here (-15 charm)":
                $ charm_start = charm
                while charm > charm_start - 15:
                    $ charm -= 1
                    pause(0.0001)
                show may laugh
                may "I'm flattered."
            "Well, I'm flattered that you took the chance":
                $ may_approval -= 7
                if may_approval <= 0:
                    jump may_leaves
            "I guess I'm glad you did":
                $ may_approval -= 7
                if may_approval <= 0:
                    jump may_leaves
    else:
        menu:
            "Well, I'm flattered that you took the chance":
                $ may_approval -= 7
                if may_approval <= 0:
                    jump may_leaves
            "I guess I'm glad you did":
                $ may_approval -= 7
                if may_approval <= 0:
                    jump may_leaves
    
    mc "So, aside from coding and games, what are your other interests?"

    may "I'm a big fan of swimming. My parents enrolled me in synchronized swimming since I was young."

    may "I don't do as much synchro anymore but I still swim often. It's my go-to way to unwind."

    mc "That sounds wonderful. I've always enjoyed the occasional swim, but I'm not as dedicated as you."

    may "There's a great pool not far from here. It's practically empty Wednesday mornings."

    may "Maybe I could take you there sometime?"

    menu:
        "That sounds amazing.":
            show may smile2
            may "Perfect! It's a date."
        "Maybe, swimming isn't really my thing.":
            $ may_approval -= 7
            if may_approval <= 0:
                jump may_leaves
            show may sweat
            may "Oh maybe we could go on another type of date then."
        "No.":
            $ may_approval -= 10
            if may_approval <= 0:
                jump may_leaves
            show may sweat
            may "Oh that's okay. Maybe we could go on a date someplace else."

    may "Speaking of dates, do you have any ideas on where you'd take me on a date?"

    if charm >= 10:
        menu:
            "Arcade games (-10 charm)":
                $ charm_start = charm
                while charm > charm_start - 10:
                    $ charm -= 1
                    pause(0.0001)
                $ may_approval -= 3
                if may_approval <= 0:
                    jump may_leaves
                show may laugh
                may "I'd love that."
            "Whale-watching":
                show may smile3
                may "No way, how'd you know - I love that."
                may "I love orcas, their coordination and teamwork is really awe-inspiring."

                show may normal
                may "Have you ever gone whale watching before?"
                mc "Not yet, but it's on my bucket list. I imagine it's a breathtaking experience."

                show may smile3
                may "It truly is. We should plan a whale-watching trip together sometime."
                mc "I'd love that, count me in!"
            "Karaoke":
                $ may_approval -= 13
                if may_approval <= 0:
                    jump may_leaves
                show may sweat
                may "Haha, my voice isn't the greatest. Maybe next time!"
    else:
        menu:
            "Whale-watching":
                show may smile3
                may "No way, how'd you know - I would love that."
                may "I love orcas, their coordination and teamwork is really awe-inspiring."

                show may normal
                may "Have you ever gone whale watching before?"
                mc "Not yet, but it's on my bucket list. I imagine it's a breathtaking experience."

                show may smile3
                may "It truly is. We should plan a whale-watching trip together sometime."
                mc "I'd love that, count me in!"
            "Karaoke":
                $ may_approval -= 13
                if may_approval <= 0:
                    jump may_leaves
                show may sweat
                may "Haha, my voice isn't the greatest. Maybe next time!"

    mc "I'm glad we have a lot of exciting plans ahead May."

    may "Likewise! If you ever want to chat more about games or anything else, then hit me up. I'm always up for a good conversation with you."

    jump athena




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
