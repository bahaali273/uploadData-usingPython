import sqlalchemy as sa
# write to database insert, update, delete
con = sa.create_engine("mysql+pymysql://root@localhost:8080/Uni")
with con.connect() as db:
    db.execute(sa.text("insert into students values(1003, 'Bahaa','Eng',88)"))
    db.commit()
    print("Done")