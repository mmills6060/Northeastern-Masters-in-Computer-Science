public class composition {
    private String name;
    
    public TennisPlayer(String name) {
        this.name = name;
    }
    
    public void play() {
        System.out.println(name + " is playing tennis.");
    }

    public static void main(String[] args) {
    }
}

public class TennisRacket {
    private String brand;
    
    public TennisRacket(String brand) {
        this.brand = brand;
    }
    
    public void swing() {
        System.out.println("Swinging the " + brand + " racket.");
    }
}

public class TennisPlayerWithRacket {
    private TennisPlayer player;
    private TennisRacket racket;
    
    public TennisPlayerWithRacket(String playerName, String racketBrand) {
        player = new TennisPlayer(playerName);
        racket = new TennisRacket(racketBrand);
    }
    
    public void playTennis() {
        player.play();
        racket.swing();
    }
}

class Main {
    public static void main(String[] args) {
        TennisPlayerWithRacket player = new TennisPlayerWithRacket("Roger Federer", "Wilson");
        player.playTennis();
    }
}
