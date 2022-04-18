from flask import Flask

if __name__ == "__main__":
    app = Flask(__name__)
    app.run()

@app.route("/get_solution/<str:encoded_board_state>")
def find_solution(encoded_board_state: str):
    #! missing error handliing
    board: Board = Board.parse_string(encoded_board_state)

    #! missing error handling
    solution = CheckUniqueRowsSolver.solve().encode()
    return {"solution": solution}