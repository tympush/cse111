#!/usr/bin/python3
import os


def init_script(file):
    os.system(f"touch {file}")
    os.system(f"chmod +x {file}")
    os.system(f"echo '#!/bin/bash' >> {file}")


def generate_help(file, arguments):
    template = f"""
if [ $# -lt 1 ] || [ "$1" = "--help" ]; then
    echo "Usage: $(basename "$0") {' '.join([f'arg{x}' for x in range(len(arguments))])}"
    echo "Example: $(basename "$0") {generate_examples_for_help(arguments)}"
    exit 1
fi"""
    os.system(f"echo '{template}' >> {file}")


def generate_examples_for_help(arguments):
    string = "hallo"
    number = "1"
    directory = "/etc"
    file = "example.txt"
    examples = []

    for key in arguments:
        match arguments[key]:
            case "STRING":
                examples.append(string)
            case "NUMBER":
                examples.append(number)
            case "DIRECTORY":
                examples.append(directory)
            case "FILE":
                examples.append(file)

    return " ".join(examples)


def optionals(file, arguments, arguments_optional):
    minargs = len(arguments)
    maxargs = len(arguments) + len(arguments_optional)
    
    optional_templates = []

    for x in range(minargs, maxargs):
        content = "set -- "
        for y in range(x):
            content += f"\"${y+1}\" "

        for y in range(maxargs - x):
            content += f"\"{arguments_optional[y+minargs][1]}\" "


        template = f"""
if [ $# -eq {x} ]; then
    {content}
fi"""
        optional_templates.append(template)


    
    if (minargs == maxargs):
        template = f"""
if [ $# -ne {minargs} ]; then
    echo "expected {minargs} arguments" >&2
    exit 1
fi"""
        os.system(f"echo '{template}' >> {file}")
        
        
    else:
        lesser_than_template = f"""
if [ $# -lt {minargs} ]; then
    exit 1
fi"""
        greater_than_template = f"""
if [ $# -gt {maxargs} ]; then
    exit 1
fi"""
        
        os.system(f"echo '{lesser_than_template}' >> {file}")
        os.system(f"echo '{greater_than_template}' >> {file}")

    for x in optional_templates:
        os.system(f"echo '{x}' >> {file}")


def as_root(file, root):
    template = """
if [ "$(id -u)" != "0" ]; then
    echo "This script must be executed as root" >&2
    exit 1
fi"""
    if root.lower() == "y":
        os.system(f"echo '{template}' >> {file}")


def header(file, arguments, arguments_optional, author, function, requires):
    os.system(f"printf '# Arguments: ' >> {file}")
    args = [f"arg{x} is a {arguments[x].lower()}" for x in arguments] + [
        f"arg{x} is a {arguments_optional[x][0].lower()}" for x in arguments_optional
    ]
    seperator = ", "
    os.system(f"echo {seperator.join(args)} >> {file}")

    os.system(f"echo '# Author: {author}' >> {file}")
    os.system(f"echo '# Copyright: 2014 GNU v3 {author}' >> {file}")
    os.system(f"echo '# Version: 0.1' >> {file}")
    os.system(f"echo '# Function: {function}' >> {file}")
    os.system(f"echo '# Requires: {requires}' >> {file}")


def input_validations(file, arguments, arguments_optional):
    os.system(f"echo '{amount_validation(len(arguments) + len(arguments_optional))}' >> {file}")
    for key in arguments:
        match arguments[key]:
            case "NUMBER":
                os.system(f"echo '{integer_validation(key)}' >> {file}")

            case "DIRECTORY":
                os.system(f"echo '{directory_validation(key)}' >> {file}")

            case "FILE":
                os.system(f"echo '{file_validation(key)}' >> {file}")

    for key in arguments_optional:
        match arguments_optional[key][0]:
            case "NUMBER":
                os.system(f"echo '{integer_validation(key)}' >> {file}")

            case "DIRECTORY":
                os.system(f"echo '{directory_validation(key)}' >> {file}")

            case "FILE":
                os.system(f"echo '{file_validation(key)}' >> {file}")


def file_validation(arg_nr):
    return f"""
if [ ! -f \"${arg_nr+1}\" ]; then
    echo "${arg_nr+1} is not a file" >&2
    exit 1
fi"""


def directory_validation(arg_nr):
    return f"""
if [ ! -d \"${arg_nr+1}\" ]; then
    echo "${arg_nr+1} is not a directory" >&2
    exit 1
fi"""


def integer_validation(arg_nr):
    return f"""
if [[ ! ${arg_nr+1} == ?(-)+([[:digit:]]) ]]; then
    echo "${arg_nr+1} is not an integer" >&2
    exit 1
fi"""


def amount_validation(count):
    return f"""
if [ $# -ne {count} ]; then
    echo "expected {count} arguments" >&2
    exit 1
fi"""


def main():
    types = ["STRING", "NUMBER", "DIRECTORY", "FILE"]

    name = str(input("Name: "))
    location = str(input("Location: "))
    arg_count = int(input("Arguments #: "))

    arguments = dict()
    arguments_optional = dict()
    optional = False

    for x in range(arg_count):
        if not optional:
            opt = str(input("Start optional parameters? [Y/N]: "))
            if opt.lower() == "y":
                optional = True

        for y in range(len(types)):
            print(f"{types[y]} ({y})", end=" ")

        argument_type = int(input(f"\nArgument {x} Type: "))

        if optional:
            default = str(input(f"Argument {x} default: "))
            arguments_optional[x] = [types[argument_type], default]
        else:
            arguments[x] = types[argument_type]

    author = str(input("Author: "))
    function = str(input("Function: "))
    requires = str(input("Requires: "))
    root = str(input("Root? [Y/N]: "))

    file = f"{location}/{name}.sh"
    init_script(file)
    header(file, arguments, arguments_optional, author, function, requires)
    optionals(file, arguments, arguments_optional)
    generate_help(file, arguments)
    as_root(file, root)
    input_validations(file, arguments, arguments_optional)


if __name__ == "__main__":
    main()
