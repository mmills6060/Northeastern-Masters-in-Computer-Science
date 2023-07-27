package second_try;
// this handles adding punctuation to a sentnece. 

public class SentenceAddPunctuation {
    public static void addPunctuation(Sentence sentence, String punctuation) {
        PunctuationNode newNode = new PunctuationNode(punctuation);

        if (sentence.head instanceof EmptyNode) {
            sentence.head = newNode;
        } else {
            Node current = sentence.head;
            while (current.getNext() != null) {
                current = current.getNext();
            }
            current.setNext(newNode);
        }
    }
}
