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

    ellie "Oh there you are [name]."
    ellie "What happened to the lights just now? That was kinda scary..."

    mc "Must've been a power outage or something."
    mc "Anyway, Ellie, I've been meaning to ask you something."
    mc "There's this big New Year's gala coming up, and I was wondering if... you'd like to be my date?"

    show ellie shy
    ellie "Oh!"
    ellie "I mean-"
    ellie "Are you sure?"
    show ellie sad
    ellie "There were so many other pretty people at the party today, maybe you should go with one of them instead..."

    menu:
        "There were so many other pretty people at the party today, maybe you should go with one of them instead..."
        "Yeah but none of them are as thoughtful and observant as you. (-[CHARM_COST_1] Charm)" if charm >= CHARM_COST_1:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_1: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show ellie shy
            ellie "Aww that's so sweet of you."
            jump ellie_question_2
        "Yeah but none of them are as good of a cook as you. (-[CHARM_COST_1] Charm)" if charm >= CHARM_COST_1:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_1: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show ellie confused
            ellie "Huh?"
            ellie "I never said anything about being a good cook..."
            jump ellie_fail
        "Yeah maybe you're right.":
            jump ellie_fail
        
label ellie_question_2:
    mc "Hey it'll be fun. I'll even buy a plushie for you."
    ellie "You would? What kind of plushie would you buy?"
    menu:
        ellie "You would? What kind of plushie would you buy?"
        "an orca one (-[CHARM_COST_2] Charm)" if charm >= CHARM_COST_2:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_2: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show ellie disappointed
            ellie "An orca...I think they are kind of scary"
            jump ellie_fail
        "a cuttlefish one (-[CHARM_COST_2] Charm)" if charm >= CHARM_COST_2:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_2: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            ellie "Aww... you even remembered my favourite animal."
            jump ellie_question_3
        "a skull design":
            show ellie disappointed
            ellie "A skull huh? That's interesting"
            jump ellie_fail

label ellie_question_3:
    ellie "Am I dreaming? This doesn't feel real."
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
        "haha...just kidding!":
            jump ellie_fail

label ellie_win:
    show ellie happy
    ellie "I'd love to go with you too [name]!"
    hide ellie happy
    with Dissolve(0.5)

    call screen game_won

label ellie_fail:
    show ellie vneutral
    ellie "Sorry [name], maybe I shouldn't go to the gala with you after all."
    show ellie smug
    ellie "Especially since it seems like we barely know each other..."
    ellie "Thanks for organizing this party and everything though."
    
    hide ellie smug
    with Dissolve(0.5)

    call screen game_over

##########################################################################################################################

label chad_question_1:
    scene bg kitchen
    show screen bars
    show chad normal

    chad "Oh hey [name]."
    chad "What happened to the lights just now?"

    mc "Probably just a small power outage, I wouldn't worry about it."
    mc "Anyway, Chad, I've been meaning to ask you something."
    mc "There's this big New Year's gala coming up, and I was wondering if... you'd like to be my date?"

    show chad blush
    chad "Oh!"
    chad "I mean-"

    show chad laugh
    chad "Will there be good food there?"

    mc "Every year there's always a good selection of food."

    menu:
        mc "Every year there's always a good selection of food."
        "But I'm sure nothing could top your sushi. (-[CHARM_COST_1] Charm)" if charm >= CHARM_COST_1:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_1: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show chad normal
            chad "What are you talking about? I've never made you sushi?"
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
            chad "Wow, I didn't expect you to be this kind of person."
            jump chad_fail
        
label chad_question_2:
    show chad smile
    chad "Hmm... I'm interested. Will there be any fun things to do at the party?"

    mc "There'll be all kinds of fun games, I know you like..."

    menu:
        mc "There'll be all kinds of fun games, I know you like..."
        "Never have I ever. (-[CHARM_COST_2] Charm)" if charm >= CHARM_COST_2:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_2: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show chad normal
            chad "Never have I ever mentioned that - I actually don't like that game at all."
            jump chad_fail
        "Truth or Dare. (-[CHARM_COST_2] Charm)" if charm >= CHARM_COST_2:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_2: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            chad "I'm glad you remembered! Sounds like it'll be a fun night."
            jump chad_question_3
        "Shattering wine glasses.":
            show chad angry
            chad "That doesn't sound like my idea of fun at all."
            jump chad_fail

label chad_question_3:
    chad "I'm down to go. What should I wear?"
    menu:
        chad "I'm down to go. What should I wear?"
        "A girl like you would look beautiful in a dress. (-[CHARM_COST_3] Charm)" if charm >= CHARM_COST_3:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_3: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show chad angry
            chad "I'm not a girl, and I don't like the way you said that [name]."
            jump chad_fail
        "I think you'd look so charming in a suit. (-[CHARM_COST_3] Charm)" if charm >= CHARM_COST_3:
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
    chad "Sounds delightful, I'd love to go with you to the party!"
    hide chad delighted
    with Dissolve(0.5)
    call screen game_won

label chad_fail:
    show chad normal
    chad "Sorry [name], maybe I shouldn't go to the gala with you after all."
    show chad annoyed
    chad "Especially since it seems like we barely know each other..."
    hide chad annoyed
    with Dissolve(0.5)
    call screen game_over

##########################################################################################################################

label may_question_1:
    scene bg sittingroom
    show screen bars
    
    show may smile1
    may "It's good to see you [name]."
    show may normal
    may "What happened to the lights just now?"

    mc "Probably just a small power outage, I wouldn't worry about it."
    mc "Anyway, may, I've been meaning to ask you something."
    mc "There's this big New Year's gala coming up, and I was wondering if... you'd like to be my date?"

    show may laugh
    may "Oh!"
    may "I mean-"

    show may laugh
    may "Will there be something fun to do there?"
    mc "Every year they host a bunch of fun competitions."

    mc "This year they're hosting a..."

    menu:
        mc "This year they're hosting a..."
        "gaming competition. (-[CHARM_COST_1] Charm)" if charm >= CHARM_COST_1:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_1: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show may smirk
            may "Ohhh sounds fun, what game?"
            jump may_question_2
        "rowing competition. (-[CHARM_COST_1] Charm)" if charm >= CHARM_COST_1:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_1: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show may normal
            may "That's a shame, I don't really like rowing."
            jump may_fail
        "loser competition - I think you could win.":
            show may sad
            may "Wow, I didn't expect you to be this kind of person."
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
            may "I've never heard of that game. I don't think I'd have fun."
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
            may "That doesn't sound like my idea of fun at all."
            jump may_fail

label may_question_3:
    show may smile2
    may "I'm down to go. Is there anyone I know there?"
    menu:
        may "I'm down to go. Is there anyone I know there?"
        "There's a guy from NCat there. (-[CHARM_COST_3] Charm)" if charm >= CHARM_COST_3:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_3: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show may surprised
            may "Double no way! I'm so excited!"
            jump may_win
        "There's a guy from Tior there. (-[CHARM_COST_3] Charm)" if charm >= CHARM_COST_3:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_3: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show may sweat
            may "I'm confused. Why would I know someone from Tior? They are fierce rivals with NCat."
            jump may_fail
        "No one that you deserve to talk to.":
            jump may_fail

label may_win:
    show may laugh
    may "Okay it's settled, I'd love to go with you to the party!"
    hide may laugh
    with Dissolve(0.5)
    call screen game_won

label may_fail:
    show may normal
    may "Sorry [name], maybe I shouldn't go to the gala with you after all."
    show may angry1
    may "Especially since it seems like we barely know each other..."
    hide may angry1
    with Dissolve(0.5)
    call screen game_over

##########################################################################################################################

label athena_question_1:
    scene bg bedroom
    show screen bars
    
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
        "I'm glad your interested. (-[CHARM_COST_2] Charm)" if charm >= CHARM_COST_2:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_2: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            athena "Melons..."
            jump athena_question_3
        "I'M GLAD YOUR INTERESTED!!! (-[CHARM_COST_2] Charm)" if charm >= CHARM_COST_2:
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
    mc "Okay it's settled, I'm going with you to the party!"
    hide athena
    with Dissolve(0.5)
    call screen game_won

label athena_fail:
    show athena tired2
    athena "mm...m.."

    show athena tired1
    athena "H-hi? Who are you?"

    mc "I'm [name], did Claire send you to my party?"

    show athena tireddark2
    athena "What party? I think there's been some kind of a mistake. I shouldn't be here."

    athena "I'll get going, goodbye..."

    hide athena tireddark2
    with Dissolve(0.5)
    call screen game_over