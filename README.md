# Instructions: 
This project builds two classes of patients, the first is Class_Patient, and the second is Class_Observation. Pdic is a dictionary to store all information of the patient_file, in the
format: {patient id : Patient class}.
## Versions of package:
pandas            1.2.2
<br>
matplotlib        3.3.4

## Example:
```python
print(patient1 < 57.0) #===> output:first patient not younger than other
print(patient1 > patient2) #===> output: first patient older than other

print(pdic['FB2ABB23-C9D0-4D09-8464-49BF0B982F0F'].age) #=>73.2
print(pdic['DB92CDC6-FA9B-4492-BC2C-0C588AD78956'].age) #=>43.7

print(pdic['FB2ABB23-C9D0-4D09-8464-49BF0B982F0F'] > pdic['DB92CDC6-FA9B-4492-BC2C-0C588AD78956')
#===>first patient older than other
print(pdic['FB2ABB23-C9D0-4D09-8464-49BF0B982F0F'] < 66.0)
#===>first patient not younger than other
pdic['FB2ABB23-C9D0-4D09-8464-49BF0B982F0F'].plot("URINALYSIS: RED BLOOD CELLS", "111.png")
patient1.plot("URINALYSIS: RED BLOOD CELLS", "Urbc_overtime.png")

Patient("220C8D43-1322-4A9D-B890-D426942A3649", "Female", "1957-01-18 19:51:12.917000", \
    "african").plot("URINALYSIS: PH", "ph_over_time.png")
```
For the graph example, please refer the plot file in the same folder.

## In the patient class
It records patients' ID, gender, DOB, race, and age. Age is a property instance attribute. 
<br>
The class Patient could compare the age of the Patient to that of other Patients _and_ floats
i.e. `Patient() > Patient()` and `Patient() > 57.0` and return two possible statements for __lt__ and __gt__ functions:
<br>__ls__:
<br> "first patient younger than other"
<br>"first patient not younger than other"
<br> "first patient older than other"
<br>"first patient not older than other"
<br><br>
And Patient class could plot lab values over time for a given patient, and saves the resulting figure as a PNG file as a given name:
<br>
For example: 
<br>`Patient().plot("URINALYSIS: PH", "ph_over_time.png")`

## Examples:

```python
patient1 = Patient("1A8791E3-A61C-455A-8DEE-763EB90C9B2C", "Male", "1947-01-18 19:51:12.917000", "african")

patient2 = Patient("220C8D43-1322-4A9D-B890-D426942A3649", "Female", "1957-01-18 19:51:12.917000", "african")
```

Patient1 plot saved as ""Urbc_over_time.png"" and Patient2 plot saved as ""Uph_over_time.png"", you can reach to these two graphs in the folder.
<br>
<br>
If```patient1 < patient```=======>
returns: "first patient not younger than other"

## In the observation class:
It records obeservation id, lab, and test value.

## Test
You could access to a simple test file in the folder as well
