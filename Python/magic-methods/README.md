# Duck Typing

The main idea of duck typing is that it doesn't matter what type the data is, if it does what I need I can use it. Since Python does not use interfaces, we can use multiple inheritance and duck typing. 

This example demonstrates that a `Car` instance can be injected any dependency that implements a `start()` method. After the car invokes the `turn_on()` method the engine starts and it prints how many pistons are running (should be the same as the number of cylinders).

# Magic Methods

Python offers lots of magic methods, this example demonstrates the use of:

- `__name__`: To get the name of the current class, function, module, descriptor or generator.
- `__class__`: To get the class of an instance
- `__repr__`: To get the official string representation of an object, useful for development. Called by the `repr()` method.
- `__str__`: To get the printable string representation of an object. Called by the `str()` method.
- `__get__`: To get the attribute of the owner class. This method returns the computed attribute value or `AttributeError`.
- `__set__`: To set an attribute of an instance of the owner class. It can raise `AttributeError`. For this example a car can set a `Transmission` object only with the values of "manual" or "automatic".

## Run the exercise

```bash
python main.py
```

## Running the tests

```bash
python tests.py
```
