################################################################################################
# major drawback of python: no const -> may accidentally alter wrong variable
#
# modules: A file that defines a collection of useful functions and
#          variables that, usually, have a common theme/purpose.
#   function call from module: <module_name>.func()
#
# what does import do?
#   - executes the module as it is imported
#   - From Python’s perspective, the module is just a bunch of
#     statements (variable assignments, function definitions,
#     etc.) which, when imported, executes from top to bottom.
#   - python only loads a module once; subsequent imports are ignored
#
# modules can and should have docstrings: triple quotes, first line of module
#
# script vs. module: effectively the same, but scripts are intended to be executed as a program;
#                    scripts may import modules
#
# if we want to use a function from a module in the command line without having to 
# start the python interpreter each time, use the __name__
#   - __name__ is a special variable defined for every module
#   - when imported as a module, variable __name__ is assigned the name of the module
#   - when executing the sutherland.py file as a script (python sutherland.py), we 
#     are executing the script as the "main program" ""user""; the __name__ variable is 
#     assigned the value, "__main__"
# This means we can query the __name__ variable provided by python to change the behavior
# of the module/script depending on how it is being used
################################################################################################
# Representing floating point numbers
#   For example,
#       507.89 = (+1) * 50789 * 10^-2
#           – the sign is +
#           – the significand is 50789
#           – the base is 10
#           – the exponent is -2
# The layout of an IEEE 754 32-bit “single precision” float is
#   – 1 sign bit                            bit 31
#   – 8 exponent bits (with a base of 2)    bits 30-23
#   – 23 significand bits                   bits 22-0
#
# Python’s float type is an IEEE 754 64-bit “double precision”
# which provides, in decimal terms,
#   - 15+ significant figures of precision
#   - A base/exponent range of 10 to 10 !308 308
#
# The difference between 1.0 and the next larger representable number is called the machine epsilon
################################################################################################





























