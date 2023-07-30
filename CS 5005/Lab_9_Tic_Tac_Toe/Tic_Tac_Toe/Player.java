
/** Public enum Player of either X or O. 
 */
public enum Player {

  X("X"),
  O("O");

  private String player;

  /** Constructor for the Player enums.
   * @param player String of whether the player is X or O.
   */
  Player(String player) {
    this.player = player;
  }

  /** Method to return who the player is in a string.
   * @return a string of who the player is.
   */
  @Override
  public String toString() {
    return this.player;
  }

}