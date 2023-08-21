    
import org.junit.Before;
import org.junit.Test;
import org.junit.jupiter.api.BeforeEach;

import static org.junit.Assert.*;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.List;


public class unit_testing {
    private TennisMatchView view;

    @BeforeEach
    public void setup() {
        view = new TennisMatchView();
    }

    @Test
    public void testGetInput() {
        int expectedInput = 1;
        assertEquals(expectedInput, view.getInput());
    }

    @Test
    public void testGetPlayerName() {
        String expectedPlayerName = "John Doe";
        assertEquals(expectedPlayerName, view.getPlayerName());
    }

    @Test
    public void testDisplayPlayers() {
        List<Player> players = new ArrayList<>();
        players.add(new Player("John Doe"));
        players.add(new Player("Jane Doe"));
        view.displayPlayers(players);
        assertEquals("Current Players:\n1. John Doe\n2. Jane Doe\n", view.toString());
    }

    @Test
    public void testDisplayCourts() {
        List<Court> courts = new ArrayList<>();
        courts.add(new Court(1));
        courts.add(new Court(2));
        view.displayCourts(courts);
        assertEquals("Current Courts:\nCourt #1\nCourt #2\n", view.toString());
    }

    @Test
    public void testGetMatchIndex() {
        List<Match> matches = new ArrayList<>();
        matches.add(new Match(new Player("John Doe"), new Player("Jane Doe")));
        assertEquals(0, view.getMatchIndex(matches));
    }

    @Test
    public void testGetScores() {
        int player1Score = 10;
        int player2Score = 20;
        PlayerScores expectedScores = new PlayerScores(player1Score, player2Score);
        assertEquals(expectedScores, view.getScores());
    }

    @Test
    public void testDisplayResults() {
        List<Player> players = new ArrayList<>();
        players.add(new Player("John Doe", 100));
        players.add(new Player("Jane Doe", 200));
        view.displayResults(players);
        assertEquals("Results:\n1. John Doe - 100 points\n2. Jane Doe - 200 points\n", view.toString());
    }

    @Test
    public void testDisplayMatches() {
        List<Match> matches = new ArrayList<>();
        matches.add(new Match(new Player("John Doe"), new Player("Jane Doe")));
        view.displayMatches(matches);
        assertEquals("Current Matches being played:\n1. John Doe vs Jane Doe\n", view.toString());
    }
}




