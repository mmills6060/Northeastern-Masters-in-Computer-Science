package second_try;
// this handles adding a word to a sentence.
public class SentenceAddWord {
    public static void addWord(Sentence sentence, String word) {
        WordNode newNode = new WordNode(word);

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
