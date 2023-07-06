public class constructor {
    private String name;
    private int age;
    
    public TennisPlayer(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String getName() {
        return name;
    }
    
    public int getAge() {
        return age;
    }
    
    public static void main(String[] args) {
        TennisPlayer player = new TennisPlayer("Roger Federer", 39);
        System.out.println("Name: " + player.getName());
        System.out.println("Age: " + player.getAge());
    }
}
