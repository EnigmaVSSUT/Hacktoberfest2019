using System;

namespace dataStructuresCsharp.Stack
{
    public class Stack<T>
    {
        private T[] _array;
        private int _top = -1;
        public Stack()
        {
            _array = new T[1];
        }

        public void Push(T value){
            if (_array.Length-1 == _top){
                IncreaseArraySize();
            }

            _top++;
            _array[_top] = value;
        }

        public T Pop(){            
            var oldTop = _top--;
            var oldTopValue = _array[oldTop];

            var halfLength = (float)_array.Length / 2;

            if (_top+1 < halfLength)
                DecreaseArraySize();

            return _array[oldTop];
        }
        private void IncreaseArraySize(){
            var newSize = _array.Length * 2;
            var newArray = new T[newSize];

            for(int i=0; i < _array.Length; i++)
                newArray[i] = _array[i];
            
            _array = newArray;
        }

        private void DecreaseArraySize(){
            var newSize = _array.Length/2;
            var newArray = new T[newSize];

            for(int i=0; i < newSize; i++)
                newArray[i] = _array[i];
            
            _array = newArray;
        }

        public void Display(){
            for(int i=0; i <= _top; i++){
                if (_array[i]==null)
                    break;

                Console.WriteLine(_array[i]);
            }

            Console.WriteLine($"Stack size is {_top+1}");
        }
    }
}
