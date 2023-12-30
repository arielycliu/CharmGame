default FIRST_CHARM_COST = 10

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
        "Yeah but none of them are as thoughtful and observant as you. (-[FIRST_CHARM_COST] Charm)" if charm >= FIRST_CHARM_COST:
            $ charm_start = charm
            while charm > charm_start - FIRST_CHARM_COST: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            jump ellie_question_2
        "Yeah but none of them are as good of a cook as you. (-[FIRST_CHARM_COST] Charm)" if charm >= FIRST_CHARM_COST:
            $ charm_start = charm
            while charm > charm_start - FIRST_CHARM_COST: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            show ellie confused
            ellie "Huh?"
            ellie "I never said anything about being a good cook..."
            jump ellie_fail
        
label ellie_question_2:
    "Good job"
    jump ellie_question_3

label ellie_fail:
    show ellie vneutral
    ellie "Sorry [name], maybe I shouldn't go to the gala with you after all."
    show ellie smug
    ellie "Especially since it seems like we barely know each other..."
    ellie "Thanks for organizing this party and everything though."
    
    hide ellie smug
    with Dissolve(0.5)

    call screen game_over

label ellie_question_3:
    "dsklfj"

    hide ellie smug
    with Dissolve(0.5)

    call screen game_won