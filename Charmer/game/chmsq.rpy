default chosen_one = "May"
default choices = ["Ellie", "Chad", "May", "Athena"]

init python:
    def generate_choices(ellie_stayed, chad_stayed, may_stayed, athena_stayed):
        choices = ["Ellie", "Chad", "May", "Athena"]
        if ellie_stayed == False:
            choices.remove("Ellie")
        if chad_stayed == False:
            choices.remove("Chad")
        if may_stayed == False:
            choices.remove("May")
        if athena_stayed == False:
            choices.remove("Athena")
        return choices

label chmsq:
    scene bg outside

    $ choices = generate_choices(ellie_stayed, chad_stayed, may_stayed, athena_stayed)
    $ choice_len = len(choices)

    if choice_len == 0:
        mc "Well that went a lot worse than I expected."
        mc "Looks like there I'll have to go to the party alone again this year."
        call screen game_over
        return
    elif choice_len == 1:
        mc "Well that went about as well as I expected."
        mc "I guess I'll try and get [choices[0]] to go with me."
        $ chosen_one = choices[0]
    else:
        mc "Well that went better than I expected."
        mc "I can only take one of them as my date though."

        "Who should I take?"
        call screen choseone
        $ chosen_one = _return
        "[chosen_one]"


label chmsq_start:
    scene bg outside night
    show screen bars
    "Time flies, it's already nighttime"

    "I guess it's time to wrap this party up..."

    scene bg hallway night
    "I head back inside and lock the door behind me"

    "I walk up to the breaker, and switch off all of the power."

    if chosen_one != "Ellie" and ellie_stayed == True:
        jump ellie_charm
    elif chosen_one != "Chad" and chad_stayed == True:
        jump chad_charm
    elif chosen_one != "May" and may_stayed == True:
        jump may_charm
    elif chosen_one != "Athena" and athena_stayed == True:
        jump athena_charm
    else:
        jump after_charm
 
#################################################################################################################

label ellie_charm:
    show ellie angry
    show screen bars
    ellie "[name] why is it so dark in here? Could you turn on the lights?"

    mc "Um... give me a second"

    show ellie veryangry
    ellie "What's taking so long!"

    mc "Just a second..."

    ellie "Why are you grabbing my arm?"

    mc "I'm a bit scared of the dark"

    ellie "[name], my arm is starting to feel kinda weird"

    mc "Good"

    $ frame_count = 64
    $ frame_number = 1
    $ image_prefix = "images/Transitions/smoke/Angry_Smoke_Circle_Burst_White_v1_A__"

    hide ellie veryangry

    label smoke_start:           
        if frame_number > frame_count:
            hide image_path
            jump smoke_end
        $ image_path = image_prefix + str(frame_number) + ".png"
        show image image_path:
            xpos 400 ypos 0
        $ frame_number += 1
        pause 0.002
        jump smoke_start
    label smoke_end:
        scene bg hallway night
        pause(0.2)

        scene bg black
        with Dissolve(0.5)

        $ charm_start = charm
        while charm < charm_start + 25:
            $ charm += 1
            pause(0.0001)

        if 0 <= charm < 25: 
            show charms0
        elif 25 <= charm < 50: 
            show charms1
        elif 50 <= charm < 75: 
            show charms2
        elif 75 <= charm < 100: 
            show charms3
        else: 
            show charms4
        "You earned 25 charm points from Ellie's soul"

        if chosen_one != "Chad" and chad_stayed == True:
            jump chad_charm
        elif chosen_one != "May" and may_stayed == True:
            jump may_charm
        elif chosen_one != "Athena" and athena_stayed == True:
            jump athena_charm
        else:
            jump after_charm

#################################################################################################################

label chad_charm:
    scene bg kitchen night
    with fade

    show screen bars
    show chad annoyed
    chad "Yo, [name] why'd you turn all the lights off?"

    mc "..."

    mc "To suck your soul"

    show chad laugh
    chad "What are you talking about?"

    mc "Stay still..."

    show chad blush
    chad "Why are you touching my chest? If you wanted to compare pects you coulda just asked!"

    show chad sleepy
    chad "Whoa, I feel like I have no strength all of a sudden..."

    $ frame_count = 64
    $ frame_number = 1
    $ image_prefix = "images/Transitions/smoke/Angry_Smoke_Circle_Burst_White_v1_A__"

    hide chad sleepy

    label smoke_start1:           
        if frame_number > frame_count:
            hide image_path
            jump smoke_end1
        $ image_path = image_prefix + str(frame_number) + ".png"
        show image image_path:
            xpos 400 ypos 0
        $ frame_number += 1
        pause 0.002
        jump smoke_start1
    label smoke_end1:
        scene bg kitchen night
        pause(0.2)

        scene bg black
        with Dissolve(0.5)

        $ charm_start = charm
        while charm < charm_start + 25:
            $ charm += 1
            pause(0.0001)

        if 0 <= charm < 25: 
            show charms0
        elif 25 <= charm < 50: 
            show charms1
        elif 50 <= charm < 75: 
            show charms2
        elif 75 <= charm < 100: 
            show charms3
        else: 
            show charms4
        "You earned 25 charm points from Chad's soul"

        if chosen_one != "May" and may_stayed == True:
            jump may_charm
        elif chosen_one != "Athena" and athena_stayed == True:
            jump athena_charm
        else:
            jump after_charm

#################################################################################################################

label may_charm:
    scene bg sittingroom night
    with fade

    show screen bars
    show may normal
    may "Hey [name], where did everyone go?"

    mc "Into my charm bracelet"

    show may laugh
    may "Your sense of humour is truly weird"

    show may normal
    may "I guess everyone else left so I'll be direct. Wanna go to the New Year's party as a couple?"

    mc "Sorry May, but I've got someone else in mind already"

    show may sweat
    may "No way, is it Ellie? Well let me know if you ever need any help - bro code and all"

    mc "May, I know you're a girl"

    show may smile1
    may "Oh come on, bro is a gender neutral term"

    mc "Sorry again, May but I need your help in another way"

    show may surprised
    may "Why are you touching m-"

    $ frame_count = 64
    $ frame_number = 1
    $ image_prefix = "images/Transitions/smoke/Angry_Smoke_Circle_Burst_White_v1_A__"

    hide may suprised

    label smoke_start2:           
        if frame_number > frame_count:
            hide image_path
            jump smoke_end2
        $ image_path = image_prefix + str(frame_number) + ".png"
        show image image_path:
            xpos 400 ypos 0
        $ frame_number += 1
        pause 0.002
        jump smoke_start2
    label smoke_end2:
        scene bg sittingroom night
        pause(0.2)

        scene bg black
        with Dissolve(0.5)

        $ charm_start = charm
        while charm < charm_start + 25:
            $ charm += 1
            pause(0.0001)

        if 0 <= charm < 25: 
            show charms0
        elif 25 <= charm < 50: 
            show charms1
        elif 50 <= charm < 75: 
            show charms2
        elif 75 <= charm < 100: 
            show charms3
        else: 
            show charms4
        "You earned 25 charm points from May's soul"

        if chosen_one != "Athena" and athena_stayed == True:
            jump athena_charm
        else:
            jump after_charm

#################################################################################################################

label athena_charm:
    scene bg bedroom night
    with fade

    show screen bars
    "You tiptoe into the upstairs bedroom"

    "You hear the sound of light snoring"

    show athena asleep
    mc "I guess that makes things easier..."

    $ frame_count = 64
    $ frame_number = 1
    $ image_prefix = "images/Transitions/smoke/Angry_Smoke_Circle_Burst_White_v1_A__"

    hide athena asleep

    label smoke_start3:           
        if frame_number > frame_count:
            hide image_path
            jump smoke_end3
        $ image_path = image_prefix + str(frame_number) + ".png"
        show image image_path:
            xpos 400 ypos 0
        $ frame_number += 1
        pause 0.002
        jump smoke_start3
    label smoke_end3:
        scene bg bedroom night
        pause(0.2)

        scene bg black
        with Dissolve(0.5)

        $ charm_start = charm
        while charm < charm_start + 25:
            $ charm += 1
            pause(0.0001)

        if 0 <= charm < 25: 
            show charms0
        elif 25 <= charm < 50: 
            show charms1
        elif 50 <= charm < 75: 
            show charms2
        elif 75 <= charm < 100: 
            show charms3
        else: 
            show charms4
        "You earned 25 charm points from Athena's soul"
        jump after_charm

#################################################################################################################

label after_charm:
    scene bg hallway night
    show screen bars
    mc "Great, now I have [charm] charm points"

    mc "I hope I have enough to woo [chosen_one]"

    mc "Sigh* I should stop being spooky and turn the lights back on now"
