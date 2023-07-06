public class composition {
    private String name;
    
    public void TennisPlayer(String name) {
        this.name = name;
    }
    
    public void play() {
        System.out.println(name + " is playing tennis.");
    }

    public static void main(String[] args) {
    }
}


