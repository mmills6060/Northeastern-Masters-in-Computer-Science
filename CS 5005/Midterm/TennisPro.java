public class TennisPro extends TennisPlayer {
    private int ranking;
    
    public TennisPro(String name, int ranking) {
        super();
        this.ranking = ranking;
    }
    
    public void serve() {
        System.out.println(getName() + " serves with precision.");
    }
    
    private String getName() {
        return null;
    }

    public int getRanking() {
        return ranking;
    }
}
