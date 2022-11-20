from sqlalchemy.sql import text
from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:root@localhost/postgres')

# 1
sql = text("select disease_code, description from discover join disease using(disease_code) where first_enc_date<:d and pathogen = :p")
print(engine.execute(sql, p='bacteria', d='1-1-1990').fetchall())

# 2
sql = text("select name, surname, degree from specialize join diseasetype using(id) join disease using(id) join doctor using(email) join users using(email) where id!= :n")
print(engine.execute(sql, n=1).fetchall())

# 3
sql = text("select name, surname, degree from specialize join diseasetype using(id) join disease using(id) join doctor using(email) join users using(email) group by name, surname, degree having count(email)>:m ")
print(engine.execute(sql, m=2).fetchall())

# 4
sql = text("select cname, avg(salary) from specialize join doctor using(email) join users using(email) join diseasetype using(id) where id= :id group by cname ")
print(engine.execute(sql, id=8).fetchall())

# 5
sql = text("select department || ' ' || count(*) as deps from (select email, count(*) as reports, " \
      "department from record join disease using(disease_code) join publicservant using(email) " \
      "where disease_code = :code group by email, department having count(*)>2) servants group by department")
print(engine.execute(sql, code='8').fetchall())

# 6
sql = text("update users set salary=salary*2 where email in (select email from record where disease_code = :code group by email having count(*)>3)")
engine.execute(sql, code='8')

# 7
sql = text("delete from specialize where email in (select email from users where Lower(name) like :f or Lower(name) like :s)")
engine.execute(sql, f='%%bek%%', s='%%gul%%')
sql = text("delete from doctor where email in (select email from users where Lower(name) like '%%bek%%' or Lower(name) like '%%gul%%');")
engine.execute(sql)
sql = text("delete from record where email in (select email from users where Lower(name) like '%%bek%%' or Lower(name) like '%%gul%%')")
engine.execute(sql)
sql = text("delete from publicservant where email in (select email from users where Lower(name) like '%%bek%%' or Lower(name) like '%%gul%%');")
engine.execute(sql)
sql = "delete from users where Lower(name) like '%%bek%%' or Lower(name) like '%%gul%%'"
engine.execute(sql)

# 8
# sql = text("create index :index on disease(pathogen)")
# engine.execute(sql, index='idx_pathogen')

# 9
sql = text("select email, name, department from record join publicservant using(email) join users using(email) where total_patients between :num1 and :num2")
print(engine.execute(sql, num1 = 100000, num2=999999).fetchall())

# 10
sql = text("select cname, sum(total_patients) from record group by cname order by sum desc")
print(engine.execute(sql).fetchmany(5))

# 11
sql = text("select diseasetype.description, sum(total_patients) from record join disease " \
      "using(disease_code) join diseasetype using(id) group by diseasetype.description")
print(engine.execute(sql).fetchall())