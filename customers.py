#Desativa alguns avisos
import warnings
warnings.filterwarnings("ignore")

#Importações necessárias
import pandas as pd #importa o pandas para 
from connect_oracle import criar_conexao #importa a conexão criada no connect_oracle.py

# Importa o arquivo excel superstore.xlsx para dentro de um dataframe
df = pd.read_excel("superstore.xlsx", sheet_name="Orders")

df.Category.unique() 

connection = criar_conexao()
cursor = connection.cursor()

cursor.execute(" drop table customers ")
cursor.execute("""
    create table customers (
               Customer_ID varchar2(8),
               Customer_Name varchar2(100),
               Segment varchar2(100),
               Country varchar2(100),
               City varchar2(100),
               State varchar2(50),
               Postal_Code varchar2(100),
               Region varchar2(100),
               primary key (Customer_ID))""")

customers = df[["Customer ID", "Customer Name", "Segment", "Country", "City", "State",
       "Postal Code", "Region",]]

customers.rename(
    columns={
        'Customer ID': 'Customer_ID',
        'Customer Name': 'Customer_Name',
        'Postal Code': 'Postal_Code'}, inplace=True)

customers.drop_duplicates(subset = 'Customer_ID', inplace=True, ignore_index=True)

customers.columns

customers

query = []
for index, row in customers.iterrows():
    query += [(
        str(customers.Customer_ID[index]),
        str(customers.Customer_Name[index]),
        str(customers.Segment[index]),
        str(customers.Country[index]),
        str(customers.City[index]),
        str(customers.State[index]),
        str(customers.Postal_Code[index]),
        str(customers.Region[index])
    )]
    
print(query[1:3])

cursor.executemany("""
        insert into customers (
            Customer_ID, 
            Customer_Name, 
            Segment, 
            Country, 
            City, 
            State, 
            Postal_Code, 
            Region) values(:1, :2, :3, :4, :5, :6, :7, :8)"""
            , query)
print(cursor.rowcount, "Rows Inserted")

#Inserting data in SQL Table:- 
cursor.executemany("insert into customers values()", customers)
print(cursor.rowcount, "Rows Inserted")

connection.commit()

connection.close()