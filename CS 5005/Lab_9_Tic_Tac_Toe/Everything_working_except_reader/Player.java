// define an enum player, representing the players (X and O) with a toString() method that returns "X" and "O"
public enum Player {
    X {
        public String toString() {
            return "X";
        }
    },
    O {
        public String toString() {
            return "O";
        }
    }, NONE
}
