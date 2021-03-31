# EHR 4 REPORT
## What is the problem?
Refactor the previous EHR analysis code to use SQLite. This is a true refactor in that the public API should not change. But instead of loading the data into Python class attributes or global variables, it should be INSERTed into a SQLite database. Create an index on PatientID..  
## Here is a breif show of the patient table:
|PatientID                           |PatientGender|PatientDateOfBirth     |PatientRace     |PatientMaritalStatus|PatientLanguage|PatientPopulationPercentageBelowPoverty|
|------------------------------------|-------------|-----------------------|----------------|--------------------|---------------|---------------------------------------|
|FB2ABB23-C9D0-4D09-8464-49BF0B982F0F|Male         |1947-12-28 02:45:40.547|Unknown         |Married             |Icelandic      |18.08                                  |
|64182B95-EB72-4E2B-BE77-8050B71498CE|Male         |1952-01-18 19:51:12.917|African American|Separated           |English        |13.03                                  |
|DB22A4D9-7E4D-485C-916A-9CD1386507FB|Female       |1970-07-25 13:04:20.717|Asian           |Married             |English        |6.67                                   |
|6E70D84D-C75F-477C-BC37-9177C3698C66|Male         |1979-01-04 05:45:29.580|White           |Married             |English        |16.09                                  |
|C8556CC0-32FC-4CA5-A8CD-9CCF38816167|Female       |1921-04-11 11:39:49.197|White           |Married             |English        |18.2                                   |
|7FD13988-E58A-4A5C-8680-89AC200950FA|Male         |1965-07-12 15:41:20.523|White           |Married             |Spanish        |12.41                                  |
|C60FE675-CA52-4C55-A233-F4B27E94987F|Male         |1957-10-30 23:26:15.303|Asian           |Married             |Spanish        |12.8                                   |
|B39DC5AC-E003-4E6A-91B6-FC07625A1285|Female       |1935-11-03 21:07:09.040|White           |Married             |English        |15.31                                  |
|FA157FA5-F488-4884-BF87-E144630D595C|Female       |1932-11-01 06:19:56.577|White           |Single              |English        |16.32                                  |
|B7E9FC4C-5182-4A34-954E-CEF5FC07E96D|Female       |1985-12-11 02:48:16.907|Unknown         |Single              |English        |11.43                                  |

We bubild the Patient class based on this table:

```python
class Patient():
    """Class Patient"""
    def __init__(self, cursor, ID):  #time efficiency O(logn)
        """Initialize"""
        """define the instance attribute for ID, where ID is a input value"""
        if not isinstance(ID, str):
            raise ValueError(f"{ID} is not a string variable")
        self.cursor = cursor
        self.id = ID

    @property
    def race(self):
        cmd = f"SELECT patient.PatientRace FROM patient where PatientID = '{self.id}'"
        self.cursor.execute(cmd)
        return cur.fetchone()[0]

    @property
    def gender(self):
        cmd = f"SELECT patient.PatientGender FROM patient where PatientID = '{self.id}'"
        self.cursor.execute(cmd)
        return cur.fetchone()[0]

    @property
    def DOB(self):
        #define the date format:
        date_format = '%Y-%m-%d %H:%M:%S.%f'
        cmd = f"SELECT patient.PatientDateOfBirth FROM patient where PatientID = '{self.id}'"
        self.cursor.execute(cmd)
        birth = cur.fetchone()[0]
        do = datetime.strptime(birth, date_format)
        return do
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
```
Patient class also has age property, function of : less_than, greater_than, plot
## Here is a breif show of the lab table:
|PatientID                           |AdmissionID|LabName                      |LabValue|LabUnits|LabDateTime            |
|------------------------------------|-----------|-----------------------------|--------|--------|-----------------------|
|1A8791E3-A61C-455A-8DEE-763EB90C9B2C|1          |URINALYSIS: RED BLOOD CELLS  |1.8     |rbc/hpf |1992-07-01 01:36:17.910|
|1A8791E3-A61C-455A-8DEE-763EB90C9B2C|1          |METABOLIC: GLUCOSE           |103.3   |mg/dL   |1992-06-30 09:35:52.383|
|1A8791E3-A61C-455A-8DEE-763EB90C9B2C|1          |CBC: MCH                     |35.8    |pg      |1992-06-30 03:50:11.777|
|1A8791E3-A61C-455A-8DEE-763EB90C9B2C|1          |METABOLIC: CALCIUM           |8.9     |mg/dL   |1992-06-30 12:09:46.107|
|1A8791E3-A61C-455A-8DEE-763EB90C9B2C|1          |CBC: RED BLOOD CELL COUNT    |4.8     |m/cumm  |1992-07-01 01:31:08.677|

We build the observation class of this table:

```python
class Observation:
    """Class Observation"""
    def __init__(self, cursor, ID): 
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
```
## Some examples:

```python
patient1 = Patient(cur, "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F")
patient2 = Patient(cur, 'DB92CDC6-FA9B-4492-BC2C-0C588AD78956')
observation1 = Observation(cur, 'DB92CDC6-FA9B-4492-BC2C-0C588AD78956')
observation2 = Observation(cur, 'FB2ABB23-C9D0-4D09-8464-49BF0B982F0F')
print(patient1.Age) #=====> 73.25
print(patient1 > patient2) #======> True
patient2.plot("URINALYSIS: PH", "Uph_over_time.png")
patient1.plot("URINALYSIS: RED BLOOD CELLS", "111.png")
```

## Following is the plot: unit_value vs time of given patient:
![Uph_over_time.png](https://i.loli.net/2021/03/30/8akPAsTFCYWQtvx.png)
![111.png](https://i.loli.net/2021/03/30/LNJ41EVzDyIXtj5.png)

## Tests:
PLEASE access to test files (test_ehr4.py), this file includes two test functions for two classes.