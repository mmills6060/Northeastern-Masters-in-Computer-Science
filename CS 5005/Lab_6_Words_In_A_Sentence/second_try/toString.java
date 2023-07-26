// convert the sentence into one string. There must be 
// a space between every two words. A punctuation mark should have no space 
// between it and whatever precedes it. There is no space between the last word and 
// the end of this sentence. If there is no punctuation mark at the end of the sentence, 
// this string should end with a period (it shouldn’t add the period to the original 
// sentence)

package second_try;

public class ToString {
    public static String toString(Sentence sentence) {
        Node current_node = sentence.getHead();
        StringBuilder result = new StringBuilder();
        while (current_node.get_next() != null) {
            current_node = current_node.get_next();
            String value = current_node.get_value();
            if (current_node instanceof WordNode) {
                result.append(value);
                if (current_node.get_next() != null && current_node.get_next() instanceof PunctuationNode) {
                    result.append(" ");
                }
            } else if (current_node instanceof PunctuationNode) {
                result.append(value);
            }
        }
        if (result.length() > 0 && result.charAt(result.length() - 1) != '.') {
            result.append('.');
        }
        return result.toString();
    }
}

