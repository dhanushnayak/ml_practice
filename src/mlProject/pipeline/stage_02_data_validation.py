from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
from mlProject.utils import logger


class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_valid_config =  config.get_validation_config()
        data_valid =  DataValidation(config=data_valid_config)
        data_valid.valid_all_columns()

STAGE_NAME = "Data Validation Stage"

if __name__=='__main__':
    try:
        logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
