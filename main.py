import subprocess
import os
import time

S3_BUCKET = os.environ["S3_BUCKET"]

timestamp = time.strftime("%Y-%m-%d-%I:%M")


def handler(event, context):

    print("Function started")

    DB_HOST = event["DB_HOST"]
    DB_NAME = event["DB_NAME"]
    DB_USER = event["DB_USER"]
    DB_PASS = event["DB_PASS"]

    print("%s %s ".format(DB_HOST, DB_NAME))
    command = f"pg_dump -h {DB_HOST} --column-inserts | gzip -c | aws s3 cp - s3://{S3_BUCKET}/{DB_NAME}_{timestamp}.gz"
    print(command)
    subprocess.Popen(command, shell=True).wait()

    print("Postgres backup finished")
    return "backup finished"
