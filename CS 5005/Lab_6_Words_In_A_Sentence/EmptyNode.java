/**
 * Author: Michael Arthur Mills 
 * Class: CS 5005 
 * Date: July 1 2023
 */

// define a class called emptynode that implements node
public class EmptyNode implements Node {
    private String word;
// define a public string getValue that returns an empty string
    public String getValue() {
        return "";
    }
// define a public method that returns the value of the word instance variable
    @Override
    public String getStringRepresentation() {
        return word;
    }
// returns a new WordNode with the same value as the word instance variable
    @Override
    public Node cloneNode() {
        return new WordNode(word);
    }
// define a public method called merge that takes in a node other and returns other
    @Override
    public Node merge(Node other) {
        return other;
    }
}
