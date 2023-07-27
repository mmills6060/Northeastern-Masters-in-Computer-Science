// merge two sentences 
// into a single sentence. The merged list should preserve all the punctuation. The 
// merged list should be returned by this method, and the original lists should be 
// unchanged.

package second_try;

public class SentenceMerge {
    public static Sentence merge(Sentence sentence, Sentence other) {
        Sentence mergedSentence = new Sentence();
        Node current = sentence.head;
        Node previous = null;
        while (current != null) {
            if (current instanceof WordNode) {
                WordNode wordNode = new WordNode(((WordNode) current).word);
                if (previous == null) {
                    mergedSentence.head = wordNode;
                } else {
                    previous.setNext(wordNode);
                }
                previous = wordNode;
            } else if (current instanceof PunctuationNode) {
                PunctuationNode punctuationNode = new PunctuationNode(((PunctuationNode) current).punctuation);
                if (previous == null) {
                    mergedSentence.head = punctuationNode;
                } else {
                    previous.setNext(punctuationNode);
                }
                previous = punctuationNode;
            }
            current = current.getNext();
        }

        if (previous != null) {
            // Find the last node in the linked list. 
            while (previous.getNext() != null) {
                previous = previous.getNext();
            }
        }

        // Merge the other sentence to the merged sentence
        current = other.head;
        while (current != null) {
            if (current instanceof WordNode) {
                WordNode wordNode = new WordNode(((WordNode) current).word);
                if (previous == null) {
                    mergedSentence.head = wordNode;
                } else {
                    previous.setNext(wordNode);
                }
                previous = wordNode;
            } else if (current instanceof PunctuationNode) {
                PunctuationNode punctuationNode = new PunctuationNode(((PunctuationNode) current).punctuation);
                if (previous == null) {
                    mergedSentence.head = punctuationNode;
                } else {
                    previous.setNext(punctuationNode);
                }
                previous = punctuationNode;
            }
            current = current.getNext();
        }

        return mergedSentence;
    }
}
