import psycopg2

PGHOST='ep-sweet-silence-a2omrlfx-pooler.eu-central-1.aws.neon.tech'
PGDATABASE='neondb'
PGUSER='neondb_owner'
PGPASSWORD='npg_Kg2fSQR9IFPp'
PORT = 5432

with psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT) as conn:
    with conn.cursor() as cursor:
        create_tables = """
        CREATE TABLE IF NOT EXISTS topic (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        );

        CREATE TABLE IF NOT EXISTS user_chat (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        );

        CREATE TABLE IF NOT EXISTS posts (            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            user_id INTEGER REFERENCES user_chat(id),
            topic_id INTEGER REFERENCES topic(id)
        );
        """
        cursor.execute(create_tables)

        topics = [('Technology',), ('Travel',), ('Food',)]
        cursor.executemany("INSERT INTO topic (name) VALUES (%s);", topics)

        users = [
            ('Alice', 'alice@gmail.com'),
            ('Bob', 'bob@gmail.com'),
            ('Charlie', 'charlie@gmail.com')
        ]
        cursor.executemany("INSERT INTO user_chat (username, email) VALUES (%s, %s);", users)

        posts = [
            ('I love Python!', 1, 1),
            ('Visited Greece last year, amazing!', 2, 2),
            ('Best pizza I ever had in Ukraine.', 3, 3),
        ]
        cursor.executemany("INSERT INTO posts (content, user_id, topic_id) VALUES (%s, %s, %s);", posts)