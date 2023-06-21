/*
take resources, produce blocks. display the inventory.
 */
public interface Factory {
    void takeResource(Object resource);
    Block produce();
    void displayInventory();
}
