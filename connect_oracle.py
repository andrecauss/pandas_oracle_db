import oracledb
def criar_conexao():
    connection = oracledb.connect(
        user="ANDRECAUSS",
        password="admin",
        dsn="localhost/xepdb1"
    )
    return connection
