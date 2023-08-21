// Define the TennisPlayer interface
interface TennisPlayer {
    void playTennis();
    void watchTennis();
}

// Implement the interface in Player1 class
class Player1 implements TennisPlayer {
    @Override
    public void playTennis() {
        System.out.println("Player1 is playing tennis.");
    }

    @Override
    public void watchTennis() {
        System.out.println("Player1 is watching tennis.");
    }
}

// Implement the interface in Player2 class
class Player2 implements TennisPlayer {
    @Override
    public void playTennis() {
        System.out.println("Player2 is playing tennis.");
    }

    @Override
    public void watchTennis() {
        System.out.println("Player2 is watching tennis.");
    }
}
public class interface {
    public static void main(String[] args) {
        TennisPlayer player1 = new Player1();
        TennisPlayer player2 = new Player2();

        player1.playTennis();
        player1.watchTennis();

        player2.playTennis();
        player2.watchTennis();
}
