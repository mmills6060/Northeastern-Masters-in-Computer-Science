import static org.junit.Assert.assertEquals;
import java.io.StringReader;
import java.util.Arrays;
import org.junit.Test;

/**
 * Test cases for the tic-tac-toe controller, using mocks for readable and appendable.
 */
public class TicTacToeControllerTest {
    @Test
    public void testSingleValidMove() {
        TicTacToe m = new TicTacToeModel();
        StringBuilder gameLog = new StringBuilder();
        TicTacToeController c = new TicTacToeConsoleController(new StringReader("1 1 q"), gameLog);
        c.playGame(m);
        assertEquals("   |   |  \n"
                + "-----------\n"
                + "   |   |  \n"
                + "-----------\n"
                + "   |   |  \n"
                + "Enter a move for X:\n"
                + "   |   |  \n"
                + "-----------\n"
                + "   | X |  \n"
                + "-----------\n"
                + "   |   |  \n"
                + "Enter a move for O:\n"
                + "Game quit! Ending game state:\n"
                + "   |   |  \n"
                + "-----------\n"
                + "   | X |  \n"
                + "-----------\n"
                + "   |   |  \n", gameLog.toString());
    }

    @Test
    public void testBogusInputAsRow() {
        TicTacToe m = new TicTacToeModel();
        StringReader input = new StringReader("!#$ 2 q");
        StringBuilder gameLog = new StringBuilder();
        TicTacToeController c = new TicTacToeConsoleController(input, gameLog);
        c.playGame(m);
        // split the output into an array of lines
        String[] lines = gameLog.toString().split("\n");
        // check that it's the correct number of lines
        assertEquals(12, lines.length);
        // check that the last 6 lines are correct
        String lastMsg = String.join("\n",
                Arrays.copyOfRange(lines, lines.length - 6, lines.length));
        assertEquals("Game quit! Ending game state:\n"
                + "   |   |  \n"
                + "-----------\n"
                + "   |   |  \n"
                + "-----------\n"
                + "   |   |  ", lastMsg);
        // note no trailing \n here, because of the earlier split
    }

    @Test
    public void testTieGame() {
        TicTacToe m = new TicTacToeModel();
        // note the entire sequence of user inputs for the entire game is in this one string:
        StringReader input = new StringReader("1 1 0 0 2 2 0 1 0 2 1 2 1 0 2 0 2 1");
        StringBuilder gameLog = new StringBuilder();
        TicTacToeController c = new TicTacToeConsoleController(input, gameLog);
        c.playGame(m);
        String[] lines = gameLog.toString().split("\n");
        assertEquals(60, lines.length);
        assertEquals("Game is over! Tie game.", lines[lines.length - 1]);
    }

    @Test
    public void testWinningGame() {
        // Play game to completion, where there is a winner
        TicTacToe m = new TicTacToeModel();
        // note the entire sequence of user inputs for the entire game is in this one string:
        StringReader input = new StringReader("0 0 0 1 1 0 1 1 2 0");
        StringBuilder gameLog = new StringBuilder();
        TicTacToeController c = new TicTacToeConsoleController(input, gameLog);
        c.playGame(m);
        String[] lines = gameLog.toString().split("\n");
        assertEquals(36, lines.length);
        assertEquals("Game is over! X wins.", lines[lines.length - 1]);
    }

    @Test
    public void testQInputAsRow() {
        // Input where the q comes instead of an integer for the row
        TicTacToe m = new TicTacToeModel();
        StringReader input = new StringReader("q 2");
        StringBuilder gameLog = new StringBuilder();
        TicTacToeController c = new TicTacToeConsoleController(input, gameLog);
        c.playGame(m);
        assertEquals("   |   |  \n"
                + "-----------\n"
                + "   |   |  \n"
                + "-----------\n"
                + "   |   |  \n"
                + "Enter a move for X:\n"
                + "Game quit! Ending game state:\n"
                + "   |   |  \n"
                + "-----------\n"
                + "   |   |  \n"
                + "-----------\n"
                + "   |   |  \n", gameLog.toString());
    }

    @Test
    public void testQInputAsColumn() {
        // Input where the q comes instead of an integer for the column
        TicTacToe m = new TicTacToeModel();
        StringReader input = new StringReader("2 q");
        StringBuilder gameLog = new StringBuilder();
        TicTacToeController c = new TicTacToeConsoleController(input, gameLog);
        c.playGame(m);
        assertEquals("   |   |  \n"
                + "-----------\n"
                + "   |   |  \n"
                + "-----------\n"
                + "   |   |  \n"
                + "Enter a move for X:\n"
                + "Game quit! Ending game state:\n"
                + "   |   |  \n"
                + "-----------\n"
                + "   |   |  \n"
                + "-----------\n"
                + "   |   |  \n", gameLog.toString());
    }

    @Test
    public void testBogusInputAsRowNoQuit() {
        // Input where non-integer garbage comes instead of an integer for the row
        TicTacToe m = new TicTacToeModel();
        StringReader input = new StringReader("s 0 0 0 1 1 0 1 1 2 0");
        StringBuilder gameLog = new StringBuilder();
        TicTacToeController c = new TicTacToeConsoleController(input, gameLog);
        c.playGame(m);
        String[] lines = gameLog.toString().split("\n");
        assertEquals(43, lines.length);
        assertEquals("Non-integer value entered for row.", lines[6]);
        assertEquals("Game is over! X wins.", lines[lines.length - 1]);
    }
    @Test
    public void testBogusInputAsColumnNoQuit() {
        // Input where non-integer garbage comes instead of an integer for the column
        TicTacToe m = new TicTacToeModel();
        StringReader input = new StringReader("0 s 0 0 1 1 0 1 1 2 0");
        StringBuilder gameLog = new StringBuilder();
        TicTacToeController c = new TicTacToeConsoleController(input, gameLog);
        c.playGame(m);
        String[] lines = gameLog.toString().split("\n");
        assertEquals(43, lines.length);
        assertEquals("Non-integer value entered for column.", lines[6]);
        assertEquals("Game is over! X wins.", lines[lines.length - 1]);
    }

    @Test
    public void testInputIntegersOutsideBounds() {
        // Input where the move is integers, but outside the bounds of the board
        TicTacToe m = new TicTacToeModel();
        StringReader input = new StringReader("0 5 0 0 0 1 1 0 1 1 2 0");
        StringBuilder gameLog = new StringBuilder();
        TicTacToeController c = new TicTacToeConsoleController(input, gameLog);
        c.playGame(m);
        String[] lines = gameLog.toString().split("\n");
        assertEquals(43, lines.length);
        assertEquals("Invalid position: outside of game board.", lines[6]);
        assertEquals("Game is over! X wins.", lines[lines.length - 1]);
    }

    @Test
    public void testInputIntegersCellOccupied() {
        // Input where the move is integers, but invalid because the cell is occupied
        TicTacToe m = new TicTacToeModel();
        StringReader input = new StringReader("0 0 0 0 0 1 1 0 1 1 2 0");
        StringBuilder gameLog = new StringBuilder();
        TicTacToeController c = new TicTacToeConsoleController(input, gameLog);
        c.playGame(m);
        String[] lines = gameLog.toString().split("\n");
        assertEquals(43, lines.length);
        assertEquals("Invalid move: space is occupied.", lines[12]);
        assertEquals("Game is over! X wins.", lines[lines.length - 1]);
    }

    @Test
    public void testMultipleBogusInputRowNoQuit() {
        // Multiple invalid moves in a row of various kinds
        TicTacToe m = new TicTacToeModel();
        StringReader input = new StringReader("s t u v 0 0 0 1 1 0 1 1 2 0");
        StringBuilder gameLog = new StringBuilder();
        TicTacToeController c = new TicTacToeConsoleController(input, gameLog);
        c.playGame(m);
        String[] lines = gameLog.toString().split("\n");
        assertEquals(64, lines.length);
        assertEquals("Non-integer value entered for row.", lines[6]);
        assertEquals("Game is over! X wins.", lines[lines.length - 1]);
    }

    @Test
    public void testMultipleBogusInputColumnNoQuit() {
        // Multiple invalid moves in a row of various kinds
        TicTacToe m = new TicTacToeModel();
        StringReader input = new StringReader("0 s t u v 0 0 1 1 0 1 1 2 0");
        StringBuilder gameLog = new StringBuilder();
        TicTacToeController c = new TicTacToeConsoleController(input, gameLog);
        c.playGame(m);
        String[] lines = gameLog.toString().split("\n");
        assertEquals(64, lines.length);
        assertEquals("Non-integer value entered for column.", lines[6]);
        assertEquals("Game is over! X wins.", lines[lines.length - 1]);
    }

    @Test
    public void testMultipleBogusInputNoQuit() {
        // Input including valid moves interspersed with invalid moves, game is played to completion
        TicTacToe m = new TicTacToeModel();
        StringReader input = new StringReader("0 s 0 t 0 1 u 1 v 0 1 x 1 2 0");
        StringBuilder gameLog = new StringBuilder();
        TicTacToeController c = new TicTacToeConsoleController(input, gameLog);
        c.playGame(m);
        String[] lines = gameLog.toString().split("\n");
        assertEquals(71, lines.length);
        assertEquals("Non-integer value entered for column.", lines[6]);
        assertEquals("Game is over! X wins.", lines[lines.length - 1]);
    }
}
