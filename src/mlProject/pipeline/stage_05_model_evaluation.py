import os
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject.utils import logger

os.environ['MLFLOW_TRACKING_URI'] = "https://dagshub.com/dhanushnayak/ml_practice.mlflow"
os.environ['MLFLOW_TRACKING_USERNAME'] = "dhanushnayak"
os.environ['MLFLOW_TRACKING_PASSWORD'] = "253df65190e7dc9ee74592f4802bc08e1df73a7e"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.log_into_mlfow()



STAGE_NAME = "Model evaluation"

if __name__=="__main__":
    try:
            logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
            obj = ModelEvaluationPipeline()
            obj.main()
            logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<")
    except Exception as e:
            logger.exception(e)
            raise e