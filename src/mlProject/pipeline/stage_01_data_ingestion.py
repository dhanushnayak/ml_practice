from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject.utils import logger


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        dataingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(dataingestion_config)
        data_ingestion.dowload_file()
        data_ingestion.extract_file()

if __name__=='__main__':
    try:
        logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e