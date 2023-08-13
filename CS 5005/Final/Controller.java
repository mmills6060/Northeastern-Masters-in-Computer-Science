import java.util.List;
import java.util.Random;
import java.util.ArrayList;

// Controller
class TennisMatchController {
    private TennisMatchModel model;
    private TennisMatchView view;
    public TennisMatchController(TennisMatchModel model, TennisMatchView view) {
        this.model = model;
        this.view = view;
    }

    public void run() {
        while (true) {
            boolean matchplayStarted = false;
            if (matchplayStarted = true) {
                view.displayMatches(model.getMatches());
            }
            view.displayPlayers(model.getPlayers());
            view.displayCourts(model.getCourts());
            int choice = view.getInput();
            switch (choice) {
                case 1:
                    String playerName = view.getPlayerName();
                    model.addPlayer(playerName);
                    break;
                case 2:
                    model.addCourt();
                    break;
                case 3:
                    if (model.getPlayers().size() < 2) {
                        System.out.println("Add at least two players before starting matchplay.");
                        break;
                    }
                    if (model.getCourts().isEmpty()) {
                        System.out.println("Add at least one court before starting matchplay.");
                        break;
                    }
                    startMatchplay();
                    break;
                case 4:
                    List<Match> matches = model.getMatches();
                    view.displayMatches(matches);
                    int matchIndex = view.getMatchIndex(matches);
                    if (matchIndex != -1) {
                        PlayerScores scores = view.getScores(); 
                        Match match = matches.get(matchIndex);
                        match.player1.points += scores.player1Score;
                        match.player2.points += scores.player2Score;
                        match.court.isOccupied = false;
                        model.recordScore(match.player1, match.player2, scores.player1Score, scores.player2Score);
                        matches.remove(matchIndex);

                        // Update match combinations
                        updateMatchCombinations(match.player1, match.player2);

                        // Check if all matches have been played
                        if (matches.isEmpty()) {
                            System.out.println("All matches have been played.");
                            List<Player> players = model.getPlayers();
                            players.sort((p1, p2) -> Integer.compare(p2.points, p1.points));
                            view.displayResults(players);
                            break;
                        }
                    }
                    break;
                case 5:
                    List<Player> players = model.getPlayers();
                    players.sort((p1, p2) -> Integer.compare(p2.points, p1.points));
                    view.displayResults(players);
                    break;
                case 6:
                    System.out.println("Exiting...");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please select again.");
            }
        }
    }

private void startMatchplay() {
    boolean matchplayStarted = true;
    List<Player> players = model.getPlayers();
    List<Court> courts = model.getCourts();
    Random random = new Random();

    // Shuffle players to randomize match order
    java.util.Collections.shuffle(players);

    int totalMatches = (players.size() * (players.size() - 1)) / 2; // Total possible matches

    List<Integer> playedMatches = new ArrayList<>(); // Store played matches

    // Iterate through players and try to match them up
    for (int i = 0; i < players.size(); i++) {
        Player player1 = players.get(i);
        for (int j = i + 1; j < players.size(); j++) {
            Player player2 = players.get(j);

            // Check if this match has already been played or if players are already playing
            int matchId = getMatchId(player1.id, player2.id);
            if (!playedMatches.contains(matchId) && !isPlayerPlaying(player1) && !isPlayerPlaying(player2)) {
                Court court = getAvailableCourt(courts);
                if (court != null) {
                    model.addMatch(player1, player2, court, -1); // Pass -1 as matchIndex
                    playedMatches.add(matchId);
                }
            }

            // Break if all possible matches have been played
            if (playedMatches.size() == totalMatches) {
                break;
            }
        }

        // Break if all possible matches have been played
        if (playedMatches.size() == totalMatches) {
            break;
        }
    }
}
    private void updateMatchCombinations(Player player1, Player player2) {
        List<Court> courts = model.getCourts();
        List<Integer> playedMatches = new ArrayList<>();

        // Generate a list of IDs for played matches
        for (Match match : model.getMatches()) {
            int matchId = getMatchId(match.player1.id, match.player2.id);
            playedMatches.add(matchId);
        }

        // Iterate through players and try to match them up
        for (Player newPlayer : model.getPlayers()) {
            if (newPlayer != player1 && newPlayer != player2) {
                // Check if this match has already been played or if the player is already playing
                int matchId1 = getMatchId(newPlayer.id, player1.id);
                int matchId2 = getMatchId(newPlayer.id, player2.id);
                if (!playedMatches.contains(matchId1) && !playedMatches.contains(matchId2)
                        && !isPlayerPlaying(newPlayer)) {
                    Court court = getAvailableCourt(courts);
                    if (court != null) {
                        model.addMatch(newPlayer, player1, court, -1); // Pass -1 as matchIndex
                        playedMatches.add(matchId1);
                    }
                }
            }
        }
    }

    private boolean isPlayerPlaying(Player player) {
        for (Match match : model.getMatches()) {
            if (match.player1 == player || match.player2 == player) {
                return true;
            }
        }
        return false;
    }
private int getMatchId(int player1Id, int player2Id) {
    // Assuming player1Id < player2Id
    return player1Id * 100 + player2Id;
}
    private Court getAvailableCourt(List<Court> courts) {
        for (Court court : courts) {
            if (!court.isOccupied) {
                return court;
            }
        }
        return null;
    }
}