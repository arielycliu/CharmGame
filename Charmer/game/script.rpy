default charm = 0
define athena = Character("Athena", color="#F4839F")
define chad = Character("Chad", color="#903A4D")
define ellie = Character("Ellie", color="#3b3545")
define may = Character("May", color="#3d3a59")

define claire_unknown = Character("???", color="#A65A4C")
define claire = Character("Claire", color="#A65A4C")

transform default_zoom:
    zoom 0.75

image athena asleep:
    "images/Athena/athena asleep.png"
    default_zoom
image athena tired1:
    "images/Athena/athena tired1.png"
    default_zoom
image athena tired2:
    "images/Athena/athena tired2.png"
    default_zoom
image athena tireddark1:
    "images/Athena/athena tireddark1.png"
    default_zoom
image athena tireddark2:
    "images/Athena/athena tireddark2.png"
    default_zoom

image chad angry:
    "images/Chad/chad angry.png"
    default_zoom
image chad annoyed:
    "images/Chad/chad annoyed.png"
    default_zoom
image chad blush:
    "images/Chad/chad blush.png"
    default_zoom
image chad delighted:
    "images/Chad/chad delighted.png"
    default_zoom
image chad laugh:
    "images/Chad/chad laugh.png"
    default_zoom
image chad normal:
    "images/Chad/chad normal.png"
    default_zoom
image chad sad:
    "images/Chad/chad sad.png"
    default_zoom
image chad shocked:
    "images/Chad/chad shocked.png"
    default_zoom
image chad sleepy:
    "images/Chad/chad sleepy.png"
    default_zoom
image chad smile:
    "images/Chad/chad smile.png"
    default_zoom
image chad smile2:
    "images/Chad/chad smile2.png"
    default_zoom
image chad smug:
    "images/Chad/chad smug.png"
    default_zoom

image ellie abashed:
    "images/Ellie/ellie abashed.png"
    default_zoom
image ellie angry:
    "images/Ellie/ellie angry.png"
    default_zoom
image ellie annoyed:
    "images/Ellie/ellie annoyed.png"
    default_zoom
image ellie confused:
    "images/Ellie/ellie confused.png"
    default_zoom
image ellie delighted:
    "images/Ellie/ellie delighted.png"
    default_zoom
image ellie disappointed:
    "images/Ellie/ellie disappointed.png"
    default_zoom
image ellie happy:
    "images/Ellie/ellie happy.png"
    default_zoom
image ellie laugh:
    "images/Ellie/ellie laugh.png"
    default_zoom
image ellie neutral:
    "images/Ellie/ellie neutral.png"
    default_zoom
image ellie sad:
    "images/Ellie/ellie sad.png"
    default_zoom
image ellie shy:
    "images/Ellie/ellie shy.png"
    default_zoom
image ellie smug:
    "images/Ellie/ellie smug.png"
    default_zoom
image ellie suprised:
    "images/Ellie/ellie suprised.png"
    default_zoom
image ellie veryangry:
    "images/Ellie/ellie veryangry.png"
    default_zoom


image may angry1:
    "images/May/may angry1.png"
    default_zoom
image may angry2:
    "images/May/may angry2.png"
    default_zoom
image may laugh:
    "images/May/may laugh.png"
    default_zoom
image may normal:
    "images/May/may normal.png"
    default_zoom
image may sad:
    "images/May/may sad.png"
    default_zoom
image may smile1:
    "images/May/may smile1.png"
    default_zoom
image may smile2:
    "images/May/may smile2.png"
    default_zoom
image may smile3:
    "images/May/may smile3.png"
    default_zoom
image may smirk:
    "images/May/may smirk.png"
    default_zoom
image may surprised:
    "images/May/may surprised.png"
    default_zoom
image may sweat:
    "images/May/may sweat.png"
    default_zoom

transform claire_zoom:
    zoom 0.75
    xpos 0.50
image claire angry1:
    "images/Claire/claire angry1.png"
    claire_zoom
image claire angry2:
    "images/Claire/claire angry2.png"
    claire_zoom
image claire annoyed:
    "images/Claire/claire annoyed.png"
    claire_zoom
image claire crying:
    "images/Claire/claire crying.png"
    claire_zoom
image claire delighted:
    "images/Claire/claire delighted.png"
    claire_zoom
image claire delighted2:
    "images/Claire/claire delighted2.png"
    claire_zoom
image claire normal:
    "images/Claire/claire normal.png"
    claire_zoom
image claire o:
    "images/Claire/claire o.png"
    claire_zoom
image claire sad:
    "images/Claire/claire sad.png"
    claire_zoom
image claire shocked:
    "images/Claire/claire shocked.png"
    claire_zoom
image claire sleepy:
    "images/Claire/claire sleepy.png"
    claire_zoom
image claire sleepy2:
    "images/Claire/claire sleepy2.png"
    claire_zoom
image claire smile:
    "images/Claire/claire smile.png"
    claire_zoom
image claire smile2:
    "images/Claire/claire smile2.png"
    claire_zoom
image claire smug:
    "images/Claire/claire smug.png"
    claire_zoom
image claire smug2:
    "images/Claire/claire smug2.png"
    claire_zoom

transform charm_zoom:
    zoom 0.75
    ypos 0.75

image charms0:
    "images/Charms/charms0.png"
    charm_zoom
image charms1:
    "images/Charms/charms1.png"
    charm_zoom
image charms2:
    "images/Charms/charms2.png"
    charm_zoom
image charms3:
    "images/Charms/charms3.png"
    charm_zoom
image charms4:
    "images/Charms/charms4.png"
    charm_zoom

label start:
    $ name = "Ariel"
    jump chmsq