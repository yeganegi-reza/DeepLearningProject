import os

from pathlib import Path
from config import ConfigManager

from dataclasses import dataclass
from ensure import ensure_annotations

from reytools.logger import logging
from reytools.file_system import create_directories
from reytools.file_system import get_file_size
from reytools.file_system import unzip_file

from urllib import request


@dataclass(frozen=True)
class DataIngestionConfig:
    artifact_root: Path
    root_dir: Path
    unzip_dir: Path
    local_data_file: Path
    data_url: str 


class DataIngConfManager(ConfigManager):
    def __init__(self):
        cur_dir = Path(os.path.dirname(os.path.abspath(__file__)))
        super().__init__(cur_dir)

    def get_configuration(self) -> DataIngestionConfig:
        config = self.config
        create_directories([config.root_dir])

        data_ingestion_conf = DataIngestionConfig(
            artifact_root=Path(config.artifact_root),
            root_dir=Path(config.root_dir),
            unzip_dir=Path(config.unzip_dir),
            local_data_file=Path(config.local_data_file),
            data_url=config.data_url,
        )
        logging.info("Data ingestion configuration loaded")
        return data_ingestion_conf


class DataIngestion:
    def __init__(self):
        self.config = DataIngConfManager().get_configuration()

    def download_file(self):
        url = self.config.data_url
        file_name = self.config.local_data_file
        if not os.path.exists(self.config.local_data_file):
            file_name, header = request.urlretrieve(url=url, filename=file_name)
            logging.info(f"{file_name} downloaded with following info {header}")

        else:
            size_of_file = get_file_size(file_name)
            logging.info(f"file already exists in: {file_name} with size: {size_of_file}")

    def extract_zip_file(self):
        """Extact the zip file of the dataset into the data directory"""
        unzip_file_dir = self.config.unzip_dir
        zip_data_dir = self.config.local_data_file
        os.makedirs(unzip_file_dir, exist_ok=True)
        unzip_file(zip_data_dir, unzip_file_dir)
