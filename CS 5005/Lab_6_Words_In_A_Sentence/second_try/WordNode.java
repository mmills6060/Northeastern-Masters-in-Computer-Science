package second_try;

public class WordNode implements Node {
    private String word;
    private Node next;

    public WordNode(String word) {
        this.word = word;
        this.next = null;
    }

    @Override
    public String get_value() {
        return word;
    }

    @Override
    public Node get_next() {
        return next;
    }

    public void set_next(Node next) {
        this.next = next;
    }
}
