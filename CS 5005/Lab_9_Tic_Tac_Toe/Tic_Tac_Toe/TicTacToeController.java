

/**
 * This is a controller;
 *     
 */
public interface TicTacToeController {

  /**
   * Player game runs for one single game of tic tac toe
   *     .
   *
   * @param m a non-null tic tac toe Modl
   */
  void playGame(TicTacToe m) throws IllegalStateException;
}