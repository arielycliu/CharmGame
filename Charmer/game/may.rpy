label may:
    scene bg sittingroom
    play music "may.mp3" fadein 1.0 fadeout 1.0 volume 0.75
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
        "Sure, I'd be down. You'd have to teach me though.":
            show may laugh
            may_unknown "Oh, it's a bit complicated to learn."
            show may smile2
            may_unknown "You should come over to my house and let me explain it sometime."
            mc "Sounds good - I look forward to it."
        "Nah, I'm good.":
            $ may_approval -= 8
            if may_approval <= 0:
                jump may_leaves
            show may sad
            may_unknown "Aww... you're no fun."
    
    show may normal
    may_unknown "Do you play any video games?"

    mc "Not really. Well, I do play a bit of NCat from time to time though."

    show may surprised
    may_unknown "Wait, you play NCat? I've written some of the code for that game! I worked as a game developer there for a while."

    menu:
        "Wait, you play NCat? I've written some of the code for that game! I worked as a game developer there for a while"
        "Wow, that's impressive! (-10 charm)" if charm >= 10:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - 5:
                $ charm -= 1
                pause(0.0001)
            show may laugh
            may_unknown "Thank you, thank you!"
        "Oh, cool.":
            $ may_approval -= 5
            show may normal
            may_unknown "Thanks."
            if may_approval <= 0:
                jump may_leaves
        "I've noticed some bugs in the code...":
            $ may_approval -= 10
            show may sweat
            may_unknown "I'm not responsible for all of the code. In reality, my individual impact was probably pretty small."
            may_unknown "If it was my error that caused your bug, though, then I'm sorry about that."
            if may_approval <= 0:
                jump may_leaves

    show may smile1
    may "My name is May, by the way. How do you know Claire?"

    mc "Oh, haha."
    
    mc "We're childhood friends."
    
    mc "We were in the same class all throughout elementary school, actually."

    show may laugh
    may "Oh, so you've known each other for a long time! Claire's always been a bit of a troublemaker, hasn't she?"

    mc "You don't need to tell me twice. She's always kept things interesting..."

    mc "I'll never forget the time she tried to bury me alive, that's for sure."

    show may surprised
    may "That sounds pretty traumatic."

    mc "Well, you know how it is."

    mc "What about you? How did you and Claire meet?"

    show may smile1
    may "We actually met at a gaming convention a few years back. We bonded over our love for coding and, of course, video games."

    show may smirk
    may "When she mentioned that she has a good-looking friend searching for a date, I had to come and see them for myself."

    menu:
        may "When she mentioned that she has a good-looking friend searching for a date, I had to come and see them for myself."

        "I think you're the good-looking one here. (-15 charm)" if charm >= 15:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - 15:
                $ charm -= 1
                pause(0.0001)
            show may laugh
            may "I'm flattered."

        "Someone sounds a little desperate.":
            $ may_approval -= 10
            show may smile2
            may "..."
            may "Wow okay..."
            if may_approval <= 0:
                jump may_leaves

        "Well I hope you find them.":
            $ may_approval -= 7
            show may normal
            may "..."
            may "Me too."
            if may_approval <= 0:
                jump may_leaves
    
    mc "So, aside from coding and gaming, what are your other interests?"

    show may smile3
    may "I'm a big fan of swimming. My parents enrolled me in synchronized swimming when I was young."

    may "I don't do as much synchro anymore, but I still swim often. It's my go-to way to unwind."

    mc "That sounds wonderful. I've always enjoyed the occasional swim, but I'm not as dedicated as you."

    show may normal
    may "It's never too late to start."

    may "There's a great pool not far from here. It's practically empty Wednesday mornings."

    show may smile1
    may "Maybe I could take you there sometime?"

    menu:
        may "Maybe I could take you there sometime?"
        "That sounds amazing. (-5 charm)" if charm >= 5:
            show may smile2
            may "Perfect! It's a date."

        "Maybe - swimming isn't really my thing.":
            $ may_approval -= 5
            show may sweat
            may "Oh, maybe we could go on another type of date then."
            if may_approval <= 0:
                jump may_leaves
        "No.":
            $ may_approval -= 10
            show may sweat
            may "Oh, that's okay. Maybe we could go on a date someplace else."
            if may_approval <= 0:
                jump may_leaves

    show may smirk
    may "Speaking of dates, do you have any ideas on where you'd take me on a date?"

    menu:
        may "Speaking of dates, do you have any ideas on where you'd take me on a date?"

        "The arcade! (-10 charm)" if charm >= 10:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - 10:
                $ charm -= 1
                pause(0.0001)
            show may laugh
            may "I'd love that."

        "Whale-watching!":
            show may smile3
            may "No way, how'd you know? I would love that."
            may "I adore orcas. Their coordination and teamwork is really awe-inspiring stuff."

            show may normal
            may "Have you ever gone whale watching before?"
            mc "Not yet, but it's on my bucket list. I imagine it's a breathtaking experience."

            show may smile3
            may "It truly is. We should plan a whale-watching trip together sometime."
            mc "I'd love that. Count me in!"

        "Karaoke!":
            $ may_approval -= 13
            show may sweat
            may "Oh..."
            may "Haha, my voice isn't the greatest. Maybe next time!"
            if may_approval <= 0:
                jump may_leaves

    

    mc "I'm glad we have a lot of exciting plans ahead, May."

    may "Likewise! If you ever want to chat more about games or anything else, then hit me up. I'm always up for a good conversation with you."

    jump athena


label may_leaves:
    $ may_approval = 0
    $ may_stayed = False
    scene bg sittingroom
    show may sweat
    may "Uh..."

    show may normal
    may "So uh, I don't like to waste people's time - So I'll just get straight to the point."
    
    show may smile2
    may "I don't think we're going to be a good fit."

    mc "Huh?"

    show may smile1
    may "It just seems like we're looking for different things."

    show may smirk
    may "I wish you all the best. Good luck."

    mc "Oh, oka-"

    hide may smirk
    with Dissolve(0.5)

    "Before I finish saying my goodbyes, she's out the door."

    "Well. Onward, we go."

    hide may smirk

    pause(0.5)
    jump athena
