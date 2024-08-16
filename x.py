# Import Python packages
import snowflake.connector
import os, re
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.files.file import File
import sys


# Create functions for SharePoint upload
class SharePoint:
    def _auth(self):
        conn = ClientContext(SHAREPOINT_SITE).with_credentials(
            UserCredential(
                USERNAME,
                PASSWORD
            )
        )
        return conn

    def upload_file(self, file_name, folder_name, content):
        conn = self._auth()
        target_folder_url = f'/sites/{SHAREPOINT_SITE_NAME}/{SHAREPOINT_DOC}/{folder_name}'
        target_folder = conn.web.get_folder_by_server_relative_path(target_folder_url)
        response = target_folder.upload_file(file_name, content).execute_query()
        return response

# Function to read text from sharepoint file
def get_sharepoint_file_content(ctx, file_url):
    # Load the text file
    file = ctx.web.get_file_by_server_relative_url(file_url)
    ctx.load(file)

    flag = 0
    try:
        ctx.execute_query()
        flag = 1
    except:
        flag = 0

    if flag == 1:
        # Download the file
        download_path = os.path.join(os.getcwd(), "temp_file.sql")

        with open(download_path, 'wb') as fh:
            file = (ctx.web.get_file_by_server_relative_url(file_url)
                    .download(fh)
                    .execute_query()
                    )

        # Read the file content
        with open(download_path, "rb") as f:
            file_content = f.read()
            return file_content

        os.remove(download_path)
    else:
        return ""

#Log file setup
old_stdout = sys.stdout
log_file = open("DDL_SCRIPT_LOG.log","w")
sys.stdout = log_file


# Snowflake connection parameters
snowflake_account = 'lz64309.east-us-2.azure'
snowflake_user = 'jsolanr3@jci.com'
snowflake_password = ''
snowflake_database = 'GLOBAL_PRODUCTS_ANALYTICS_PROD'
snowflake_warehouse = 'EDP_PROD_GLOBAL_COMMERCIAL_ANALYTICS_MEDIUM_WH'
snowflake_role = 'SF_EDP_GLOBAL_PRODUCTS_OPERATIONS_ANALYST_PROD'

# SharePoint Connection Parameters
USERNAME = "A1001564@jci.com"
PASSWORD = "X3tSACf%4m>]-6=wApSd}4kHiZfs%37"
SHAREPOINT_SITE = "https://apps.jci.com/sites/datamanagement"
SHAREPOINT_SITE_NAME = "datamanagement"
SHAREPOINT_DOC = "Snowflake"

# Connection configuration for ADSSO
authenticator = 'externalbrowser'

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=snowflake_user,
    account=snowflake_account,
    role=snowflake_role,
    warehouse=snowflake_warehouse,
    database=snowflake_database,
    authenticator=authenticator
)

# Authenticate with SharePoint
ctx_auth = AuthenticationContext(SHAREPOINT_SITE)
if ctx_auth.acquire_token_for_user(USERNAME, PASSWORD):
    ctx = ClientContext(SHAREPOINT_SITE, ctx_auth)

# Create a cursor
cur = conn.cursor()

# Get the list of schemas
cur.execute(f"SHOW SCHEMAS")
schemas = cur.fetchall()


# Create a directory to store SQL files
output_directory = "C://Temp"
os.makedirs(output_directory, exist_ok=True)

# read files and return the content of files
def get_file_content(file_path):
    with open(file_path, 'rb') as f:
        return f.read()

for schema in schemas:
    snowflake_schema = schema[1]
    print("Checking schema: " + snowflake_schema)

    # Get the list of views
    cur.execute(f"SHOW VIEWS IN SCHEMA {snowflake_schema}")
    views = cur.fetchall()

    # Get the list of tables
    cur.execute(f"SHOW TABLES IN SCHEMA {snowflake_schema}")
    tables = cur.fetchall()

    # Get the list of dynamic tables
    cur.execute(f"SHOW DYNAMIC TABLES IN SCHEMA {snowflake_schema}")
    dtables = cur.fetchall()

    # Get the list of functions
    cur.execute(f"SHOW USER FUNCTIONS IN SCHEMA {snowflake_schema}")
    ufuncs = cur.fetchall()

    # Get the list of procs
    cur.execute(f"SHOW USER PROCEDURES IN SCHEMA {snowflake_schema}")
    uprocs = cur.fetchall()

    # Get the list of tasks
    cur.execute(f"SHOW TASKS IN SCHEMA {snowflake_schema}")
    tasks = cur.fetchall()

    if snowflake_schema != 'INFORMATION_SCHEMA' and snowflake_schema != 'GLOBAL_PRODUCTS_PLAYGROUND':
        # Iterate over views and get DDL
        for view in views:
            view_name = view[1]
            #print(f"Creating DDL for VIEW {snowflake_schema}.{view_name}")
            cur.execute(f"SELECT GET_DDL('VIEW', '{snowflake_schema}.{view_name}')")
            ddl = cur.fetchone()[0]

            # Create a directory to store SQL files
            if snowflake_schema=="GLOBAL_PRODUCTS_FINAL" or snowflake_schema=="GLOBAL_PRODUCTS_STAGE" or snowflake_schema=="MKT" :
                SHAREPOINT_FOLDER_NAME = f"{snowflake_schema}//DT-VIEWS"
                output_directory = f"C://Temp//Snowflake_temp//{snowflake_schema}//DT-VIEWS"
                sharepoint_file_url = "/Snowflake/" + SHAREPOINT_FOLDER_NAME + "//" + f"{view_name}.sql"
            else:
                if view_name.endswith('_S_V'):
                    SHAREPOINT_FOLDER_NAME = f"{snowflake_schema}//Ingestions"
                    output_directory = f"C://Temp//Snowflake_temp//{snowflake_schema}//Ingestions"
                    sharepoint_file_url = "/Snowflake/" + SHAREPOINT_FOLDER_NAME + "//" + f"{view_name}.sql"
                else:
                    SHAREPOINT_FOLDER_NAME = f"{snowflake_schema}//Final"
                    output_directory = f"C://Temp//Snowflake_temp//{snowflake_schema}//Final"
                    sharepoint_file_url = "/Snowflake/" + SHAREPOINT_FOLDER_NAME + "//" + f"{view_name}.sql"

            os.makedirs(output_directory, exist_ok=True)


            if ddl:
                # Add database name and schema name
                ddl = ddl.replace("create or replace view ", f"CREATE OR REPLACE VIEW {snowflake_database}.{snowflake_schema}.")

                # Create temp SQL file for each view
                file_path = os.path.join(output_directory, f"{view_name}.sql")

                with open(file_path, 'w', encoding="utf-8") as sql_file:
                    sql_file.write(ddl)

                file_content = get_file_content(file_path)
                sharepoint_file_content = get_sharepoint_file_content(ctx, sharepoint_file_url)

                if file_content != sharepoint_file_content:
                    # Create SQL file for each view
                    SharePoint().upload_file(f"{view_name}.sql", SHAREPOINT_FOLDER_NAME, file_content)
                    print("Updated " + sharepoint_file_url)

        # Iterate over dynamic tables and get DDL
        for dtable in dtables:
            dtable_name = dtable[1]
            #print(f"Creating DDL for Dynamic table {snowflake_schema}.{dtable_name}")
            cur.execute(f"SELECT GET_DDL('DYNAMIC_TABLE', '{snowflake_schema}.{dtable_name}')")
            ddl = cur.fetchone()[0]

            # Create a directory to store SQL files
            if snowflake_schema == "GLOBAL_PRODUCTS_FINAL" or snowflake_schema == "GLOBAL_PRODUCTS_STAGE" or snowflake_schema=="MKT":
                SHAREPOINT_FOLDER_NAME = f"{snowflake_schema}//DT-VIEWS"
                output_directory = f"C://Temp//Snowflake_temp//{snowflake_schema}//DT-VIEWS"
                sharepoint_file_url = "/Snowflake/" + SHAREPOINT_FOLDER_NAME + "//" + f"{dtable_name}.sql"
            else:
                if dtable_name.endswith('_F'):
                    SHAREPOINT_FOLDER_NAME = f"{snowflake_schema}//Final"
                    output_directory = f"C://Temp//Snowflake_temp//{snowflake_schema}//Final"
                    sharepoint_file_url = "/Snowflake/" + SHAREPOINT_FOLDER_NAME + "//" + f"{dtable_name}.sql"
                else:
                    SHAREPOINT_FOLDER_NAME = f"{snowflake_schema}//Ingestions"
                    output_directory = f"C://Temp//Snowflake_temp//{snowflake_schema}//Ingestions"
                    sharepoint_file_url = "/Snowflake/" + SHAREPOINT_FOLDER_NAME + "//" + f"{dtable_name}.sql"

            os.makedirs(output_directory, exist_ok=True)

            if ddl:
                # Add database name and schema name
                ddl = ddl.replace("create or replace dynamic table ",
                                  f"CREATE OR REPLACE DYNAMIC TABLE {snowflake_database}.{snowflake_schema}.")

                # Create temp SQL file for each view
                file_path = os.path.join(output_directory, f"{dtable_name}.sql")

                with open(file_path, 'w', encoding="utf-8") as sql_file:
                    sql_file.write(ddl)

                file_content = get_file_content(file_path)
                sharepoint_file_content = get_sharepoint_file_content(ctx, sharepoint_file_url)

                if file_content != sharepoint_file_content:
                    # Create SQL file for each dynamic table
                    SharePoint().upload_file(f"{dtable_name}.sql", SHAREPOINT_FOLDER_NAME, file_content)
                    print("Updated " + sharepoint_file_url)

        # Iterate over tables and get DDL
        for table in tables:
            table_name = table[1]
            #print(f"Creating DDL for table {snowflake_schema}.{table_name}")
            cur.execute(f"SELECT GET_DDL('TABLE', '{snowflake_schema}.{table_name}')")
            ddl = cur.fetchone()[0]

            # Create a directory to store SQL files
            SHAREPOINT_FOLDER_NAME = f"{snowflake_schema}//DDL"
            sharepoint_file_url = "/Snowflake/" + SHAREPOINT_FOLDER_NAME + "//" + f"{table_name}.sql"

            output_directory = f"C://Temp//Snowflake_temp//{snowflake_schema}//DDL"
            os.makedirs(output_directory, exist_ok=True)

            if ddl:

                # Add database name and schema name
                ddl = ddl.replace("create or replace TABLE ",
                                  f"CREATE OR REPLACE TABLE {snowflake_database}.{snowflake_schema}.")

                # Create temp SQL file for each view
                file_path = os.path.join(output_directory, f"{table_name}.sql")

                with open(file_path, 'w', encoding="utf-8") as sql_file:
                    sql_file.write(ddl)

                file_content = get_file_content(file_path)
                sharepoint_file_content = get_sharepoint_file_content(ctx, sharepoint_file_url)

                if file_content != sharepoint_file_content:
                    # Create SQL file for each table
                    SharePoint().upload_file(f"{table_name}.sql", SHAREPOINT_FOLDER_NAME, file_content)
                    print("Updated " + sharepoint_file_url)

        # Iterate over functions and get DDL
        for ufunc in ufuncs:
            func_name = ufunc[1]
            func_name_full = (re.findall(r'.*(?= RETURN)', ufunc[8]))[0]
            #print(f"Creating DDL for function {snowflake_schema}.{func_name}")
            cur.execute(f"SELECT GET_DDL('FUNCTION', '{snowflake_schema}.{func_name_full}')")
            ddl = cur.fetchone()[0]

            # Create a directory to store SQL files
            SHAREPOINT_FOLDER_NAME = f"{snowflake_schema}//Functions"

            output_directory = f"C://Temp//Snowflake_temp//{snowflake_schema}//Functions"
            os.makedirs(output_directory, exist_ok=True)

            if ddl:

                # Add database name and schema name
                ddl = ddl.replace("CREATE OR REPLACE FUNCTION ",
                                  f"CREATE OR REPLACE FUNCTION {snowflake_database}.{snowflake_schema}.")

                ddl = ddl.replace('"' + func_name + '"', func_name)

                # Create temp SQL file for each view
                file_path = os.path.join(output_directory, f"{func_name}.sql")

                sharepoint_file_url = "/Snowflake/" + SHAREPOINT_FOLDER_NAME + "//" + f"{func_name}.sql"

                with open(file_path, 'w', encoding="utf-8") as sql_file:
                    sql_file.write(ddl)

                file_content = get_file_content(file_path)
                sharepoint_file_content = get_sharepoint_file_content(ctx, sharepoint_file_url)

                if file_content != sharepoint_file_content:
                    # Create SQL file for each table
                    SharePoint().upload_file(f"{func_name}.sql", SHAREPOINT_FOLDER_NAME, file_content)
                    print("Updated " + sharepoint_file_url)

        # Iterate over procedures and get DDL
        for uproc in uprocs:
            proc_name = uproc[1]
            proc_name_full = (re.findall(r'.*(?= RETURN)', uproc[8]))[0]
            #print(f"Creating DDL for function {snowflake_schema}.{proc_name}")
            cur.execute(f"SELECT GET_DDL('PROCEDURE', '{snowflake_schema}.{proc_name_full}')")
            ddl = cur.fetchone()[0]

            # Create a directory to store SQL files
            SHAREPOINT_FOLDER_NAME = f"{snowflake_schema}//Procedures"

            output_directory = f"C://Temp//Snowflake_temp//{snowflake_schema}//Procedures"
            os.makedirs(output_directory, exist_ok=True)

            if ddl:

                # Add database name and schema name
                ddl = ddl.replace("CREATE OR REPLACE PROCEDURE ",
                                  f"CREATE OR REPLACE PROCEDURE {snowflake_database}.{snowflake_schema}.")

                ddl = ddl.replace('"' + proc_name + '"', proc_name)

                # Create temp SQL file for each view
                file_path = os.path.join(output_directory, f"{proc_name}.sql")

                sharepoint_file_url = "/Snowflake/" + SHAREPOINT_FOLDER_NAME + "//" + f"{proc_name}.sql"

                with open(file_path, 'w', encoding="utf-8") as sql_file:
                    sql_file.write(ddl)

                file_content = get_file_content(file_path)
                sharepoint_file_content = get_sharepoint_file_content(ctx, sharepoint_file_url)

                if file_content != sharepoint_file_content:
                    # Create SQL file for each table
                    SharePoint().upload_file(f"{proc_name}.sql", SHAREPOINT_FOLDER_NAME, file_content)
                    print("Updated " + sharepoint_file_url)

        # Iterate over tasks and get DDL
        for task in tasks:
            task_name = task[1]
            # task_name_full = (re.findall(r'.*(?= RETURN)', task[8]))[0]
            #print(f"Creating DDL for function {snowflake_schema}.{task_name}")
            cur.execute(f"SELECT GET_DDL('TASK', '{snowflake_schema}.{task_name}')")
            ddl = cur.fetchone()[0]

            # Create a directory to store SQL files
            SHAREPOINT_FOLDER_NAME = f"{snowflake_schema}//Tasks"

            output_directory = f"C://Temp//Snowflake_temp//{snowflake_schema}//Tasks"
            os.makedirs(output_directory, exist_ok=True)

            if ddl:

                # Add database name and schema name
                ddl = ddl.replace("create or replace task ",
                                  f"create or replace task {snowflake_database}.{snowflake_schema}.")

                ddl = ddl.replace('"' + task_name + '"', task_name)

                # Create temp SQL file for each view
                file_path = os.path.join(output_directory, f"{task_name}.sql")

                sharepoint_file_url = "/Snowflake/" + SHAREPOINT_FOLDER_NAME + "//" + f"{task_name}.sql"

                with open(file_path, 'w', encoding="utf-8") as sql_file:
                    sql_file.write(ddl)

                file_content = get_file_content(file_path)
                sharepoint_file_content = get_sharepoint_file_content(ctx, sharepoint_file_url)

                if file_content != sharepoint_file_content:
                    # Create SQL file for each table
                    SharePoint().upload_file(f"{task_name}.sql", SHAREPOINT_FOLDER_NAME, file_content)
                    print("Updated " + sharepoint_file_url)
    print("Checked schema: " + snowflake_schema)

# Close the cursor and connection
cur.close()
conn.close()

print("Done")

# Log file close
sys.stdout = old_stdout
log_file.close()