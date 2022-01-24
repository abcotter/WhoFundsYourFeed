import os
from pathlib import Path
import boto3
import tarfile
import json
from typing import List

MODELS_DIRECTORY = "/tmp/models"
MODELS_BUCKET = os.environ['MODELS_BUCKET']

def get_model_path(model: str) -> str:
    """Get model path after ensuring model is downloaded"""

    file_name = os.path.join(Path(MODELS_DIRECTORY), model)
    if not os.path.exists(file_name):
        download_model(model, file_name)
    return f"{file_name}/en_core_web_sm/en_core_web_sm-3.0.0"

def download_model(model: str, file_name: str):
    """Download model from s3 into model directory"""

    if not os.path.exists(MODELS_DIRECTORY):
        os.makedirs(MODELS_DIRECTORY)

    model_object = f'{model}.tar.gz'
    s3 = boto3.client('s3')
    zip_file = f"/tmp/{model_object}"
    s3.download_file(MODELS_BUCKET, model_object, zip_file)
    unzip_file(zip_file)
    os.remove(zip_file)

def unzip_file(file_name: str):
    """Extract all files in tarball"""

    with tarfile.open(file_name) as f:
        f.extractall(path=MODELS_DIRECTORY)

def is_video_processed(video_id):
    """Check if Youtube video has already been processed"""
    payload = {
        "youtubeVideoId": video_id
    }

    client = boto3.client('lambda')
    response = client.invoke(
        FunctionName="arn:aws:lambda:us-east-1:560621042947:function:isProcessedVideoChecker",
        InvocationType="RequestResponse",
        Payload=json.dumps(payload))
    return json.load(response["Payload"])

def process_sponsors(result: dict, video_id: str) -> None:
    """Request video details and found sponsors to be processed"""
    client = boto3.client('lambda')
    result["youtubeVideoId"] = video_id
    client.invoke(
        FunctionName="arn:aws:lambda:us-east-1:560621042947:function:newVideoHandler",
        InvocationType="Event",
        Payload=json.dumps(result))
