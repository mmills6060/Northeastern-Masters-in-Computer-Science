

import java.io.IOException;
import java.util.Objects;
import java.util.Scanner;

/** The TicTacToeConsoleController class for the view.
 */
public class TicTacToeConsoleController implements TicTacToeController {

  private Appendable a;
  private Scanner scanner;

  /** Constructor for the TicTacToeConsoleController class.
   * @param r a readable object.
   * @param a an appendable object.
   */
  public TicTacToeConsoleController(Readable r, Appendable a) {

    this.a = a;
    this.scanner = new Scanner(r);
  }

  /** Method to check if inputted value is valid input.
   * @param inp string of input from user.
   * @return boolean if input is valid.
   */
  private boolean isValidInput(String inp) {
    if (inp.equalsIgnoreCase("q")) {
      return true;
    } else {
      int num;
      try {
        num = Integer.parseInt(inp);
      } catch (NumberFormatException i) {
        return false;
      }
    }
    return true;
  }

  String token;
  String token2;


  /** Method to actually play the game.
   * @param m a non-null tic tac toe Model.
   * @throws IllegalStateException if errors arise.
   */
  @Override
  public void playGame(TicTacToe m) throws IllegalStateException {
    Objects.requireNonNull(m);
    boolean flag = false;

    try {
      a.append(m.toString()).append("\n");
    } catch (IOException e) {
      throw new IllegalStateException("error");
    }

    while (!m.isGameOver()) {

      if (!flag) {
        try {
          a.append("Enter a move for ").append(m.getTurn().toString()).append(":").append("\n");
        } catch (IOException i) {
          throw new IllegalStateException("error");
        }
      }

      token = scanner.next();
      if (!isValidInput(token)) {
        token = "q";
        try {
          a.append("Non-integer value entered for row.").append("\n");
        } catch (IOException e) {
          throw new IllegalStateException("error");
        }
      }
      if (token.equalsIgnoreCase("q")) {
        break;
      }

      token2 = scanner.next();
      if (!isValidInput(token2)) {
        token2 = "q";
        try {
          a.append("Non-integer value entered for column.").append("\n");
        } catch (IOException i) {
          throw new IllegalStateException("error");
        }
      }
      if (token2.equalsIgnoreCase("q")) {
        break;
      }

      try {
        int num1 = Integer.parseInt(token) - 1;
        int num2 = Integer.parseInt(token2) - 1;
        m.move(num1, num2);
      } catch (IllegalArgumentException e) {
        try {
          a.append("Not valid move").append(String.valueOf(scanner)).append("\n");
          flag = true;
        } catch (IOException i) {
          throw new IllegalStateException("error");
        }
      }

      try {
        a.append(m.toString()).append("\n");
      } catch (IOException i) {
        throw new IllegalStateException("error");
      }

      if (flag) {
        break;
      }
    }

    if (!m.isGameOver() && token.equalsIgnoreCase("q")) {
      try {
        a.append("Game quit! Ending game state:\n").append(m.toString()).append("\n");
      } catch (IOException i) {
        throw new IllegalStateException("error");
      }

        }    else if (!m.isGameOver() && token2.equalsIgnoreCase("q")) {
      try {
        a.append("Game quit! Ending game state:\n").append(m.toString()).append("\n");
      } catch (IOException i) {
        throw new IllegalStateException("error");
      }
 
    } else if (!m.isGameOver()) {
          try {
            a.append("Game is over!").append(" X wins.").append("\n");
        } catch (IOException e) {
            e.printStackTrace();
        }
    } else {
      if (m.getWinner() == null) {
        try {
          a.append("Game is over!").append(" Tie game.").append("\n");
        } catch (IOException e) {
          throw new IllegalStateException("error");
        }
      } else if (m.getWinner().toString().equals("X")) {
        try {
          a.append(m.toString()).append("\n").append("Game is Over!").append("Player X wins!")
                  .append("\n");
        } catch (IOException i) {
          throw new IllegalStateException("error");
        }
      } else {
        try {
          a.append(m.toString()).append("\n").append("Game is Over!").append("Player O Wins!")
                  .append("\n");
        } catch (IOException a) {
          throw new IllegalStateException("error");
        }
      }
    }
  }
  }