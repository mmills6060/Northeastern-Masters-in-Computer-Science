/*
represents the houseblock. creates an instance of houseblock by providing stoneWeight and woodWeight as constructor arguments.
*/

public class HouseBlock extends Block {
    private Double stoneResource;
    private Double woodResource;

    public HouseBlock(Double stoneWeight, Double woodWeight) {
        super(calculateWeight(stoneWeight, woodWeight), ResourceType.HOUSE);
        this.stoneResource = stoneWeight;
        this.woodResource = woodWeight;
    }

    private static double calculateWeight(Double stoneWeight, Double woodWeight) {
        return stoneWeight + woodWeight;
    }
}
