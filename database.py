from sqlalchemy.sql import text
from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:root@localhost/postgres')

def getDiseaseType(name):
    sql = text('select * from diseasetype where description=:name')
    return engine.execute(sql, name=name).fetchone()

def addDiseaseType(name):
    sql = 'Select max(id) from diseasetype'
    id = engine.execute(sql).fetchone()[0] + 1
    sql = text('INSERT INTO public.diseasetype(	id, description) VALUES (:id, :desc);')
    engine.execute(sql,id=id,desc=name)

def deleteDiseaseType(name):
    sql = text('delete from diseasetype where description=:name')
    engine.execute(sql, name=name)

def getDiseaseTypeById(id):
    sql = text('select * from diseasetype where id=:id')
    return engine.execute(sql, id=id).fetchone()

def updateDiseaseType(id, name):
    sql = text('update diseasetype set description=:name where id=:id')
    return engine.execute(sql, name=name, id=id)

def getCountry(name):
    sql = text('select * from country where Lower(cname)=:name')
    return engine.execute(sql, name=name.lower()).fetchone()

def addCountry(name, population):
    deleteCountry(name)
    sql = text('INSERT INTO public.country(cname, population)VALUES (:name, :num);')
    engine.execute(sql, name=name.lower().capitalize(), num=population)

def deleteCountry(name):
    sql = text('delete from country where lower(cname)=:name')
    engine.execute(sql, name=name.lower())


def getDiseaseByCode(code):
    sql = text('select * from disease where disease_code=:code')
    return engine.execute(sql, code=code).fetchone()

def addDisease(code, pathogen, id, name):
    sql = text('INSERT INTO public.disease(disease_code, pathogen, id, description) VALUES (:code, :pathogen, :id, :name);')
    engine.execute(sql, code=code, pathogen=pathogen, id=id, name=name)

def deleteDisease(code):
    sql = text('delete from disease where disease_code= :code')
    engine.execute(sql, code=code)

def updateDisease(code, pathogen, id, name):
    sql = text("update disease set pathogen= :pathogen, id=:id, description=:name where disease_code=:code")
    engine.execute(sql, code=code, pathogen=pathogen, id=id, name=name)

def getDiscover(code, country):
    sql = text("select * from discover where cname=:country and disease_code=:code")
    return engine.execute(sql, code=code, country=country).fetchone()

def addDiscover(code, country, date):
    sql = text("INSERT INTO public.discover(cname, disease_code, first_enc_date) VALUES (:country, :code, :date);")
    engine.execute(sql, country=country.lower().capitalize(), code=code, date=date)

def deleteDiscover(code, country):
    sql = text("delete from discover where cname=:country and disease_code=:code")
    engine.execute(sql, country=country, code=code)

def updateDiscover(code, country, date):
    sql = text("update discover set first_enc_date=:date where disease_code=:code and cname=:country")
    engine.execute(sql, code=code, country=country, date=date)

def getUser(email):
    sql = text("Select * from users where email= :email")
    return engine.execute(sql, email=email).fetchone()


def addUser(email, name, surname, salary, phone, country):
    sql = text("INSERT INTO public.users(email, name, surname, salary, phone, cname) VALUES (:email, :name, :surname, :salary, :phone, :country);")
    engine.execute(sql, email=email, name=name, surname=surname, salary=salary, phone=phone, country=country)

def deleteUser(email):
    sql = text("delete from users where email=:email")
    engine.execute(sql, email=email)

def updateUser(email, name, surname, salary, phone, country):
    sql = text("update users set name=:name, surname=:surname, salary=:salary, phone=:phone, cname=:country where email=:email")
    engine.execute(sql, email=email, name=name, surname=surname, salary=salary, phone=phone, country=country)


def getPublicServant(email):
    sql = text("select * from publicservant where email=:email")
    return engine.execute(sql, email=email).fetchone()

def addPublicServant(email, department):
    sql = text("INSERT INTO public.publicservant(email, department)	VALUES (:email, :department);")
    engine.execute(sql, email=email, department=department)

def deletePublicServant(email):
    sql = text("Delete from publicservant where email=:email")
    engine.execute(sql, email=email)

def updatePublicServant(email, department):
    sql = text("update publicservant set department=:department where email=:email")
    engine.execute(sql, department=department, email=email)

def getDoctor(email):
    sql = text("select * from doctor where email=:email")
    return engine.execute(sql, email=email).fetchone()

def addDoctor(email, degree):
    sql = text("INSERT INTO public.doctor(email, degree)	VALUES (:email, :degree);")
    engine.execute(sql, email=email, degree=degree)

def deleteDoctor(email):
    sql = text("Delete from doctor where email=:email")
    engine.execute(sql, email=email)

def updateDoctor(email, degree):
    sql = text("update doctor set degree=:degree where email=:email")
    engine.execute(sql, degree=degree, email=email)

def getSpecialize(email, diseasetypeId):
    sql = text("select * from specialize where email=:email and id=:id")
    return engine.execute(sql, email=email, id=diseasetypeId).fetchone()

def getSpecializes(email):
    sql = text("select * from specialize where email=:email")
    return engine.execute(sql, email=email).fetchall()
def addSpecialize(email, id):
    sql = text("INSERT INTO public.specialize(id, email) VALUES (:id, :email);")
    engine.execute(sql, email=email, id=id)

def deleteSpecialize(email, id):
    sql = text("delete from specialize where email=:email and id=:id")
    engine.execute(sql, email=email, id=id)

def getRecord(email, country, code):
    sql = text("select * from record where email=:email and cname=:country and disease_code=:code")
    return engine.execute(sql, email=email, country=country, code=code).fetchone()
def addRecord(email, country, code, deaths, patients):
    sql = text("INSERT INTO public.record(email, cname, disease_code, total_deaths, total_patients) "
               "VALUES (:email, :country, :code, :deaths, :patients);")
    engine.execute(sql, email=email, code=code, country=country, deaths=deaths, patients=patients)

def deleteRecord(email, country, code):
    sql = text("delete from record where email=:email and cname=:country and disease_code=:code")
    engine.execute(sql, email=email, code=code, country=country)

def updateRecord(email, country, code, deaths, patients):
    sql = text("update record set total_deaths=:deaths, total_patients=:patients where "
               "email=:email and cname=:country and disease_code=:code")
    engine.execute(sql, email=email, code=code, country=country, deaths=deaths, patients=patients)