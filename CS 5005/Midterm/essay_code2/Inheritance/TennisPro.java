// This code creates a class called TennisPro that extends the TennisPlayer class.
// The TennisPro class has two instance variables: ranking and name. 
// The ranking instance variable is an int and the name instance variable is a String. 
// The TennisPro class has one constructor method that takes two parameters: name and ranking.
//  The TennisPro class also has two methods: serve() and play(). 
// The serve() method prints out the name of the TennisPro instance and the text "serves with precision." 
// The play() method does nothing. The TennisPro class also has two getter methods and one setter method.
// The getter methods are getRanking(), which returns the ranking instance variable, and getName(),
// which returns the name instance variable. The setter method is setName(), which takes one parameter, 
//name, and sets the name instance variable to the value of name.

package essay_code2.Inheritance;

public class TennisPro extends TennisPlayer {
    private int ranking;
    private String name; 
    public TennisPro(String name, int ranking) {
        super(name);
        this.ranking = ranking;
        this.name = name;
    }
    
    public void serve() {
        System.out.println(getName() + " serves with precision.");
    }
  
    public void setName(String name) {
    this.name = name;
    }

    public int getRanking() {
        return ranking;
    }

    public void play() {
    }

    public String getName() {
        return name;
    }
}