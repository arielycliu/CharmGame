label chad:
    scene bg kitchen
    show screen bars
    play music "<loop 1.564>chad.mp3" fadein 1.0 fadeout 1.0

    "I know the party just started but I'm so nervous that my insides feel like they're in knots."

    "I decide to head to the kitchen, hoping that filling my stomach with something will get it to stop doing backflips."

    "There's someone in the back of the kitchen, rummaging through the fridge."
    
    mc "Uh... what are you doing in there?"

    show chad shocked
    chad_unknown "Oh, I didn't see you there. I was thinking of baking a chocolate soufflé to impress you but I couldn't find your eggs."
    
    "I take a look at the contents of my fridge, scanning for eggs."

    show chad normal
    mc "Hm, I think I used up all of them making deviled eggs."

    mc "Is there anything else you could make with what's left in my fridge?"

    "Wait, what am I saying?"

    "They're not my maid!"

    mc "Sorry, I didn't mean for it to sound like a request."

    show chad delighted
    chad_unknown "No, don't worry about it. I can tell you're feeling a bit peckish, and I'm happy to assist anyone, especially someone as charming as yourself."

    "I feel myself blushing just a bit."

    "They turn around and start boiling some water."

    hide chad delighted
    with Dissolve(0.5)
    "Once the water boils, they drop in the pasta. While it's cooking, they prepare a quick sauce of olive oil, garlic, basil, and canned tomatoes."

    "They combine the sauce with the spaghetti, season it with salt and pepper, and plate it beautifully."

    hide chad delighted

    show bg pasta
    with Dissolve(0.5)

    pause(0.5)

    show bg kitchen
    with Dissolve(0.5)

    "While I'm slurping down the pasta, they pull out a chair and sit down next to me."

    show chad smile
    chad_unknown "I don't think we've met formally before. My name's Chad."

    show chad blush
    chad "I heard a bit about you from Claire. Your name is [name], right? You're even better-looking in person - Claire's photo doesn't do you justice."

    if charm >= 15:  # charm choice 1
        menu:
            chad "I heard a bit about you from Claire. Your name is [name], right? You're even better-looking in person - Claire's photo doesn't do you justice."
            "If you keep this up, I think I'll like you too much. (-15 Charm)":
                $ chad_approval += 0
                play sound "audio/charm-sound.wav"
                $ charm_start = charm
                while charm > charm_start - 15: # decrease charm bar
                    $ charm -= 1
                    pause(0.0001)
                jump photo_1
            "Thanks.":
                $ chad_approval -= 5
                if chad_approval <= 0:
                    jump chad_leaves
                jump photo_2
            "Chad? That's a stupid name for a girl.":
                $ chad_approval -= 20
                # don't leave yet give mc another chance
                jump photo_3
    else:
        menu:
            chad "I heard a bit about you from Claire. Your name is [name], right? You're even better-looking in person - Claire's photo doesn't do you justice."
            "Thanks.":
                $ chad_approval -= 5
                if chad_approval <= 0:
                    jump chad_leaves
                jump photo_2
            "Chad? That's a stupid name for a girl.":
                $ chad_approval -= 20
                jump photo_3
    
    label photo_1:
        "Whoa, I don't even sound like myself. I better thank Claire properly later for the charms."
        show chad shocked
        chad "Ha, bold. I kinda like it..."
        jump photo_merge

    label photo_2:
        show chad smug
        chad "No problem, you don't need to thank me for speaking the plain truth."
        jump photo_merge
    
    label photo_3:
        show chad angry
        chad "That's such a mean thing to say. I'm not even a girl!"

        if charm >= 50: # charm choice 2
            menu:
                chad "That's such a mean thing to say. I'm not even a girl!"

                "Nonono, I didn't mean it. Sorry... I get really nervous when talking to new people. I just said whatever I thought of. (-50 charm)":
                    $ chad_approval += 10 # approval went from 0 to 10
                    play sound "audio/charm-sound.wav"
                    $ charm_start = charm
                    while charm > charm_start - 50:
                        $ charm -= 1
                        pause(0.0001)

                    show chad normal
                    chad "Oh..."

                    chad "I can understand being nervous."
                    
                    chad "I get nervous too."

                    chad "Guess it's all right, then."
                
                "Oh, well. It's still an ugly name for a boy.":
                    jump chad_leaves
        else:
            mc "Oh, well. It's still an ugly name for a boy."        
            jump chad_leaves
        jump photo_merge
    
label photo_merge:
    scene bg kitchen
    show chad smile2
    # I would recommend adding a transition between the previous part and here
    chad "I think the best way to get to know someone is to play some Truth or Dare. Are you down to play with me?"

    menu: 
        chad "I think the best way to get to know someone is to play some Truth or Dare. Are you down to play with me?"
        "I'm down.":
            $ chad_approval -= 0
            jump chad_truthordare
        "No thanks.":
            $ chad_approval -= 10
            if chad_approval <= 0:
                jump chad_leaves

            show chad normal
            chad "Aww... That's no fun."
            mc "Sorry, I'd rather not take risks. I have secrets, after all."
            chad "Wow. Now, I'm intrigued. won't you tell me about yourself?"
            mc "How about you go first?"
            jump chad_hobbies

label chad_truthordare:
    chad "All right! Truth or dare?"
    mc "Truth. (Dares are intimidating.)"
    chad "What do you like the most about me?"
    menu:
        chad "What do you like the most about me?"
        "Face":
            show chad blush
            $ chad_approval -= 5
            if chad_approval <= 0:
                jump chad_leaves
            chad "Aww you're so sweet."
        "Voice":
            show chad shocked
            chad "Really?"
            
            chad "I'm quite insecure about my voice, actually, so it's nice to hear that."
        "Personality":
            show chad blush
            $ chad_approval -= 5
            if chad_approval <= 0:
                jump chad_leaves
            chad "Aww, you're so sweet."

    show chad normal
    mc "Your turn - truth or dare?"
    chad "Truth."

    menu:
        chad "Truth."
        "Have you ever broken someone's heart?":
            $ chad_approval -= 8
            if chad_approval <= 0:
                jump chad_leaves
            show chad annoyed
            chad "Never. I don't break hearts - I mend them."
            mc "With a face like that, you sure you don't have a hobby of breaking hearts?"
            chad "Positive."
            jump chad_hobbies
        "What's your biggest pet peeve?":
            show chad sleepy
            chad "Hmm... I guess, being told that I'm not masculine enough."

            show chad angry
            chad "I look like a girl and have some more feminine hobbies, so some people think it's okay to say I'm not a man."
            jump chad_hobbies

label chad_hobbies:
    show chad normal
    mc "So what kind of hobbies do you enjoy?"
    chad "Why don't you take a guess first? That'll make it more interesting."
    mc "Sure. That pasta you cooked for me was delicious, and you were trying to bake me a chocolate soufflé... So I think you must like cooking."
    show chad smile2
    chad "Quite the detective, aren't you?"
    chad "Well, you'd be correct - I like to cook, and I can also bake a few things."
    mc "I'm a bit jealous. I don't mind cooking, but I'm not great at it. If only I could eat your food every day."
    "I sigh a little, eyeing the empty plate of pasta with longing."
    show chad laugh
    chad "I could make that happen."

    if charm >= 10:
        menu:
            chad "I could make that happen."
            "Really? You'd teach me?":
                show chad blush
                chad "Of course! I definitely wouldn't mind having a sous-chef as charming as yourself in my kitchen."
                mc "Well, I might just take you up on that offer. In the meantime, I guess I'll just have to savor the memory of your delicious meal."

                show chad normal
                chad "Well, I won't take up much more of your time. I know you still have many more people to meet."
            "Would you like to move in with me? (-10 charm)":
                play sound "audio/charm-sound.wav"
                $ charm_start = charm
                while charm > charm_start - 10:
                    $ charm -= 1
                    pause(0.0001)

                show chad shocked
                $ chad_approval -= 5
                if chad_approval <= 0:
                    jump chad_leaves
                chad "Move in? That's a big step, isn't it? I think it might be too early for me to say yes."

                show chad smile
                chad "Err, how about dinner at my place tomorrow, instead?"
                menu: 
                    chad "Err, how about dinner at my place tomorrow, instead?"
                    "Count me in!":
                        show chad delighted
                        chad "Heck yeah! I'll make my specialty dish!"

                        show chad normal 
                        chad "Well, I won't take up much more of your time. I know you still have many more people to meet."

                    "No, thank you.":
                        show chad sad
                        $ chad_approval -= 10
                        if chad_approval <= 0:
                            jump chad_leaves
                        chad "Aww, that's a shame."

                        show chad normal
                        chad "Well, I won't take up much more of your time. I know you still have many more people to meet."
            "No, thanks.":
                $ chad_approval -= 10
                if chad_approval <= 0:
                    jump chad_leaves
                show chad normal
                chad "Oh okay, sorry for imposing."
                chad "Well, I won't take up much more of your time. I know you still have many more people to meet."
    else:
        menu:
            chad "I could make that happen."
            "Really? You'd teach me?":
                show chad blush
                chad "Of course! I definitely wouldn't mind having a sous-chef as charming as yourself in my kitchen."
                mc "Well, I might just take you up on that offer. In the meantime, I guess I'll just have to savor the memory of your delicious meal."
                show chad normal
                chad "Well, I won't take up much more of your time. I know you still have many more people to meet."
            "No, thanks.":
                $ chad_approval -= 10
                if chad_approval <= 0:
                    jump chad_leaves
                show chad normal
                chad "Oh okay, sorry for imposing."
                chad "Well, I won't take up much more of your time. I know you still have many more people to meet."

    show chad smile
    chad "Feel free to drop back in anytime. I'll be in the kitchen, waiting to share it with you."
    jump ellie
            

label chad_leaves:
    $ chad_approval = 0
    $ chad_stayed = False

    show chad normal
    chad "..."
    chad "I think I should go."
    mc "You're leaving so soon?"
    chad "Sorry."
    chad "I just remembered that I have to prepare some drafts for my boss at work."
    mc "Oh, that's unlucky. I guess I'll see you around, then."
    chad "Yeah."
    chad "See you."
    jump ellie