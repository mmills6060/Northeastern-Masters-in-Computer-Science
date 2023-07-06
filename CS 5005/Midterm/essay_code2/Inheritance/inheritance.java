// This code creates a class called inheritance that has a single variable name.
// The class has a function called TennisPlayer that takes a string as a parameter
// and assigns the string to the name variable.
// The class also has a function called play that prints the string name + " is playing tennis."

package essay_code2.Inheritance;
public class inheritance {
    private String name;
    
    public void TennisPlayer(String name) {
        this.name = name;
    }
    
    public void play() {
        System.out.println(name + " is playing tennis.");
    }

}
