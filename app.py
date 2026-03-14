from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def connect_db():
    return mysql.connector.connect(
        host='db',
        user='root',
        password='password123',
        database='projeto_db'
    )

@app.route('/')
def index():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT nome, cor FROM itens")
        rows = cursor.fetchall()
        
        
        html = "<h1>Consulta ao Banco de Dados</h1><ul>"
        for row in rows:
            html += f"<li><strong>{row[0]}</strong> - Cor: {row[1]}</li>"
        html += "</ul>"
        
        cursor.close()
        conn.close()
        return html
    except Exception as e:
        return f"<h1>Erro na conexão!</h1><p>{str(e)}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)