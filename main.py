import sys

from reytools.logger import logging
from reytools.exception import CustomException

from pipeline.stage_0_1_data_ingestion import DataIngestionPipeline


STAGE_NAME = "Data Ingestion"   

try: 
    pipeline = DataIngestionPipeline()
    pipeline.start()
    logging.info(f">>>> Stage {STAGE_NAME} completed <<<<<\n\nX======X")
except Exception as e:
    logging.exception(e)
    raise CustomException(e, sys)
