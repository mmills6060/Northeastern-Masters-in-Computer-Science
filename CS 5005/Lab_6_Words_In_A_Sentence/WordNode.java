public class WordNode implements Node {
    private String word;
// define a field named word of type string
    public WordNode(String word) {
        this.word = word;
    }
// define a method named getWord, which returns the value of the word field
    public String getWord() {
        return word;
    }
// return the value of the word field
    public String getStringRepresentation() {
        return word;
    }

    public Node cloneNode() {
        return new WordNode(word);
    }
// method named merge that returns accepts a node parameter and returns a node value. The method returns the Node paramter
    public Node merge(Node other) {
        return other;
    }
// method named getValue that returns an Object value
    @Override
    public Object getValue() {
        throw new UnsupportedOperationException("Unimplemented method 'getValue'");
    }
}