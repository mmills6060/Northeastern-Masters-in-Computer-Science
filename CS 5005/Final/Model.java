import java.util.ArrayList;
import java.util.List;

// Model: Player
class Player {
    String name;
    int id;
    int points;

    public Player(String name, int id) {
        this.name = name;
        this.id = id;
        this.points = 0;
    }
}

// Model: Court
class Court {
    boolean isOccupied;
    int courtNumber;
    public Court(int courtNumber) {
        this.isOccupied = false;
        this.courtNumber = courtNumber;
    }
}

// Model: Match
class Match {
    Player player1;
    Player player2;
    Court court;
    int matchIndex;

    public Match(Player player1, Player player2, Court court, int matchIndex) {
        this.player1 = player1;
        this.player2 = player2;
        this.court = court;
        this.matchIndex = matchIndex;
    }
}
class PlayerScores {
    int player1Score;
    int player2Score;

    public PlayerScores(int player1Score, int player2Score) {
        this.player1Score = player1Score;
        this.player2Score = player2Score;
    }
}
// Model
class TennisMatchModel {
    private List<Player> players;
    private List<Court> courts;
    private List<Match> matches;
    private int[][] scores;
    public TennisMatchModel() {
        players = new ArrayList<>();
        courts = new ArrayList<>();
        matches = new ArrayList<>();
        scores = new int[100][100];
    }

    public void addPlayer(String playerName) {
        int playerId = players.size(); // Assign an ID to each player
        players.add(new Player(playerName, playerId));
    }

    public void addCourt() {
        int courtNumber = courts.size();
        courts.add(new Court(courtNumber));
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

    public void recordScore(Player player1, Player player2, int player1Score, int player2Score) {
        scores[player1.id][player2.id] = player1Score;
        scores[player2.id][player1.id] = player2Score;
    }

    public int getScore(Player player1, Player player2) {
        return scores[player1.id][player2.id];
    }
    public void addMatch(Player player1, Player player2, Court court, int matchIndex) {
        if (court.isOccupied) {
            System.out.println("Court is already occupied.");
            return;
        }

        Match match = new Match(player1, player2, court, matchIndex);
        matches.add(match);
        court.isOccupied = true;
    }

    public List<Match> addMatch() {
        List<Match> matches = new ArrayList<>();
        for (int i = 0; i < players.size(); i += 2) {
            matches.add(new Match(players.get(i), players.get(i + 1), courts.get(i / 2), matches.size()));
        }
        return matches;
    }
}



