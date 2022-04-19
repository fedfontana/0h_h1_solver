# 0h h1 solver

[0h h1](https://0hh1.com) solver.

## TODO

style stuff
- better layout
- dark mode
- use same font as [0hh1.com](0hh1.com) - JosefinSans-Bold
- better ukrainian flag shades
- after clicking "check solution": error toast (probably different component, no close button, closes with timeout) that shakes sideways if wrong, green toast otherwise
- fix board size issues (12x12 is way too big)
  - prolly just use grid with max-w and max-h in the board component
  - ideally the whole board should fit in the middle section
- add icons to buttons

functionality stuff
- check that the board is completely full before checking the solution
- maybe add possibilty to highlight initial state (easier way to copy solution)
- change things so that right click in the middle of the tiles doesnt bring up context menu
  - either preventDefault on contextmenu on all of the main Board div 
  - or use padding instead of gap? (with second option, even a slightly missed click would result in a successfull tile coloring)
- add settings and about tab with:
  - theme
  - about and credits
  - source code url
  - keyboard shortcuts info

code stuff
- !!! move stuff to __layout and stores.js

utility stuff
- cltr+l clears the board
- ctrl+enter solves the board
- ctrl+shift+enter checks the solution
- tab tabs through the board
- shif+tab tabs through the board
- enter changes the selected tile color like a left click
- shift+enter changes the selected tile color like a left click

checks
- check what happens when multiple error/info/success toasts are rendered