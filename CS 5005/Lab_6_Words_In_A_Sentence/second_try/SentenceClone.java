// returns a duplicate of a given sentence. A 
// duplicate is a list that has the same words and punctuation in the same 
// sequence, but is independent of the original list. (Not an alias.)

package second_try;

import java.util.ArrayList;
import java.util.List;




public class SentenceClone {
    public static Sentence clone(Sentence sentence) {
        Sentence clonedSentence = new Sentence();
        Node current = sentence.head;
        Node previous = null;
        while (current != null) {
            if (current instanceof WordNode) {
                WordNode wordNode = new WordNode(((WordNode) current).word);
                if (previous == null) {
                    clonedSentence.head = wordNode;
                } else {
                    previous.setNext(wordNode);
                }
                previous = wordNode;
            } else if (current instanceof PunctuationNode) {
                PunctuationNode punctuationNode = new PunctuationNode(((PunctuationNode) current).punctuation);
                if (previous == null) {
                    clonedSentence.head = punctuationNode;
                } else {
                    previous.setNext(punctuationNode);
                }
                previous = punctuationNode;
            }
            current = current.getNext();
        }
        return clonedSentence;
    }
}
