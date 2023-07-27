// determines and returns the longest word 
//in a sentence. The word returned is just the word, and should not begin or end with 
//punctuation. If the sentence contains no words, longestWord should return an 
// empty

package second_try;

public class SentenceLongestWord {
    public static String longestWord(Sentence sentence) {
        String longest = "";
        Node current = sentence.head;
        while (current != null) {
            if (current instanceof WordNode) {
                String word = ((WordNode) current).word;
                if (word.length() > longest.length()) {
                    longest = word;
                }
            }
            current = current.getNext();
        }
        return longest;
    }
}
