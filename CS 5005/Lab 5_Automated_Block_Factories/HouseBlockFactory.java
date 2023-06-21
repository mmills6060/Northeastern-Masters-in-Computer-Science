/*
implements factory interface and represents a factory that produces houseblocks. 
uses stoneblockaccumulator and woodblockaccumulator to keep track of created blocks.
*/

public class HouseBlockFactory implements Factory {
    private int stoneBlockAccumulator;
    private int woodBlockAccumulator;
    // define accumulator
    public HouseBlockFactory() {
        stoneBlockAccumulator = 0;
        woodBlockAccumulator = 0;
    }
    @Override
    public void takeResource(Object resource) {
        if (resource == null) {
            System.out.println("Null resource encountered: Skipping resource...");
            return; // Skip the resource and continue execution
        }
// if the resource contains the phrases either stoneblock or woodblock 
    String resourceString = resource.toString().toLowerCase(); // not sure if I need to convert to lowercase

    if (resourceString.contains("stoneblock")) {
        stoneBlockAccumulator++;
    } else if (resourceString.contains("woodblock")) {
        woodBlockAccumulator++;
    } else {
        System.out.println("Invalid block type: " + resourceString);
    }
}
// produces a houseblock if there are sufficient accumulated stone and wood blocks. 
    @Override
    public Block produce() {
        if (stoneBlockAccumulator >= Const.STONE_WEIGHT && woodBlockAccumulator >= Const.WOOD_WEIGHT) {
            stoneBlockAccumulator -= Const.STONE_WEIGHT;
            woodBlockAccumulator -= Const.WOOD_WEIGHT;
            return new HouseBlock(Const.STONE_WEIGHT, Const.WOOD_WEIGHT);
        } else {
            return null; // Not enough resources to produce a block
        }
    }

    @Override
    public void displayInventory() {
        System.out.println("Stone block accumulator: " + stoneBlockAccumulator);
        System.out.println("Wood block accumulator: " + woodBlockAccumulator);
    }
}
