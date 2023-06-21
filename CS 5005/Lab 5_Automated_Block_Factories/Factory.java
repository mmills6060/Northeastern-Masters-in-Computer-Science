public interface Factory {
    void takeResource(Object resource);
    Block produce();
    void displayInventory();
}
