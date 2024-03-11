#!/usr/bin/python3
"""
Defines HBNBCommand class
This module contains the entry point of the command interpreter
"""

from ast import literal_eval
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """
        Called when an empty line is entered
          - Do nothing
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id
        Usage: create <class>
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            if arg == 'User':
                obj = User()
            else:
                obj = literal_eval(arg)()

            storage = FileStorage()
            storage.new(obj)
            storage.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
         Prints the string representation of an instance
         based on the class name and id.
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            obj_id = args[1]
            storage = FileStorage()
            storage.reload()
            key = "{}.{}".format(class_name, obj_id)
            obj_dict = storage.all().get(key)
            if not obj_dict:
                print("** no instance found **")
            else:
                print(obj_dict)
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            obj_id = args[1]
            storage = FileStorage()
            storage.reload()
            key = "{}.{}".format(class_name, obj_id)
            obj_dict = storage.all().get(key)
            if not obj_dict:
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name."""
        args = arg.split()
        if args and args[0] not in ['BaseModel']:
            print("** class doesn't exist **")
            return
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        print([str(obj) for obj in objects.values()])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change
        into the JSON file).
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            obj_id = args[1]
            storage = FileStorage()
            storage.reload()
            key = "{}.{}".format(class_name, obj_id)
            obj_dict = storage.all().get(key)
            if not obj_dict:
                print("** no instance found **")
            else:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attr_name = args[2]
                    attr_value = args[3]
                    if hasattr(obj_dict, attr_name):
                        setattr(obj_dict, attr_name, attr_value)
                        storage.save()
                    else:
                        print("** attribute doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
