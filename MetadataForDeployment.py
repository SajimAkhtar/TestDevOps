import snowflake.connector

# Snowflake connection parameters
snowflake_user = 'SajimAkhtar'
snowflake_password = 'Kasmo@123'
snowflake_account = 'wh49805.central-india.azure'
snowflake_database = 'MYINTERNALTABLEDB'
snowflake_schema = 'INFORMATION_SCHEMA'
snowflake_warehouse='COMPUTE_WH'

# Establishing connection to Snowflake
conn = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account,
    database=snowflake_database,
    schema=snowflake_schema
    # warehouse=snowflake_warehouse
)

# Execute a SQL query to retrieve deployment statistics

# query = "CREATE OR REPLACE DATABASE SAJIM"
query = "select * from MYINTERNALTABLEDB.information_schema.TABLES"


cursor = conn.cursor()
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Close the cursor
cursor.close()


# # Storing deployment statistics in a metadata object
# metadata_object = {
#     "deployment_stats": results
# }
#
# # You can serialize the metadata_object and store it as needed, for example in a JSON file
# import json
#
# with open('deployment_stats_metadata.json', 'w') as json_file:
#     json.dump(metadata_object, json_file)
#
# # Close the Snowflake connection
# conn.close()
#
print("Deployment statistics captured and stored in metadata object.")
