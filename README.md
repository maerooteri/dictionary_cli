This application is a dictionary cli tool that give you the meaning of words

# How to use this tool

1. Download this repository or clone the repository to your local
2. Navigate to the src directory using your command line and run the command below

python dictionary.py

It prompts you to enter a word, e.g exercise

Then it gives you an output that looks like this;
ek-sər-ˌsīz (noun): the act of bringing into play or realizing in action

The first output parameter is the dictionary pronunciation of the word
The parameter in the brackets gives the part of speech the word belongs to.
The last parameter gives a description of the word



# Development
Signed up to dictionaryapi website and Requested API keys from https://dictionaryapi.com/products/api-collegiate-dictionary for Collegiate Dictionary
After registering, Sign in and Go to "Your Keys" section to get the API keys


To create a python virtual environment from our cmd terminal/cli we use the command
python -m venv pvenv 

We activate the virtual environment on windows with the command below
pvenv\Scripts\activate.bat

We activate the virtual environment On mac or linux with the command below
source venv/bin/activate


After activating the virtual environment (pvenv), run this command
pip install --upgrade pip

pip install requests
pip install python-dotenv
pip install pytest

To get the python libraries used for this project
pip freeze > requirements.txt

The requirements.txt file is important for Contionous testing and Continuous integration using Github Actions which we will set up to run our tests automatically when we push changes to github

OR if you want to use my requirements.txt file, run the below command

pip install -r requirements.txt

To run the tests locally on windows (Run the command below in Command Line CLI Terminal), First (set Environment variables)
set PYTHONPATH=src
pytest

To run the tests locally on mac/linux (Run in Command Line CLI Terminal)
export PYTHONPATH=src
pytest



