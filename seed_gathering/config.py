import yaml
import os
from typing import Optional
import boto3
from botocore import UNSIGNED
from botocore.config import Config

class ProcessingConfig:
    # Processing settings
    num_workers: int = os.cpu_count() or 1
    chunk_multiplier: int = 1000  # Controls CHUNK_SIZE per worker
    
    # Dataset settings
    dataset_name: str = "bigcode/the-stack-v2-dedup"
    dataset_subset: str = "Python"
    cache_dir: str = "../stack"
    streaming: bool = True
    
    # S3 settings
    s3_unsigned: bool = True
    
    @classmethod
    def from_yaml(cls, path: str) -> 'ProcessingConfig':
        """Load configuration from a YAML file."""
        with open(path, 'r') as f:
            config_dict = yaml.safe_load(f)
        return cls(**config_dict)

    def validate(self):
        """Validate configuration values."""
        if self.num_workers < 1:
            raise ValueError("num_workers must be at least 1")
        if self.chunk_multiplier < 1:
            raise ValueError("chunk_multiplier must be at least 1")
            
    def setup_s3_client(self):
        """Setup and return S3 client based on configuration."""
        if self.s3_unsigned:
            return boto3.client("s3", config=Config(signature_version=UNSIGNED))
        return boto3.client("s3")  # Default client if signed access is needed
        
    def get_chunk_size(self):
        """Calculate chunk size based on workers and multiplier."""
        return self.chunk_multiplier * self.num_workers