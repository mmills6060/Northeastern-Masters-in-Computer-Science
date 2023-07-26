package second_try;

public class PunctuationNode implements Node {
    private String punctuation;
    private Node next;

    public PunctuationNode(String punctuation) {
        this.punctuation = punctuation;
        this.next = null;
    }

    @Override
    public String get_value() {
        return punctuation;
    }

    @Override
    public Node get_next() {
        return next;
    }

    public void set_next(Node next) {
        this.next = next;
    }
}

