package second_try;
// this is the sentence class. I really wasn't sure if I should split up add punctuation and add word but I did. 


public class Sentence {
    Node head; // Points to the first node in the sentence

// create an empty node at the head. this is good so we can determine that it is a new sentence.  
    public Sentence() {
        head = new EmptyNode(); 
    }
}