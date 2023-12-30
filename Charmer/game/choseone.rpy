style chosen is button:
    background Image("GUI/buttons/choice_idle_background.png", xalign=0.5, yalign=0.5)
    hover_background Image("GUI/buttons/choice_hover_background.png", xalign=0.5, yalign=0.5)
    xminimum 1185
    yminimum 100

style chosen_text is text:
    yalign 0.5
    xalign 0.5
    size 45
    hover_color "#ffffff"
    color "#000000"  

screen choseone():
    vbox spacing 50:
        # $ choices = generate_choices(ellie_stayed, chad_stayed, may_stayed, athena_stayed)
        for name in choices:
            textbutton "[name]":
                action Return(name)
                style "chosen"
        xalign 0.5
        yalign 0.5