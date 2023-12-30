style yes_btn is button:
    background Image("GUI/buttons/yes_btn.png", xalign=0.5, yalign=0.5)
    hover_background Image("GUI/buttons/yes_btn_hover.png", xalign=0.5, yalign=0.5)
    xminimum 200
    yminimum 100

style no_btn is button:
    background Image("GUI/buttons/no_btn.png", xalign=0.5, yalign=0.5)
    hover_background Image("GUI/buttons/no_btn_hover.png", xalign=0.5, yalign=0.5)
    xminimum 200
    yminimum 100

style yes_btn_text is text:
    yalign 0.6
    xalign 0.5
    size 45
    hover_color "#ffffff"
    color "#000000" 

style no_btn_text is text:
    yalign 0.6
    xalign 0.5
    size 45
    hover_color "#ffffff"
    color "#000000"  


screen game_won():
    frame:
        vbox spacing 50:
            text "Congratulations, you are no longer single!":
                size 35
                xalign 0.5
            text "Would you like to play again?":
                size 35
                xalign 0.5
            hbox spacing 200:
                textbutton "Yes":
                    action Jump("tutorial")
                    style "yes_btn"
                textbutton "No":
                    action MainMenu()
                    style "no_btn"
                xalign 0.5
                yalign 0.5
            xalign 0.5
            yalign 0.5
        background Image("GUI/PopUpContainer.png", xalign=0.5, yalign=0.5)
        xalign 0.5
        yalign 0.5