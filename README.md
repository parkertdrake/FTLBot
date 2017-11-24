### FTL Bot 

A bot to play FTL, 2 parts.

  1. A game interaction library. The ability to:
      - Read the game state (all done through image processing)
        - When I say "image processing", I mean checking pixel colors. 
      - Ship health, weapon status, power status, shield status, enemy charging status, etc.
      - Execute commands in the game (fire, pause, charge weapons, shields, move crew, etc.)
        - I can do this with pyautogui.

  2. An AI to make decisions on how to play the game.
      - I could make a dumb AI that essentially follows a script. Makes no attempt to play the game in a really strategic fashion.
        - I could model this on how I play the game (Easy ish)
      - I could apply real machine learning techniques to play the game (hard)
   


