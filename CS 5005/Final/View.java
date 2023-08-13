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

    public int getMatchIndex(List<Match> matches) {
        System.out.println("Enter match index to enter score: ");
        int matchIndex = scanner.nextInt();
        if (matchIndex < 0 || matchIndex >= matches.size()) {
            System.out.println("Invalid match index.");
            return -1;
        }
        return matchIndex;
    }

    public int getScore() {
        System.out.print("Enter score: ");
        return scanner.nextInt();
    }

    public void displayResults(List<Player> players) {
        System.out.println("Results:");
        for (int i = 0; i < players.size(); i++) {
            System.out.println((i + 1) + ". " + players.get(i).name + " - " + players.get(i).points + " points");
        }
    }
}
