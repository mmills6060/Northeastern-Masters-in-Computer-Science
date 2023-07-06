public class Main {
        public static void main(String[] args) {
        TennisPlayerWithRacket player = new TennisPlayerWithRacket("Roger Federer", "Wilson");
        player.playTennis();

        //class design and usage

      TennisPlayer player1 = new TennisPlayer();
        TennisPlayer player2 = new TennisPlayer();
        
        player1.greet();
        player1.serve();
        
        player2.greet();
        player2.serve();
//dynamic and static variables
      TennisCourt court1 = new TennisCourt();
        court1.displayCourtInfo();
        
        TennisCourt court2 = new TennisCourt();
        court2.displayCourtInfo();
        
        TennisCourt court3 = new TennisCourt();
        court3.displayCourtInfo();
    // comments and syntax

        System.out.println("Let's play tennis!");
    // inheritance

        TennisPro player4 = new TennisPro("Roger Federer", 3);
        player.play();
        player.serve();
        System.out.println(player.getName() + "'s ranking: " + player.getRanking());
 
        // constructor
     TennisPlayer player3 = new TennisPlayer();
        System.out.println("Name: " + player.getName());
        System.out.println("Age: " + player.getAge());
    
        // interface
            
        TennisPlayer proPlayer = new ProfessionalPlayer("Roger Federer");
        proPlayer.playTennis();

        TennisPlayer amateurPlayer = new AmateurPlayer("John Doe");
        amateurPlayer.playTennis();

        // dangers_of_inheritance
        TennisPlayer player = new SuperstarPlayer("Roger Federer");
        player.playTennis();
 
        // getter and setter
        TennisPlayer player5 = new TennisPlayer();
        player5.setName("Roger Federer");
        player5.setAge(39);
        System.out.println("Name: " + player5.getName());
        System.out.println("Age: " + player5.getAge());
 
    }

}
