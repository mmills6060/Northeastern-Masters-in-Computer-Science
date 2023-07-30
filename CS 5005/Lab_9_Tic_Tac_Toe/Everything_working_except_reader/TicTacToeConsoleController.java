import java.io.IOException;
import java.io.Reader;
import java.util.Scanner;

public class TicTacToeConsoleController implements TicTacToeController {

    private TicTacToe model;
    private Scanner scanner;

    public TicTacToeConsoleController(TicTacToe model, Readable input) {
        this.model = model;
        this.scanner = new Scanner(System.in); // Cast the Readable input to Reader for Scanner
        // cast the readable input to reader for scanner
    }
    @Override
    public void playGame() {
        try {
            while (!model.isGameOver()) {
                outputGameState();
                System.out.print("Enter a move for " + model.getTurn().toString() + ": ");
                try {
                    // Set the delimiter to include space character in addition to the default delimiters
                    String input = scanner.nextLine();
                    // if the input contains "q", exit the program   
                    if (input.contains("q")) {
                        System.out.println("Game quit! Ending game state:");
                        break;
                    }
                    // take the two numbers from the input and assign them to int r and int c, the two variables are separated by a space
                    String row = input.substring(0, 1);
                    String column = input.substring(2, 3);

                    // convert String row and String column to type int
                    int r = Integer.parseInt(row);
                    int c = Integer.parseInt(column);
                    // call move() method 
                    model.move(r, c);
                    model.getTurn();
                } catch (Exception e) {
                    System.out.println("An error occurred during the game: " + e.getMessage());
                }

            }
            outputGameState();
        } catch (IOException e) {
            model.getTurn();
            System.out.println(e.getMessage());
        }
            }
                    
    
    private void outputGameState() throws IOException {
        System.out.println(model.toString());
    }
}
