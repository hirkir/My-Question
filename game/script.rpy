define b = Character("Bob", color="#3dd8a9")
define h = Character("Herbert", color="#bb663e")

transform slightleft:
    xalign 0.3
    yalign 1.0

transform slightright:
    xalign 0.7
    yalign 1.0

label start:

    scene bg room
    with fade

    "Oh crap, I overslept."

    "I better get up quick."

    show bob happy
    with dissolve

    b "I'll just skip breakfast for now."

    "I grab my bag and bolt out of the door."

    scene bg neighbourhood
    with fade

    show bob happy
    with dissolve

    b "If only this day could be a little better."

    show bob happy at slightleft
    with move

    show herbert happy at slightright
    with dissolve

    h "Heya Bob, running a little late I see!"

    "My spirits are lifted as Herbert appears."

    b "Hello there Herbert, I could say the same to you."

    h "Well you know I kinda just forgot about time I guess."

    b "Doing what, sleeping?"

    h "Haha no, I actually started learning the banjo."

    b "Wow that's awesome! You should play it for me sometime."

    b "Or maybe you could play for the festival?"

    return