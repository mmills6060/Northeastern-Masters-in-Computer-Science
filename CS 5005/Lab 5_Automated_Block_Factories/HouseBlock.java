public class HouseBlock extends Block {
    private Resource stoneResource;
    private Resource woodResource;

    public HouseBlock(Resource stoneResource, Resource woodResource) {
        super(calculateWeight(stoneResource, woodResource), ResourceType.HOUSE);
        this.stoneResource = stoneResource;
        this.woodResource = woodResource;
    }

    private static double calculateWeight(Resource stoneResource, Resource woodResource) {
        return stoneResource.getWeight() + woodResource.getWeight();
    }
}
