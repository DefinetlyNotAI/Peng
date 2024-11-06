import os
import subprocess
import sys
import argparse
import logging
from Replacements import replacements_function, replacements_non_function


def combine_dicts(Operator_Dictionary, Function_Dictionary):
    modified_dict = {}
    for key, value in Operator_Dictionary.items():
        modified_dict[key] = value + " "
    non_func = {' ' + key + ' ': value for key, value in modified_dict.items()}
    func = {' ' + key: value for key, value in Function_Dictionary.items()}
    combined_dict = {**non_func, **func}
    return combined_dict


def transcriber():
    parser = argparse.ArgumentParser(description="Transcribe .peng files to .py files.")
    parser.add_argument('filename', type=str, nargs='?', default=None, help='Filename to process')
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-d", "--delete", action="store_true", help="Delete the inputted .peng file.")
    group.add_argument("-r", "--run", action="store_true", help="Run the generated .py file.")

    args = parser.parse_args()

    if args.filename is None:
        logging.info("Usage: python Peng.py [--del] [--run]")
        return

    replacements = combine_dicts(replacements_non_function, replacements_function)
    if len(sys.argv) < 2:
        logging.error("Usage: python peng.py <filename> [-d|--del] [-r|--run]")
        return

    peng_file = sys.argv[1].replace(".peng", ".py")
    if args.delete:
        try:
            os.remove(sys.argv[1])
        except FileNotFoundError:
            logging.error(f"File '{sys.argv[1]}' not found.")
        return

    if args.run:
        try:
            subprocess.run(["python", peng_file], check=True)
        except Exception as e:
            logging.error(f"Failed to run file: {peng_file}\nError: {e}")
        return

    try:
        with open(sys.argv[1], "r") as infile, open(peng_file, "w") as outfile:
            for line in infile:
                for key, value in replacements.items():
                    line = line.replace(key, " " + value)
                outfile.write(line)
    except FileNotFoundError:
        logging.error(f"File '{sys.argv[1]}' not found.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    transcriber()
else:
    raise ImportError("Peng should be run as a standalone script.")
