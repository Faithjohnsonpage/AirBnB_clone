# AirBnB Clone - The Console

The AirBnB Clone Console is a command-line interface(CLI) tool built as part
of a project to create a simplified version of the AirBnB website. This
console serves as the backbone for managing the backend operations of the
AirBnB clone, including creating, updating, deleting, and displaying objects
such as users, places, reviews, and bookings.

# Features

- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on
various objects within the AirBnB clone database.
- **Interactive Interface**: Navigate the console through a user-friendly 
command-line interface.
- **Data Persistence**: Data entered and modified through the console is
stored persistently in the backend database.
- **Extensible Architecture**: Easily extend the functionality of the console
    by adding new commands and modules.

### Files and Directories

- **models** directory contains all classes used for the entire project.
- **tests** directory contains all unit tests.
- **console.py** file is the entry point of our command interpreter.
- **models/base_model.py** file is the base class of all our models. It
contains common elements:
- **Attributes:** `id`, `created_at`, and `updated_at`.
- **Methods:** `save()` and `to_json()`.
- **models/engine** directory contains all storage classes(using the same
prototype). For the moment we have only one: `file_storage.py`.

## Usage

To use the AirBnB Clone Console, simply run the console application and start
issuing commands to manage your AirBnB clone data. Refer to the documentation
for a list of available commands and their usage instructions.

## Installation

To install the AirBnB Clone Console, clone the repository to your local
machine and follow the installation instructions in the README file. Ensure
that you have the necessary dependencies installed, and you're ready to start
using the console.

## Documentation

This contains how to use the AirBnB Clone Console, including a list of
available commands, usage examples, and additional features.

### List of Available Commands
- **create** Creates a new instance of BaseModel, saves it (to the JSON
file) and prints the id.
- **show** Prints the string representation of an instance based on the class
name and id.
- **update** Updates an instance based on the class name and id by adding or
updating attribute (saves the change into the JSON file).
- **destroy** Deletes an instance based on the class name and id (saves the
change into the JSON file).
- **all** Prints all string representation of all instances based or not on
the class name.
- **EOF** Exit the command interpreter gracefully.
- **quit** Quit command to exit the program

### How to Start the Console
To start the AirBnB Clone Console, navigate to the project directory in your
terminal and execute the following command:

```
ermac@faithjohnson25:~/AirBnB_clone$ ./console.py
(hbnb)
```

Once the console is launched, you'll see the (hbnb) prompt, indicating that
the console is ready to accept commands. From here, you can interact with the
console by entering commands and receiving corresponding responses.

### How to Use the Console
```
ermac@faithjohnson25:~/AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
(hbnb) help quit
Quit command to exit the program
(hbnb) quit
ermac@faithjohnson25:~/AirBnB_clone$
```

In the example above, the help command is used to display a list of available
commands. You can then proceed to use any of the listed commands to perform
various actions within the console.

### Examples
```
ermac@faithjohnson25:~/AirBnB_clone$ ./console.py

(hbnb) all MyModel
** class doesn't exist **

(hbnb) show BaseModel
** instance id missing **

(hbnb) show BaseModel My_First_Model
** no instance found **

(hbnb) create BaseModel
a8ed5170-22fe-448c-b4b6-3f7742765173

(hbnb) all BaseModel
["[BaseModel] (a8ed5170-22fe-448c-b4b6-3f7742765173) {'id': 'a8ed5170-22fe-448c-b4b6-3f7742765173', 'created_at': datetime.datetime(2024, 2, 10, 16, 7, 8, 939203), 'updated_at': datetime.datetime(2024, 2, 10, 16, 7, 8, 939234)}"]

(hbnb) show BaseModel a8ed5170-22fe-448c-b4b6-3f7742765173
[BaseModel] (a8ed5170-22fe-448c-b4b6-3f7742765173) {'id': 'a8ed5170-22fe-448c-b4b6-3f7742765173', 'created_at': datetime.datetime(2024, 2, 10, 16, 7, 8, 939203), 'updated_at': datetime.datetime(2024, 2, 10, 16, 7, 8, 939234)}

(hbnb) destroy
** class name missing **
(hbnb) update BaseModel a8ed5170-22fe-448c-b4b6-3f7742765173 first_name "Betty"

(hbnb) show BaseModel a8ed5170-22fe-448c-b4b6-3f7742765173
[BaseModel] (a8ed5170-22fe-448c-b4b6-3f7742765173) {'id': 'a8ed5170-22fe-448c-b4b6-3f7742765173', 'created_at': datetime.datetime(2024, 2, 10, 16, 7, 8, 939203), 'updated_at': datetime.datetime(2024, 2, 10, 16, 7, 8, 939234), 'first_name': 'Betty'}

(hbnb) create BaseModel
e206094d-e234-4446-be72-8b1e791c725b

(hbnb) all BaseModel
["[BaseModel] (a8ed5170-22fe-448c-b4b6-3f7742765173) {'id': 'a8ed5170-22fe-448c-b4b6-3f7742765173', 'created_at': datetime.datetime(2024, 2, 10, 16, 7, 8, 939203), 'updated_at': datetime.datetime(2024, 2, 10, 16, 7, 8, 939234), 'first_name': 'Betty'}", "[BaseModel] (e206094d-e234-4446-be72-8b1e791c725b) {'id': 'e206094d-e234-4446-be72-8b1e791c725b', 'created_at': datetime.datetime(2024, 2, 10, 16, 9, 54, 915350), 'updated_at': datetime.datetime(2024, 2, 10, 16, 9, 54, 915409)}"]

(hbnb) destroy BaseModel a8ed5170-22fe-448c-b4b6-3f7742765173

(hbnb) show BaseModel a8ed5170-22fe-448c-b4b6-3f7742765173
** no instance found **
(hbnb) quit
ermac@faithjohnson25:~/AirBnB_clone$
```
