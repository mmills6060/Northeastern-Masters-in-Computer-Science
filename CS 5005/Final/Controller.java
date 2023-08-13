import java.util.List;
import java.util.Random;
import java.util.ArrayList;

// Controller
class TennisMatchController {
    private TennisMatchModel model;
    private TennisMatchView view;
    private List<Match> matches;
    public TennisMatchController(TennisMatchModel model, TennisMatchView view) {
        this.model = model;
        this.view = view;
        this.matches = new ArrayList<>();
    }

    public void run() {
        while (true) {
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
                    int matchIndex = view.getMatchIndex(matches);
                    if (matchIndex != -1) {
                        int score = view.getScore();
                        Match match = matches.get(matchIndex);
                        match.player1.points += score;
                        match.court.isOccupied = false;
                        matches.remove(matchIndex);
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
        List<Player> players = model.getPlayers();
        List<Court> courts = model.getCourts();
        Random random = new Random();

        // Shuffle players to randomize match order
        java.util.Collections.shuffle(players);

        // Create matches between players and assign courts
        for (int i = 0; i < players.size(); i += 2) {
            if (i + 1 < players.size()) {
                Player player1 = players.get(i);
                Player player2 = players.get(i + 1);
                Court court = getAvailableCourt(courts);
                if (court != null) {
                    matches.add(new Match(player1, player2, court));
                    court.isOccupied = true;
                }
            }
        }
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