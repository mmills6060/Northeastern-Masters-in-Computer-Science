package essay_code2.Getters_and_setter;

public class Main {
        
    public static void main(String[] args) {
        TennisPlayer player = new TennisPlayer();
        player.setName("Roger Federer");
        player.setAge(39);
        System.out.println("Name: " + player.getName());
        System.out.println("Age: " + player.getAge());
    }
}