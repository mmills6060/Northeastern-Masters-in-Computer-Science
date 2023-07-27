// Computes and returns the number of words 
// in a sentence. The punctuation does not count as a word.

package second_try;

public class SentenceGetNumberOfWords {
    public static int getNumberOfWords(Sentence sentence) {
        int count = 0;
        Node current = sentence.head;
        while (current != null) {
            if (current instanceof WordNode) {
                count++;
            }
            current = current.getNext();
        }
        return count;
    }
}
