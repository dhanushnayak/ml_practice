from mlProject.utils import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline




STAGE_NAME = 'Data Ingestion'

try:
        logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<")
except Exception as e:
        logger.exception(e)
        raise e
    



    
STAGE_NAME = 'Data Validation'

try:
        logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<")
except Exception as e:
        logger.exception(e)
        raise e