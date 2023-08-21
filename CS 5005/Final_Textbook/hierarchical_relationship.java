class Achievement {
    private String name;

    public Achievement(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void display() {
        System.out.println(name);
    }
}

class MatchAchievement extends Achievement {
    public MatchAchievement(String name) {
        super(name);
    }
}

class TitleAchievement extends Achievement {
    public TitleAchievement(String name) {
        super(name);
    }
}

class GrandSlamAchievement extends TitleAchievement {
    public GrandSlamAchievement(String name) {
        super(name);
    }
}

class YearAchievement extends GrandSlamAchievement {
    public YearAchievement(String name) {
        super(name);
    }
}

public class PlayerAchievements {
    public static void main(String[] args) {
        Achievement match = new MatchAchievement("Won a match");
        Achievement title = new TitleAchievement("Won a title");
        Achievement grandSlam = new GrandSlamAchievement("Won a Grand Slam");
        Achievement year = new YearAchievement("Player of the Year");

        match.display();
        title.display();
        grandSlam.display();
        year.display();
    }
}