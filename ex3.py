import pandas as pd
import sqlalchemy as sa
# name => root and localhost name of the server and maybe there's IP address from the company
#if there is pass i have to add : and the pass
con = sa.create_engine("mysql+pymysql://root@localhost:8080/Uni")
stdid = input("Enter Student ID")
data = pd.read_sql("select * from students where id =" + stdid, con)
print(data)

