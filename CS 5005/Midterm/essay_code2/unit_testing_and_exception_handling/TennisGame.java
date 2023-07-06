package essay_code2.unit_testing_and_exception_handling;

public class TennisGame {

    private int player1Score;
    private int player2Score;

    public TennisGame(String player1Name, String player2Name) {
        // Constructor logic
    }

    public String getScore() {
        String[] scoreNames = { "Love", "15", "30", "40" };
        String player1ScoreName = scoreNames[player1Score];
        String player2ScoreName = scoreNames[player2Score];

        return player1ScoreName + " - " + player2ScoreName;
    }

    public void player1Scores() {
        player1Score++;
    }

    public void player2Scores() {
        player2Score++;
    }

    public void setScore(int player1Score, int player2Score) {
        if (player1Score < 0 || player2Score < 0) {
            throw new IllegalArgumentException("Invalid score value");
        }

        this.player1Score = player1Score;
        this.player2Score = player2Score;
    }
}
