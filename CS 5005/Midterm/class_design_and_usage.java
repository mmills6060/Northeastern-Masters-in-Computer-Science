public class class_design_and_usage {
    private String name;
    private int age;
   // Constructor to initialize object properties
    public void TennisPlayer(String name, int age) {
        this.name = name;
        this.age = age;
    }
   // two methods within this class, one to greet and one to show the serve status. 
    public void greet() {
        System.out.println("Hello, I'm " + name + "! Let's play tennis!");
    }
    
    public void serve() {
        System.out.println(name + " serves the ball with power!");
    }
    
    public static void main(String[] args) {
        TennisPlayer player1 = new TennisPlayer();
        TennisPlayer player2 = new TennisPlayer();
        
        player1.greet();
        player1.serve();
        
        player2.greet();
        player2.serve();
    }
}
// main