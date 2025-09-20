import sys
from components import ModelTraining

from reytools.exception import CustomException
from reytools.logger import logging

STAGE_NAME = "Model Trainig Stage"


class ModelTrainigPipeline:
    def __init__(self):
        pass

    def start(self):
        component = ModelTraining()


if __name__ == "__main__":
    try:
        logging.info(f">>>> stage {STAGE_NAME} started <<<<<\n\nX======X")
        pipeline = ModelTrainigPipeline()
        pipeline.start()
        logging.info(f">>>> stage {STAGE_NAME} completed <<<<<\n\nX======X")
    except Exception as e:
        logging.exception(e)
        raise CustomException(e, sys)
