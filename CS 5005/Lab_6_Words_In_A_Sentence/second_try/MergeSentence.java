// merge two sentences 
// into a single sentence. The merged list should preserve all the punctuation. The 
// merged list should be returned by this method, and the original lists should be 
// unchanged.

package second_try;

public class MergeSentence {
    public static Sentence merge(Sentence sentence1, Sentence sentence2) {
        Sentence merged_list = new Sentence();
        Node current_node = sentence1.getHead();
        while (current_node.get_next() != null) {
            current_node = current_node.get_next();
            if (current_node instanceof WordNode) {
                merged_list.append_word(current_node.get_value());
            } else if (current_node instanceof PunctuationNode) {
                merged_list.append_punctuation(current_node.get_value());
            }
        }

        Node other_node = sentence2.getHead();
        while (other_node.get_next() != null) {
            other_node = other_node.get_next();
            if (other_node instanceof WordNode) {
                merged_list.append_word(other_node.get_value());
            } else if (other_node instanceof PunctuationNode) {
                merged_list.append_punctuation(other_node.get_value());
            }
        }

        return merged_list;
    }
}

