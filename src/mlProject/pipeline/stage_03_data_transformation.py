from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject.utils import logger


class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            with open("artifacts/data_validation/status.txt","r") as f:
                status = f.read().split(" ")[-1]
            if status == 'True' or str(status).lower() == 'true':
                config = ConfigurationManager()
                data_trans_config =  config.get_data_transformation_config()
                data_trans =  DataTransformation(config=data_trans_config)
                data_trans.train_test_spliting()
            else:
                raise Exception("Your Data Schema is not valid")
        except Exception as e:
            raise e

STAGE_NAME = "Data Transformation Stage"

if __name__=='__main__':
    try:
        logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
