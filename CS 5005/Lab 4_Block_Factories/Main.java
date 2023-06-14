import java.util.Random;
import java.lang.Math;
/*
Driver for Lab 4 - Block Factories
This file should not be modified.
*/
public class Main
{
    public static void main(String[] args) throws InterruptedException {
        // Initialize variables and objects to be used in the simulation
        Resource resource;

        Factory stoneBlockProducer = new StoneBlockFactory();
        Factory woodBlockProducer = new WoodBlockFactory();

        int stoneBlocks = 0;
        int woodBlocks = 0;

        //Infinite simulation loop CTRL + C to terminate simulation
        while(true) {
            resource = mineResource();

            System.out.println("Resource mined: " + resource.getType());
            System.out.println("Mined weight: " + resource.getWeight());

            // Pass the randomly generated resource to its corresponding factory
            switch (resource.getType()) {
                case STONE -> stoneBlockProducer.takeResource(resource);
                case WOOD -> woodBlockProducer.takeResource(resource);
            }

            System.out.print("Stone bin weight: ");
            stoneBlockProducer.displayInventory();
            System.out.print("Wood bin weight: ");
            woodBlockProducer.displayInventory();

            if (stoneBlockProducer.produce() != null) {
                System.out.println("Stone block produced!");
                stoneBlocks++;
            }

            if (woodBlockProducer.produce() != null) {
                System.out.println("Wood block produced!");
                woodBlocks++;
            }

            System.out.println("Stone blocks: " + stoneBlocks);
            System.out.println("Wood blocks: " + woodBlocks);
            System.out.println();

            // Pauses simulation for 2 seconds so it is visible
            Thread.sleep(2000);
        }
    }

    /**
     *  Generates a new resource using randomization.
     *  The resource is of type Stone or Wood
     *  and has a weight in the range (0.0, 10.0)
     *
     *  @return A newly generated resource object.
     */
    public static Resource mineResource() {
        Random r = new Random();

        double weight = Math.round(r.nextDouble() * 100.0) / 10.0;
        int select = r.nextInt(2);

        ResourceType type = null;
        switch (select) {
            case 0 -> type = ResourceType.STONE;
            case 1 -> type = ResourceType.WOOD;
        }

        return new Resource(weight, type);
    }
}
