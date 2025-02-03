import os
import sys
import logging
import pandas as pd
import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

# Fetch database connection parameters
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Configure logging to use the specified log file
log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'data_cleaner.log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class DatabaseManager:
    """
    A class to handle database operations including loading data and saving DataFrame to a database table.
    """
    
    def __init__(self):
        # Use the globally configured logger
        self.logger = logging.getLogger(__name__)
        
        # Check database connection on initialization
        self._check_database_connection()

    def _check_database_connection(self):
        """
        Check the database connection and log the status.
        """
        connection = self._get_connection()
        if connection:
            self.logger.info("Database connection check successful.")
            connection.close()
        else:
            self.logger.error("Database connection check failed.")

    def _get_connection(self):
        """
        Create and return a database connection using psycopg2.
        Also, verify the connection by fetching the database version.
        """
        try:
            connection = psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            self.logger.info("Successfully connected to the database.")

            # Verify the connection by fetching the database version
            cursor = connection.cursor()
            cursor.execute("SELECT version();")
            db_version = cursor.fetchone()
            self.logger.info(f"Database version: {db_version[0]}")
            cursor.close()

            return connection
        except Exception as e:
            self.logger.error(f"Error connecting to the database: {e}")
            return None

    def _get_sqlalchemy_engine(self):
        """
        Create and return a SQLAlchemy engine.
        """
        try:
            connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
            engine = create_engine(connection_string)
            self.logger.info("Successfully created SQLAlchemy engine.")
            return engine
        except Exception as e:
            self.logger.error(f"Error creating SQLAlchemy engine: {e}")
            return None
    def save_dataframe_to_db(self, df, table_name, if_exists='replace'):
        """
        Save a DataFrame to a PostgreSQL table in a schema with the same name 
        as the table, using SQLAlchemy.
        """
        engine = self._get_sqlalchemy_engine()
        if engine is None:
            return

        schema_name = table_name  # Schema name is the same as the table name

        try:
            # Create the schema if it doesn't exist (important!)
            with engine.connect() as conn: # Use the existing engine to connect
                conn.execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name};")
                conn.commit()

            df.to_sql(table_name, engine, schema=schema_name, if_exists=if_exists, index=False)
            self.logger.info(f"Successfully saved DataFrame to table {table_name} in schema {schema_name}.")
        except Exception as e:
            self.logger.error(f"Error saving DataFrame to database: {e}")



# Usage Example:
'''
if __name__ == "__main__":
    # Create a DatabaseManager object (this will check the database connection)
    db_manager = DatabaseManager()

    # Example DataFrame to save
    sample_data = {
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35]
    }
    df_to_save = pd.DataFrame(sample_data)

    # Save the DataFrame to the database as a table
    db_manager.save_dataframe_to_db(df_to_save, "people")
    '''