package second_try;

import first_try.EmptyNode;

public class Sentence {
    private Node head;

    public Sentence() {
        this.head = (Node) new EmptyNode();
    }

    public void append_word(String word) {
        WordNode new_node = new WordNode(word);
        Node current_node = this.head;
        while (current_node.get_next() != null) {
            current_node = current_node.get_next();
        }
        ((WordNode) current_node).set_next(new_node);
    }

    public void append_punctuation(String punctuation) {
        PunctuationNode new_node = new PunctuationNode(punctuation);
        Node current_node = this.head;
        while (current_node.get_next() != null) {
            current_node = current_node.get_next();
        }
        ((WordNode) current_node).set_next(new_node);
    }

}