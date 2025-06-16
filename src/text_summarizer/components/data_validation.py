import os
from text_summarizer.logging import logger
from text_summarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = True
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion"))
            logger.info(f"Files found in directory: {all_files}")

            for file in self.config.ALL_REQUIRED_FILES:
                if file not in all_files:
                    validation_status = False
                    logger.error(f"Missing required file: {file}")
                else:
                    logger.info(f"Found required file: {file}")

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")
            
            logger.info(f"Validation status: {validation_status}")
            return validation_status
        except Exception as e:
            logger.error(f"Error during validation: {str(e)}")
            raise e 