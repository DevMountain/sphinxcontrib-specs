public class Mars
{
    public static void main(String[] args) throws InterruptedException {
        //Mars Adventure Game Part 1

        //Create a string variable named ColonyName, and set it equal to your desired name
        String ColonyName = "SpaceX";

        //Create an int variable named ShipPopulation, and set it equal to 300
        int ShipPopulation = 300;

        //Create a double variable named ShipFood, and set it equal to 4000.00
        double ShipFood = 4000.00;

        //Create a boolean variable named Landing, and set it equal to true
        boolean Landing = true;

        //Apon reaching Mars everyone will eat 0.75 meals a day, to perserve food

        //The landing process takes 2 days, calculate how much food is left after landing
        //Equation: Food = Food - (Pop * 0.75);
        //Use the equation twice
        ShipFood = ShipFood - (ShipPopulation * 0.75);
        ShipFood = ShipFood - (ShipPopulation * 0.75);

        //Print the amount of food that is left
        System.out.println(ShipFood);

        //An extra crate of food is found increasing ShipFood by 50%
        ShipFood = ShipFood + (ShipFood * .5);

        //The births very timed perfectly and 5 more babies join the ShipPopulation
        ShipPopulation = ShipPopulation + 5;

        //Choose where you want the ship to land. The Hill, The Plain, or The Ocean
        //Create a String value called LandingLocation and set it equal to "The Hill" or "The Plain" or "The Ocean"
        String LandingLocation = "The Hill";

        //Create an if else statement. That checks to see if the LandingLocation is equal to "The Plain" ignoring case
        if (LandingLocation.equalsIgnoreCase("The Plain"))
        {
            //Print "Bbzzz Landing on the Plain"
            System.out.println("Bbzzz Landing on the Plain");
        }
        else
        {
            //Print "ERROR!!! Flight plan already set. Landing on the Plain"
            System.out.println("ERROR!!! Flight plan already set. Landing on the Plain");

        }

        Landing = LandingCheck(100);

        //Mars Adventure Game part 2

        //During the downtime after landing you decide to play the guessing game that came preload on the rockets computer
        //Create a new Java file called GuessingGame
        //Run the GuessingGame by calling a new GuessingGame constructor
        //new GuessingGame();

        //Mars Adventure Game part 3

        //After playing the GuessingGame it is finally time for the expedition team to pack and head out
        //Run the MarsExpedition by calling a new MarsExpedition constructor
        //new MarsExpedition();

        //Mars Adventure Game part 4

        //After an excited expedition it is time for the boring paperwork
        //Run the FindingsLists by calling a new FindingsLists constructor
        new FindingsLists();
    }

    //Create a public static void function called LandingCheck with an int parameter called Loops
    private static boolean LandingCheck(int Loops) throws InterruptedException {
        //Create a for loop that starts at i = 0, loops until i is equal to Loops, and i increments by 1 each loop
        for (int i = 0; i <= Loops; i++)
        {
            //Create an if statement with 1 if, 2 else ifs, and 1 else
            //The if statement should check to see if i divisiable by 3 equals 0, and that i divisiable by 5 equals 0
            if (((i % 3) == 0) && ((i % 5) == 0))
            {
                //Print "Keep Center
                System.out.println("Keep Center");
            }
            //The first else if statement should check if i divisiable by 5 equals 0
            else if ((i % 5) == 0)
            {
                //Print "Right"
                System.out.println("Right");
            }
            //The first else if statement should check if i divisiable by 3 equals 0
            else if ((i % 3) == 0)
            {
                //Print "Left"
                System.out.println("Left");
            }
            //Like always else statements do not have a condition
            else
            {
                //Print "Calculating"
                System.out.println("Calculating");
            }

            //Thread.sleep(250) slows the console down by 250 milliseconds
            Thread.sleep(250);
        }
        //Print "Landed"
        System.out.println("Landed");

        //The ship has landed on Mars. Return the value false;
        return false;
    }
}