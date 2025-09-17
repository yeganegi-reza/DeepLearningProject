import os
import sys

import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import any
import base64


from logger import logging
from exception import CustomException


@ensure_annotations
def read_yaml(path_to_yaml: Path):
    """This fuction reads a yaml file and returs its content

    Args:
        path_to_yaml (str): path like input

    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        logging.info(f"yaml file: {path_to_yaml} loading Failed")
        raise CustomException(e, sys)


@ensure_annotations
def save_json(path: Path, data: dict):
    pass
