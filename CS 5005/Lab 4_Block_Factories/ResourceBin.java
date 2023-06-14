import java.util.Random;
import java.lang.Math;

/*
creates a class resourcebin

*/
public class ResourceBin {
    private static final double BLOCK_WEIGHT = 10.0;
    private double currentWeight;

    public ResourceBin() {
        this.currentWeight = 0.0;
    }

    public void addResource(double weight) {
        currentWeight += weight;
    }

    public Block produceBlock() throws InsufficientWeightException {
        // Check if the bin has sufficient weight to produce a block
        if (currentWeight < BLOCK_WEIGHT) {
            throw new InsufficientWeightException("Insufficient weight in the resource bin.");
        }

        // Deduct the block weight from the bin
        currentWeight -= BLOCK_WEIGHT;

        // Produce the block
        Block block = new Block(ResourceType.STONE, BLOCK_WEIGHT); // Replace ResourceType.STONE with the appropriate type
        return block;
   
    }

    public void displayInventory() {
        System.out.println("Current weight in resource bin: " + currentWeight);
    }
}




