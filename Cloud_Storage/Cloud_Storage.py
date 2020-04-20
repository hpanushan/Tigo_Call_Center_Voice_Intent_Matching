#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START storage_quickstart]
# Imports the Google Cloud client library
from google.cloud import storage
import pprint

class Cloud_Storage_Client:

    def __init__(self):
        # Instantiates a client
        self.storage_client = storage.Client()

    def create_new_bucket(self,bucket_name):
        # Creates the new bucket
        bucket = self.storage_client.create_bucket(bucket_name)

        print("Bucket {} created.".format(bucket.name))
        # [END storage_quickstart]

    def list_available_buckets(self):
        # Available buckets
        buckets = self.storage_client.list_buckets()

        for bucket in buckets:
            print(bucket.name)

    def delete_bucket(self,bucket_name):
        # Delete existing storage bucket
        bucket = self.storage_client.get_bucket(bucket_name)
        bucket.delete()

        print("Bucket {} deleted".format(bucket.name))

    def display_bucket_metadata(self,bucket_name):
        # Displaying bucket metadata
        bucket = self.storage_client.get_bucket(bucket_name)
        print("ID: {}".format(bucket.id))
        print("Name: {}".format(bucket.name))
        print("Storage Class: {}".format(bucket.storage_class))
        print("Location: {}".format(bucket.location))
        print("Location Type: {}".format(bucket.location_type))
        print("Cors: {}".format(bucket.cors))
        print(
            "Default Event Based Hold: {}".format(bucket.default_event_based_hold)
        )
        print("Default KMS Key Name: {}".format(bucket.default_kms_key_name))
        print("Metageneration: {}".format(bucket.metageneration))
        print(
            "Retention Effective Time: {}".format(
                bucket.retention_policy_effective_time
            )
        )
        print("Retention Period: {}".format(bucket.retention_period))
        print("Retention Policy Locked: {}".format(bucket.retention_policy_locked))
        print("Requester Pays: {}".format(bucket.requester_pays))
        print("Self Link: {}".format(bucket.self_link))
        print("Time Created: {}".format(bucket.time_created))
        print("Versioning Enabled: {}".format(bucket.versioning_enabled))
        print("Labels:")
        pprint.pprint(bucket.labels)

    def list_objects_in_bucket(self,bucket_name):
        # Note: Client.list_blobs requires at least package version 1.17.0.
        blobs = self.storage_client.list_blobs(bucket_name)

        for blob in blobs:
            print(blob.name)

    def add_label_to_bucket(self,bucket_name):
        bucket = self.storage_client.get_bucket(bucket_name)
        labels = bucket.labels
        labels["example"] = "label"
        bucket.labels = labels
        bucket.patch()

        print("Updated labels on {}.".format(bucket.name))
        pprint.pprint(bucket.labels)

    def view_bucket_labels(self,bucket_name):
        bucket = self.storage_client.get_bucket(bucket_name)

        labels = bucket.labels
        pprint.pprint(labels)

    def remove_bucket_label(self,bucket_name,label_name):
        bucket = self.storage_client.get_bucket(bucket_name)

        labels = bucket.labels

        if label_name in labels:
            del labels[label_name]

        bucket.labels = labels
        bucket.patch()

        print("Removed labels on {}.".format(bucket.name))

        # Get the list of remaining labels for bucket
        pprint.pprint(bucket.labels)

    def uploading_objects(self,bucket_name,source_file_name,destination_blob_name):
        # Adding objects to storage bucket
        # bucket_name = "your-bucket-name"
        # source_file_name = "local/path/to/file"
        # destination_blob_name = "storage-object-name"

        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print(
            "File {} uploaded to {}.".format(
                source_file_name, destination_blob_name
            )
        )

    def make_objects_public(self,bucket_name,blob_name):
        # Makes a blob publicly accessible.
        # bucket_name = "your-bucket-name"
        # blob_name = "your-object-name"

        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        blob.make_public()

        print(
            "Blob {} is publicly accessible at {}".format(
                blob.name, blob.public_url
            )
        )

if __name__ == "__main__":
    name = "anushan31"
    source_file_name = "Data/Dual_Channel/Service_Failure/Recording (29)-2.wav"
    storageObj = Cloud_Storage_Client()
    storageObj.make_objects_public(name,'Recording29')
