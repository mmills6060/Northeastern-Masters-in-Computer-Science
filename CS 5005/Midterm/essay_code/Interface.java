interface Interface {
    void playTennis();
}

class ProfessionalPlayer implements TennisPlayer {
    private String name;

    public ProfessionalPlayer(String name) {
        this.name = name;
    }

    @Override
    public void playTennis() {
        System.out.println(name + " is playing tennis as a professional player.");
    }
}

class AmateurPlayer implements TennisPlayer {
    private String name;

    public AmateurPlayer(String name) {
        this.name = name;
    }

    @Override
    public void playTennis() {
        System.out.println(name + " is playing tennis as an amateur player.");
    }
}

class Main {
    public static void main(String[] args) {
        TennisPlayer proPlayer = new ProfessionalPlayer("Roger Federer");
        proPlayer.playTennis();

        TennisPlayer amateurPlayer = new AmateurPlayer("John Doe");
        amateurPlayer.playTennis();
    }
}
