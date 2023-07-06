public class dangers_of_inheritance {
   private String name;
    
    public TennisPlayer(String name) {
        this.name = name;
    }
    
    public void playTennis() {
        System.out.println(name + " is playing tennis.");
    }

    public static void main(String[] args) {
    }
}

class ProfessionalPlayer extends TennisPlayer {
    public ProfessionalPlayer(String name) {
        super(name);
    }
    
    public void playTennis() {
        System.out.println("Playing tennis like a professional.");
    }
}

class SuperstarPlayer extends ProfessionalPlayer {
    public SuperstarPlayer(String name) {
        super(name);
    }
    
    public void playTennis() {
        System.out.println("Playing tennis like a superstar.");
    }
}
