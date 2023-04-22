"""
Splunk .Conf Compiler is intended to improve the capabilities 
of maintaining .conf stanzas across all .conf files in local/ of a splunk app
"""
import os
import glob
import argparse
import sys


def argument_parser() -> argparse.Namespace:
    """
    Generates the argument parser and returns the parsed arguments.
    """
    # Settings for ArgumentParser()
    program_name = "splunk-conf-compiler"
    description = "A tool for compiling or decompiling splunk .conf files"   
    # Instance an argument parser
    parser = argparse.ArgumentParser(prog=program_name, description=description, )
    
    # Add arguments to argument parser
    parser.add_argument("action", choices=["compile", "decompile"], help="decide to compile or decompile the .conf directory")
    
    # TODO Implement include/exclude filter for .conf types. Only base on .conf type
    
    # return the parsed args
    return parser.parse_args()

def splunk_conf_compile() -> None:
    """
    The splunk_conf_compile function returns None, but will do all of the work for compiling .conf files in local/
    """

    # TODO Implement splunk_conf_compile
    # TODO Check if local/ exists in the direcctory
        # TODO handle and exit if local/ doesn't exist
    # TODO Determine types of .conf files to be compiled together
    # TODO Check only one layer deep for .conf files, Also check in the base of local/ dir for any .conf files
    # TODO Mash same named .conf files together and put them into the base of local/ dir
        # TODO spit out status page of compiling X number of whatever.conf
    return

def splunk_conf_decompile() -> None:
    """
    The splunk_conf_decompile function returns None, 
    but will do all of the work for decompiling .conf files in local/
    """
    # TODO Implement splunk_conf_decompile
    # TODO Check if local/ dir exists in the directory
    #     TODO handle and exit if local/ dir doesn't exist
    # TODO Determine .conf files to split by stanza 
    # TODO Parse through each .conf, stanza by stanza generating a <folder of stanza name>/whatever.conf
    return

def main() -> None:
    """
    The entry point for the splunk-conf-compiler module
    """
    args = argument_parser()
    if args.action == "compile":
        splunk_conf_compile()
    if args.action == "decompile":
        splunk_conf_decompile()
    return

if __name__ == '__main__':
    sys.exit(main())
