public interface Node {
    String getStringRepresentation();
    Node cloneNode();
    Node merge(Node other);
    Object getValue();
}