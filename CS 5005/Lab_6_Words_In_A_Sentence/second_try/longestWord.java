// determines and returns the longest word 
//in a sentence. The word returned is just the word, and should not begin or end with 
//punctuation. If the sentence contains no words, longestWord should return an 
// empty

package second_try;

public class LongestWord {
    public static String longestWord(Sentence sentence) {
        Node current_node = sentence.getHead();
        String longest = "";
        while (current_node.get_next() != null) {
            current_node = current_node.get_next();
            if (current_node instanceof WordNode) {
                String word = current_node.get_value();
                String word_without_punctuations = word.replaceAll("[^a-zA-Z0-9]", "");
                if (word_without_punctuations.length() > longest.length()) {
                    longest = word_without_punctuations;
                }
            }
        }
        return longest;
    }
}
