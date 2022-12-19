import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

public class FindingsLists
{
    public FindingsLists() throws InterruptedException
    {
        //Use Thread.sleep(500) to stop the terminal for half a second
        Thread.sleep(500);

        //Print "Welcome back from your expedition. Time to catalog everything you found,"
        System.out.println("Welcome back from your expedition. Time to catalog everything you found.");

        //Create an Arraylist<String> named rockList and set it equal to new ArrayList<String>()
        ArrayList<String> rockList = new ArrayList<String>();

        //Print "Rock data downloaded."
        System.out.println("Rock data downloaded.");

        //You will be adding 4 rocks to the list using rockList.add("")
        //rock, weird rock, smooth rock, and not rock
        rockList.add("rock");
        rockList.add("weird rock");
        rockList.add("smooth rock");
        rockList.add("not rock");

        //Print the rockList;
        System.out.println(rockList);

        //Print "Wait a second that last on is not a rock we need to delete that one from the list."
        System.out.println("Wait a second that last on is not a rock we need to delete that one from the list");

        //Remove "not rock" from the rockList ArrayList by using rockList.remove()
        rockList.remove("not rock");

        //Print the rockList;
        System.out.println(rockList);

        //Print "Perfect"
        System.out.println("Perfect");

        //Use Thread.sleep(500) to stop the terminal for half a second
        Thread.sleep(500);

        //Create a Hashmap<String, String> named fossilDirectory and set it equal to new Hashmap<>()
        HashMap<String, String> fossilDirectory = new HashMap<>();
        //Hashmap<String, String> allows each fossilDirectory element to have 2 attributes, like name and description

        //Print "Fossil data downloaded"
        System.out.println("Fossil data downloaded");

        //You will be adding 3 fossils and their description to the Hashmap using fossilDirectory.put("","")
        //Bird Fossil, The fossil has wings implying it was capable of flight
        //Fish Fossil, The fossil is vaguely fish shaped implies there was once water
        //Tooth Fossil, The tooth from an unknown fossil
        fossilDirectory.put("Bird Fossil", "The fossil has wings implying it was capable of flight");
        fossilDirectory.put("Fish Fossil", "The fossil is vaguely fish shaped implies there was once water");
        fossilDirectory.put("Tooth Fossil", "The tooth from an unknown fossil");

        //Print "Which of the fossils would you like to learn more about (Spelling and Spacing is important)?"
        System.out.println("Which of the fossils would you like to learn more about (Spelling and Spacing is important)?");

        //Create a scanner input object
        Scanner input = new Scanner(System.in);

        //Create a String variable called fossilChoice and set it equal to input.nextLine()
        String fossilChoice = input.nextLine();

        //Create an if statement that checks if fossilChoice equals "Bird Fossil"
        if (fossilChoice.equalsIgnoreCase("Bird Fossil"))
        {
            //Print "Fossil: fossilChoice \nDescription: fossilDirectory.get(fossilChoice)
            System.out.println("Fossil: " + fossilChoice + "\nDescription: " + fossilDirectory.get(fossilChoice));
        }
        //Create an else if statement to check if fossilChoice equals "Fish Fossil"
        else if (fossilChoice.equalsIgnoreCase("Fish Fossil"))
        {
            //Print "Fossil: fossilChoice \nDescription: fossilDirectory.get(fossilChoice)
            System.out.println("Fossil: " + fossilChoice + "\nDescription: " + fossilDirectory.get(fossilChoice));
        }
        //Create an else if statement to check if fossilChoice equals "Tooth Fossil"
        else if (fossilChoice.equalsIgnoreCase("Tooth Fossil"))
        {
            //Print "Fossil: fossilChoice \nDescription: fossilDirectory.get(fossilChoice)
            System.out.println("Fossil: " + fossilChoice + "\nDescription: " + fossilDirectory.get(fossilChoice));
        }

        //Use Thread.sleep(500) to stop the terminal for half a second
        Thread.sleep(500);

        //Create a HashSet<String> called suppliesBrought and set it equal to new HashSet<>()
        HashSet<String> suppliesBrought = new HashSet<>();

        //Create a HashSet<String> called suppliesUsed and set it equal to new HashSet<>()
        HashSet<String> suppliesUsed = new HashSet<>();

        //Use .add() to add "Food" to the HashSet suppliesBrought
        suppliesBrought.add("Food");
        //Use .add() to add "Water" to the HashSet suppliesBrought
        suppliesBrought.add("Water");
        //Use .add() to add "Medicine" to the HashSet suppliesBrought
        suppliesBrought.add("Medicine");

        //Use .add() to add "Food" to the HashSet suppliesUsed
        suppliesUsed.add("Food");
        //Use .add() to add "Water" to the HashSet suppliesUsed
        suppliesUsed.add("Water");

        //Print what is left over
        System.out.println("Medicine");
    }
}
