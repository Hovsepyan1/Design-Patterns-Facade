# Design-Patterns-Facade
Facade Design Pattern
This repository demonstrates the Facade Design Pattern in software design. The Facade pattern simplifies complex subsystems by providing a unified interface. This example simulates a Home Theater System with subsystems such as a DVD player, projector, and sound system, all controlled through a single facade.

Overview
The Facade Design Pattern aims to:

Simplify the interaction with a complex system.
Provide a single entry point (the facade) that abstracts the complexity of interacting with multiple subsystems.
Reduce dependencies between the client code and the subsystem.
In this example, the Facade pattern is applied to a home theater system consisting of:

DVD Player: Controls the DVD player's operations.
Projector: Controls the projector settings.
Sound System: Controls the sound system settings.
The HomeTheaterFacade class provides a simple interface for the client to use, without needing to interact with each individual subsystem.

Code Structure
DVDPlayer: A class that simulates the DVD player's functionality.
Projector: A class that simulates the projector's functionality.
SoundSystem: A class that simulates the sound system's functionality.
HomeTheaterFacade: The facade class that provides a unified interface to interact with all the subsystems.
Key Methods:
HomeTheaterFacade.watch_movie(): Simplifies the process of watching a movie by interacting with the DVD player, projector, and sound system.
Requirements
Python 3.x or higher
How to Run
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/Hovsepyan1/Design-Patterns-Facade.git
Navigate to the project directory:

bash
Copy code
cd Design-Patterns-Facade
Run the Python script:

bash
Copy code
python main.py
You should see output simulating the actions taken by the HomeTheaterFacade class to start a movie.

Example Output
bash
Copy code
Get ready to watch a movie...
DVD Player is ON
Projector is ON
Projector is in widescreen mode
Sound system is ON
Volume set to 10
Playing movie
Contributing
Feel free to fork the repository, submit issues, or create pull requests if you have improvements or enhancements for this code!

