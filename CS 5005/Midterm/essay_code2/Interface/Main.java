package essay_code2.Interface;


class Main {
    public static void main(String[] args) {
        TennisPlayer proPlayer = new ProfessionalPlayer("Roger Federer");
        proPlayer.playTennis();

        TennisPlayer amateurPlayer = new AmateurPlayer("John Doe");
        amateurPlayer.playTennis();
    }
}
