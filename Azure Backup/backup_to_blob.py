from azure.storage.blob import BlobServiceClient
import os
from datetime import datetime

# Replace with your values
account_name = "studentbackupfiles"
account_key = ""
container_name = "backups"
local_folder = "C:/Users/komal/Documents/"  

# Connect to Blob Service
blob_service = BlobServiceClient(
    f"https://{account_name}.blob.core.windows.net",
    credential=account_key
)
container_client = blob_service.get_container_client(container_name)

# Upload all files in the folder
for filename in os.listdir(local_folder):
    file_path = os.path.join(local_folder, filename)
    if os.path.isfile(file_path):
        blob_name = f"{datetime.now().strftime('%Y-%m-%d')}/{filename}"  # Organize by date
        with open(file_path, "rb") as data:
            container_client.upload_blob(blob_name, data, overwrite=True)
        print(f"Uploaded {filename} to {blob_name}")
