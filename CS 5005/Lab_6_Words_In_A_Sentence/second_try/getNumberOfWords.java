// Computes and returns the number of words 
// in a sentence. The punctuation does not count as a word.

package second_try;

public class getNumberOfWords {
    public static int getNumberOfWords(Sentence sentence) {
        Node current_node = sentence.getHead();
        int count = 0;
        while (current_node.get_next() != null) {
            current_node = current_node.get_next();
            if (current_node instanceof WordNode) {
                count++;
            }
        }
        return count;
    }
}
