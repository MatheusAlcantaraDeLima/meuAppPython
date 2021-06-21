import psycopg2
conn = psycopg2.connect("dbname= teste user=matheus password=1997")
cur = conn.cursor()
