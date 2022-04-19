from flask import Flask
from flask_cors import CORS
from ohhi.solver.exceptions import NoSolutionFound
from ohhi.board import Board
from ohhi.solver.unique_rows import CheckUniqueRowsSolver

app = Flask(__name__)
CORS(app)

@app.route("/get_solution/<string:encoded_board_state>")
def find_solution(encoded_board_state: str):
    try:
        board: Board = Board.decode(encoded_board_state)
    except ValueError:
        return {"error_message": "Bad board string encoding."}, 400

    try:
        solution = CheckUniqueRowsSolver.solve(board).encode()
    except NoSolutionFound:
        return {"error_message": "No solution found for this board."}, 404

    return {"solution": solution}

@app.route("/check_solution/<string:encoded_board_state>")
def check_solution(encoded_board_state: str):
    try:
        board: Board = Board.decode(encoded_board_state)
    except ValueError:
        return {"error_message": "Bad board string encoding."}, 400

    return {"is_solution": board.is_solution()}

if __name__ == "__main__":
    app.run()