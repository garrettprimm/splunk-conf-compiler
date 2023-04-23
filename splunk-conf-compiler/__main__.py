"""
Splunk .Conf Compiler is intended to improve the capabilities 
of maintaining .conf stanzas across all .conf files in local/ of a splunk app
"""
from ast import And
import fileinput
import os
import glob
import argparse
import sys
from itertools import groupby
import shutil

def path_check(configdir: str) -> bool:
    """
    Check if the config dir exists. This takes an input from the argument parser. 
    The default value is configured in argument parser.
    """
    # Check if local/ exists in the direcctory
    if os.path.exists(configdir):
        print(f"{configdir} exists")
    else:
        raise FileNotFoundError(f"{configdir} does not exist")

def argument_parser() -> argparse.Namespace:
    """
    Generates the argument parser and returns the parsed arguments.
    """
    # Settings for ArgumentParser()
    program_name = "splunk-conf-compiler"
    description = "A tool for compiling or decompiling splunk .conf files."
    # Instance an argument parser
    parser = argparse.ArgumentParser(prog=program_name, description=description, )
    
    # Add arguments to argument parser
    parser.add_argument("action",type=str, choices=["compile", "decompile"], help="decide to compile or decompile the .conf directory")
    parser.add_argument("-cd","--config_dir",type=str,default=os.path.join(os.getcwd(),"local/"),nargs="?", help="directory of .conf files to be compiled")
    # TODO Implement include/exclude filter for .conf types. Only base on .conf type
    
    # return the parsed args
    return parser.parse_args()

def splunk_conf_compile(arguments: argparse.Namespace) -> None:
    """
    The splunk_conf_compile function returns None, 
    but will do all of the work for compiling .conf files in local/
    """
    config_dir = arguments.config_dir
    path_check(config_dir)
    print("compiling .conf")
    # DONE Check only one layer deep for .conf files, Also check in the base of local/ dir for any .conf files
    conf_files = glob.glob(pathname=f"{config_dir}/**/**.conf", recursive=True)
    # DONE Determine types of .conf files to be compiled together
    conf_object = sorted([{"path": file, "type":os.path.split(file)[1]} for file in conf_files], key=lambda e: e['type'])
    # DONE Mash same named .conf files together and put them into the base of local/ dir
    for conf_type, grouped_conf_object in groupby(conf_object, key=lambda e: e['type']):
        grouped_conf_files = [conf['path'] for conf in grouped_conf_object]
        with open(f"{config_dir}/.tmp.{conf_type}", 'w') as fout, fileinput.input(grouped_conf_files) as fin:
            # TODO spit out status page of compiling X number of whatever.conf
            for line in fin:
                if fin.isfirstline() and (os.path.dirname(fin.filename()) != os.path.dirname(config_dir) ):
                    fout.write("\n\n")
                    fout.write(line)
                elif (os.path.dirname(fin.filename()) != os.path.dirname(config_dir)):
                    fout.write(line)
                else:
                    fout.write(line)
    # TODO implement writing .tmp.* file
    tmp_files = glob.glob(pathname=f"{config_dir}/.tmp.*.conf")
    for file in tmp_files:
        shutil.move(file, os.path.join(os.path.dirname(file),os.path.basename(file).strip(".tmp.")))
    # TODO Cleanup any old files not in root of config_dir
    cleanup_files =  [os.path.dirname(file) for file in conf_files if os.path.dirname(file) != os.path.dirname(config_dir)]
    for each in cleanup_files:
        shutil.rmtree(each)
    print("compiling complete")
    return

def splunk_conf_decompile(arguments: argparse.Namespace) -> None:
    """
    The splunk_conf_decompile function returns None, 
    but will do all of the work for decompiling .conf files in local/
    """
    config_dir = arguments.config_dir
    path_check(config_dir)
    
    
    # TODO Determine .conf files to split by stanza 
    # TODO Parse through each .conf, stanza by stanza generating a <folder of stanza name>/whatever.conf
    return

def main() -> None:
    """
    The entry point for the splunk-conf-compiler module
    """
    args = argument_parser()
    if args.action == "compile":
        splunk_conf_compile(args)
    if args.action == "decompile":
        splunk_conf_decompile(args)
    return

if __name__ == '__main__':
    sys.exit(main())
