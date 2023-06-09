import java.util.Random;
import java.lang.Math;

/*
creates a class resourcebinfacctory

*/
public class ResourceBinFactory {
    public static void main(String[] args) {
        ResourceBin resourceBin = new ResourceBin();
        double resourceWeight = 10.0; // Example resource weight

        resourceBin.addResource(resourceWeight);

        try {
            resourceBin.produceBlock();
            System.out.println("Block produced successfully");
        } catch (InsufficientWeightException e) {
            System.out.println("Error: " + e.getMessage());
            // Handle the insufficient weight situation
            // ...
        }
    }
}

interface Factory {
    double BLOCK_WEIGHT = 20.0;
    void produceBlock() throws InsufficientWeightException;
}




