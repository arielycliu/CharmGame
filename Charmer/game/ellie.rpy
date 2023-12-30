label ellie:
    scene bg hallway
    show screen bars
    play music "ellie.mp3" fadein 0.25 fadeout 1.0
    
    "I slip into the hallway to take a moment to gather myself. Claire was right - these conversations do take up a lot of energy. I've only just gotten started, though, so I can't afford to take a break now."

    "I already caught loads of flak from the head succubus at last year's gala."

    "\"So many desperate people in th\' world, an\' y\' still ain\'t got a date? It\'s like y\' ain\'t even tryin\', darlin\'.\""

    "The memory makes me wince, and I huff with frustration. This year, I'll prove them wrong. I'm sure of it."

    ellie_unknown "Are you okay?"

    show ellie vneutral
    "A girl is standing in front of me. How did I miss her?"

    "She looks like she's waiting for me to say something."

    mc "Huh? Yeah, I'm fine."

    "I put on my shiniest smile."

    mc "Sorry about that. Eleanor, right?"

    show ellie abashed
    ellie "Please, call me Ellie. Only my parents call me Eleanor."

    menu:
        "Eleanor's such a lovely name, though. (-10 Charm)" if charm >= 10:
            $ ellie_approval -= 10
            play sound "audio/charm-sound.wav"
            $ charm_start = charm

            while charm > charm_start - 10:
                $ charm -= 1
                pause(0.0001)

            if ellie_approval <= 0:
                jump ellie_leaves

            jump ellie_1

        "Got it. It's nice to meet you, Ellie. (-5 Charm)" if charm >= 5:
            jump ellie_2

        "Um, hello, Ellie.":
            $ ellie_approval -= 5
            if ellie_approval <= 0:
                jump ellie_leaves
            jump ellie_3

    label ellie_1:
        show ellie sad
        ellie "It might be, but it doesn't really feel like it fits me."

        ellie "Plus, none of my friends call me that."

        show ellie vneutral
        ellie "So seriously, please, I'd rather you call me Ellie."

        "She looks pretty uncomfortable. Maybe I shouldn't have brought it up."

        jump ellie_merge
        
    label ellie_2:
        show ellie happy
        ellie "Nice to meet you, too, [name]. Claire's said some really nice things about you, haha."

        mc "Yeah, I've heard."

        jump ellie_merge
        
    label ellie_3:
        show ellie neutral
        ellie "Er, hi."

        mc "Hello."

        show ellie confused
        ellie "Hi."

        mc "Hey."

        ellie "...Okay, then."

        jump ellie_merge

        
label ellie_merge:
    mc "So, why are you hanging about in the hallway, Ellie? I don't have anything interesting out here."

    show ellie abashed
    ellie "I guess not. But I sort of just wanted to know what kind of person [name] was."
    
    show ellie neutral
    ellie "I think you can learn a lot about a person from their belongings, even if they're boring."

    ellie "Like this. For example, if I just take a look at this..."

    "She swipes a dark green book from my console table and holds it up to the light."

    show ellie happy
    ellie "I can learn that you're a fan of Charles Dickens."

    ellie "See? It works."

    menu:
        "Yeah, I've always been interested in his theories.":
            $ ellie_approval -= 5
            if ellie_approval <= 0:
                jump ellie_leaves
            jump dickens_1

        "I'm not really, haha. I just bought that because it looked nice.":
            $ ellie_approval -= 5
            if ellie_approval <= 0:
                jump ellie_leaves
            jump dickens_2

        "You're right - that it does.":
            jump dickens_3

    label dickens_1:
        show ellie confused
        ellie "Theories...?"

        ellie "Maybe you're thinking of Charles Darwin."

        show ellie happy
        ellie "Charles Dickens was an English novelist of the Victorian era, while Charles Darwin was a naturalist, so basically someone who studied natural history."

        ellie "They both wrote a lot of pretty influential works, though."

        show ellie disappointed
        ellie "Oh, sorry. I didn't mean to come across as a know-it-all or anything."

        show ellie sad
        ellie "That was pretty rude of me."

        jump dickens_merge
        
    label dickens_2:
        show ellie confused
        ellie "Oh, I see."

        ellie "Fair enough, I suppose."

        show ellie vneutral
        ellie "But I never really understand why people buy objects to put in their house just to make it look good, even if they don't care about any of that stuff at all."

        ellie "Your belongings should represent you as a person, shouldn't they?"

        show ellie disappointed
        ellie "Ah, sorry, not that I'm trying to tell you how to decorate your home."

        show ellie sad
        ellie "That's not very polite of me."

        jump dickens_merge
        
    label dickens_3:
        show ellie smug
        ellie "Haha! I told you so."

        ellie "Clever, huh?"
        
        show ellie disappointed
        ellie "Ah, wait, I didn't mean to gloat."

        show ellie sad
        ellie "That's not very nice of me. Sorry."

        "I don't think that even counts as gloating."

        jump dickens_merge


label dickens_merge:
    mc "There's no need to apologize, Ellie. You haven't done anything wrong."

    mc "You can try and see what else you can learn from my decor, if you'd like."

    mc "Not that I've really spent a lot of time setting it up, to be honest."

    show ellie abashed
    ellie "Oh..."

    ellie "Well, if you say so..."

    ellie "Let's see."

    show ellie neutral
    "Ellie steps back and surveys the area, eyes darting between the table and the pieces on the wall. She seems like she's pretty serious about this."

    show ellie happy
    ellie "These are paper roses - symbolizing romance, and lasting youth?"

    mc "More or less."

    ellie "You have some abstract expressionist landscapes over here, which tells me that you have good taste."

    mc "Haha, sure."
    
    mc "And..."

    menu:
        "What about the tablecloth?":

            jump look_1

        "What about your face?":
            $ ellie_approval -= 10
            jump look_2

        "What about the floor?":
            $ ellie_approval -= 5
            
            jump look_3

    label look_1:
        show ellie confused
        ellie "What about it?"

        "She peers closer."

        show ellie surprised
        ellie "Oh!"

        show ellie delighted
        ellie "Did you make this yourself, [name]?"

        ellie "The embroidery is gorgeous. Look at these peonies!"

        "Before I can answer, she moves on."

        jump look_merge
        
    label look_2:
        show ellie confused
        ellie "Huh? My face?"

        ellie "What does that mean? I thought we were talking about your decor."

        show ellie vneutral
        ellie "Plus, I don't think a person's face really says much about their personality."

        ellie "We can't judge people by their appearances, right?"

        if ellie_approval <= 0:
            jump ellie_leaves

        "Her eyes go to the things hanging on the wall."

        jump look_merge
        
    label look_3:
        show ellie confused
        ellie "Huh? The floor?"

        ellie "Did you do something special with it?"
        
        mc "Er- no, not really."

        ellie "I'm not sure it tells me anything, then."

        if ellie_approval <= 0:
            jump ellie_leaves

        "She looks back up at the wall."

        jump look_merge


label look_merge:
    show ellie neutral
    ellie "Oh, and you've got this picture frame that looks like a family tree, but it's all just photos of yourself."

    "Is that weird? I wasn't sure what the frame was supposed to be for, so I just put a bunch of random pictures into it."

    show ellie confused
    ellie "Actually, I have no clue what that one's supposed to say about you."

    "Okay, maybe I need to stop her from reading too much into my things."

    "Before she thinks my furniture's too out of the ordinary, or something."
    
    "I guess I'll make an excuse, then."

    mc "I guess you could say that I don't get along with my family."

    show ellie neutral
    ellie "Oh. I see."
    
    show ellie vneutral
    ellie "I know the feeling."

    mc "Yeah?"

    show ellie abashed
    ellie "Yeah."

    show ellie neutral
    ellie "You know, before I came out here to university, my parents would always chide me."

    ellie "They said they wanted the best for me, and that's why they'd be so critical of everything I did."

    ellie "\"Eleanor, don't be so fidgety.\" \"Eleanor, you need to shut up and stop asking so many questions.\" \"Eleanor, you need to try harder, or you'll never figure this out.\""

    show ellie sad
    ellie "\"Eleanor, other people won't put up with you like we will.\""

    show ellie vneutral
    ellie "But when I got here, everyone else was so much nicer than they were."

    ellie "Even my strictest professors are more patient with me."

    ellie "But still, I feel like my parents really do want me to be happy."

    show ellie sad
    ellie "So what am I supposed to make of that?"

    menu:
        "It sounds like they were just trying to help you.":
            $ ellie_approval -= 5
            if ellie_approval <= 0:
                jump ellie_leaves
            jump parents_1

        "They seem like pretty terrible people to me. Maybe you should cut contact with them.":
            $ ellie_approval -= 5
            if ellie_approval <= 0:
                jump ellie_leaves
            jump parents_2

        "Sometimes families don't have the right idea of what's best.":
        
            jump parents_3

    label parents_1:
        show ellie sad
        ellie "Well, I'm not sure it really helped."

        ellie "People can have good intentions but still not be helpful."

        show ellie vneutral
        ellie "I don't think that really makes up for all the times they've been hurtful with me."

        jump parents_merge
        
    label parents_2:
        show ellie sad
        ellie "It's not really that simple. I've still got my sisters to think about, you know?"

        ellie "Even if I wanted to just stop talking to my parents, I've got them to think about. Plus, it's pretty scary, thinking about breaking up with people who've been around for all of your life."

        show ellie confused
        ellie "I kind of thought you'd understand that."

        show ellie sad
        ellie "But I suppose everyone's family is different."

        jump parents_merge
        
    label parents_3:
        show ellie vneutral
        ellie "Yeah, that's definitely true."

        show ellie sad
        ellie "They never listen to me, though."
        
        mc "I'm sorry. It's a terrible position to be in."

        show ellie vneutral
        ellie "Yeah."

        show ellie neutral
        ellie "Yeah, it is."

        jump parents_merge

label parents_merge:
    show ellie sad
    ellie "I don't really even want to go home and see them anymore."
    
    ellie "That's why I'm stuck in a strange town for New Year's Eve, instead of spending it with my relatives like I did every year until now."

    "She sighs."

    show ellie neutral
    ellie "Sorry. Actually, that was a pretty random thing to just blurt out to a stranger."

    show ellie vneutral
    ellie "Maybe I've said too much."

    ellie "I didn't want to bum you out or anything."

    if charm >= 10:
        menu:
            "No, that's okay. I'm touched that you trusted me enough to tell me that. (-10 Charm)":
                $ ellie_approval += 0
                play sound "audio/charm-sound.wav"
                $ charm_start = charm
                while charm > charm_start - 10: # decrease charm bar
                    $ charm -= 1
                    pause(0.0001)
                jump random_1

            "Kind of, yeah, but I'm glad you mentioned it.":
                $ ellie_approval -= 5
                if ellie_approval <= 0:
                    jump ellie_leaves
                jump random_2

            "It's always nice to get juicy family backstory, haha.":
                $ ellie_approval -= 10
                if ellie_approval <= 0:
                    jump ellie_leaves
                jump random_3
    else:
        menu:
            "Kind of, yeah, but I'm glad you mentioned it.":
                $ ellie_approval -= 5
                if ellie_approval <= 0:
                    jump ellie_leaves
                jump random_2

            "It's always nice to get juicy family backstory, haha.":
                $ ellie_approval -= 10
                if ellie_approval <= 0:
                    jump ellie_leaves
                jump random_3

    label random_1:
        show ellie shy
        ellie "Aww, okay."

        ellie "You seem like a nice, reliable person, I suppose."

        ellie "I appreciate you having listened, even if I'm just complaining."

        mc "I don't know if I would call it complaining, but all right."

        show ellie neutral
        ellie "Either way, thank you."

        jump random_merge
        
    label random_2:
        show ellie abashed
        ellie "Oh, sorry."

        ellie "But I'm happy that I wasn't too much of a bother."

        jump random_merge
        
    label random_3:
        show ellie sad
        ellie "I don't know if I'd really think of it like that."

        ellie "I didn't really say all of that in a gossiping sort of way."
        
        show ellie vneutral
        ellie "But I guess I'm glad it was interesting, at least."

        jump random_merge

label random_merge:
    mc "But enough about our families. What about you?"

    show ellie confused
    ellie "Me?"

    mc "Yeah. You've learned about me, right? And talked about your family."

    mc "But I don't even know anything about you, Ellie."

    show ellie abashed
    ellie "Oh..."

    ellie "What is there to know?"

    ellie "Well, let's see."

    show ellie happy
    ellie "I'm a big animal person, I'd say."

    ellie "Not big, as in large animals, but just that I like them a lot."

    ellie "I volunteer at the shelter when my schedule allows for it."

    mc "You seem like an animal person, somehow. Do you have a favorite species?"

    show ellie delighted
    ellie "I wouldn't know about a species, haha. But if I had to pick an animal, I'd say cuttlefish."

    show ellie happy
    ellie "Besides that, I like map collecting, bad movies, fencing, and..."

    ellie "...and long walks on the beach!"

    show ellie laugh
    "She suddenly breaks into a peal of laughter - a loud, sharp sound that I both would and wouldn't have expected, coming from her."
    
    ellie "Hahaha, sorry."

    show ellie delighted

    if charm >= 10:
        menu:
            "Oh, you laugh at your own jokes?":
                $ ellie_approval -= 5
                if ellie_approval <= 0:
                    jump ellie_leaves
                jump laugh_1

            "You should smile like that for me more often. (-10 Charm)":
                $ ellie_approval -= 5
                play sound "audio/charm-sound.wav"
                $ charm_start = charm
                while charm > charm_start - 10: # decrease charm bar
                    $ charm -= 1
                    pause(0.0001)

                if ellie_approval <= 0:
                    jump ellie_leaves
                jump laugh_2

            "No need to apologize - I got to see your pretty laugh.":

                jump laugh_3
    else:
        menu:
            "Oh, you laugh at your own jokes?":
                $ ellie_approval -= 5
                if ellie_approval <= 0:
                    jump ellie_leaves
                jump laugh_1

            "No need to apologize - I got to see your pretty laugh.":

                jump laugh_3

    label laugh_1:
        show ellie happy
        ellie "I guess I do, haha."

        show ellie neutral
        ellie "Apparently it's a bit lame to do that, but at least I make myself laugh."

        ellie "Better to be able to keep yourself entertained, right?"

        jump laugh_merge
        
    label laugh_2:
        show ellie disappointed
        ellie "For you? I don't know about that part..."

        show ellie confused
        ellie "I'm just here to keep myself entertained."

        jump laugh_merge
        
    label laugh_3:
        show ellie abashed
        ellie "Oh..."

        show ellie shy
        ellie "Thank you."
        
        ellie "People say my smile is un-ladylike."

        ellie "Even my friends have made fun of me for it."

        show ellie happy
        ellie "So it's nice to know that someone likes how I look when I smile."

        ellie "I wish I could smile more often, without people making fun of me."

        mc "I don't see why not."

        jump laugh_merge

label laugh_merge:
    hide ellie
    "I take a moment in our conversation to glance at my watch."

    "Wait, it's so much later than I thought it was already. I still have two other people to meet!"

    "My nervousness must show in my expression, because Ellie smiles encouragingly."

    show ellie neutral
    ellie "You've got other guests to tend to, don't you?"

    ellie "It's okay. I understand."

    ellie "I think we've been talking for a quite a while."

    ellie "Just come back to see me when you're done, alright?"

    show ellie happy
    ellie "I had fun talking to you tonight, [name]."

    mc "Of course, Ellie."

    jump may

label ellie_leaves:
    $ ellie_approval = 0
    $ ellie_stays = False
    scene bg hallway
    show ellie disappointed
    ellie "Uh... I don't really want to stay anymore."
    ellie "I think I'm going to leave early."
    mc "Oh."
    mc "Okay, Ellie."
    ellie "Sorry. I had..."
    ellie "A good time tonight."

    hide ellie
    jump may