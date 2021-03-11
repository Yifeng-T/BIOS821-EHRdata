import datetime
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

class Patient():
    """Class Patient"""
    def __init__(self, ID, sex, birth, race): 
        """Initialize. 4 instance attributes"""
        """define the instance attribute for id, where ID is a input value"""
        #define the date format:
        date_format = '%Y-%m-%d %H:%M:%S.%f'
        if not isinstance(ID, str):
            raise ValueError(f"{ID} is not a string variable")
        if not isinstance(sex, str):
            raise ValueError(f"{sex} is not a string variable")
        if not isinstance(birth, str):
            raise ValueError(f"{birth} is not a string variable")
        if not isinstance(race, str):
            raise ValueError(f"{race} is not a string variable")
        self.id = ID
        self.gender = sex
        self.DOB = datetime.strptime(birth, date_format)
        self.race = race

        #define the current date:
        current_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')
        current_date = datetime.strptime(current_date, date_format)
        # self.age is a time value
        total_age = current_date - self.DOB
        self.age = round(total_age.days/365.25, 2)
    
    @property
    def Age(self):
        """define the property value: age"""
        # self.age is a time value
        return self.age

    def __lt__(self, other):
        """working comparison operators for less than '<'"""
        if isinstance(other, Patient): # check other ===? patient class
            age1 = self.age
            age2 = other.age
            if age1 < age2:
                return "first patient younger than other"
            else:
                return "first patient not younger than other"
        elif isinstance(other, float): # check other ===? float
            age1 = self.age
            age2 = other.age 
            if age1 < age2:
                return "first patient younger than other"
            else:
                return "first patient not younger than other"
        else:
            raise ValueError(f"{other} is not a 'Patient' or float")

    
    def __gt__(self, other):
        """working comparison operators for larger than '>'"""
        if isinstance(other, Patient): # check other ===? patient class
            age1_sec = self.age.total_seconds()
            age2_sec = other.age.total_seconds()
            if age1_sec > age2_sec:
                return "first patient older than other"
            else:
                return "first patient not older than other"
        elif isinstance(other, float): # check other ===? float
            age1_sec = self.age.total_seconds()
            age2_sec = other * 31536000 # change the year unit ===> second unit
            if age1_sec > age2_sec:
                return "first patient older than other"
            else:
                return "first patient not older than other"
        else:
            raise ValueError(f"{other} is not a 'Patient' or float")
    
    def plot(self, lab_name, picture_name):
        """plotting the graph: lab values over time"""
        if not isinstance(lab_name, str):
            raise ValueError(f"lab_name: {lab_name} should be a string")
        if not isinstance(picture_name, str):
            raise ValueError(f"plot_name: {picture_name} should be a string")
        
        #read_in data frame
        lab = pd.read_table("./LabsCorePopulatedTable.txt", delimiter = "\t")

        #sort the date value: in chronological order:
        lab['LabDateTime']=pd.to_datetime(lab['LabDateTime'])
        lab.sort_values('LabDateTime',inplace=True)

        #----filter the rows have for given patient id
        is_id = lab["PatientID"] == self.id 
        lab_select_id = lab[is_id] 
        #----filter the rows match the input lab_name for given patient
        is_lab = lab_select_id["LabName"] == lab_name
        lab_filter = lab_select_id[is_lab]

        if lab_filter.empty:
            raise ValueError(f"The patient haven't taken test in {lab_name}")

        #-----select the lab value units:
        Units = lab_filter["LabUnits"]
        Units = list(Units)

        #define the X and Y values of plot:        
        Y = lab_filter["LabValue"]
        X = lab_filter["LabDateTime"]
        Y = list(Y)
        X = list(X)
        for i in range(0, len(X)):
            X[i] = str(X[i])
            X[i] = X[i][0:16]    #date value -> string
        
        #clean the previous graph
        plt.clf()
        plt.plot(X, Y, marker='o', color = "black")
        plt.title(f"Patient ID:{self.id} \n Lab Name, {lab_name}",fontsize=12)
        plt.xlabel("X: Test Time (Year-Month-Date-Hour-Minute)")
        plt.ylabel(f"Y: Test result unit in {Units[1]}")
        plt.xticks(rotation = 90)
        plt.tight_layout()
        plt.savefig(f"{picture_name}")
        
   
class Observation:
    """Class Observation"""
    def __init__(self, ID, lab_value, lab_units): 
        #lab_value (1.8). lab_unitss ('bc/hpf')
        """Initialize. 2 instance attributes"""
        """define the instance attribute for ID, where ID is a input value"""
        if not isinstance(ID, str):
            raise ValueError(f"{ID} is not a string variable")
        if not isinstance(lab_value, float):
            raise ValueError(f"{lab_value} is not a float variable")
        if not isinstance(lab_units, str):
            raise ValueError(f"{lab_units} is not a string variable")
        self.id = ID
        self.value = lab_value
        self.units = lab_units

if __name__ == "__main__":
    """some examples"""
    patient1 = Patient("1A8791E3-A61C-455A-8DEE-763EB90C9B2C", "Male", \
        "1947-01-18 19:51:12.917000", "african")
    patient2 = Patient("220C8D43-1322-4A9D-B890-D426942A3649", "Female", \
        "1957-01-18 19:51:12.917000", "african")
    ob1 = Observation("14", 103.3, "mg/dL")
    #print(patient1.id)
    #print(patient1.gender)
    #print(patient1.DOB)
    #print(patient1.race)
    #print(ob1.id)
    #print(ob1.value)
    #print(ob1.units)
    patient1.plot("URINALYSIS: RED BLOOD CELLS", "Urbc_overtime.png")
    #Patient("220C8D43-1322-4A9D-B890-D426942A3649", "Female", "1957-01-18 19:51:12.917000", "african").\
        #plot("URINALYSIS: PH", "ph_over_time.png")
    patient2.plot("URINALYSIS: PH", "Uph_over_time.png")
    #print(patient1 < 57.0)
    print(patient1 < patient2)

