/*
Defines stonelockfactory. implements factory. produces woodbblocks if there are sufficient resources. 
*/


public class StoneBlockFactory implements Factory {
    private double binWeight;

    public void takeResource(Object resource) {
        if (resource instanceof Resource) {
            Resource stoneResource = (Resource) resource;
            if (stoneResource.getType() == ResourceType.STONE) {
                binWeight += stoneResource.getWeight();
            } else {
                throw new IllegalArgumentException("Invalid resource type. Expected stone.");
            }
        } else {
            throw new IllegalArgumentException("Invalid resource object. Expected Resource.");
        }
    }

    public Block produce() {
        if (binWeight >= Const.STONE_BLOCK_WEIGHT) {
            binWeight -= Const.STONE_BLOCK_WEIGHT;
            return new StoneBlock(binWeight, null);
        } else {
            return null;
        }
    }
// displays current bin weight
    public void displayInventory() {
        System.out.println(binWeight);
    }
}
