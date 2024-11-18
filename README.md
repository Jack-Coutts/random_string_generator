# Random String Generator

A simple program that can create a random alphanumeric string. The user can choose the length of the string and whether they want to append something to the random string. The program simply prints the output string to the terminal. I'll mostly use this to create "project codes" used for task management. 

## Developer Instructions


### Dependencies

* [Poetry](https://python-poetry.org/) for dependency management.
* [Python (3.12-3.14)](https://www.python.org/downloads/)

### Directory Structure

* `src/random_string_generator/main.py` is the file containing all of the code for the program.
* `pyproject.toml` is the configuration file used by poetry.
* `poetry.lock` controls dependency versions.
* `dist/main` the executable file created by [PyInstaller](https://pyinstaller.org/en/stable/) (the current one is only for mac).

### Development Instructions

* After the project has been git cloned, run `poetry install` to install the relevant dependencies from the `pyproject.toml`.
* To add a dependency, run `poetry add <dependency>`.
* To run the script via the poetry virtual environment, run `poetry run csv_writer`.
* To create a new executable, run `poetry run pyinstaller --onefile src_random_string_generator/main.py`. This pyinstaller command will also produce other artifacts: the `build/` directory and `main.spec` file. I do not need these so I delete them. 


## User Instructions

### Running the program

There are two ways to run this program:

* Using the executable file `rnd_str_exe_mac`. Using a GUI this file can simply be clicked and using the command line you can just run `rnd_str_exe_main`.
* Running `poetry run rnd_str` after the dependencies have been installed. 

### How it works

* The program might take a few seconds to start up after running.
* You will first be asked how long you want the random string to be, if you leave this blank the string will be 10 characters long.
* You will then be asked if you want to append anything to the random string. Answering no will print the random string, and answering yes will prompt you to enter this addition before printing the entire string.




