#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""


import cmd
import shlex
import models.base_model
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """A HBNBCommand Class"""
    prompt = '(hbnb) '

    def precmd(self, arg):
        if arg:
            # Handling when there is a dot method in command execution
            if "." in arg:
                # Splitting into arg_1 and command_plus
                arg_1, command_plus = arg.split('.', 1)

                if command_plus.startswith('update'):
                    # Slicing command_plus to extract command and arg_2
                    command, arg_2 = command_plus.split('("', 1)
                    arg_split = arg_2.split(',')
                    if len(arg_split) == 3:
                        a3, a4, a5 = arg_split
                        a3 = a3.strip('"')
                        a4 = a4[1:].strip('"')
                        a5 = a5[1:].strip('")')
                        arg = f"{command} {arg_1} {a3} {a4} {a5}"
                    elif len(arg_split) == 2:
                        a3, a4 = arg_split
                        a3 = a3.strip('"')
                        arg = f"{command} {arg_1} {a3} {a4}"
                    elif len(arg_split) == 1:
                        a3 = arg_2.strip('")')
                        arg = f"{command} {arg_1} {a3}"
                else:
                    # Slicing command_plus to extract command and arg_2
                    if '("' in command_plus:
                        command, arg_2 = command_plus.split('("', 1)
                        arg_2 = arg_2[:-2]
                    elif '(' in command_plus:
                        command, arg_2 = command_plus.split('(', 1)
                        arg_2 = arg_2[:-1]
                    elif "('" in command_plus:
                        command, arg_2 = command_plus.split("('", 1)
                        arg_2 = arg_2[:-2]
                    else:
                        return arg

                    # Reorder and format the components
                    arg = "{} {} {}".format(command, arg_1, arg_2)

        return arg

    def do_create(self, arg=""):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if arg == "":
            print("** class name missing **")
            return

        if arg not in ["BaseModel", "User", "State",
                       "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        if arg == "BaseModel":
            new_instance = models.base_model.BaseModel()
            new_instance.save()
            print(new_instance.id)
        elif arg == "User":
            new_instance = User()
            new_instance.save()
            print(new_instance.id)
        elif arg == "State":
            new_instance = State()
            new_instance.save()
            print(new_instance.id)
        elif arg == "City":
            new_instance = City()
            new_instance.save()
            print(new_instance.id)
        elif arg == "Amenity":
            new_instance = Amenity()
            new_instance.save()
            print(new_instance.id)
        elif arg == "Place":
            new_instance = Place()
            new_instance.save()
            print(new_instance.id)
        elif arg == "Review":
            new_instance = Review()
            new_instance.save()
            print(new_instance.id)

    def do_count(self, arg):
        """Retrieves the number of instances of a class"""
        count = 0
        all_objs = storage.all()
        for key in all_objs.keys():
            if key.startswith(arg):
                count += 1
        print(count)

    def do_show(self, arg=""):
        """Prints the string representation of an instance
        based on the class name and id"""
        if arg == "":
            print("** class name missing **")
            return

        args = arg.split(" ")
        if len(args) == 1:
            if args[0] not in ["BaseModel", "User",
                               "State", "City", "Amenity", "Place", "Review"]:
                print("** class doesn't exist **")
                return
            print("** instance id missing **")
            return

        if len(args) == 2:
            if args[0] == "BaseModel":
                class_name = args[0]
                instance_id = args[1]

                all_objs = storage.all()

                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "BaseModel":
                        all_ids.append(ids)

                if instance_id not in all_ids:
                    print("** no instance found **")
                else:
                    key_id = "BaseModel.{}".format(instance_id)
                    model = all_objs[key_id]
                    print(model)
            elif args[0] == "User":
                class_name = args[0]
                instance_id = args[1]

                all_objs = storage.all()

                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "User":
                        all_ids.append(ids)

                if instance_id not in all_ids:
                    print("** no instance found **")
                else:
                    key_id = "User.{}".format(instance_id)
                    model = all_objs[key_id]
                    print(model)
            elif args[0] == "State":
                class_name = args[0]
                instance_id = args[1]

                all_objs = storage.all()

                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "State":
                        all_ids.append(ids)

                if instance_id not in all_ids:
                    print("** no instance found **")
                else:
                    key_id = "State.{}".format(instance_id)
                    model = all_objs[key_id]
                    print(model)
            elif args[0] == "City":
                class_name = args[0]
                instance_id = args[1]

                all_objs = storage.all()

                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "City":
                        all_ids.append(ids)

                if instance_id not in all_ids:
                    print("** no instance found **")
                else:
                    key_id = "City.{}".format(instance_id)
                    model = all_objs[key_id]
                    print(model)
            elif args[0] == "Amenity":
                class_name = args[0]
                instance_id = args[1]

                all_objs = storage.all()

                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "Amenity":
                        all_ids.append(ids)

                if instance_id not in all_ids:
                    print("** no instance found **")
                else:
                    key_id = "Amenity.{}".format(instance_id)
                    model = all_objs[key_id]
                    print(model)
            elif args[0] == "Place":
                class_name = args[0]
                instance_id = args[1]

                all_objs = storage.all()

                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "Place":
                        all_ids.append(ids)

                if instance_id not in all_ids:
                    print("** no instance found **")
                else:
                    key_id = "Place.{}".format(instance_id)
                    model = all_objs[key_id]
                    print(model)
            elif args[0] == "Review":
                class_name = args[0]
                instance_id = args[1]

                all_objs = storage.all()

                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "Review":
                        all_ids.append(ids)

                if instance_id not in all_ids:
                    print("** no instance found **")
                else:
                    key_id = "Review.{}".format(instance_id)
                    model = all_objs[key_id]
                    print(model)

    def do_destroy(self, arg=""):
        """Deletes an instance based on the class name and
        id (save the change into the JSON file)."""
        if arg == "":
            print("** class name missing **")
            return

        args = arg.split(" ")
        if len(args) == 1:
            if args[0] not in ["BaseModel", "User",
                               "State", "City", "Amenity", "Place", "Review"]:
                print("** class doesn't exist **")
                return
            print("** instance id missing **")
            return

        if len(args) == 2:
            if args[0] == "BaseModel":
                class_name = args[0]
                instance_id = args[1]

                all_objs = storage.all()
                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "BaseModel":
                        all_ids.append(ids)

                if instance_id not in all_ids:
                    print("** no instance found **")
                else:
                    key_id = "BaseModel.{}".format(instance_id)
                    all_objs.pop(key_id)
                    storage.save()
            elif args[0] == "User":
                class_name = args[0]
                instance_id = args[1]

                all_objs = storage.all()
                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "User":
                        all_ids.append(ids)

                if instance_id not in all_ids:
                    print("** no instance found **")
                else:
                    key_id = "User.{}".format(instance_id)
                    all_objs.pop(key_id)
                    storage.save()
            elif args[0] == "State":
                class_name = args[0]
                instance_id = args[1]

                all_objs = storage.all()
                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "State":
                        all_ids.append(ids)

                if instance_id not in all_ids:
                    print("** no instance found **")
                else:
                    key_id = "State.{}".format(instance_id)
                    all_objs.pop(key_id)
                    storage.save()
            elif args[0] == "City":
                class_name = args[0]
                instance_id = args[1]

                all_objs = storage.all()
                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "City":
                        all_ids.append(ids)

                if instance_id not in all_ids:
                    print("** no instance found **")
                else:
                    key_id = "City.{}".format(instance_id)
                    all_objs.pop(key_id)
                    storage.save()
            elif args[0] == "Amenity":
                class_name = args[0]
                instance_id = args[1]

                all_objs = storage.all()
                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "Amenity":
                        all_ids.append(ids)

                if instance_id not in all_ids:
                    print("** no instance found **")
                else:
                    key_id = "Amenity.{}".format(instance_id)
                    all_objs.pop(key_id)
                    storage.save()
            elif args[0] == "Place":
                class_name = args[0]
                instance_id = args[1]

                all_objs = storage.all()
                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "Place":
                        all_ids.append(ids)

                if instance_id not in all_ids:
                    print("** no instance found **")
                else:
                    key_id = "Place.{}".format(instance_id)
                    all_objs.pop(key_id)
                    storage.save()
            elif args[0] == "Review":
                class_name = args[0]
                instance_id = args[1]

                all_objs = storage.all()
                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "Review":
                        all_ids.append(ids)

                if instance_id not in all_ids:
                    print("** no instance found **")
                else:
                    key_id = "Review.{}".format(instance_id)
                    all_objs.pop(key_id)
                    storage.save()

    def do_all(self, arg=""):
        """Prints all string representation of all instances
        based or not on the class name."""
        if arg == "":
            instances_strings = []
            all_objs = storage.all()
            for key in all_objs.keys():
                instance = all_objs[key]
                instance_to_str = str(instance)
                instances_strings.append(instance_to_str)
            print(instances_strings)
            return

        if arg not in ["BaseModel", "User",
                       "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        if arg == "BaseModel":
            instances_strings = []
            all_objs = storage.all()
            for key in all_objs.keys():
                model, ids = key.split(".")
                if model == "BaseModel":
                    instance = all_objs[key]
                    instance_to_str = str(instance)
                    instances_strings.append(instance_to_str)
            print(instances_strings)
        elif arg == "User":
            instances_strings = []
            all_objs = storage.all()
            for key in all_objs.keys():
                model, ids = key.split(".")
                if model == "User":
                    instance = all_objs[key]
                    instance_to_str = str(instance)
                    instances_strings.append(instance_to_str)
            print(instances_strings)
        elif arg == "State":
            instances_strings = []
            all_objs = storage.all()
            for key in all_objs.keys():
                model, ids = key.split(".")
                if model == "State":
                    instance = all_objs[key]
                    instance_to_str = str(instance)
                    instances_strings.append(instance_to_str)
            print(instances_strings)
        elif arg == "City":
            instances_strings = []
            all_objs = storage.all()
            for key in all_objs.keys():
                model, ids = key.split(".")
                if model == "City":
                    instance = all_objs[key]
                    instance_to_str = str(instance)
                    instances_strings.append(instance_to_str)
            print(instances_strings)
        elif arg == "Amenity":
            instances_strings = []
            all_objs = storage.all()
            for key in all_objs.keys():
                model, ids = key.split(".")
                if model == "Amenity":
                    instance = all_objs[key]
                    instance_to_str = str(instance)
                    instances_strings.append(instance_to_str)
            print(instances_strings)
        elif arg == "Place":
            instances_strings = []
            all_objs = storage.all()
            for key in all_objs.keys():
                model, ids = key.split(".")
                if model == "Place":
                    instance = all_objs[key]
                    instance_to_str = str(instance)
                    instances_strings.append(instance_to_str)
            print(instances_strings)
        elif arg == "Review":
            instances_strings = []
            all_objs = storage.all()
            for key in all_objs.keys():
                model, ids = key.split(".")
                if model == "Review":
                    instance = all_objs[key]
                    instance_to_str = str(instance)
                    instances_strings.append(instance_to_str)
            print(instances_strings)

    def do_update(self, arg=""):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        if arg == "":
            print("** class name missing **")
            return

        args = arg.split(" ")
        if len(args) == 1:
            if args[0] not in ["BaseModel", "User",
                               "State", "City", "Amenity", "Place", "Review"]:
                print("** class doesn't exist **")
                return
            print("** instance id missing **")
            return

        all_objs = storage.all()
        if len(args) == 2:
            if args[0] == "BaseModel":
                key_id = "BaseModel.{}".format(args[1])
                if key_id not in all_objs.keys():
                    print("** no instance found **")
                    return
                print("** attribute name missing **")
                return
            elif args[0] == "User":
                key_id = "User.{}".format(args[1])
                if key_id not in all_objs.keys():
                    print("** no instance found **")
                    return
                print("** attribute name missing **")
                return

        if len(args) == 3:
            print("** value missing **")
            return

        if len(args) == 4:
            if args[0] == "BaseModel":
                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "BaseModel":
                        all_ids.append(ids)

                if args[1] not in all_ids:
                    print("** no instance found **")
                    return
                else:
                    class_name = args[0]
                    instance_id = args[1]
                    attribute = args[2]
                    attr_value = args[3]

                    # Strip surrounding quotes on attribute if any
                    if attribute.startswith('"') and attribute.endswith('"'):
                        attribute = attribute[1:-1]
                    elif attribute.startswith("'") and attribute.endswith("'"):
                        attribute = attribute[1:-1]

                    # Strip surrounding quotes on attribute_value if any
                    if attr_value.startswith('"') and attr_value.endswith('"'):
                        attr_value = attr_value[1:-1]
                    elif attr_value.startswith("'") and \
                            attr_value.endswith("'"):
                        attr_value = attr_value[1:-1]

                    key_id = "{}.{}".format(class_name, instance_id)
                    value = all_objs.get(key_id)
                    value_dict = value.to_dict()
                    value_dict[attribute] = attr_value
                    value_object = models.base_model.BaseModel(**value_dict)
                    value = value_object
                    for keys in all_objs.keys():
                        if keys == key_id:
                            all_objs[keys] = value
                    storage.save()
            if args[0] == "User":
                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "User":
                        all_ids.append(ids)

                if args[1] not in all_ids:
                    print("** no instance found **")
                    return
                else:
                    class_name = args[0]
                    instance_id = args[1]
                    attribute = args[2]
                    attr_value = args[3]

                    # Strip surrounding quotes on attribute if any
                    if attribute.startswith('"') and attribute.endswith('"'):
                        attribute = attribute[1:-1]
                    elif attribute.startswith("'") and attribute.endswith("'"):
                        attribute = attribute[1:-1]

                    # Strip surrounding quotes on attribute_value if any
                    if attr_value.startswith('"') and attr_value.endswith('"'):
                        attr_value = attr_value[1:-1]
                    elif attr_value.startswith("'") and \
                            attr_value.endswith("'"):
                        attr_value = attr_value[1:-1]

                    key_id = "{}.{}".format(class_name, instance_id)
                    value = all_objs.get(key_id)
                    value_dict = value.to_dict()
                    value_dict[attribute] = attr_value
                    value_object = models.base_model.BaseModel(**value_dict)
                    value = value_object
                    for keys in all_objs.keys():
                        if keys == key_id:
                            all_objs[keys] = value
                    storage.save()
            if args[0] == "State":
                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "State":
                        all_ids.append(ids)

                if args[1] not in all_ids:
                    print("** no instance found **")
                    return
                else:
                    class_name = args[0]
                    instance_id = args[1]
                    attribute = args[2]
                    attr_value = args[3]

                    # Strip surrounding quotes on attribute if any
                    if attribute.startswith('"') and attribute.endswith('"'):
                        attribute = attribute[1:-1]
                    elif attribute.startswith("'") and attribute.endswith("'"):
                        attribute = attribute[1:-1]

                    # Strip surrounding quotes on attribute_value if any
                    if attr_value.startswith('"') and attr_value.endswith('"'):
                        attr_value = attr_value[1:-1]
                    elif attr_value.startswith("'") and \
                            attr_value.endswith("'"):
                        attr_value = attr_value[1:-1]

                    key_id = "{}.{}".format(class_name, instance_id)
                    value = all_objs.get(key_id)
                    value_dict = value.to_dict()
                    value_dict[attribute] = attr_value
                    value_object = models.base_model.BaseModel(**value_dict)
                    value = value_object
                    for keys in all_objs.keys():
                        if keys == key_id:
                            all_objs[keys] = value
                    storage.save()
            if args[0] == "City":
                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "City":
                        all_ids.append(ids)

                if args[1] not in all_ids:
                    print("** no instance found **")
                    return
                else:
                    class_name = args[0]
                    instance_id = args[1]
                    attribute = args[2]
                    attr_value = args[3]

                    # Strip surrounding quotes on attribute if any
                    if attribute.startswith('"') and attribute.endswith('"'):
                        attribute = attribute[1:-1]
                    elif attribute.startswith("'") and attribute.endswith("'"):
                        attribute = attribute[1:-1]

                    # Strip surrounding quotes on attribute_value if any
                    if attr_value.startswith('"') and attr_value.endswith('"'):
                        attr_value = attr_value[1:-1]
                    elif attr_value.startswith("'") and \
                            attr_value.endswith("'"):
                        attr_value = attr_value[1:-1]

                    key_id = "{}.{}".format(class_name, instance_id)
                    value = all_objs.get(key_id)
                    value_dict = value.to_dict()
                    value_dict[attribute] = attr_value
                    value_object = models.base_model.BaseModel(**value_dict)
                    value = value_object
                    for keys in all_objs.keys():
                        if keys == key_id:
                            all_objs[keys] = value
                    storage.save()
            if args[0] == "Amenity":
                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "Amenity":
                        all_ids.append(ids)

                if args[1] not in all_ids:
                    print("** no instance found **")
                    return
                else:
                    class_name = args[0]
                    instance_id = args[1]
                    attribute = args[2]
                    attr_value = args[3]

                    # Strip surrounding quotes on attribute if any
                    if attribute.startswith('"') and attribute.endswith('"'):
                        attribute = attribute[1:-1]
                    elif attribute.startswith("'") and attribute.endswith("'"):
                        attribute = attribute[1:-1]

                    # Strip surrounding quotes on attribute_value if any
                    if attr_value.startswith('"') and attr_value.endswith('"'):
                        attr_value = attr_value[1:-1]
                    elif attr_value.startswith("'") and \
                            attr_value.endswith("'"):
                        attr_value = attr_value[1:-1]

                    key_id = "{}.{}".format(class_name, instance_id)
                    value = all_objs.get(key_id)
                    value_dict = value.to_dict()
                    value_dict[attribute] = attr_value
                    value_object = models.base_model.BaseModel(**value_dict)
                    value = value_object
                    for keys in all_objs.keys():
                        if keys == key_id:
                            all_objs[keys] = value
                    storage.save()
            if args[0] == "Place":
                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "Place":
                        all_ids.append(ids)

                if args[1] not in all_ids:
                    print("** no instance found **")
                    return
                else:
                    class_name = args[0]
                    instance_id = args[1]
                    attribute = args[2]
                    attr_value = args[3]

                    # Strip surrounding quotes on attribute if any
                    if attribute.startswith('"') and attribute.endswith('"'):
                        attribute = attribute[1:-1]
                    elif attribute.startswith("'") and attribute.endswith("'"):
                        attribute = attribute[1:-1]

                    # Strip surrounding quotes on attribute_value if any
                    if attr_value.startswith('"') and attr_value.endswith('"'):
                        attr_value = attr_value[1:-1]
                    elif attr_value.startswith("'") and \
                            attr_value.endswith("'"):
                        attr_value = attr_value[1:-1]

                    key_id = "{}.{}".format(class_name, instance_id)
                    value = all_objs.get(key_id)
                    value_dict = value.to_dict()
                    value_dict[attribute] = attr_value
                    value_object = models.base_model.BaseModel(**value_dict)
                    value = value_object
                    for keys in all_objs.keys():
                        if keys == key_id:
                            all_objs[keys] = value
                    storage.save()
            if args[0] == "Review":
                all_ids = []
                base_ids = [key for key in all_objs.keys()]
                for value in base_ids:
                    model, ids = value.split(".")
                    if model == "Review":
                        all_ids.append(ids)

                if args[1] not in all_ids:
                    print("** no instance found **")
                    return
                else:
                    class_name = args[0]
                    instance_id = args[1]
                    attribute = args[2]
                    attr_value = args[3]

                    # Strip surrounding quotes on attribute if any
                    if attribute.startswith('"') and attribute.endswith('"'):
                        attribute = attribute[1:-1]
                    elif attribute.startswith("'") and attribute.endswith("'"):
                        attribute = attribute[1:-1]

                    # Strip surrounding quotes on attribute_value if any
                    if attr_value.startswith('"') and attr_value.endswith('"'):
                        attr_value = attr_value[1:-1]
                    elif attr_value.startswith("'") and \
                            attr_value.endswith("'"):
                        attr_value = attr_value[1:-1]

                    key_id = "{}.{}".format(class_name, instance_id)
                    value = all_objs.get(key_id)
                    value_dict = value.to_dict()
                    value_dict[attribute] = attr_value
                    value_object = models.base_model.BaseModel(**value_dict)
                    value = value_object
                    for keys in all_objs.keys():
                        if keys == key_id:
                            all_objs[keys] = value
                    storage.save()
        else:
            return

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("Exit the command interpreter gracefully.")

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
