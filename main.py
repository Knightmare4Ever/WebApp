from flask import render_template, request, Flask
import database
app = Flask(__name__, static_folder="templates")

@app.route('/disease-type')
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/country')
def country():
    return render_template('country.html')
@app.route('/disease')
def disease():
    return render_template('disease.html')
@app.route('/discover')
def discover():
    return render_template('discover.html')
@app.route('/users')
def users():
    return render_template('users.html')
@app.route('/public-servant')
def public_servant():
    return render_template('public-servant.html')
@app.route('/doctor')
def doctor():
    return render_template('doctor.html')
@app.route('/specialize')
def specialize():
    return render_template('specialize.html')
@app.route('/record')
def record():
    return render_template('record.html')




@app.route('/add-diseasetype', methods=['POST'])
def addDiseaseType():
    name = request.form.get('name')
    if database.getDiseaseType(name) is not None:
        return render_template('index.html',add="The disease type already exist!")
    database.addDiseaseType(name)
    return render_template('index.html',add='Added')

@app.route('/delete-diseasetype', methods=['POST'])
def deleteDiseaseType():
    name = request.form.get('name')
    if database.getDiseaseType(name) is None:
        return render_template('index.html',delete="The disease type doesn't exist!")
    database.deleteDiseaseType(name)
    return render_template('index.html',delete='Deleted')
@app.route('/get-diseasetype', methods=['GET'])
def getDiseaseType():
    name = request.args.get('name')
    if database.getDiseaseType(name) is None:
        return render_template('index.html',get="The disease type doesn't exist!")
    diseasetype = database.getDiseaseType(name)
    return render_template('index.html',get=f'ID = {diseasetype[0]}')
@app.route('/update-diseasetype', methods=['POST'])
def updateDiseaseType():
    name = request.form.get('name')
    id = int(request.form.get('id'))
    if database.getDiseaseTypeById(id) is None:
        return render_template('index.html',update="The disease type doesn't exist!")
    database.updateDiseaseType(id, name)
    return render_template('index.html',update="Updated")

@app.route('/get-diseasetypebyid', methods=['GET'])
def getDiseaseTypeById():
    id = request.args.get('id')
    if database.getDiseaseTypeById(id) is None:
        return render_template('index.html',id="The disease type doesn't exist!")
    diseasetype = database.getDiseaseTypeById(id)
    return render_template('index.html',id=f'Name = {diseasetype[1]}')


@app.route('/add-country', methods=['POST'])
def addCountry():
    name = request.form.get('name')
    population = request.form.get('population')
    if database.getCountry(name.lower()) is not None:
        return render_template('country.html',add="The country already exist!")
    database.addCountry(name, population)
    return render_template('country.html',add='Added')


@app.route('/delete-country', methods=['POST'])
def deleteCountry():
    name = request.form.get('name')
    if database.getCountry(name.lower()) is None:
        return render_template('country.html',delete="The country doesn't exist!")
    database.deleteCountry(name)
    return render_template('country.html',delete='Deleted')


@app.route('/get-country', methods=['GET'])
def getCountry():
    name = request.args.get('name')
    if database.getCountry(name.lower()) is None:
        return render_template('country.html',get="The country doesn't exist!")
    country = database.getCountry(name.lower())
    return render_template('country.html',get=f'The population of {name} is {country[1]}')

@app.route('/update-country', methods=['POST'])
def updateCountry():
    name = request.form.get('name')
    population = request.form.get('population')
    if database.getCountry(name.lower()) is None:
        return render_template('country.html',update="The country doesn't exist!")
    database.deleteCountry(name)
    database.addCountry(name, population)
    return render_template('country.html',update='Updated')


@app.route('/add-disease', methods=['POST'])
def addDisease():
    name = request.form.get('name')
    code = request.form.get('code')
    pathogen = request.form.get('pathogen')
    diseasetypeid = request.form.get('id')
    if database.getDiseaseByCode(code) is not None:
        return render_template('disease.html',add="The disease code already exist!")
    if database.getDiseaseTypeById(diseasetypeid) is None:
        return render_template('disease.html',add="The disease type doesn't exist!")
    database.addDisease(code, pathogen, diseasetypeid, name)
    return render_template('disease.html',add='Added')

@app.route('/delete-disease', methods=['POST'])
def deleteDisease():
    code = request.form.get('code')
    if database.getDiseaseByCode(code) is None:
        return render_template('disease.html',delete="The disease doesn't exist!")
    database.deleteDisease(code)
    return render_template('disease.html',delete='Deleted')

@app.route('/get-disease', methods=['GET'])
def getDisease():
    code = request.args.get('code')
    if database.getDiseaseByCode(code) is None:
        return render_template('disease.html',get="The disease doesn't exist!")
    disease = database.getDiseaseByCode(code)
    return render_template('disease.html',get=f"Pathogen: {disease[1]}  |"
                                              f"Disease type ID: {disease[2]}   |"
                                              f"Name: {disease[3]}")


@app.route('/update-disease', methods=['POST'])
def updateDisease():
    name = request.form.get('name')
    code = request.form.get('code')
    pathogen = request.form.get('pathogen')
    diseasetypeid = request.form.get('id')
    if database.getDiseaseByCode(code) is None:
        return render_template('disease.html',update="The disease code doesn't exist!")
    if database.getDiseaseTypeById(diseasetypeid) is None:
        return render_template('disease.html',update="The disease type doesn't exist!")
    database.updateDisease(code, pathogen, diseasetypeid, name)
    return render_template('disease.html',update='Updated')


@app.route('/add-discover', methods=['POST'])
def addDiscover():
    country = request.form.get('country')
    code = request.form.get('code')
    date = request.form.get('date')
    if database.getDiseaseByCode(code) is None:
        return render_template('discover.html',add="The disease code doesn't exist!")
    if database.getCountry(country) is None:
        return render_template('discover.html',add="The country doesn't exist!")
    if database.getDiscover(code, country) is not None:
        return render_template('discover.html',add="The discover already exist!")
    database.addDiscover(code, country, date)
    return render_template('discover.html',add='Added')

@app.route('/delete-discover', methods=['POST'])
def deleteDiscover():
    country = request.form.get('country')
    code = request.form.get('code')
    if database.getDiscover(code, country) is None:
        return render_template('discover.html',delete="The discover doesn't exist!")
    database.deleteDiscover(code, country)
    return render_template('discover.html',delete='Deleted')


@app.route('/get-discover', methods=['GET'])
def getDiscover():
    country = request.args.get('country')
    code = request.args.get('code')
    if database.getDiscover(code, country) is None:
        return render_template('discover.html',get="The discover doesn't exist!")
    discover = database.getDiscover(code, country)
    return render_template('discover.html',get=f"The discover date is {discover[2]}")


@app.route('/update-discover', methods=['POST'])
def updateDiscover():
    country = request.form.get('country')
    code = request.form.get('code')
    date = request.form.get('date')
    if database.getDiscover(code, country) is None:
        return render_template('discover.html',update="The discover doesn't exist!")
    database.updateDiscover(code, country, date)
    return render_template('discover.html',update='Updated')


@app.route('/add-user', methods=['POST'])
def addUser():
    country = request.form.get('country')
    email = request.form.get('email')
    name = request.form.get('name').split(' ')
    salary = request.form.get('salary')
    phone = request.form.get('phone')
    if database.getUser(email) is not None:
        return render_template('users.html',add="The user already exist!")
    if database.getCountry(country) is None:
        return render_template('users.html',add="The country doesn't exist!")
    database.addUser(email, name[0], name[1], salary, phone, country)
    return render_template('users.html',add='Added')

@app.route('/delete-user', methods=['POST'])
def deleteUser():
    email = request.form.get('email')
    if database.getUser(email) is None:
        return render_template('users.html',delete="The user doesn't exist!")
    database.deleteUser(email)
    return render_template('users.html',delete='Deleted')

@app.route('/get-user', methods=['GET'])
def getUser():
    email = request.args.get('email')
    print(email)
    if database.getUser(email) is None:
        return render_template('users.html',get="The user doesn't exist!")
    user = database.getUser(email)
    return render_template('users.html',get=f"Name and surname: {user[1]} {user[2]}     | Salary: {user[3]}     | Phone: {user[4]}      | Country: {user[5]}")


@app.route('/update-user', methods=['POST'])
def updateUser():
    country = request.form.get('country')
    email = request.form.get('email')
    name = request.form.get('name').split(' ')
    salary = request.form.get('salary')
    phone = request.form.get('phone')
    if database.getUser(email) is None:
        return render_template('users.html',update="The user doesn't exist!")
    if database.getCountry(country) is None:
        return render_template('users.html',update="The country doesn't exist!")
    database.updateUser(email, name[0], name[1], salary, phone, country)
    return render_template('users.html',update  ='Updated')


@app.route('/add-public-servant', methods=['POST'])
def addPublicServant():
    department = request.form.get('department')
    email = request.form.get('email')
    if database.getUser(email) is None:
        return render_template('public-servant.html',add="The user doesn't exist!")
    if database.getPublicServant(email) is not None:
        return render_template('public-servant.html',add="The public servant already exist!")
    database.addPublicServant(email, department)
    return render_template('public-servant.html',add='Added')

@app.route('/delete-public-servant', methods=['POST'])
def deletePublicServant():
    email = request.form.get('email')
    if database.getPublicServant(email) is None:
        return render_template('public-servant.html',delete="The public servant doesn't exist!")
    database.deletePublicServant(email)
    return render_template('public-servant.html',delete='Deleted')

@app.route('/get-public-servant', methods=['GET'])
def getPublicServant():
    email = request.args.get('email')
    if database.getPublicServant(email) is None:
        return render_template('public-servant.html',get="The public servant doesn't exist!")
    serv = database.getPublicServant(email)
    return render_template('public-servant.html',get=f"Servant department: {serv[1]}")


@app.route('/update-public-servant', methods=['POST'])
def updatePublicServant():
    email = request.form.get('email')
    department = request.form.get('department')
    if database.getPublicServant(email) is None:
        return render_template('public-servant.html', update="The public servant doesn't exist!")
    database.updatePublicServant(email, department)
    return render_template('public-servant.html', update='Updated')


@app.route('/add-doctor', methods=['POST'])
def addDoctor():
    degree = request.form.get('degree')
    email = request.form.get('email')
    if database.getUser(email) is None:
        return render_template('doctor.html',add="The user doesn't exist!")
    if database.getDoctor(email) is not None:
        return render_template('doctor.html',add="The doctor already exist!")
    database.addDoctor(email, degree)
    return render_template('doctor.html',add='Added')

@app.route('/delete-doctor', methods=['POST'])
def deleteDoctor():
    email = request.form.get('email')
    if database.getDoctor(email) is None:
        return render_template('doctor.html',delete="The doctor doesn't exist!")
    database.deleteDoctor(email)
    return render_template('doctor.html',delete='Deleted')

@app.route('/get-doctor', methods=['GET'])
def getDoctor():
    email = request.args.get('email')
    if database.getDoctor(email) is None:
        return render_template('doctor.html',get="The doctor doesn't exist!")
    doc = database.getDoctor(email)
    return render_template('doctor.html',get=f"Doctor degree: {doc[1]}")


@app.route('/update-doctor', methods=['POST'])
def updateDoctor():
    email = request.form.get('email')
    degree = request.form.get('degree')
    if database.getDoctor(email) is None:
        return render_template('doctor.html', update="The doctor doesn't exist!")
    database.updateDoctor(email, degree)
    return render_template('doctor.html', update='Updated')


@app.route('/add-specialize', methods=['POST'])
def addSpecialize():
    diseasetypeId = request.form.get('id')
    email = request.form.get('email')
    if database.getDoctor(email) is None:
        return render_template('specialize.html',add="The doctor doesn't exist!")
    if database.getDiseaseTypeById(diseasetypeId) is None:
        return render_template('specialize.html',add="The disease doesn't exist!")
    if database.getSpecialize(email, diseasetypeId) is not None:
        return render_template('specialize.html',add="The specialize already exist!")
    database.addSpecialize(email, diseasetypeId)
    return render_template('specialize.html',add='Added')

@app.route('/delete-specialize', methods=['POST'])
def deleteSpecialize():
    diseasetypeId = request.form.get('id')
    email = request.form.get('email')
    if database.getDoctor(email) is None:
        return render_template('specialize.html',delete="The doctor doesn't exist!")
    if database.getSpecialize(email, diseasetypeId) is None:
        return render_template('specialize.html',delete="The specialize doesn't exist!")
    database.deleteSpecialize(email, diseasetypeId)
    return render_template('specialize.html',delete='Deleted')

@app.route('/get-specialize', methods=['GET'])
def getSpecialize():
    email = request.args.get('email')
    if database.getSpecializes(email) is None:
        return render_template('specialize.html',get="The specializes doesn't exist!")
    specializes = database.getSpecializes(email)
    txt = ""
    for sp in specializes:
        txt+=str(sp[0])+' | '
    return render_template('specialize.html',get=f"Doctor specializes: {txt}")

@app.route('/add-record', methods=['POST'])
def addRecord():
    email = request.form.get('email')
    country = request.form.get('country')
    disease_code = request.form.get('code')
    deaths = request.form.get('deaths')
    patients = request.form.get('patients')
    if database.getPublicServant(email) is None:
        return render_template('record.html', add="The public servant doesn't exist")
    if database.getCountry(country) is None:
        return render_template('record.html', add="The country exist")
    if database.getDiseaseByCode(disease_code) is None:
        return render_template('record.html', add="The disease doesn't exist")
    if database.getRecord(email, country, disease_code) is not None:
        return render_template('record.html', add="The record already exist")
    database.addRecord(email, country, disease_code, deaths, patients)
    return render_template('record.html',add="Added")

@app.route('/delete-record', methods=['POST'])
def deleteRecord():
    email = request.form.get('email')
    country = request.form.get('country')
    disease_code = request.form.get('code')
    if database.getRecord(email, country, disease_code) is None:
        return render_template('record.html', delete="The record doesn't exist")
    database.deleteRecord(email, country, disease_code)
    return render_template('record.html',delete="Deleted")

@app.route('/get-record', methods=['GET'])
def getRecord():
    email = request.args.get('email')
    country = request.args.get('country')
    disease_code = request.args.get('code')
    if database.getRecord(email, country, disease_code) is None:
        return render_template('record.html', get="The record doesn't exist")
    record = database.getRecord(email, country, disease_code)
    return render_template('record.html',get=f"Deaths: {record[3]}   | Patients: {record[4]}")


@app.route('/update-record', methods=['POST'])
def updateRecord():
    email = request.form.get('email')
    country = request.form.get('country')
    disease_code = request.form.get('code')
    deaths = request.form.get('deaths')
    patients = request.form.get('patients')
    if database.getRecord(email, country, disease_code) is None:
        return render_template('record.html', update="The record doesn't exist")
    database.updateRecord(email, country, disease_code, deaths, patients)
    return render_template('record.html',update="Updated")

if __name__=='__main__':
    app.run()

