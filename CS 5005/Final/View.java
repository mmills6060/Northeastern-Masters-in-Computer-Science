import java.util.List;
import java.util.Scanner;

// View
class TennisMatchView {
    private Scanner scanner;

    public TennisMatchView() {
        this.scanner = new Scanner(System.in);
    }

    public int getInput() {
        System.out.println("1. Add Player");
        System.out.println("2. Add Court");
        System.out.println("3. Start Matchplay");
        System.out.println("4. Enter Score");
        System.out.println("5. Display Results");
        System.out.println("6. Exit");
        System.out.print("Select an option: ");
        return scanner.nextInt();
    }

    public String getPlayerName() {
        System.out.print("Enter player name: ");
        scanner.nextLine(); // Consume newline
        return scanner.nextLine();
    }
    public void displayPlayers(List<Player> players) {
        System.out.println("Current Players:");
        for (int i = 0; i < players.size(); i++) {
            System.out.println((i + 1) + ". " + players.get(i).name);
        }
        System.out.println(" ");
    }
    public void displayCourts(List<Court> courts) {
        System.out.println("Current Courts:");
        for (int i = 0; i < courts.size(); i++) {
            System.out.println( "Court #" + (((courts.get(i).courtNumber) + 1)));
        }
        System.out.println(" ");
    }
    public int getMatchIndex(List<Match> matches) {
        System.out.print("Enter match index: ");
        int userInput = scanner.nextInt();

        // If user input is 1, treat it as index 0
        if (userInput == 1) {
            return 0;
        }

        // Subtract 1 from user input to convert it to a zero-based index
        return userInput - 1;
    }

    public PlayerScores getScores() {
        System.out.print("Enter score for player 1: ");
        int player1Score = scanner.nextInt();
        System.out.print("Enter score for player 2: ");
        int player2Score = scanner.nextInt();
        return new PlayerScores(player1Score, player2Score);
    }

    public void displayResults(List<Player> players) {
        System.out.println("Results:");
        for (int i = 0; i < players.size(); i++) {
            System.out.println((i + 1) + ". " + players.get(i).name + " - " + players.get(i).points + " points");
        }
        System.out.println(" ");
    }

    public void displayMatches(List<Match> matches) {
        System.out.println("Current Matches being played:");
        for (int i = 0; i < matches.size(); i++) {
            System.out.println((i + 1) + ". " + matches.get(i).player1.name + " vs " + matches.get(i).player2.name);
        }
        System.out.println(" ");
    }
}
