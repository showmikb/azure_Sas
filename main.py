from azure.storage.blob import BlobServiceClient, generate_blob_sas

from azure.cosmosdb.table.tableservice import TableService
from datetime import datetime, timedelta

########################################INPUT STARTS#######################################################

# Specify the storage account name, account key, and endpoint
storage_account_name = ""
storage_account_key = ""

# Specify the table name and FIleshare name
table_name = ""
file_share_name = ""
########################################INPUT ENDS#######################################################


storage_account_endpoint = "https://{0}.blob.core.windows.net/".format(storage_account_name)

# Create a BlobServiceClient object
blob_service_client = BlobServiceClient(account_url=storage_account_endpoint, credential=storage_account_key)


# Specify the file share name
blob_name = "None"
# Create a SAS token for the file share
file_share_sas_token = generate_blob_sas(account_name=storage_account_name,
                                         account_key=storage_account_key,
                                         container_name=file_share_name,
                                         permission="r",
                                         blob_name=blob_name,
                                         expiry=datetime.utcnow() + timedelta(minutes=60))


# Create a TableService object
table_service = TableService(account_name=storage_account_name, account_key=storage_account_key)

# Create a SAS token for the table
table_sas_token = table_service.generate_table_shared_access_signature(table_name,
                                                                        "r",
                                                                        datetime.utcnow() + timedelta(minutes=60))

# Print the SAS tokens
print("File share SAS token:", file_share_sas_token)
print("Table SAS token:", table_sas_token)

