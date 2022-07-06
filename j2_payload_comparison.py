# Jinja2 Payload Example

import argparse
import jinja2
import json
import os


def init_lol_payload():
    """
    Initialize a hardcoded list of lists (lol) data structure with two elements,
    0 the vlan number
    1 the vlan name
    :return: payload_list
    """
    payload_list = [
    ["5", "vlan5_1.1.1.0_24"],
    ["7", "vlan7_7.1.1.0_24"],
    ["10", "vlan10_10.1.1.0_24"],
    ]

    return payload_list

def init_lod_payload():
    """
    Initialize a hardcoded list of dictionaries (lod) data structure.  Each element of the list is a dictionary.
    key "vlan" holds the vlan number
    key "name"  holds the vlan name
    :return:
    """
    payload_lod = [
    {"vlan": "5", "name": "vlan5_1.1.1.0_24"},
    {"vlan": "7", "name": "vlan7_7.1.1.0_24"},
    {"vlan": "10", "name": "vlan10_10.1.1.0_24"},
    ]
    return payload_lod

def main():

    """
    Examples of data structures used as Jinja2 Template payload
    :return:
    """

    print("\n\n---- Configuration Payload of type list[] of lists[] ----\n\n")
    print(json.dumps(init_lol_payload(), indent=4))
    print("\n\n---- Configuration Payload of type list[] of dictionaries {} ----\n\n")
    print(json.dumps(init_lod_payload(), indent=4))

    # Define a template environment or directory that will hold all your templates
    j2template_env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))

    # Load a specific template in your environment in preparation for rendering
    vlan_template = j2template_env.get_template("test.j2")
    print(vlan_template.render(mylistvar=init_lol_payload()))

    print("\n\n--- Template Rendering with a List of Lists Payload")
    vlan_list_template = j2template_env.get_template("vlan_list.j2")
    print(vlan_list_template.render(mylistvar=init_lol_payload()))


    print("\n\n--- Template Rendering with a List of Dictionaries Payload")
    vlan_lod_template = j2template_env.get_template("vlan_lod.j2")
    print(vlan_lod_template.render(mylistvar=init_lod_payload()))


    # Save List of Dictionary to a JSON
    my_list_of_dicts_payload = init_lod_payload()
    my_lod_filename = "vlan_lod.json"

    with open(my_lod_filename, "w") as json_file:
        json.dump(my_list_of_dicts_payload, json_file, indent=4)

    print(f"\nList of dictionaries configuration payload saved to directory:\n\t{os.getcwd()} \n\tas file {my_lod_filename}\n\n")



# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python j2_payload_comp.py' ")

    # parser.add_argument('all', help='Execute all exercises in week 4 assignment')
    # parser.add_argument('-a', '--all', help='Execute all exercises in week 4 assignment', action='store_true', default=False)
    arguments = parser.parse_args()
    main()
