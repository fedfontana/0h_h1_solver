# 0h h1 solver

[0h h1](https://0hh1.com) solver.

## TODO

style stuff
- better layout
  - https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Ordering_Flex_Items#the_order_property
- dark mode
- after clicking "check solution": 
  - error toast (probably different component, no close button, closes with timeout) that shakes sideways if wrong
  -  green toast otherwise
- maybe add icons to buttons?

- maybe on `board/<repr>` show only the board, the solve button and the check button and make it so that the clear button returns to the original url of the page (original puzzle)

functionality stuff
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
- `WEBSITE_URL` may be useless, just get the url from the sveltekit store (`$page.something.somethingelse`?)

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