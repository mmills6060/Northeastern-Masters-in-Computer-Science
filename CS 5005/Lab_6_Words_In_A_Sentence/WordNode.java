public class WordNode implements Node {
    private String word;

    public WordNode(String word) {
        this.word = word;
    }

    public String getWord() {
        return word;
    }

    @Override
    public String getStringValue() {
        return word;
    }

    @Override
    public String getValue() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'getValue'");
    }
}