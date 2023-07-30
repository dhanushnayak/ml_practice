from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject.utils import logger

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer  = ModelTrainer(model_trainer_config)
        model_trainer.train()



STAGE_NAME = "Model training"

if __name__=="__main__":
    try:
            logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
            obj = ModelTrainerPipeline()
            obj.main()
            logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<")
    except Exception as e:
            logger.exception(e)
            raise e
