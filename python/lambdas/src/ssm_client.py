import boto3

client = boto3.client('ssm')


def get_secret(param_name: str) -> str:
    response = client.get_parameter(
        Name=param_name,
        WithDecryption=True
    )
    return response['Parameter']['Value']
