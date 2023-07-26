// convert the sentence into one string. There must be 
// a space between every two words. A punctuation mark should have no space 
// between it and whatever precedes it. There is no space between the last word and 
// the end of this sentence. If there is no punctuation mark at the end of the sentence, 
// this string should end with a period (it shouldn’t add the period to the original 
// sentence)

package second_try;

public class toString {
        // Definition of the recursive data structure for the linked list
        static class ListNode {
            String data;
            ListNode next;
    
            ListNode(String data) {
                this.data = data;
            }
        }
    
        // Recursive method to convert the sentence to a string
        public static String sentenceToString(ListNode node) {
            // Base case: If the current node is null, return an empty string.
            if (node == null) {
                return "";
            }
    
            // Recursive call to convert the rest of the sentence to a string
            String restOfTheSentence = sentenceToString(node.next);
    
            // Check if the current node contains punctuation or a word
            if (isPunctuation(node.data)) {
                // If it contains punctuation, return the punctuation without a space before it.
                return node.data + restOfTheSentence;
            } else {
                // If it contains a word, add a space before it unless it's the first word in the sentence.
                if (!restOfTheSentence.isEmpty()) {
                    return " " + node.data + restOfTheSentence;
                } else {
                    return node.data;
                }
            }
        }
    
        // Helper method to check if a string contains punctuation
        private static boolean isPunctuation(String str) {
            // Simple check: If the string is not alphanumeric, consider it as punctuation.
            return !str.matches("[a-zA-Z0-9]+");
        }
}
