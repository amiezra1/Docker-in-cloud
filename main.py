from flask import Flask
from components import *
import json
import os
import logging

CONFIG_PATH = "config.json"

def loadConfig():
    try:
        with open(CONFIG_PATH) as config_file:
            return set(json.load(config_file))
    except FileNotFoundError:
        logger.critical("Error: Config file missing")

def savePermissions(permissions_set):
    with open(CONFIG_PATH, "w") as json_file:
        json.dump(list(permissions_set), json_file, indent=4)

def initLogger():
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s|%(funcName)s|%(levelname)s|%(message)s',
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )
    return logger

def createPage(text, size=20):
    input_box = createTextInputConnection()
    button = createButtonConnection("Click Here", size)
    script = createRedirectScript()
    
    return text + input_box + button + script


app = Flask(__name__)
logger = initLogger()
permissions_set = loadConfig()

@app.route("/")
def homePage():
    try:
        logger.info("The user has reached the home page")
        text_title = printBlue("If you want to connect, you need enter your name.")
        return createPage(text_title)
    except Exception as e:
        logger.critical(f"Error: {e}")

@app.route("/login/<name>")
def connect(name):
    try:
        name = name.lower()
        logger.info(f"The user has accessed the login with name {name}")
        if name in permissions_set:
            logger.info(f"Name {name} exists in list, access granted.")
            response = printGreen(f"{name.capitalize()} Welcome to my system!")
        else:
            logger.warning(f"Name {name} does not exists in list, access denied.")
            response = printRed("Access Denied")
        return createPage(response)
    except Exception as e:
        logger.critical(f"Error: {e}")

@app.route("/addNema")
def pageAddNema():
    try:
        response= "If you want to register, you need to add /(your name) in the URL"
        response_example = "Example: http://localhost/addNema/david" 
        logger.info("The user has reached the page 'addNema'")
        return printBlue(response,30)+printBlue(response_example,20)
    except Exception as e:
        logger.critical(f"Error: {e}")

@app.route("/addNema/<name>")
def addNema(name):
    try:
        name = name.lower()
        logger.info("The user tried to connect")
        permissions_set.add(name)

        savePermissions(permissions_set)

        logger.info(f"The name {name} has been successfully added")
        response = printGreen(f"The name {name} has been successfully added")
        
        return response
    except Exception as e:
        logger.critical(f"Error: {e}")



if __name__ == "__main__":
    app.run(host=os.environ.get("HOST_IP"), port=80)
