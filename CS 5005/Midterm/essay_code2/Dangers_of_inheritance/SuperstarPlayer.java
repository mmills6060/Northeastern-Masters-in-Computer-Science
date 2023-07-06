// This code creates a SuperstarPlayer object that is a subclass of ProfessionalPlayer and
// has a method called playTennis() that prints "Playing tennis like a superstar."

package essay_code2.Dangers_of_inheritance;


class SuperstarPlayer extends ProfessionalPlayer {
    public SuperstarPlayer(String name) {
        super(name);
    }
    
    public void playTennis() {
        System.out.println("Playing tennis like a superstar.");
    }
}