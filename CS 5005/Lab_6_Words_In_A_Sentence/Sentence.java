public class Sentence {
    private Node head;

    public Sentence(Node head) {
        this.head = head;
    }

    public int getNumberOfWords() {
        int count = 0;
        Node current = head;
        while (!(current instanceof EmptyNode)) {
            if (current instanceof WordNode) {
                count++;
            }
            current = getNextNode(current);
        }
        return count;
    }

    public String longestWord() {
        String longest = "";
        Node current = head;
        while (!(current instanceof EmptyNode)) {
            if (current instanceof WordNode) {
                String word = current.getValue();
                if (isWordValid(word) && word.length() > longest.length()) {
                    longest = word;
                }
            }
            current = getNextNode(current);
        }
        return longest;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        Node current = head;
        while (!(current instanceof EmptyNode)) {
            if (current instanceof WordNode) {
                sb.append(current.getValue()).append(" ");
            } else if (current instanceof PunctuationNode) {
                sb.append(current.getValue());
            }
            current = getNextNode(current);
        }
        String result = sb.toString().trim();
        if (result.isEmpty() || result.endsWith(".")) {
            return result;
        } else {
            return result + ".";
        }
    }

    public Sentence clone() {
        Node current = head;
        Node clonedHead = cloneNode(current);
        Node clonedCurrent = clonedHead;

        while (!(current instanceof EmptyNode)) {
            Node nextNode = getNextNode(current);
            Node clonedNextNode = cloneNode(nextNode);
            setNextNode(clonedCurrent, clonedNextNode);

            current = nextNode;
            clonedCurrent = clonedNextNode;
        }

        return new Sentence(clonedHead);
    }

    public Sentence merge(Sentence other) {
        Node current = head;
        Node mergedHead = cloneNode(current);
        Node mergedCurrent = mergedHead;

        while (!(current instanceof EmptyNode)) {
            Node nextNode = getNextNode(current);
            Node mergedNextNode = cloneNode(nextNode);
            setNextNode(mergedCurrent, mergedNextNode);

            current = nextNode;
            mergedCurrent = mergedNextNode;
        }

        Node otherCurrent = other.head;
        while (!(otherCurrent instanceof EmptyNode)) {
            Node clonedOtherNode = cloneNode(otherCurrent);
            setNextNode(mergedCurrent, clonedOtherNode);

            otherCurrent = getNextNode(otherCurrent);
            mergedCurrent = clonedOtherNode;
        }

        return new Sentence(mergedHead);
    }

    private Node getNextNode(Node current) {
        // Implement this method according to your linked list implementation
        // It should return the next node after the current node
        // If current is the last node, it should return an instance of EmptyNode
        return null;
    }

    private void setNextNode(Node current, Node next) {
        // Implement this method according to your linked list implementation
        // It should set the next node of the current node to the provided next node
    }

    private Node cloneNode(Node node) {
        // Implement this method to create a copy of the provided node
        // and return the cloned node
        // Make sure the cloned node has the same value as the original node
        return null;
    }

    private boolean isWordValid(String word) {
        // Implement this method to check if the word is valid
        // You can define your own conditions for a valid word
        // For example, you can check if the word matches a regular expression
        return true;
    }
}