from collections import namedtuple
from xml.dom.minidom import NamedNodeMap

DataIngestionConfig = namedtuple('DataIngestionConfig', ['dataset_download_url', 'tgz_download_dir',
                                 'raw_data_dir', 'ingested_train_dir', 'ingested_test_dir'])


DataValidationConfig = namedtuple("DataValidationConfig", ['dchema_file_path'])

DataTransformationConfig = namedtuple('DataTransformationConfig', ['add_besdroom_per_room', 
                                                                  'transformed_train_dir',
                                                                  'transformed_test_dir',
                                                                  'preprocessed_object_file_path']) #the final saved pickle file
                                                                  
ModelTrainerConfig = namedtuple('ModelTrainerConfig', ['trained_model_file_path', "base_madel"])  


ModelEvaluationConfig = namedtuple('ModelEvaluationConfig', ["model_evaluation_file_path", 'time_stamp']) 

                                                              
ModelPusherConfig = namedtuple('ModelPusherConfig', ['export_dir_path'])   


TrainingPipelineConfig = namedtuple('TrainingPipelineConfig', ['artifact_dir'])   

                                             