package essay_code2.Composition;

public class TennisPlayerWithRacket {
    private TennisPlayer player;
    private TennisRacket racket;
    
    // Constructor method
    public TennisPlayerWithRacket(String playerName, String racketBrand) {
        // Create a TennisPlayer object using the player name
        player = new TennisPlayer(playerName);
        // Create a TennisRacket object using the racket brand
        racket = new TennisRacket(racketBrand);
    }
    
    // Play tennis by calling the TennisPlayer and TennisRacket object methods
    public void playTennis() {
        player.play();
        racket.swing();
    }
}

