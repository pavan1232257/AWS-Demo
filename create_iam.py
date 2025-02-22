
import boto3
from botocore.exceptions import ClientError

# Initialize a session using AWS credentials
iam_client = boto3.client('iam')

def create_iam_user(username):
    try:
        # Create a new IAM user
        response = iam_client.create_user(
            UserName=username
        )
        print(f"User {username} created successfully.")
        return response
    except ClientError as e:
        print(f"An error occurred: {e}")
        return None

# Call the function to create an IAM user
username = 'new_user'  # Change this to the desired username
create_iam_user(username)
