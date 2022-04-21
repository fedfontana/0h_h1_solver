# 0h h1 solver

[0h h1](https://0hh1.com) solver.

## TODO

style stuff
- dark mode
- after clicking "check solution": 
  - error toast (probably different component, no close button, closes with timeout) that shakes sideways if wrong
  - green toast otherwise
- maybe add icons to buttons?

functionality stuff
- add settings and about tab with:
  - theme
  - about and credits
  - source code url
  - keyboard shortcuts info

code stuff
- usare eventi che vengono catchati in __layout:
  - on:error -- in questo modo da __error si possono anche catchare i vari "Can't update a readonly board" e fare si che non venga mostrato il toast
  - on:info
  - on:success

utility stuff
- cltr+l clears the board
- ctrl+enter solves the board
- ctrl+shift+enter checks the solution
- tab tabs through the board
- shif+tab tabs through the board
- enter changes the selected tile color like a left click
- shift+enter changes the selected tile color like a left click