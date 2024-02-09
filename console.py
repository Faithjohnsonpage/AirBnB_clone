#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """A HBNBCommand Class"""
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("Exiting the command interpreter gracefully.")

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
