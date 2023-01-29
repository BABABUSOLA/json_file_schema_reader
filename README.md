# Installation

- Let’s start by installing the python3-venv package that provides the venv module on an ubuntu machine

sudo apt install python3-venv

# Activate virtual environment

- Switch to the directory where you would like to store your Python 3 virtual environments. Within the directory run the following command to create your new virtual environment:

python3 -m venv venv

- To start using this virtual environment, you need to activate it by running the activate script:

source venv/bin/activate

# Run the main.py file

- To run the main.py file

python main.py

# Run the main_test.py file

- To run the unittest main_test.py file

python -m unittest full_test.py

# Other information

- Uncomment the lines referencing the data_2.json and schema_2.json files when ready, to test.
