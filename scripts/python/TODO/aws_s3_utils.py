!/usr/bin/env python3

import botocore

def get_creds(account):
    # Get what's needed to authenticate against a given IAM account
    pass

def list_buckets(account):
    # For a given IAM account, which buckets can be seen?
    pass

def put_to_bucket(bucketID, file, remote_path):
    # Upload a file or folder to a bucket
    pass

def get_from_bucket(bucketID, file, local_path):
    # Download a file or folder from a bucket
    pass

def create_bucket(IAM, region, az, bucket_name):
    # Create a bucket or buckets
    pass

def delete_bucket(IAM, region, az, bucket_name):
    # Delete a bucket or buckets
    pass

def bucket_permissions_get(IAM, region, az, bucket_name):
    # Enumerate current permissions on a bucket
    pass

def bucket_permissions_set(IAM, region, az, bucket_name, new_perms_flags):
    # Set or update permissions on a bucket
    pass

