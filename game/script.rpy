# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sylvie", color="#c8ffc8")
define m = Character("Me", color="#c8c8ff")

# The game starts here.

label start:

    scene bg meadow
    with fade

    s "Hi there! How was class?"

    m "Good..."

    "I can't bring myself to admit that it all went in one ear and out the other."

    s "Are you going home now? Wanna walk back with me?"

    m "Sure!"

    return