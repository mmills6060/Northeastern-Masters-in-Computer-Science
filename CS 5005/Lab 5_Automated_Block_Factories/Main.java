import java.util.Random;
import java.lang.Math;

/*
Driver for Lab 5 - Automated House Factory
This file should not be modified.
*/
public class Main {
    public static void main(String[] args) throws InterruptedException {
        // Initialize objects to be used in the simulation
        Factory stoneBlockProducer = new StoneBlockFactory();
        Factory woodBlockProducer = new WoodBlockFactory();
        Factory houseBlockProducer = new HouseBlockFactory();

        //Infinite simulation loop CTRL + C to terminate simulation
        while(true) {
            Block houseBlock;
            Resource resource = mineResource();

            System.out.println("Resource mined: " + resource.getType());
            System.out.println("Mined weight: " + resource.getWeight());

            // Pass the randomly generated resource to its corresponding factory
            switch (resource.getType()) {
                case STONE -> stoneBlockProducer.takeResource(resource);
                case WOOD -> woodBlockProducer.takeResource(resource);
            }

            System.out.print("Stone factory bin weight: ");
            stoneBlockProducer.displayInventory();
            System.out.print("Wood factory bin weight: ");
            woodBlockProducer.displayInventory();

            /* Try to produce stone and wood blocks if each factory has sufficient
            resource weight to construct a block.  If successful, pass those blocks
            to the house factory.
             */
            houseBlockProducer.takeResource(stoneBlockProducer.produce());
            houseBlockProducer.takeResource(woodBlockProducer.produce());

            // Try to produce a house block if the factory has sufficient blocks
            houseBlock = houseBlockProducer.produce();

            // Notify the user of the status of the house factory
            System.out.println("House factory status:");
            houseBlockProducer.displayInventory();

            if (houseBlock != null){
                System.out.println("House built!");
            }

            System.out.println();

            // Pauses simulation for 3  seconds so it is visible
            Thread.sleep(3000);
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
