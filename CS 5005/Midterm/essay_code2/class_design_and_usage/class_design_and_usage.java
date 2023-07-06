package essay_code2.class_design_and_usage;

public class class_design_and_usage {
    private String name;
    // Constructor to initialize object properties
    public void TennisPlayer(String name, int age) {
        this.name = name;
    }
   // two methods within this class, one to greet and one to show the serve status. 
    public void greet() {
        System.out.println("Hello, I'm " + name + "! Let's play tennis!");
    }
    
    public void serve() {
        System.out.println(name + " serves the ball with power!");
    }
}