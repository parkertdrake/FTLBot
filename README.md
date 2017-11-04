##FTL Bot Thoughts:

Here's how I can interact with the game:
    1. I have images of the screen.
    2. I can send input to the game. Keypresses for sure, need to figure out mouse input. But it's gotta be easy.

What I need to build:
    1. A game interaction library. The ability to:
        - Read the game state (all done through image processing)
            - Ship health, weapon status, power status, shield status, enemy charging status, etc.
            - Big question mark on if I'm capable of this.
        - Execute commands in the game (fire, pause, charge weapons, shields, move crew, etc.)
            - This feels actually pretty doable. The Kestrel is always at a fixed position onscreen.

    2. An AI to make decisions on how to play the game.
        - I could make a dumb AI that essentially follows a script. Makes no attempt to play the game in a strategic fashion.
        - I could model this on how I play the game (Easy ish)
        - I could apply real machine learning techniques to play the game (hard)

Notes on scope:
    - The game is large and complex. Building a bot to the play the whole thing from start to finish would be very very hard.
        - It would probably be reasonable to set a single ship to ship engagement as the goal.
    - Neither the AI or the interaction library are easy to build. I might have to choke down on how robust either is to get something that actually works.
