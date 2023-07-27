package second_try;
// I think there is something wrong with my interpreter because it is telling me 
// that word is not visible even though im pretty sure it is. 
// 
// everything compiles despite the error. 

public class WordNode implements Node {
    public String word; 

    private Node next;

    public WordNode(String word) {
        this.word = word;
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
