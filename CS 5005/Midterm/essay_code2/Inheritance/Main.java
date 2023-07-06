package essay_code2.Inheritance;

class Main {
    public static void main(String[] args) {
        TennisPro player = new TennisPro("Roger Federer", 3);
        player.play();
        player.serve();
        System.out.println(player.getName() + "'s ranking: " + player.getRanking());
    }
}
