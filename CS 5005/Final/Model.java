import java.util.ArrayList;
import java.util.List;

// Model: Player
class Player {
    String name;
    int points;

    public Player(String name) {
        this.name = name;
        this.points = 0;
    }
}

// Model: Court
class Court {
    boolean isOccupied;

    public Court() {
        this.isOccupied = false;
    }
}

// Model: Match
class Match {
    Player player1;
    Player player2;
    Court court;

    public Match(Player player1, Player player2, Court court) {
        this.player1 = player1;
        this.player2 = player2;
        this.court = court;
    }
}

// Model
class TennisMatchModel {
    private List<Player> players;
    private List<Court> courts;
    private List<Match> matches;

    public TennisMatchModel() {
        players = new ArrayList<>();
        courts = new ArrayList<>();
        matches = new ArrayList<>();
    }

    public void addPlayer(String playerName) {
        players.add(new Player(playerName));
    }

    public void addCourt() {
        courts.add(new Court());
    }

    public List<Player> getPlayers() {
        return players;
    }

    public List<Court> getCourts() {
        return courts;
    }

    public List<Match> getMatches() {
        return matches;
    }


}


