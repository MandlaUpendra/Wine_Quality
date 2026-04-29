from src import logger
from src.components.data_ingestion import DataIngestion
from src.config.configuration import ConfigurationManager
from src.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nxx")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nxxx")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation_result = data_transformation.initiate_data_transformation()
    print(data_transformation_result)
    logger.info(f">>>>>> stage {STAGE_NAME} completed   <<<<<<<\n\nxxx")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<\n\nxxx")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.initiate_model_trainer()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n\nxxx")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "model Evaluation Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelEvaluationTrainingPipeline()
    model_trainer.initiate_model_evaluation()
    logger.info(f">>>>>> stage{STAGE_NAME} completed <<<<<<\n\nxxx")
except Exception as e:
    logger.exception(e)
    raise e