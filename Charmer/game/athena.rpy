label athena:
    scene bg hallway
    show screen bars
    play music "athena.mp3" fadein 1.0 volume 0.5 fadeout 1.0

    "There's only one person left."

    "I've been walking over the whole house searching for them - the bedroom's the only place I've yet to look."

    "Someone is definitely here, though. I can hear them..."

    "Humming?"

    scene bg bedroom
    "I gently open the door to my own bedroom and take a look around."

    show athena asleep
    "Oh, there's a girl lying on my bed. I've already met Chad, Ellie, and May. But something's not right."

    mc "Is this... Henry? It's [name]."

    mc "Um, hello."

    athena_unknown "Mmph... No..."

    athena_unknown "Athena... Hello..."

    "It looks like she's totally knocked out. I guess she's just talking in her sleep."

    "I suppose that also means that her name is Athena."

    athena "... Hoot... Outside... Shield..."

    "I try to think back to what Claire has mentioned to me."

    "From what she said, there was supposed to be another guy named Henry here."

    "Did he stand me up?"

    "...Then who is this girl?"
    
    "Whoever she is, it seems like I should be trying not to wake her up."

    "So let's focus on that."

    athena "... Hoot... Hoot..."

    menu:
        "Hoot... Hoot...":

            jump hoot_1

        "Hiss... Hiss...":
            $ athena_approval -= 5
            if athena_approval <= 0:
                jump athena_leaves
            jump hoot_2

        "Hush, hush. I'm here. (-5 Charm)" if charm >= 5:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - 5: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            jump hoot_3

    label hoot_1:
        athena "Mmph..."

        "Seems like that worked."

        jump hoot_merge
        
    label hoot_2:
        show athena tired2
        athena "Eehh..."

        "Seems like she's stirring. I guess that wasn't the right thing to say?"

        jump hoot_merge
        
    label hoot_3:
        athena "Mmph..."

        "Seems like that worked."

        if charm <= 10:
            "I put a lot of CHARM into that, though. Not sure if I can keep this up."

        jump hoot_merge

label hoot_merge:
    show athena asleep
    "This... is certainly a situation."

    athena "Oh... I always did want a dog like this..."

    "I don't even know what to do with her."

    "..."

    "I just remembered that Claire said Henry likes musical theatre, too."

    "That would have been useful information, if he was here."

    "Good place to start a conversation from."

    "I guess I missed that opportunity."

    "At least there's nothing to be nervous about, since Athena doesn't really seem conscious enough to hear me."

    athena "... Do geese see god...?"

    "...Case in point."

    menu:
        "No lemons, no melon...":

            jump geese_1

        "The angels that fall...":
            $ athena_approval -= 5
            if athena_approval <= 0:
                jump athena_leaves
            jump geese_2

        "Good night, good night. (-5 Charm)" if charm >= 5:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - 5: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            jump geese_3

    label geese_1:
        athena "Ohhh..."

        "I guess that was an okay response?"

        "She didn't really move, at least."

        jump geese_merge
        
    label geese_2:
        show athena tired2
        athena "Uuhh..."

        "She twists in the bed, tossing over to her left side, then back."

        "Not what she wanted to hear, I guess."

        jump geese_merge
        
    label geese_3:
        athena "Ohhh..."

        "Worked pretty well."

        if charm <= 10:
            "Still, I think I spent a lot of CHARM on that. I don't think I can do this for long."

        jump geese_merge

label geese_merge:
    show athena asleep
    "It's pretty quiet in here, with nothing going on. I can hear wind rustling the trees outside."

    "Maybe someone could call this peaceful, but I'm starting to feel tense again. If I can't earn her favour, I'll never get any CHARM from her."

    "This isn't really how I wanted the last conversation of tonight to go."

    "I mean, it could always be worse."

    athena "[name]..."

    "!!!"

    "That's my name."

    "Is she awake?"

    "Her eyes are still closed."

    mc "Athena?"

    athena "Mmph..."

    "Back to incoherence, I see. Well, she's listening in there. Somewhere."

    "And anyway, how tired would someone have to be, to fall asleep in another person's bed?"

    "I don't think I've seen anyone else do that."

    "Ever."

    "Maybe I could get her to listen, even if she's not going to wake up."

    "I'm sure a bit of CHARM would get her attention."

    menu:
        "I'm sure a bit of CHARM would get her attention."

        "FIRE! FIRE! THERE'S A FIRE!":
            $ athena_approval -= 15
            if athena_approval <= 0:
                jump athena_leaves
            jump wake_1

        "Hey, listen up... (-10 Charm)" if charm >= 10:
            $ athena_approval -= 5
            if athena_approval <= 0:
                jump athena_leaves
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - 10: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            jump wake_2

        "Oh, you're finally awake... (-10 Charm)" if charm >= 10:
            play sound "audio/charm-sound.wav"
            $ charm_start = charm
            while charm > charm_start - 10: # decrease charm bar
                $ charm -= 1
                pause(0.0001)
            jump wake_3

    label wake_1:
        show athena tired2
        athena "Shhh... I hear you..."

        athena "Don't be so loud..."

        "Chastized by the girl sleeping in my bed."

        "Not even a girl that I invited there."

        "This day gets better and better."

        jump wake_merge
        
    label wake_2:
        show athena tired2
        athena "Uuhh..."

        "She twists in the bed, tossing over to her left side, then back."

        "Not what she wanted to hear, I guess."

        jump wake_merge
        
    label wake_3:
        athena "Ohhh..."

        "Looks like it worked pretty well."

        "I watch as she turns over and goes back to sleep."

        "...Or not."

        jump wake_merge

label wake_merge:
    
    mc "Hmm, I don't think I can make much progress with her in this state."

    mc "I guess I'll head outside for a bit of fresh air."

    jump chmsq


label athena_leaves:

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

    hide athena
    with Dissolve(0.5)

    mc "Well, that's... Unfortunate."

    mc "I guess I'll head outside for a bit of fresh air."

    jump chmsq