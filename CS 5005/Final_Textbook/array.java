
class TennisPlayer {
    String name;
    int rank;

    public TennisPlayer(String name, int rank) {
        this.name = name;
        this.rank = rank;
    }

    public void playMatch() {
        System.out.println(name + " is playing a match.");
        // Implement the logic to play the match here
    }

    public void watchMatch() {
        System.out.println(name + " is watching a match.");
        // Implement the logic to watch the match here
    }
}

public class array {
    public static void main(String[] args) {
        TennisPlayer[] players = new TennisPlayer[8]; // Array to store 8 players

        players[0] = new TennisPlayer("PlayerA", 1);
        players[1] = new TennisPlayer("PlayerB", 2);
        players[2] = new TennisPlayer("PlayerC", 3);
        players[3] = new TennisPlayer("PlayerD", 4);
        players[4] = new TennisPlayer("PlayerE", 5);
        players[5] = new TennisPlayer("PlayerF", 6);
        players[6] = new TennisPlayer("PlayerG", 7);
        players[7] = new TennisPlayer("PlayerH", 8);

        // Accessing players by index
        int playerIndex = 3; // For example, access PlayerD
        TennisPlayer player = players[playerIndex];
        System.out.println("Accessed player: " + player.name);

        // Example: Playing a match
        player.playMatch();

        // Example: Watching a match
        player.watchMatch();
    }
}