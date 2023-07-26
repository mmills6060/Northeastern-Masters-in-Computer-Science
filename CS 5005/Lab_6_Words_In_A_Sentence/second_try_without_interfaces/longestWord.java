// determines and returns the longest word 
//in a sentence. The word returned is just the word, and should not begin or end with 
//punctuation. If the sentence contains no words, longestWord should return an 
// empty

package second_try;

public class longestWord {
        // Definition of the recursive data structure for the linked list
        static class ListNode {
            String data;
            ListNode next;
    
            ListNode(String data) {
                this.data = data;
            }
        }
    
        // Recursive method to find the longest word in the sentence
        public static String findLongestWord(ListNode node) {
            // Base case: If the current node is null, return an empty string.
            if (node == null) {
                return "";
            }
    
            // Recursive call to find the longest word in the rest of the sentence
            String longestInRest = findLongestWord(node.next);
    
            // If the current node contains punctuation, return the longest word found so far.
            if (isPunctuation(node.data)) {
                return longestInRest;
            }
    
            // If the current node contains a word, compare its length with the longest word found so far.
            // Return the longer word between the current node's word and the longest word in the rest.
            String currentWord = removePunctuation(node.data);
            return currentWord.length() >= longestInRest.length() ? currentWord : longestInRest;
        }
    
        // Helper method to check if a string contains punctuation
        private static boolean isPunctuation(String str) {
            // Simple check: If the string is not alphanumeric, consider it as punctuation.
            return !str.matches("[a-zA-Z0-9]+");
        }
    
        // Helper method to remove leading and trailing punctuation from a word
        private static String removePunctuation(String word) {
            // Use regular expression to remove leading and trailing punctuation
            return word.replaceAll("^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$", "");
        }
}
