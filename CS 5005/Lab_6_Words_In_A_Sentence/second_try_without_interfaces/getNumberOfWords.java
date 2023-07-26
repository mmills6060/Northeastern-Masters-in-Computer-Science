// Computes and returns the number of words 
// in a sentence. The punctuation does not count as a word.

package second_try;

public class getNumberOfWords {
        // Definition of the recursive data structure for the linked list
        static class ListNode {
            String word;
            ListNode next;
    
            ListNode(String word) {
                this.word = word;
            }
        }
    
        // Recursive method to compute the number of words in the sentence
        public static int getNumberOfWordsInSentence(ListNode sentence) {
            // Base case: If the current node is null, we've reached the end of the linked list.
            // Return 0 to stop the recursion.
            if (sentence == null) {
                return 0;
            }
    
            // If the current node contains a word (i.e., not punctuation), increment the count by 1.
            int count = 0;
            if (!sentence.word.isEmpty()) {
                count = 1;
            }
    
            // Recursively call the method on the next node and add its result to the current count.
            return count + getNumberOfWordsInSentence(sentence.next);
        }
}
