// returns a duplicate of a given sentence. A 
// duplicate is a list that has the same words and punctuation in the same 
// sequence, but is independent of the original list. (Not an alias.)

package second_try;

import java.util.ArrayList;
import java.util.List;




public class CloneSentence {
    public static Sentence clone(Sentence sentence) {
        Sentence clone_list = new Sentence();
        Node current_node = sentence.getHead();
        while (current_node.get_next() != null) {
            current_node = current_node.get_next();
            if (current_node instanceof WordNode) {
                clone_list.append_word(current_node.get_value());
            } else if (current_node instanceof PunctuationNode) {
                clone_list.append_punctuation(current_node.get_value());
            }
        }
        return clone_list;
    }
}
