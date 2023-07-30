import java.io.IOException;
import java.io.InputStreamReader;

public class Main 
{
  /** Runs a Tic Tac Toe game
 * @throws IOException
 * @throws IllegalStateException
   */
  public static void main(String[] args) throws IllegalStateException, IOException 
  {
    new TicTacToeConsoleController(new InputStreamReader(System.in),
            System.out).playGame(new TicTacToeModel());
  }
}

