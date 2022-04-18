# 0h h1 solver

[0h h1](https://0hh1.com) solver.

## TODO

style stuff
- better layout
- dark mode
- use same font as [0hh1.com](0hh1.com) - JosefinSans-Bold
- better ukrainian flag shades
- after clicking "check solution": error "pill" (probably different component, no close button, closes with timeout) that shakes sideways if wrong, other green pill else
- fix size issues (12x12 is way too big)
  - prolly just use grid with max-w and max-h in the board component
- add icons to buttons

functionality stuff
- `/board/<repr>`
- maybe add possibilty to highlight initial state (easier way to copy solution)
- add "check solution" button functionality
- change things so that right click in the middle of the tiles doesnt bring up context menu
  - either preventDefault on contextmenu on all of the main Board div 
  - or use padding instead of gap? (with second option, even a slightly missed click would result in a successfull tile coloring)

code stuff
- add vite `$lib/$src/$components` stuff
- !!! move stuff to __layout and stores.js
- add typescript
- extract components
- change name to the pill component