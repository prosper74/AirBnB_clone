#!/usr/bin/python3
"""
Defines HBNBCommand class
This module contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """
        Called when an empty line is entered
          - Do nothing
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
