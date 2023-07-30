/**
 * Represents a Controller for Tic Tac Toe: handle user moves by executing them using the model;
 * convey move outcomes to the user in some form.
 */
public interface TicTacToeController {

    /**
     * Execute a single game of tic-tac-toe given a tic-tac-toe Model. When the game is over,
     * the playGame method ends.
     *
     * @param m a non-null tic tac toe Model
     */
    void playGame(TicTacToe m) throws IllegalStateException;
}
