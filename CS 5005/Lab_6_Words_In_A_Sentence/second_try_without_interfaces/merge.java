// merge two sentences 
// into a single sentence. The merged list should preserve all the punctuation. The 
// merged list should be returned by this method, and the original lists should be 
// unchanged.

package second_try;

public class merge {
    // Definition of the recursive data structure for the linked list
    static class ListNode {
        String data;
        ListNode next;

        ListNode(String data) {
            this.data = data;
        }
    }

    // Recursive method to merge two sentences
    public static ListNode mergeSentences(ListNode sentence1, ListNode sentence2) {
        // Base case: If either of the sentences is null, return the other sentence.
        if (sentence1 == null) {
            return sentence2;
        }
        if (sentence2 == null) {
            return sentence1;
        }

        // Create a new node to store the merged data
        ListNode mergedNode = new ListNode(sentence1.data);

        // If the current node is punctuation, recursively merge the next nodes.
        // Otherwise, merge both sentences independently.
        if (isPunctuation(sentence1.data)) {
            mergedNode.next = mergeSentences(sentence1.next, sentence2);
        } else {
            // Find the next word node in sentence1
            ListNode nextWordNode = findNextWordNode(sentence1.next);

            if (nextWordNode != null) {
                // If there's a next word node in sentence1, merge it with sentence2.
                mergedNode.next = mergeSentences(nextWordNode, sentence2);
            } else {
                // If there's no next word node in sentence1, directly connect sentence2.
                mergedNode.next = sentence2;
            }
        }

        return mergedNode;
    }

    // Helper method to check if a string contains punctuation
    private static boolean isPunctuation(String str) {
        // Simple check: If the string is not alphanumeric, consider it as punctuation.
        return !str.matches("[a-zA-Z0-9]+");
    }

    // Helper method to find the next word node in a linked list
    private static ListNode findNextWordNode(ListNode node) {
        if (node == null) {
            return null;
        }

        if (isPunctuation(node.data)) {
            return findNextWordNode(node.next);
        } else {
            return node;
        }
    }
}

