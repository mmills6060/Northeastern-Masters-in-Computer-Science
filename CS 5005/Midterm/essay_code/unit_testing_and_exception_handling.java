    
import org.junit.Test;
import static org.junit.Assert.*;


public class unit_testing_and_exception_handling {
    @Test
    public void testGetScore() {
        TennisGame game = new TennisGame("Player A", "Player B");
        
        // Test initial score
        assertEquals("Love - Love", game.getScore());
        
        // Test player 1 scores
        game.player1Scores();
        assertEquals("15 - Love", game.getScore());
        
        // Test player 2 scores
        game.player2Scores();
        assertEquals("15 - 15", game.getScore());
        
        // Test exception handling for invalid score
        try {
            game.setScore(-1, 0);
            fail("Exception not thrown for invalid score");
        } catch (IllegalArgumentException e) {
            assertEquals("Invalid score value", e.getMessage());
        }
    }
}
