import boto3


s3 = boto3.resource('s3')

source_bucket_name = 'source-bucket-name'
destination_bucket_name = 'destination-bucket-name'

source_bucket = s3.Bucket(source_bucket_name)
destination_bucket = s3.Bucket(destination_bucket_name)


for obj in source_bucket.objects.all():
    source_key = obj.key
    destination_key = source_key 
    destination_bucket.Object(destination_key).copy_from(CopySource={'Bucket': source_bucket_name, 'Key': source_key})

    print(f"Copied {source_key} to {destination_key}")


