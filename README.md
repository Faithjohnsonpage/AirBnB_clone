# AirBnB Clone Console

The AirBnB Clone Console is a command-line interface (CLI) tool built as part of a project to create a simplified version of the AirBnB website. This console serves as the backbone for managing the backend operations of the AirBnB clone, including creating, updating, deleting, and displaying objects such as users, places, reviews, and bookings.

## Features

- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on various objects within the AirBnB clone database.
- **Interactive Interface**: Navigate the console through a user-friendly command-line interface.
- **Data Persistence**: Data entered and modified through the console is stored persistently in the backend database.
- **Extensible Architecture**: Easily extend the functionality of the console by adding new commands and modules.

### Files and Directories

- **models** directory contains all classes used for the entire project.
- **tests** directory contains all unit tests.
- **console.py** file is the entry point of our command interpreter.
- **models/base_model.py** file is the base class of all our models. It contains common elements:
  - **Attributes:** `id`, `created_at`, and `updated_at`.
  - **Methods:** `save()` and `to_json()`.
- **models/engine** directory contains all storage classes (using the same prototype). For the moment we have only one: `file_storage.py`.

## Usage

To use the AirBnB Clone Console, simply run the console application and start issuing commands to manage your AirBnB clone data. Refer to the documentation for a list of available commands and their usage instructions.

## Installation

To install the AirBnB Clone Console, clone the repository to your local machine and follow the installation instructions in the README file. Ensure that you have the necessary dependencies installed, and you're ready to start using the console.

## Documentation

Refer to the documentation for detailed information on how to use the AirBnB Clone Console, including a list of available commands, usage examples, and additional features.
