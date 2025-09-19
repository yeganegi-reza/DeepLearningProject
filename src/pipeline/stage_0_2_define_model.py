import sys
from components import ModelDefinition

from reytools.logger import logging
from reytools.exception import CustomException


STAGE_NAME = "Data Ingestion Stage"


class ModelDefinitionPipeline():
    def __init__(self):
        pass
    def start():
        model_definitaion = ModelDefinition()
        model_definitaion.load_base_model()
        model_definitaion.save_base_model()
        model_definitaion.update_base_model()
        model_definitaion.save_modified_model()



if __name__ == "__main__":
    try:
        logging.info(f">>>> stage {STAGE_NAME} started <<<<<\n\nX======X")
        pipeline = ModelDefinitionPipeline()
        pipeline.start()
        logging.info(f">>>> stage {STAGE_NAME} completed <<<<<\n\nX======X")

    except Exception as e:
                logging.exception(e)

        raise CustomException(e, sys)
