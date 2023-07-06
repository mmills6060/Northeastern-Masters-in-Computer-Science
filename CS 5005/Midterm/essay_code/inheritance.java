public class inheritance {
    private String name;
    
    public void TennisPlayer(String name) {
        this.name = name;
    }
    
    public void play() {
        System.out.println(name + " is playing tennis.");
    }

    public static void main(String[] args) {
    }
}

public class TennisPro extends TennisPlayer {
    private int ranking;
    
    public TennisPro(String name, int ranking) {
        super(name);
        this.ranking = ranking;
    }
    
    public void serve() {
        System.out.println(getName() + " serves with precision.");
    }
    
    public int getRanking() {
        return ranking;
    }
}

class Main {
    public static void main(String[] args) {
        TennisPro player = new TennisPro("Roger Federer", 3);
        player.play();
        player.serve();
        System.out.println(player.getName() + "'s ranking: " + player.getRanking());
    }
}
