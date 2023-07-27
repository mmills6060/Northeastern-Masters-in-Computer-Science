package second_try;
// this is the punctuation node that is logically implemented.


public class PunctuationNode implements Node {
    String punctuation;
    private Node next;

    public PunctuationNode(String punctuation) {
        this.punctuation = punctuation;
    }

    @Override
    public Node getNext() {
        return next;
    }

    @Override
    public void setNext(Node next) {
        this.next = next;
    }
}

