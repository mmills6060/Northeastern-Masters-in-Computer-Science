import java.util.Random;
import java.lang.Math;

/*
creates a factory interface

*/
public interface Factory {
    void takeResource(Resource resource);
    Block produce();
    void displayInventory();
}



