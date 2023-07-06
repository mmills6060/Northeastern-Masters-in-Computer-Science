package essay_code2.Type_casting;

public class type_casting {
    public static void main(String[] args) {
        int playerScore = 6;
        float averageScore = 8.5f;
        
        // Type casting from int to float
        float convertedScore = (float) playerScore;
        
        // Type casting from float to int
        int roundedAverage = (int) averageScore;
        
        System.out.println("Player Score: " + playerScore);
        System.out.println("Converted Score (float): " + convertedScore);
        System.out.println("Average Score (float): " + averageScore);
        System.out.println("Rounded Average Score (int): " + roundedAverage);
    }
}

