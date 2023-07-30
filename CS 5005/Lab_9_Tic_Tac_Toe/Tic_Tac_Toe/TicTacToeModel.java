import java.util.Arrays;
import java.util.stream.Collectors;

/** Public class for the TicTacToeModel.
 */
public class TicTacToeModel implements TicTacToe {

  private Player[][] board;
  private Player player;
  private Player winner;

  /** Constructor for the TicTacToeModel class.
   */
  public TicTacToeModel() {
    this.board = new Player[3][3];
    this.player = Player.X;
    this.winner = null;
  }


  /** Method to return the board.
   * @return a string of the board.
   */
  @Override
  public String toString() {
    // Using Java stream API to save code:
    return Arrays.stream(getBoard()).map(
            row -> " " + Arrays.stream(row).map(
                    p -> p == null ? " " : p.toString()).collect(Collectors.joining(" | ")))
            .collect(Collectors.joining("\n-----------\n"));
  }

  /** Method for the current player to mark a place on the board.
   * @param r the row of the intended move.
   * @param c the column of the intended move.
   */
  @Override
  public void move(int r, int c) {
    if (r > 2 || r < 0 || c > 2 || c < 0) {
      throw new IllegalArgumentException("Selection is not valid.");
    } else if (board[r][c] != null) {
      throw new IllegalArgumentException("This spot is already taken");
    } else if (isGameOver()) {
      throw new IllegalStateException("Game is over!");
    } else {
      board[r][c] = this.player;

      if (this.player == Player.X) {
        this.player = Player.O;
      } else {
        this.player = Player.X;
      }

      if (isGameOver()) {
        getWinner();
      }
    }
  }

  /** Method to return who the current player's turn is.
   * @return the player whose turn it is.
   */
  @Override
  public Player getTurn() {
    return this.player;
  }

  /** Method to determine if the game is over.
   * @return boolean if the game is over.
   */
  @Override
  public boolean isGameOver() {
    this.winner = getWinner();
    if (this.winner != null) {
      return true;
    }

    for (Player[] each : board) {
      for (Player check : each) {
        if (check == null) {
          return false;
        }
      }
    }
    return true;
  }

  /** Method to determine who the winner is, if there is one.
   * @return string of which player is the winner.
   */
  @Override
  public Player getWinner() {
    for (int i = 0; i < 2; i++) {
      if (board[i][0] != null && board[i][0] == board[i][1] && board[i][1] == board[i][2]) {
        return board[i][0];
      }
    }
    for (int j = 0; j < 2; j++) {
      if (board[0][j] != null && board[0][j] == board[1][j] && board[1][j] == board[2][j]) {
        return board[0][j];
      }
    }

    if (board[0][0] != null && board[0][0] == board[1][1] && board[1][1] == board[2][2]) {
      return board[0][0];
    } else if (board[2][0] != null && board[2][0] == board[1][1] && board[1][1] == board[0][2]) {
      return board[2][0];
    }
    return null;
  }

  /** Method to get the current board, and create a deep copy for a new variable.
   * @return a deep copy of the current board.
   */
  @Override
  public Player[][] getBoard() {
    Player[][] newBoard = new Player[3][3];
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        newBoard[i][j] = board[i][j];
      }
    }
    return newBoard;
  }

  /** Method to retrieve a board place's status.
   * @param r the row.
   * @param c the column.
   * @return the mark on the board's place, or null if no mark.
   */
  @Override
  public Player getMarkAt(int r, int c) {
    if (r > 2 || r < 0 || c > 2 || c < 0) {
      throw new IllegalArgumentException("Out of board's bounds.");
    }
    if (board[r][c] == null) {
      return null;
    }
    return board[r][c];
  }

}
