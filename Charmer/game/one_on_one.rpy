default CHARM_COST_1 = 10
default CHARM_COST_2 = 20
default CHARM_COST_3 = 30

label one_on_one:
    scene bg hallway
    show screen bars
    
    mc "Alright then, time to find-"

    if chosen_one == "Chad":
        jump chad_question_1
    elif chosen_one == "Ellie":
        jump ellie_question_1
    elif chosen_one == "May":
        jump may_question_1
    elif chosen_one == "Athena":
        jump athena_question_1

##################################################################################################

label ellie_question_1:
    scene bg hallway
    show screen bars
    show ellie happy
    play music "ellie.mp3" fadein 1.0

    ellie "Oh, there you are, [name]."

    show ellie vneutral
    ellie "What happened to the lights just now? That was sort of scary..."

    mc "Must've been a power outage or something."
    mc "It's okay. You don't need to worry about that."
    mc "At any rate, it's fixed now."

    show ellie neutral
    mc "Anyway, Ellie, I've been meaning to ask you something."
    mc "There's this big New Year's gala coming up that I have to attend, and I was wondering if..."
    mc "You'd like to be my date?"

    show ellie shy
    ellie "Oh!"
    ellie "I mean-"
    ellie "Are you sure?"
    show ellie vneutral
    ellie "There were so many other lovely people at the party today."
    ellie "Don't you want to go with one of them, instead?"

    show ellie neutral
    ellie "Of course I want to go with you."
    ellie "But I don't want you to make a decision you'll regret, and I don't know if I'm the best person to go with you."

    menu:
        ellie "But I don't want you to make a decision you'll regret, and I don't know if I'm the best person to go with you."

        "Yeah, but none of them are as thoughtful and observant as you. (-[CHARM_COST_1] Charm)" if charm >= CHARM_COST_1:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_1: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show ellie shy
            ellie "Oh..."
            ellie "That's so sweet of you."
            jump ellie_question_2
        "Yeah, but none of them are as good of a cook as you. (-[CHARM_COST_1] Charm)" if charm >= CHARM_COST_1:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_1: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show ellie confused
            ellie "Huh?"
            ellie "I never said anything about being a good cook..."
            jump ellie_fail
        "Yeah, maybe you're right.":
            jump ellie_fail
        
label ellie_question_2:
    mc "Of course."
    mc "I can promise it'll be good fun."
    mc "And I hope it's not an imposition, but I even have a dress in mind for you."

    show ellie delighted
    ellie "You do?"
    ellie "I can't believe you thought this through so much."

    show ellie shy
    ellie "That'd be incredible, if it doesn't mean you're spending too much on me. I couldn't have that."

    ellie "What kind of dress are you thinking of?"
    menu:
        ellie "What kind of dress are you thinking of?"

        "One that looks like an orca. (-[CHARM_COST_2] Charm)" if charm >= CHARM_COST_2:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_2: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show ellie disappointed
            ellie "An orca..."
            ellie "I think they're kind of scary, actually."
            jump ellie_fail
        "One that looks like a cuttlefish. (-[CHARM_COST_2] Charm)" if charm >= CHARM_COST_2:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_2: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            
            show ellie happy
            ellie "Aww..."
            ellie "You even remembered my favourite animal."
            jump ellie_question_3
        "A hot pink pantsuit.":
            show ellie disappointed
            ellie "A skull, huh?"

            show ellie confused
            ellie "Sorry to say this, but I just wanted to let you know..."
            ellie "I'm not sure a pantsuit is a dress, actually."
            jump ellie_fail

label ellie_question_3:
    show ellie shy
    ellie "Am I dreaming? This doesn't feel real."

    ellie "I've never been to a big party before."

    ellie "Much less a gala."

    mc "I promise you it is..."

    menu:
        mc "I promise you it is..."

        "I'd love to go with you, Ellie. (-[CHARM_COST_3] Charm)" if charm >= CHARM_COST_3:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_3: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            jump ellie_win
        "I'd love to go with you, Eleanor. (-[CHARM_COST_3] Charm)" if charm >= CHARM_COST_3:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_3: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            jump ellie_fail
        "Haha... Only kidding! I've been kicked out of all the local galas.'":
            ellie "That wasn't such a nice prank to pull [name]."
            mc "Sorry, I though you'd find it funny."
            jump ellie_fail

label ellie_win:
    show ellie happy
    ellie "I'd love to go with you too, [name]!"
    ellie ""
    ellie "Let's have "
    hide ellie happy
    with Dissolve(0.5)
    $ charm = 0
    hide screen bars
    call screen game_won

label ellie_fail:
    show ellie vneutral
    ellie "Sorry [name], maybe I shouldn't go to the gala with you after all."
    show ellie smug
    ellie "Especially since it seems like we barely know each other..."
    ellie "Thanks for organizing this party and everything, though."
    
    hide ellie smug
    with Dissolve(0.5)
    $ charm = 0
    hide screen bars
    call screen game_over

##########################################################################################################################

label chad_question_1:
    scene bg kitchen
    show screen bars
    show chad normal

    play music "<loop 1.564>chad.mp3" fadein 1.0

    chad "Oh, hey, [name]."
    chad "What happened to the lights just now?"

    mc "Must've been a power outage or something."
    mc "Pretty weird. That never really happens."
    mc "At any rate, it's fixed now."

    mc "Anyway, Chad, I've been meaning to ask you something."
    mc "There's this big New Year's gala coming up that I have to attend, and I was wondering if..."
    mc "You'd like to be my date?"

    show chad blush
    chad "Oh!"
    chad "I mean-"

    show chad laugh
    chad "Will there be good food there?"
    chad "Good food and good company's all I need for a lovely night."

    mc "Every year, there's always a wonderful selection of food."

    menu:
        mc "Every year, there's always a wonderful selection of food."
        "But I'm sure nothing could top your sushi. (-[CHARM_COST_1] Charm)" if charm >= CHARM_COST_1:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_1: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show chad normal
            chad "Huh?"
            chad "What are you talking about? I've never made you sushi."
            jump chad_fail
        "But I'm sure nothing could top your pasta dish. (-[CHARM_COST_1] Charm)" if charm >= CHARM_COST_1:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_1: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show chad delighted
            chad "I'm glad you think so highly of my cooking."
            jump chad_question_2
        "It's bound to be better than your cooking.":
            show chad normal
            chad "That's..."
            chad "Wow."
            chad "I didn't expect you to be that kind of person."
            jump chad_fail
        
label chad_question_2:
    show chad smile
    chad "Well, consider me interested. Will there be any fun things to do at the party?"

    mc "There'll be all kinds of fun games!"
    
    mc "I know you like..."

    menu:
        mc "I know you like..."
        "Never have I ever. (-[CHARM_COST_2] Charm)" if charm >= CHARM_COST_2:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_2: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show chad normal
            chad "Never have I ever mentioned that - I actually don't like that game at all."
            chad "It's pretty boring, to be honest."
            jump chad_fail
        "Truth or dare. (-[CHARM_COST_2] Charm)" if charm >= CHARM_COST_2:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_2: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            chad "Heck yeah, I do! Sounds like it'll be a fun night."
            jump chad_question_3
        "Shattering wine glasses.":
            show chad angry
            chad "What is that supposed to mean?"
            chad "That doesn't sound like my idea of fun at all."
            jump chad_fail

label chad_question_3:
    chad "I'm down to go."
    
    chad "On such short notice, though..."
    chad "What should I wear?"

    menu:
        chad "What should I wear?"
        "A girl like you would look beautiful in a dress. (-[CHARM_COST_3] Charm)" if charm >= CHARM_COST_3:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_3: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show chad angry
            chad "I'm."
            chad "Not."
            chad "A." 
            chad "Girl."
            chad "And I don't like the way you said that, [name]."
            jump chad_fail
        "I think you'd look charming in a suit. (-[CHARM_COST_3] Charm)" if charm >= CHARM_COST_3:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_3: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            jump chad_win
        "How about nothing?":
            jump chad_fail

label chad_win:
    show chad delighted
    chad "Keep it simple. Makes sense."
    
    chad "That sounds delightful. I'd love to go with you to the party!"
    hide chad delighted
    with Dissolve(0.5)
    $ charm = 0
    hide screen bars
    call screen game_won

label chad_fail:
    show chad normal
    chad "Sorry [name], maybe I shouldn't go to the gala with you after all."
    show chad annoyed
    chad "Especially since it seems like we barely know each other..."
    hide chad annoyed
    with Dissolve(0.5)
    $ charm = 0
    hide screen bars
    call screen game_over

##########################################################################################################################

label may_question_1:
    scene bg sittingroom
    show screen bars

    play music "may.mp3" fadein 1.0 volume 0.75
    
    show may smile1
    may "It's good to see you, [name]."
    show may normal
    may "What happened to the lights just now?"

    mc "Must've been a power outage or something."
    mc "It's okay. It's not really a big deal."
    mc "At any rate, it's fixed now."

    mc "Anyway, May, I've been meaning to ask you something."
    mc "There's this big New Year's gala coming up that I have to attend, and I was wondering if..."
    mc "You'd like to be my date?"

    show may laugh
    may "Oh!"
    may "I mean-"

    show may laugh
    may "I can get pretty busy around this time of year, but I'd be interested."
    may "Will there be something fun to do there?"

    mc "Of course. Every year, they host a bunch of cool competitions."

    mc "This year, they're hosting a..."

    menu:
        mc "This year, they're hosting a..."
        "gaming competition. (-[CHARM_COST_1] Charm)" if charm >= CHARM_COST_1:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_1: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show may smirk
            may "Oh, now that sounds like fun."
            
            may "What game?"
            jump may_question_2
        "rowing competition. (-[CHARM_COST_1] Charm)" if charm >= CHARM_COST_1:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_1: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show may normal
            may "That's a shame. I don't really like rowing."
            jump may_fail
        "loser competition - I think you could win.":
            show may sad
            may "Wow, [name], I didn't expect you to be that kind of person."
            jump may_fail
        
label may_question_2:
    show may smirk
    mc "I heard that they're playing..."
    menu:
        mc "I heard that they're playing..."
        "LOL. (-[CHARM_COST_2] Charm)" if charm >= CHARM_COST_2:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_2: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show may sweat
            may "I've never heard of that game."
            
            may "If it's a competition, I don't think I'd have much fun."
            jump may_fail
        "OLO. (-[CHARM_COST_2] Charm)" if charm >= CHARM_COST_2:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_2: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show may surprised
            may "No way!"
            jump may_question_3
        "people like you - haha.":
            show may angry1
            may "Very funny."

            may "That doesn't sound like my idea of fun at all."
            jump may_fail

label may_question_3:
    show may smile2
    may "Okay, I'm down to go. Is there anyone I know there?"
    menu:
        may "I'm down to go. Is there anyone I know there?"
        "There's a guy from NCat there. (-[CHARM_COST_3] Charm)" if charm >= CHARM_COST_3:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_3: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show may surprised
            may "Double no way!"

            show may smile3
            may "I'm so excited!"
            jump may_win
        "There's a guy from Tior there. (-[CHARM_COST_3] Charm)" if charm >= CHARM_COST_3:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_3: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show may sweat
            may "I'm confused. Why would I know someone from Tior? They've got a pretty fierce rivalry going with NCat."
            jump may_fail
        "No one that you deserve to talk to.":
            may "Ugh, what is that supposed to mean?"

            jump may_fail

label may_win:
    show may laugh
    may "Okay, it's settled, then."
    
    may "I'd love to go with you to the party!"
    hide may laugh
    with Dissolve(0.5)
    $ charm = 0
    hide screen bars
    call screen game_won

label may_fail:
    show may normal
    may "Sorry [name], maybe I shouldn't go to the gala with you after all."
    show may angry1
    may "Especially since it seems like we barely know each other..."
    hide may angry1
    with Dissolve(0.5)
    $ charm = 0
    hide screen bars
    call screen game_over

##########################################################################################################################

label athena_question_1:
    scene bg bedroom
    show screen bars

    play music "athena.mp3" fadein 1.0 volume 0.5
    
    show athena asleep
    
    "Looks like she's still asleep..."

    "I guess I'll just ask her directly."
    mc "Would you like to..."
    menu:
        mc "Would you like to..."
        "GO TO THE PARTY WITH ME!!! (-[CHARM_COST_1] Charm)" if charm >= CHARM_COST_1:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_1: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            jump athena_fail
        "go to the party with me. (-[CHARM_COST_1] Charm)" if charm >= CHARM_COST_1:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_1: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            athena "Mmm...mm."
            jump athena_question_2
        "DIE IN A HOLEEEEE.":
            jump athena_fail
        
label athena_question_2:
    show athena asleep
    menu:
        "I'm glad you're interested. (-[CHARM_COST_2] Charm)" if charm >= CHARM_COST_2:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_2: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            athena "Melons..."
            jump athena_question_3
        "I'M GLAD YOU'RE INTERESTED!!! (-[CHARM_COST_2] Charm)" if charm >= CHARM_COST_2:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_2: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            jump athena_fail
        "WAKE UP TO REALITY!":
            jump athena_fail

label athena_question_3:
    show athena asleep
    mc "Great, I'll see you there at..."
    menu:
        mc "Great, I'll see you there at..."
        "FIVE!!!! (-[CHARM_COST_3] Charm)" if charm >= CHARM_COST_3:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_3: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            jump athena_fail
        "five. (-[CHARM_COST_3] Charm)" if charm >= CHARM_COST_3:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_3: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            athena "...[name]...party..."
            jump athena_win
        "WHY AM I TALKING TO YOU?!?":
            jump athena_fail

label athena_win:
    mc "Okay, it's settled."

    show athena tired2
    athena "Hmm...?"

    mc "I'm going with you to the party!"

    show athena tired1
    athena "Oh-!"

    hide athena
    with Dissolve(0.5)
    $ charm = 0
    hide screen bars
    call screen game_won

label athena_fail:
    show athena tireddark2
    athena "Eeuu..."

    show athena tireddark1
    athena "...Hi? Who are you?"

    mc "I'm [name]."
    mc "You're, um."
    mc "In my bed."
    mc "Did Claire send you to my party?"

    show athena tireddark2
    athena "Huh? I don't..."
    athena "I don't know a Claire."

    show athena tireddark1
    athena "I don't even know where I am."

    show athena tireddark2
    athena "I think there's been some kind of a mistake."
    athena "I shouldn't be here."

    show athena tireddark1
    athena "I'm sorry to have bothered you."

    hide athena tireddark1
    with Dissolve(0.5)
    $ charm = 0
    hide screen bars
    call screen game_over