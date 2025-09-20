import os

from pathlib import Path
from config import ConfigManager, ParamManager

from dataclasses import dataclass
from ensure import ensure_annotations

from reytools.logger import logging
from reytools.file_system import create_directories

import tensorflow as tf


@dataclass(frozen=True)
class ModelDefinitionConfig:
    root_dir: Path
    base_model_path: Path
    modified_model_path: Path


@dataclass(frozen=True)
class ModelDefinitionParams:
    image_size: list
    include_top: bool
    classes: int
    weights: str
    learning_rate: float


class ModelDefinitionConfManager(ConfigManager):
    def __init__(self):
        cur_dir = Path(os.path.dirname(os.path.abspath(__file__)))
        super().__init__(cur_dir)

    def get_configuration(self) -> ModelDefinitionConfig:
        config = self.config
        create_directories([config.root_dir])

        box_config = ModelDefinitionConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            modified_model_path=Path(config.modified_model_path),
        )
        logging.info("Model definition configuration loaded")
        return box_config


class ModelDefinitionParamManager(ParamManager):
    def __init__(self):
        cur_dir = Path(os.path.dirname(os.path.abspath(__file__)))
        super().__init__(cur_dir)

    def get_params(self) -> ModelDefinitionParams:
        parmas = self.params
        model_def_params = ModelDefinitionParams(
            image_size=parmas.IMAGE_SIZE,
            include_top=parmas.INCLUDE_TOP,
            classes=parmas.CLASSES,
            weights=parmas.WEIGHTS,
            learning_rate=parmas.LEARNING_RATE,
        )
        logging.info("Model definition params loaded")
        return model_def_params


class ModelDefinition:
    def __init__(self):
        self.config = ModelDefinitionConfManager().get_configuration()
        self.params = ModelDefinitionParamManager().get_params()

    def load_base_model(self):
        self.base_model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.params.image_size,
            weights=self.params.weights,
            include_top=self.params.include_top,
        )
        logging.info("Base Model Model loaded")

    def _prepare_full_model(self):
        self.base_model.trainable = False
    
        flatten_in = tf.keras.layers.Flatten()(self.base_model.output)
        prediction = tf.keras.layers.Dense(units=self.params.classes, activation="softmax")(flatten_in)

        self.full_model = tf.keras.models.Model(inputs=self.base_model.input, outputs=prediction)

        self.full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=self.params.learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"],
        )
        self.full_model.summary()
        logging.info(f"Base model modified")

    def update_base_model(self):
        self._prepare_full_model()

    def save_base_model(self):
        self.base_model.save(self.config.base_model_path)
        logging.info(f"Base model saved to {self.config.base_model_path}")

    def save_modified_model(self):
        self.full_model.save(self.config.modified_model_path)
        logging.info(f"Modified model saved to {self.config.modified_model_path}")
