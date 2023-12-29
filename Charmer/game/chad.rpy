label chad:
    scene bg kitchen

    "I know the party just started but I'm so nervous that my intestines feel like they're in knots."

    "I decide to head to the kitchen, hoping that filling my stomach with something will get it to stop doing backflips."

    "There's someone in the back of the kitchen, rummaging through the fridge."
    
    mc "Uh... what are you doing in there?"

    show chad shocked
    chad_unknown "Oh, I didn't see you there. I was thinking of baking a chocolate souffle to impress you but I couldn't find your eggs."
    
    "I take a look at the contents of my fridge, scanning for eggs."

    show chad normal
    mc "Hm, I think I used up all of them making deviled eggs."

    mc "Is there anything else you could make with what is left in my fridge?"

    "What am I saying?"

    "This guy isn't my maid!"

    mc "Sorry, I didn't mean it to sound like a request."

    show chad delighted
    chad_unknown "No, don't worry about it. I can tell you're feeling a bit peckish, and I'm happy to assist anyone, especially someone as charming as yourself."

    "I feel yourself blushing just a bit at how smooth they are. "

    "You see them turn around and start to boil water. "

    "Once the water boils, they drop in the pasta and while that is cooking, he prepares a quick sauce of olive oil, garlic, basil, and canned tomatoes."

    "He combines the sauce with the spaghetti, seasons it with salt and pepper, and plates it beautifully."

    hide chad delighted

    show bg pasta
    with Dissolve(0.5)

    pause(0.5)

    show bg kitchen
    with Dissolve(0.5)

    "While I'm slurping down the pasta, they pulls out a chair and sit down next to me."

    show chad smile
    chad "I don't think we've meet formally before, my name is Chad"

    show chad blush
    chad "I heard a bit about you from Claire. Your name is [name] right? You're even prettier in person - Claire's photo doesn't do you justice."

    menu:
        "How should I respond to Chad?"
        "If you keep this up, I think I'll like you too much. (-10 Charm)":
            $ chad_approval += 0
            jump photo_1
        "Thanks":
            $ chad_approval -= 5
            jump photo_2
        "Your name is Chad right? That's a stupid name for a girl.":
            $ chad_approval -= 20
            jump photo_3
    
    label photo_1:
        "Whoa, I don't even sound like myself. I better thank Claire properly later for the charms."

        show chad shocked

        chad "Whoa bold... not that I don't like it..."
        chad "I kinda like it..."
        jump photo_merge

    label photo_2:
        show chad smug
        chad "No problem, you don't need to thank me for speaking the plain truth."
        jump photo_merge
    
    label photo_3:
        show chad angry
        chad "That's such a mean thing to say. Plus I'm a boy!"

        menu:
            "How should I salvage this?"

            "Nonono I didn't mean it. Sorry I get nervous when talking to new people. (-50 charm)":
                $ chad_approval += 10
                show chad normal
                chad "Oh no worries, I can understand being nervous. I get nervous too."
            
            "Oh, well it's still an ugly name for a guy.":
                $ chad_approval = 0
                $ chad_stayed = False

                show chad normal
                chad "..."
                chad "I think I should leave this party early."
                mc "You're leaving so soon?"
                chad "Sorry I just remembered that I have to prepare some drafts for my boss at work."
                jump ellie
        
        jump photo_merge
    
label photo_merge:
    scene bg kitchen
    show chad smile2
    chad "I think the best way to get to know someone is to play some Truth or Dare. Are you down to play with me?"