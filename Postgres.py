# Connect into DB on the PC Саша
import psycopg3

# Connect to an existing database
with psycopg3.connect(
        user="two",
        password="123",
        host="localhost",
        dbname="shop",
        port="5432") as conn:
    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        # Execute a command: this creates a new table
        cur.execute("""
            CREATE TABLE test (
                id serial PRIMARY KEY,
                num integer,
                data text)
            """)

        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no SQL injections!)
        cur.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s)",
            (100, "abide"))
        cur.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s)",
            (101, "abide"))
        cur.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s)",
            (102, "abide"))
        cur.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s)",
            (103, "abide"))
        cur.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s)",
            (104, "abide"))
        cur.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s)",
            (105, "abide"))

        # Query the database and obtain data as Python objects.
        cur.execute("SELECT * FROM test where (num<103 OR num>103)")
        # cur.fetchone()
        # will return (1, 100, "abide")

        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor
        for record in cur:
            print(record)

        # Make the changes to the database persistent
        conn.commit()
        cur.execute("DROP TABLE test")
