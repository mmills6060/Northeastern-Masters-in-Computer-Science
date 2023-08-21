import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class TennisPlayer implements Comparable<TennisPlayer> {
    private String name;
    private int score;

    public TennisPlayer(String name, int score) {
        this.name = name;
        this.score = score;
    }

    public int getScore() {
        return score;
    }

    @Override
    public int compareTo(TennisPlayer other) {
        // Compare based on scores in descending order
        return Integer.compare(other.score, this.score);
    }

    @Override
    public String toString() {
        return name + " (" + score + ")";
    }
}

public class PlayerRanking {
    public static void main(String[] args) {
        List<TennisPlayer> players = new ArrayList<>();
        players.add(new TennisPlayer("PlayerA", 1800));
        players.add(new TennisPlayer("PlayerB", 1500));
        players.add(new TennisPlayer("PlayerC", 2100));
        players.add(new TennisPlayer("PlayerD", 1700));

        Collections.sort(players);

        System.out.println("Player Rankings:");
        int rank = 1;
        for (TennisPlayer player : players) {
            System.out.println(rank + ". " + player);
            rank++;
        }
    }
}
