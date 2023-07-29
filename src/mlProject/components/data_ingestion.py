import os
import urllib.request as request
import zipfile
from pathlib import Path
from mlProject.utils import logger
from mlProject.utils.comman import get_size
from mlProject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def dowload_file(self):
        if not os.path.exists(self.config.local_dir):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename=self.config.local_dir
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_dir))}")

    def extract_file(self):

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_dir,'r') as zip_ref: zip_ref.extractall(unzip_path)
