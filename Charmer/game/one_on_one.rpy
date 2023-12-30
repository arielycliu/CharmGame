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


label ellie_question_1:
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
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_1: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show ellie shy
            ellie "Aww that's so sweet of you."
            jump ellie_question_2
        "Yeah but none of them are as good of a cook as you. (-[CHARM_COST_1] Charm)" if charm >= CHARM_COST_1:
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
    menu:
        "question 2"
        "something orca (-[CHARM_COST_2] Charm)" if charm >= CHARM_COST_2:
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_2: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            jump ellie_fail
        "something cuttlefish (-[CHARM_COST_2] Charm)" if charm >= CHARM_COST_2:
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_2: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            jump ellie_question_3
        "fail":
            jump ellie_fail

label ellie_question_3:
    menu:
        "question 3"
        "I'd love to go with you, Ellie. (-[CHARM_COST_3] Charm)" if charm >= CHARM_COST_3:
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_3: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            jump ellie_win
        "I'd love to go with you, Eleanor. (-[CHARM_COST_3] Charm)" if charm >= CHARM_COST_3:
            $ charm_start = charm
            while charm > charm_start - CHARM_COST_3: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            jump ellie_fail
        "fail":
            jump ellie_fail

label ellie_win:
    show ellie happy
    ellie "win"
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