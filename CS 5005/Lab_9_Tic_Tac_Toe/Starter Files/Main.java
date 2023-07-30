import java.io.InputStreamReader;

/**
 * Run a Tic Tac Toe game interactively on the console.
 */
public class Main {
    /**
     * Run a Tic Tac Toe game interactively on the console.
     */
    public static void main(String[] args) {
        new TicTacToeConsoleController(new InputStreamReader(System.in),
                System.out).playGame(new TicTacToeModel());
    }
}
