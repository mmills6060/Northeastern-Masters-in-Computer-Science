import java.util.Arrays;
import java.util.stream.Collectors;

public class TicTacToeModel implements TicTacToe {
  @Override
  public String toString() {
    // Using Java stream API to save code:
    return Arrays.stream(getBoard()).map(
      row -> " " + Arrays.stream(row).map(
        p -> p == null ? " " : p.toString()).collect(Collectors.joining(" | ")))
          .collect(Collectors.joining("\n-----------\n"));
    // This is the equivalent code as above, but using iteration, and still using 
    // the helpful built-in String.join method.
    /**********
    List<String> rows = new ArrayList<>();
    for(Player[] row : getBoard()) {
      List<String> rowStrings = new ArrayList<>();
      for(Player p : row) {
        if(p == null) {
          rowStrings.add(" ");
        } else {
          rowStrings.add(p.toString());
        }
      }
      rows.add(" " + String.join(" | ", rowStrings));
    }
    return String.join("\n-----------\n", rows);
    ************/
  }
  private Player[][] board;
  private Player turn;
  private boolean gameOver;
  private Player winner;

  public TicTacToeModel() {
      board = new Player[3][3];
      turn = Player.X; // Player X goes first
      gameOver = false;
      winner = null;
  }
  @Override
  public void move(int r, int c) {
    isGameOver();
    if (gameOver) {
        throw new IllegalStateException("The game is already over.");
    }

    if (r < 0 || r >= 3 || c < 0 || c >= 3) {
        throw new IllegalArgumentException("Invalid position. Outside of game board.");
    }

    if (board[r][c] != null) {
        throw new IllegalArgumentException("Invalid move: space is occupied.");
    }
    // exception handling for non integer value entered for column
    if (c != (int)c) {
        throw new IllegalArgumentException("Non-integer value entered for column.");
    }
    // exception handling for non integer value entered for row
    if (r != (int)r) {
        throw new IllegalArgumentException("Non-integer value entered for row.");
    }
    board[r][c] = turn;
    getTurn();
}

  @Override
  public Player getTurn() {
    // alternate between player X and player O
    if (turn == Player.X) {
        turn = Player.O;
    } else {
        turn = Player.X;
    }
    return turn;
  }

  @Override
  public boolean isGameOver() {
    // Determine if there is a winner.
    Player winner = getWinner();

    // If there is a winner, set gameOver to true.
    if (winner != null) {
        this.gameOver = true;
    } else {
        // If there is no winner, check if the board is full.
        boolean isBoardFull = true;
        Player[][] board = getBoard();

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == null) {
                    isBoardFull = false;
                    break;
                }
            }
            if (!isBoardFull) {
                break;
            }
        }

        // If the board is full, set gameOver to true; otherwise, set it to false.
        this.gameOver = isBoardFull;
    }

    return this.gameOver;
}

@Override
public Player getWinner() {
    // Check for horizontal wins
    for (int row = 0; row < 3; row++) {
        if (board[row][0] != null && board[row][0] == board[row][1] && board[row][0] == board[row][2]) {
            return board[row][0];
        }
    }

    // Check for vertical wins
    for (int col = 0; col < 3; col++) {
        if (board[0][col] != null && board[0][col] == board[1][col] && board[0][col] == board[2][col]) {
            return board[0][col];
        }
    }

    // Check for diagonal wins
    if (board[0][0] != null && board[0][0] == board[1][1] && board[0][0] == board[2][2]) {
        return board[0][0];
    }
    if (board[0][2] != null && board[0][2] == board[1][1] && board[0][2] == board[2][0]) {
        return board[0][2];
    }

    // Check for a draw
    boolean isDraw = true;
    for (int row = 0; row < 3; row++) {
        for (int col = 0; col < 3; col++) {
            if (board[row][col] == null) {
                isDraw = false;
                break;
            }
        }
    }
    if (isDraw) {
        return null;
    }

    // Game is still ongoing
    return null;
}

    @Override
    public Player[][] getBoard() {
        Player[][] copy = new Player[3][3];
        for (int i = 0; i < 3; i++) {
            copy[i] = Arrays.copyOf(board[i], board[i].length);
        }
        return copy;
    }

    @Override
    public Player getMarkAt(int r, int c) {
      if (r < 0 || r >= 4) {
        throw new IllegalArgumentException("Invalid row index: " + r);
    }

    if (c < 0 || c >= 4) {
        throw new IllegalArgumentException("Invalid column index: " + c);
    }
      // get a specific player mark at a specific location on the board.
        return board[r][c];
    }
}
