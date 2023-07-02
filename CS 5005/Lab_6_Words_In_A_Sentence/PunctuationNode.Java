public class PunctuationNode implements Node {
    private char punctuation;
    private Node next;

    public PunctuationNode(char punctuation) {
        this.punctuation = punctuation;
        this.next = new EmptyNode();
    }
// this method returns the punctuation varibale as a string
    @Override
    public String getStringRepresentation() {
        return String.valueOf(punctuation);
    }
// this method sets the next variable to the result of calling merge on the next variable with the argument and returns this object
    @Override
    public Node merge(Node other) {
        next = next.merge(other);
        return this;
    }

    @Override
    public Node cloneNode() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'cloneNode'");
    }

    @Override
    public Object getValue() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'getValue'");
    }

}
