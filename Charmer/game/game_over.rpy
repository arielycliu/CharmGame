style yes_btn is button:
    background Image("GUI/buttons/BlueBtn.png", xalign=0.5, yalign=0.5)
    hover_background Image("GUI/buttons/BlueBtnPressed.png", xalign=0.5, yalign=0.5)
    xminimum 100
    yminimum 100

style no_btn is button:
    background Image("GUI/buttons/RedBtn.png", xalign=0.5, yalign=0.5)
    hover_background Image("GUI/buttons/RedBtnPressed.png", xalign=0.5, yalign=0.5)
    xminimum 100
    yminimum 100

style yes_btn_text is text:
    yalign 0.5
    xalign 0.5
    size 45
    hover_color "#ffffff"
    color "#000000" 

style no_btn_text is text:
    yalign 0.5
    xalign 0.5
    size 45
    hover_color "#ffffff"
    color "#000000"  


screen game_over():
    frame:
        vbox spacing 100:
            text "Would you like to restart?":
                size 45
                xalign 0.5
            hbox spacing 300:
                textbutton "Yes":
                    action Jump("tutorial")
                    style "yes_btn"
                textbutton "No":
                    action Return()
                    style "no_btn"
                xalign 0.5
                yalign 0.5
            xalign 0.5
            yalign 0.5
        background Image("GUI/PopUpContainer.png", xalign=0.5, yalign=0.5)
        xalign 0.5
        yalign 0.5