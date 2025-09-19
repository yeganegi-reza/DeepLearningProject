import sys
from components import DataIngestion

from reytools.exception import CustomException
from reytools.logger import logging

STAGE_NAME = "Data Ingestion Stage"


class DataIngestionPipeline:
    def __init__(self):
        pass

    def start(self):
        data_ing_comp = DataIngestion()
        data_ing_comp.download_file()
        data_ing_comp.extract_zip_file()


if __name__ == "__main__":
    try:
        logging.info(f">>>> stage {STAGE_NAME} started <<<<<\n\nX======X")
        pipeline = DataIngestionPipeline()
        pipeline.start()
        logging.info(f">>>> stage {STAGE_NAME} completed <<<<<\n\nX======X")
    except Exception as e:
        logging.exception(e)
        raise CustomException(e, sys)
