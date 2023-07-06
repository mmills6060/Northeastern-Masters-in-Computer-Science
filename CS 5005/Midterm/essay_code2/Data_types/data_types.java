// This code displays the results of a tennis match. 
//It displays the players' scores, the match duration, whether or not there was a tiebreak, 
// and the winner's initial.


package essay_code2.Data_types;
public class data_types {
    public static void main(String[] args) {
        int player1Score = 3;
        int player2Score = 2;
        float matchDuration = 1.5f;
        boolean isTiebreak = false;
        char winnerInitial = 'A';
        
        System.out.println("Tennis Match Result:");
        System.out.println("Player 1 Score: " + player1Score);
        System.out.println("Player 2 Score: " + player2Score);
        System.out.println("Match Duration: " + matchDuration + " hours");
        System.out.println("Is Tiebreak? " + isTiebreak);
        System.out.println("Winner Initial: " + winnerInitial);
    }
}
