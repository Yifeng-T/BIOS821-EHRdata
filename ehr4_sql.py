import  sqlite3
import datetime
from datetime import datetime
import matplotlib.pyplot as plt

# create database and initialize cursor.
# patient db: con ||||| lab db: con2
con = sqlite3.connect(":memory")
cur = con.cursor()

# create table if not exists
cur.execute('''CREATE TABLE IF NOT EXISTS patient(PatientID text, PatientGender text, PatientDateOfBirth text, \
    PatientRace text, PatientMaritalStatus text, PatientLanguage text, \
    PatientPopulationPercentageBelowPoverty flow)''')

cur.execute('''CREATE TABLE IF NOT EXISTS lab(PatientID text, AdmissionID int, LabName text, LabValue flow, \
    LabUnits text, LabDateTime text)''')


with open("PatientCorePopulatedTable.txt", 'r') as fr:
    index = 0
    for line in fr.readlines(): #time efficiency: O(n)
        # parse the results.txt, create a list of comma separated values
        line = line.replace('\n', '').split('\t')
        a,b,c,d,e,f,g = line
        if index == 0:
            g = g
            index = index + 1
        else:
            g = float(g)
            index = index + 1
        cmd = f"INSERT INTO patient VALUES ('{a}', '{b}', '{c}', '{d}', '{e}', '{f}', '{g}')"
        cur.execute(cmd)

with open("LabsCorePopulatedTable.txt", 'r') as gr:
    index2 = 0
    for line in gr.readlines(): #time efficienct O(n)
        # parse the results.txt, create a list of comma separated values
        line = line.replace('\n', '').split('\t')
        A,B,C,D,E,F = line
        if index2 == 0:
            B = B
            D = D
            index2 = index2 + 1
        else:
            B = int(B)
            D = float(D)
            index2 = index2 + 1
        cmd = f"INSERT INTO lab VALUES ('{A}', '{B}', '{C}', '{D}', '{E}', '{F}')"
        cur.execute(cmd)

con.commit()
cmd = "CREATE INDEX IF NOT EXISTS ID ON patient(PatientID)"
cur.execute(cmd)


class Patient():
    """Class Patient"""
    def __init__(self, cursor, ID):  #time efficiency O(logn)
        """Initialize"""
        """define the instance attribute for ID, where ID is a input value"""
        #define the date format:
        date_format = '%Y-%m-%d %H:%M:%S.%f'
        if not isinstance(ID, str):
            raise ValueError(f"{ID} is not a string variable")
        self.cursor = cursor
        self.id = ID
        cmd = f"SELECT patient.PatientGender FROM patient where PatientID = '{self.id}'"
        cursor.execute(cmd)
        self.gender = cur.fetchall()[0][0]
        cmd = f"SELECT patient.PatientDateOfBirth FROM patient where PatientID = '{self.id}'"
        cursor.execute(cmd)
        birth = cur.fetchall()[0][0]
        self.DOB = datetime.strptime(birth, date_format)
        cmd = f"SELECT patient.PatientRace FROM patient where PatientID = '{self.id}'"
        cursor.execute(cmd)
        self.race = cur.fetchall()[0][0]
        
    @property
    def Age(self):   #time efficiency: O(1)
        """define the property value: age"""
        #define the date format:
        date_format = '%Y-%m-%d %H:%M:%S.%f'
        #define the current date:
        current_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')
        current_date = datetime.strptime(current_date, date_format)
        # self.age is a time value
        total_age = current_date - self.DOB
        age = round(total_age.days/365.25, 2)
        return age
    def __lt__(self, other): #time efficiency O(1)
        """working comparison operators for less than '<'"""
        if isinstance(other, Patient): # check other ===? patient class
            age1 = self.Age
            age2 = other.Age
            if age1 < age2:
                return True
            else:
                return False
        elif isinstance(other, float): # check other ===? float
            age1 = self.Age
            age2 = other 
            if age1 < age2:
                return True
            else:
                return False
        else:
            raise ValueError(f"{other} is not a 'Patient' or float")
    def __gt__(self, other): #time efficiency O(1)
        """working comparison operators for less than '<'"""
        if isinstance(other, Patient): # check other ===? patient class
            age1 = self.Age
            age2 = other.Age
            if age1 > age2:
                return True
            else:
                return False
        elif isinstance(other, float): # check other ===? float
            age1 = self.Age
            age2 = other 
            if age1 > age2:
                return True
            else:
                return False
        else:
            raise ValueError(f"{other} is not a 'Patient' or float")
    
    def plot(self, lab_name, picture_name): #time efficiency O(n)
        """plotting the graph: lab values over time"""
        if not isinstance(lab_name, str):
            raise ValueError(f"lab_name: {lab_name} should be a string")
        if not isinstance(picture_name, str):
            raise ValueError(f"plot_name: {picture_name} should be a string")
        
        cmd = f"SELECT lab.LabValue FROM lab \
            where (lab.PatientID = '{self.id}' and lab.LabName = '{lab_name}')"
        cur.execute(cmd)
        a = cur.fetchall()

        if len(a) == 0:
            raise ValueError(f"The patient haven't taken test in {lab_name}")
        
        cmd = f"SELECT lab.LabDateTime FROM lab \
            where (lab.PatientID = '{self.id}' and lab.LabName = '{lab_name}')"
        cur.execute(cmd)
        b = cur.fetchall()

        value = []
        date = []
        for i in range(0, len(a)):
            value.append(a[i][0])
            date.append(b[i][0])

        #-----select the lab value units:
        #Units = lab_filter["LabUnits"]
        #Units = list(Units)
        cmd = f"SELECT distinct(lab.LabUnits) FROM lab \
            where (lab.PatientID = '{self.id}' and lab.LabName = '{lab_name}')"
        cur.execute(cmd)
        c = cur.fetchall()
        unit = c[0][0]

        #define the X and Y values of plot:        
        Y = value
        X = date

        #draw the plot:
        plt.clf()#clean the previous graph
        plt.scatter(X, Y, marker='o', color = "black")
        plt.title(f"Patient ID:{self.id} \n Lab Name, {lab_name}",fontsize=12)
        plt.xlabel("X: Test Time (Year-Month-Date-Hour-Minute)")
        plt.ylabel(f"Y: Test result unit in {unit}")
        plt.xticks(rotation = 90)
        plt.tight_layout()
        plt.savefig(f"{picture_name}")
    

class Observation:  
    """Class Observation"""
    def __init__(self, cursor, ID):  #time efficiency O(log(n))
        #lab_value (1.8). lab_unitss ('bc/hpf')
        """Initialize. 2 instance attributes"""
        """define the instance attribute for ID, where ID is a input value"""
        if not isinstance(ID, str):
            raise ValueError(f"{ID} is not a string variable")
        self.id = ID
        self.cursor = cursor
        cmd = f"SELECT lab.LabValue FROM lab where PatientID = '{self.id}'"
        cursor.execute(cmd)
        self.value = cursor.fetchall()
        cmd = f"SELECT lab.LabUnits FROM lab where PatientID = '{self.id}'"
        cursor.execute(cmd)
        self.units = cursor.fetchall()
    
patient1 = Patient(cur, "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F")
patient2 = Patient(cur, 'DB92CDC6-FA9B-4492-BC2C-0C588AD78956')
observation1 = Observation(cur, 'DB92CDC6-FA9B-4492-BC2C-0C588AD78956')
observation2 = Observation(cur, 'FB2ABB23-C9D0-4D09-8464-49BF0B982F0F')
print(patient1.Age) #====>64.14
print(patient1 > patient2) #===> true
print(observation1.units[5][0]) 
print(observation2.value[0][0])
patient2.plot("URINALYSIS: PH", "Uph_over_time.png")
patient1.plot("URINALYSIS: RED BLOOD CELLS", "111.png")
con.commit()



