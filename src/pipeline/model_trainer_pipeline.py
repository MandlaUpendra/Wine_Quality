from src.config.configuration import ConfigurationManager
from src.entity.config_entity import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
from src import logger

STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train()
        