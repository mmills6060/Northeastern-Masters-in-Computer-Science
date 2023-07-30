/**
 * A single game of Tic Tac Toe, played on a three-by-three grid with two players,
 * with the object of the game to achieve three markers in a row either vertically,
 * horizontally, or diagonally. {@link Player} X goes first.
 */
public interface TicTacToe {

    /**
     * Execute a move in the position specified by the given row and column.
     *
     * @param r the row of the intended move
     * @param c the column of the intended move
     * @throws IllegalArgumentException if the space is occupied or the position is otherwise invalid
     * @throws IllegalStateException if the game is over
     */
    void move(int r, int c);

    /**
     * Get the current turn, i.e., the player who will mark on the next call to move().
     *
     * @return the {@link Player} whose turn it is
     */
    Player getTurn();

    /**
     * Return whether the game is over. The game is over when either the board is full, or
     * one player has won.
     *
     * @return true if the game is over, false otherwise
     */
    boolean isGameOver();

    /**
     * Return the winner of the game, or {@code null} if there is no winner. If the game is not
     * over, returns {@code null}.
     *
     * @return the winner, or null if there is no winner
     */
    Player getWinner();

    /**
     * Return the current game state, as a 2D array of Player. A {@code null} value in the grid
     * indicates an empty position on the board.
     *
     * @return the current game board
     */
    Player[][] getBoard();

    /**
     * Return the current {@link Player} mark at a given row and column, or {@code null} if the
     * position is empty.
     *
     * @param r the row
     * @param c the column
     * @return the player at the given position, or null if it's empty
     */
    Player getMarkAt(int r, int c);

}
