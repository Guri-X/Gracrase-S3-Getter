import boto3
from dotenv import load_dotenv
import os

load_dotenv()

class GracraseS3:

    def get_buckets():
        AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
        AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

        # Get The List Of All Buckets In AWS Account
        s3 = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name="us-west-2"
        )

        gracrase_buckets = s3.list_buckets()

        for bucket in gracrase_buckets.objects.all():
            print("Bucket Name:", bucket.name)

if __name__ == "__main__":

    gs = GracraseS3
    gs.get_buckets()