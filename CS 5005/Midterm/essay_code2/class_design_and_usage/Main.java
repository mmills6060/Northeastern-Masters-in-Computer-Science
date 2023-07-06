package essay_code2.class_design_and_usage;

public class Main {
        
    public static void main(String[] args) {
        TennisPlayer player1 = new TennisPlayer();
        TennisPlayer player2 = new TennisPlayer();
        
        player1.greet();
        player1.serve();
        
        player2.greet();
        player2.serve();
    }
}
