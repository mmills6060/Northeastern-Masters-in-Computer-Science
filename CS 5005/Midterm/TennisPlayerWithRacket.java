public class TennisPlayerWithRacket {
    private TennisPlayer player;
    private TennisRacket racket;
    
    public TennisPlayerWithRacket(String playerName, String racketBrand) {
        player = new TennisPlayer();
        racket = new TennisRacket(racketBrand);
    }
    
    public void playTennis() {
        player.play();
        racket.swing();
    }

    public void play() {
    }

    public void serve() {
    }

    public String getName() {
        return null;
    }

    public String getRanking() {
        return null;
    }

    public String getAge() {
        return null;
    }
}

