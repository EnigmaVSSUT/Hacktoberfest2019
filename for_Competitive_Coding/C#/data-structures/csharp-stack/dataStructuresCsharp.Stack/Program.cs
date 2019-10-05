using System;

namespace dataStructuresCsharp.Stack
{
    class Program
    {
        static void Main(string[] args)
        {
            var stack = new Stack<string>();

            stack.Push("Hello");
            stack.Push("World");
            stack.Push("I");
            stack.Push("love");
            stack.Push("programming");
            
            stack.Pop();
            stack.Pop();

            stack.Display();
        }
    }
}
