import java.io.StringReader;

public class Main {
    public static void main(String[] args) {
        // Create a TicTacToeModel instance
        TicTacToeModel model = new TicTacToeModel();

        // Create a StringReader with initial input (empty string)
        StringReader inputSource = new StringReader("");

        // Create a StringBuilder for output
        StringBuilder outputDestination = new StringBuilder();

        // Create a TicTacToeConsoleController instance with StringReader and StringBuilder as input/output sources
        TicTacToeConsoleController controller = new TicTacToeConsoleController(model, inputSource);

        // Start the game
        controller.playGame();

    }
}
