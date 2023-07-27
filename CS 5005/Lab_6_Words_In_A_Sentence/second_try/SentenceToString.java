// convert the sentence into one string. There must be 
// a space between every two words. A punctuation mark should have no space 
// between it and whatever precedes it. There is no space between the last word and 
// the end of this sentence. If there is no punctuation mark at the end of the sentence, 
// this string should end with a period (it shouldn’t add the period to the original 
// sentence)

package second_try;

public class SentenceToString {
    public static String toString(Sentence sentence) {
        StringBuilder sentenceBuilder = new StringBuilder();
        Node current = sentence.head;
        while (current != null) {
            if (current instanceof WordNode) {
                sentenceBuilder.append(" ").append(((WordNode) current).word);
            } else if (current instanceof PunctuationNode) {
                sentenceBuilder.append(((PunctuationNode) current).punctuation);
            }
            current = current.getNext();
        }

        // Remove the leading space if it exists
        // I added this because in the tests there was always a space when adding or merging. 
        if (sentenceBuilder.length() > 0 && sentenceBuilder.charAt(0) == ' ') {
            sentenceBuilder.deleteCharAt(0);
        }


        return sentenceBuilder.toString();
    }
}
