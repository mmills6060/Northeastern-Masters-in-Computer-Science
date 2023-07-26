// returns a duplicate of a given sentence. A 
// duplicate is a list that has the same words and punctuation in the same 
// sequence, but is independent of the original list. (Not an alias.)

package second_try;

import java.util.ArrayList;
import java.util.List;




public class Clone {
        public static List<String> clone(List<String> list) {
        List<String> duplicate = new ArrayList<>(list);
        return duplicate;
    }
}
