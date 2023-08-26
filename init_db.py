import os
import dotenv
import sqlite3
import uuid

print('''WARNING: This script will delete the previous database and create a new one.
 If you want to delete the database and initiate it, type DELETE.''')
answer = input('Type DELETE to continue: ')

if answer == 'DELETE':

    # Read variables DATABASE_PATH and DATABASE_FILE_NAME from `env.prod` file

    dotenv.load_dotenv(dotenv_path='.env.prod')

    DATABASE_PATH = os.environ['DATABASE_PATH'] + '/'
    DATABASE_FILE_NAME = os.environ['DATABASE_FILE_NAME']

    # Check if database file exist and if so
    # backup the database file with a new unique name based on uuid
    if os.path.exists(DATABASE_PATH + DATABASE_FILE_NAME):
        new_name = str(uuid.uuid4()) + '.db'
        os.rename(DATABASE_PATH + DATABASE_FILE_NAME, DATABASE_PATH + new_name)
        print('Database file backed up to ' + new_name)

    # Initiating the database connection
    conn = sqlite3.connect(DATABASE_PATH + DATABASE_FILE_NAME)
    c = conn.cursor()

    # As an example, create the users table with the following columns:
    # - user_id: the user's id, coming form firebase
    # - user_email: the user's email


    c.execute('''CREATE TABLE users
                    (user_id text, user_email text)''')

    print('Users table initiated')

else:
    print('Database not initiated')
