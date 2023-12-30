style chosen is button:
    background Image("choice_idle_background.png", xalign=0.5, yalign=0.5)
    hover_background Image("choice_hover_background.png", xalign=0.5, yalign=0.5)
    xminimum 100
    yminimum 100

style chosen_text is text:
    yalign 0.5
    xalign 0.5
    size 45
    hover_color "#ffffff"
    color "#000000"  

screen game_over():
    hbox:
        textbutton "Yes":
            action Jump("tutorial")
            style "chosen"
        textbutton "No":
            action Return()
            style "chosen"
        xalign 0.5
        yalign 0.5