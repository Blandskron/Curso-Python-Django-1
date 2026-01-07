import psycopg2
from psycopg2.extras import RealDictCursor

try:
    conn = psycopg2.connect(
        host="172.26.240.1",
        port=5433,
        dbname="app_db",
        user="app_user",
        password="app_password_123",
        connect_timeout=5
    )

    print("✅ Conexión exitosa a PostgreSQL")

    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("SELECT version();")
        result = cursor.fetchone()
        print("PostgreSQL version:", result["version"])

except psycopg2.Error as e:
    print("❌ Error de conexión:")
    print(e)

finally:
    if 'conn' in locals():
        conn.close()
        print("🔒 Conexión cerrada")
