package second_try;

// Implementation for the EmptyNode

public class EmptyNode implements Node {
    private Node next;

    @Override
    public Node getNext() {
        return next;
    }

    @Override
    public void setNext(Node next) {
        this.next = next;
    }
}
