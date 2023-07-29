from mlProject.utils import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline,STAGE_NAME



if __name__=='__main__':
    try:
        logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e