package essay_code2.Dangers_of_inheritance;

class ProfessionalPlayer extends TennisPlayer {
    public ProfessionalPlayer(String name) {
        super(name);
    }
    
    public void playTennis() {
        System.out.println("Playing tennis like a professional.");
    }
}