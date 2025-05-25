from django.shortcuts import render, redirect 



def index(request):
    # Initialize session data if not already set
    if 'board' not in request.session:
        request.session['board'] = [''] * 9
        request.session['current_player'] = 'X'

    board = request.session['board']
    current_player = request.session['current_player']
    winner = check_winner(board)
    print(f"Board State-{board} -- Current Player :{current_player} -- Winner-{winner}")

    context = {
        'board': board,
        'current_player': current_player,
        'winner': winner,
        "sidebar_content": "Tic-Tac-Toe : Session in Depth"
    }
    return render(request, 'app7_game/index.html', context)


def make_move(request, cell):
    board = request.session['board']
    current_player = request.session['current_player']

    # Make the move if the cell is empty and there’s no winner yet
    if board[cell] == '' and not check_winner(board):
        print(f"Print cell index - {cell}")
        board[cell] = current_player
        print(f"Print cell value - {board[cell]}")
        
        request.session['board'] = board
        print(f"State of board is : {board}")
        # Switch player
        request.session['current_player'] = 'O' if current_player == 'X' else 'X'

    return redirect('index-app7-capstone')

 

 
def reset_game(request):
    # Clear the session data
    request.session.flush()
    return redirect('index-app7-capstone')




def check_winner(board):
    # Winning combinations
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6],             # Diagonals
    ]
    for condition in win_conditions:
        print(f"State of board[condition[0]] : {board[condition[0]]}")
        print(f"State of board[condition[1]] : {board[condition[1]]}")
        print(f"State of board[condition[2]] : {board[condition[2]]}")

        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != '':
            return board[condition[0]]  # Return the winner ('X' or 'O')
    if '' not in board:
        return 'Draw'  # If all cells are filled, it's a draw
    return None  # No winner yet




