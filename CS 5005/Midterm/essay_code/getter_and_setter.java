public class getter_and_setter {
    
    private String name;
    private int age;
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public int getAge() {
        return age;
    }
    
    public void setAge(int age) {
        this.age = age;
    }
    
    public static void main(String[] args) {
        TennisPlayer player = new TennisPlayer();
        player.setName("Roger Federer");
        player.setAge(39);
        System.out.println("Name: " + player.getName());
        System.out.println("Age: " + player.getAge());
    }
}
