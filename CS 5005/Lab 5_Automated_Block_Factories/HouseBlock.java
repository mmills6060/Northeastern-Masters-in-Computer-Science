public class HouseBlock extends Block {
    private static final int STONE_REQUIRED = 10;
    private static final int WOOD_REQUIRED = 20;

    public HouseBlock(Resource stone, Resource wood) throws InsufficientResourceException {
        super(BlockType.HOUSE);
        
        if (stone.getType() != ResourceType.STONE || wood.getType() != ResourceType.WOOD) {
            throw new IllegalArgumentException("Invalid resource types for HouseBlock.");
        }
        
        if (stone.getWeight() < STONE_REQUIRED || wood.getWeight() < WOOD_REQUIRED) {
            throw new InsufficientResourceException("Insufficient stone or wood resources to create a HouseBlock.");
        }
        
        // Additional validation and initialization if necessary
        
        // Set the resource type and weight for the HouseBlock object
        setResource(stone.getType(), stone.getWeight() + wood.getWeight());
    }
}