define b = Character("Bob", color="#3dd8a9")
define h = Character("Herbert", color="#bb663e")

transform slightleft:
    xalign 0.3
    yalign 1.0

transform slightright:
    xalign 0.7
    yalign 1.0

default band = False

label start:
    scene bg room
    with fade

    #play music "audio/Swimming Lessons - Bail Bonds.mp3"

    "Oh crap, I overslept."

    "I better get up quick."

    show bob
    with dissolve

    b "I'll just skip breakfast for now."

    "I grab my bag and bolt out of the door."

    scene bg neighbourhood
    with fade

    show bob
    with dissolve

    b "If only this day could be a little better."

    show bob at slightleft
    with move

    show herbert at slightright
    with dissolve

    h "Heya Bob, running a little late I see!"

    "My spirits are lifted as Herbert appears."

    b "Hello there Herbert, I could say the same to you."

    h "Well you know I kinda just forgot about time I guess."

    b "Doing what, sleeping?"

    h "Haha no, I actually started learning the banjo."

    b "Wow that's awesome! You should play it for me sometime."

    h "Uh... I'd rather play for you when I'm better."

    menu:
        b "Well I think you should..."

        "Play at the festival":
            jump play_at_festival

        "Join our band":
            jump join_band
            
label play_at_festival:
    b "There is the school festival coming up..."
    
    h "Then I'd have to practice a whole lot, and besides my nervousness would make it unable for me to play."

    b "It would give you a lot of experience playing in front of a crowd."
    
    b "You know, when I played at the festival, I was really nervous,\nbut when I saw that people were loving it, I got a confidence boost."

    h "You say that as if I'm like you, which I'm not."

    h "Maybe I could practice with you..."

    h "...If you want to."

    b "Yeah, that sounds like fun!"

    jump school

label join_band:
    $ band = True

    b "What if you join our band? You get all the time you need to practice."

    h "Alright then, I'll consider it."

    b "That's great! You know, you can come in and jam with us on friday if you want."

    h "Yep, sounds like a plan."

    jump school

label school:
    if band:
        "As we make our way to school I think about how excited I am to have Herbert jam with the band."
    else:
        "We walk besides one another as I think about how fun it will be to practice together."

    scene bg hallway
    with fade

    show herbert at slightright

    show bob at slightleft
    with dissolve

    h "I gotta get to class, see ya!"

    b "Bye!"

    hide herbert
    with dissolve

    show bob at default
    with move

    "I run to the classroom considering I'm late."

    scene bg classroom
    with fade

    show bob
    with dissolve

    "As I get in, I notice everyone staring at me."
    
    "The teacher gives me a stern look, but continues the lesson anyway."

    "I sit down and try to catch up with what's being taught."

    "The day goes by as I'm ready to go home."