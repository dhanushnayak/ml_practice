from mlProject.utils import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

#########################################################################################################################

STAGE_NAME = 'Data Ingestion'

try:
        logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<\n\nX===========X")
except Exception as e:
        logger.exception(e)
        raise e
    
#########################################################################################################################
  
STAGE_NAME = 'Data Validation'

try:
        logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<\n\nX===========X")
except Exception as e:
        logger.exception(e)
        raise e

#########################################################################################################################

STAGE_NAME = "Data Transformation"

try:
        logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<\n\nX===========X")
except Exception as e:
        logger.exception(e)
        raise e

#########################################################################################################################

STAGE_NAME = "Model Training "

try:
        logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<\n\nX===========X")
except Exception as e:
        logger.exception(e)
        raise e

#########################################################################################################################

STAGE_NAME = "Model Evaluation"

try:
        logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<\n\nX===========X")
except Exception as e:
        logger.exception(e)
        raise e

#########################################################################################################################


