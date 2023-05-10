# PyPatternedCurrencyConverter
PyPatternedCurrencyConverter : A Design Patterns-Powered Concurrency Converter in Python



1. Dependency Injection Pattern:
- This pattern focuses on making the code loosely coupled and easy to maintain.
- It allows the injection of dependencies as parameters into the constructor of the CurrencyConverter class, making it more flexible and easy to test.

2. Factory Pattern:
- This pattern provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.
- In your implementation, you have a CurrencyConverterFactory class that returns an instance of the appropriate CurrencyConverter subclass based on user input.

3. MVC Pattern:
- This pattern separates the application into three main components: Model, View, and Controller.
- In your implementation, the Model is the CurrencyConverter class, the View is the tkinter GUI, and the Controller is the CurrencyConverterController class that acts as a mediator between the Model and the View.

4. Observer Pattern:
- This pattern allows for one-to-many communication between objects. 
- In your implementation, the CurrencyConverter class is observed by the CurrencyConverterView class which updates the View whenever the Model changes.

5. Singleton Pattern:
- This pattern ensures that there is only one instance of a class, and provides a global point of access to that instance.
- In your implementation, the CurrencyConverterFactory class is a singleton as there is only one instance of it created.

6. Strategy Pattern:
- This pattern allows the behavior of a class to be changed at runtime by selecting an appropriate algorithm to use.
- In your implementation, the CurrencyConverter class has a conversion_strategy attribute that is set based on user input, allowing for different conversion strategies to be used.

Overall, your implementation uses a variety of design patterns to make the code more modular, flexible, and maintainable. The use of a GUI built with tkinter makes it easy for users to interact with the CurrencyConverter app. However, it would be helpful to include more descriptive comments within the code itself to make it easier for other developers to understand the purpose of each class, method, and variable.
