// 2. Write vs WriteLine

using System;

class Program
{
    static void Main()
    {
        Console.Write("Hi!"); 
        Console.Write(" I am Timmy!"); 
        Console.Write(" And this is all in one Line.")

        Console.WriteLine(); // Next line

        Console.Write("This is another Line after WriteLine.");

        /*
            Output:
            Hi! I am Timmy! And this is all in one Line.
            This is another Line after WriteLine.

            explanation: "Write" displays text inline and "WriteLine" moves them to another line
        */
    }
}



// 3. Try catch and blocks
using System;

class Program
{
    static void Main()
    {
        try {
            Console.Write("Type in your Monroe ID: ");
            int monroe_id = int.Parse(Console.ReadLine());

            Console.WriteLine($"ID entered: {monroe_id}");
        }
        catch (FormatException error) {
            Console.WriteLine("Monroe ID must be only numbers. Please try again.");
        }
        finally {
            Console.WriteLine("Program ended");
        }
        
        /*
            ----- CASE 1 -----
            User Input:
                Type in your Monroe ID: Temajio Boodle

            Program Output:
                Monroe ID must be only numbers. Please try again.
                Program ended

            ----- CASE 2 ------
            User Input:
                Type in your Monroe ID: 123

            Program Output:
                ID entered: 123
                Program ended

            Explanation:
                - in the first case the user entering a string instead of a number, and since the program expect a number instead
                it will throw the error message written then execute the code inside finally
                - in the second case, the use input was in a correct format so it kept executing the rest of the code inside try, then went to the code 
                inside of finally
                - In BOTH cases, the code wrapped inside finally is always executed at the end of the program
        */  
    }
}