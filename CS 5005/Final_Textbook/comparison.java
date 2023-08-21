public class TennisScoreComparison {
    public static void main(String[] args) {
        int[] dataset1 = {6, 3, 7, 6}; 
        int[] dataset2 = {6, 3, 7, 6}; 

        boolean scoresConsistent = true;

        if (dataset1.length != dataset2.length) {
            scoresConsistent = false;
        } else {
            for (int i = 0; i < dataset1.length; i++) {
                if (dataset1[i] != dataset2[i]) {
                    scoresConsistent = false;
                    break; 
                }
            }
        }

        if (scoresConsistent) {
            System.out.println("Scores are consistent.");
        } else {
            System.out.println("Scores are inconsistent.");
        }
    }
}
