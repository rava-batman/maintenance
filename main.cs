// 5. Single inheritance demo

using System;

class Animal
{
    public virtual void MakeSound() { Console.WriteLine("All animals can make sounds"); }
}

class Dog : Animal
{
    public override void MakeSound() { Console.WriteLine("Dog barks"); }
}

class Program
{
    static void Main(string[] args)
    {
        Dog droopy = new Dog();
        droopy.MakeSound();
    }
}

// Output: Dog barks




// 6. Circle circle thing
using System;

abstract class Shape
{
    public abstract double CalculateArea();
}

class Circle : Shape
{
    public double Radius { get; private set; }
    public Circle(double radius) { Radius = radius; }
    public override double CalculateArea() => Math.PI * Radius * Radius;
}

class Rectangle : Shape
{
    public double Length { get; private set; }
    public double Width { get; private set; }
    public Rectangle(double length, double width)
    {
        Length = length;
        Width = width;
    }
    public override double CalculateArea() => Length * Width;
}

class Program
{
    static void Main(string[] args)
    {
        Shape circle = new Circle(5);
        Shape rectangle = new Rectangle(4, 7);

        Console.WriteLine("Circle Area: " + circle.CalculateArea());
        Console.WriteLine("Rectangle Area: " + rectangle.CalculateArea());
    }
}

/*
    OUTPUT: 
            Circle Area: 78.53981633974483
            Rectangle Area: 28
*/


// 7. SchoolContext framework
using System;


// a. this the Student class
class Student
{
    public int Id { get; set; }
    public string Name { get; set; }
    public int Age { get; set; }
}

// b. DbContext
class SchoolContext : DbContext
{
    public DbSet<Student> Students { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        /*
            This is a connnection to my postgreSQL but if you try it, replace the server string with urs
            optionsBuilder.UseSqlServer("ASNKJFennvleNFlea");
        */
    }
}

// c. Add student
class Program
{
    static void Main(string[] args)
    {
        using (var context = new SchoolContext())
        {
            var student = new Student { Name = "Timmy", Age = 22 };
            context.Students.Add(student);
            context.SaveChanges();
        }
    }
}

