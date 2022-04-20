# 0h h1 solver

[0h h1](https://0hh1.com) solver.

## TODO

- error page?
  - [this puzzle](http://localhost:3000/board/yyyxbbxxyyxx-yxxxbxbxyxyx-yyxxbbxxyyxx-yxxxbxbxyxyx-yyyxbxbxyxyx-xxxxxxxxxxxx-xxxxxxxxxxxx-xxbbbxyyxxxx-xxbxbxyxyxxx-xxbxbxyyxxxx-xxbxbxyxyxxx-xxbbbxyxyxxx)

style stuff
- dark mode
- after clicking "check solution": 
  - error toast (probably different component, no close button, closes with timeout) that shakes sideways if wrong
  -  green toast otherwise
- maybe add icons to buttons?

- maybe on `board/<repr>` show only the board, the solve button and the check button and make it so that the clear button returns to the original url of the page (original puzzle)

functionality stuff
- maybe add possibilty to highlight initial state (easier way to copy solution)
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