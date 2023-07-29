import pandas as pd
from mlProject.entity.config_entity import DataValidationConfig
from mlProject.utils import logger

class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config  = config

    def valid_all_columns(self):
        try:
            validation_status=None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_col =  list(data.columns)

            all_schema = self.config.all_schema.keys()
            
            for col in all_col:
                if col not in all_schema:
                    validation_status = False
                else:
                        validation_status =  True

            with open(self.config.STATUS_FILE,"w") as f:
                        f.write(f"Validation status: {validation_status}")

            logger.info(f'>>>>>>> Validation status of the data: {validation_status} <<<<<<<<<')
            return validation_status
                        
        except Exception as e:
            raise e
        
        