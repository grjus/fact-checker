import json
import boto3

from python.lambdas.src.schemas import FactCheckSecret

client = boto3.client("secretsmanager")


def get_secret(secret_name: str) -> FactCheckSecret:
    response = client.get_secret_value(SecretId=secret_name)
    secret_dict = json.loads(response["SecretString"])
    return FactCheckSecret(**secret_dict)
