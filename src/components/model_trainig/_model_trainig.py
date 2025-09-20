import os

from pathlib import Path
from config import ConfigManager, ParamManager

from dataclasses import dataclass
from ensure import ensure_annotations

from reytools.logger import logging

import tensorflow as tf

@dataclass(frozen=True)
class ModelTrainingConfig:
    modified_model_path: Path
    trained_model_path: Path


@dataclass(frozen=True)
class ModelTrainigParams:
    epochs: int
    batch_size: int
    augmentation: bool


class ModelTrainigConfManager(ConfigManager):
    def __init__(self):
        cur_dir = Path(os.path.dirname(os.path.abspath(__file__)))
        super().__init__(cur_dir)

    def get_configuration(self) -> ModelTrainingConfig:
        config = self.config
        box_config = ModelTrainingConfig(
            modified_model_path=config.modified_model_path, trained_model_path=config.trained_model_path
        )

        logging.info("Model Training configuration loaded")
        return box_config


class ModelTrainigParamManager(ParamManager):
    def __init__(self):
        cur_dir = Path(os.path.dirname(os.path.abspath(__file__)))
        super().__init__(cur_dir)

    def get_params(self) -> ModelTrainigParams:
        parmas = self.params
        model_def_params = ModelTrainigParams(
            epochs=parmas.EPOCHS,
            batch_size=parmas.BATCH_SIZE,
            augmentation=parmas.AUGMENTATION,
        )

        logging.info("Model Training params loaded")
        return model_def_params


class ModelTraining:
    def __init__(self):
        self.config = ModelTrainigConfManager().get_configuration()
        self.params = ModelTrainigParamManager().get_params()

    def train_model(self):
        model = tf.keras.load(self.config.)
    
model_trainign = ModelTraining()
