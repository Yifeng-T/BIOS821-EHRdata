#------------------------------------
#for PatientCorePopulatedTable file:
import datetime
from datetime import datetime

def load_patients(name):
    # check the input value is a file name
    if not isinstance(name, str):
        raise ValueError(f"{name} is not a str file_name: input name should be your file name")
    pat = [] #set the initial list
    data_table = {} #set the initial dictionary
    #read in data with time efficiency O(n^2+n+2)===>O(n^2)
    with open(name) as stream:
        data_lines = stream.readlines() #(one assignment dropped)
        #split the lines at first row
        pat = data_lines[0].split() #(one assignment dropped)
        # (n assignment for this loop)
        for i in pat: 
            data_table[i]=[] 
        # (O(n^2) assignment)
        for j in data_lines[1:]:
            line_data = j.split('\t')
            for n in range(0, len(pat)):
                data_table[pat[n]].append(line_data[n])
                
    
    return data_table['PatientDateOfBirth']

patients = load_patients('PatientCorePopulatedTable.txt')


def num_older_than(patients, age):
    #check the input patients is a suffieicent list with patiens birth date
    if not isinstance(patients, list):
        raise ValueError(f"{patients} is not a sufficient list contains patients birth_date")
    for i in range(len(patients)):
        if not isinstance(patients[i], str):
            raise ValueError(f"{patients[i]} is not a string of birth_date of patient")
    #check the input age is a sufficient number
    if not (isinstance(age, float) or isinstance(age, int)):
        raise ValueError(f"input_value:age {age} is not a sufficient number value")
    birth = patients
    
    date_format = '%Y-%m-%d %H:%M:%S.%f'
    for i in range(0, len(birth)): #change the format: string to date_format
        birth[i] = datetime.strptime(birth[i], date_format)
    
    current_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')
    #change the date_string to date_value
    current_date = datetime.strptime(current_date, date_format)

    count = 0 #index (recording satisfied number of patients)
    
    for i in range(len(birth)):
        delta = current_date - birth[i] #calculate the date difference
        year_difference = delta.days/365.25
        if year_difference > age: 
         count = count + 1
    return count

#-----------------------------------------
#for LabsCorePopulatedTable file:
def load_labs(name):
    if not isinstance(name, str):
        raise ValueError(f"input_value:file_name {name} is not a sufficient file_name string value")
    lab = {} # set initial_dictionary
    keylab = [] # set initial_list
#read in data: using the dictionary to readin data one line by one line
# time efficiency (O(n^2))
    with open(name) as stream:
        datalines = stream.readlines()
        keylab = datalines[0].split()
        for i in keylab:
            lab[i] = []
        for j in datalines[1:]:
            line_data = j.split('\t') #seperate by tab
            for m in range(len(keylab)):
                lab[keylab[m]].append(line_data[m])
    pati_id = lab['\ufeffPatientID']
#find the lab_name value from dictionary: lab
    lab_name = lab['LabName']
#find the test_value from dictionary: lab
#change the string type to float
    lab_value = lab['LabValue']
    for i in range(0, len(lab_value)):
        lab_value[i] = float(lab_value[i])
    infor = []
    infor = [pati_id, lab_name, lab_value]
    return infor

lab_infor = load_labs('LabsCorePopulatedTable.txt')

def sick_patients(lab_infor, lab, gt_lt, value): #time efficiency(O(n))
    if not isinstance(lab_infor, list):
        raise ValueError(f"input_value:lab_information {lab_infor} is not a sufficient list")
    sick = [] #define an initial list to store sick_patients id
    pati_id = lab_infor[0]
    lab_name = lab_infor[1]
    lab_value = lab_infor[2]
    for k in range(len(lab_name)):
        if lab == lab_name[k]:
            if gt_lt == '>' and lab_value[k] > value:
                sick.append(pati_id[k])
            elif gt_lt == '<' and lab_value[k] < value:
                sick.append(pati_id[k])
    return set(sick)

def get_age(birth):
    if not isinstance(birth, str):
        raise ValueError(f"input_value:birth {birth} is not a sufficient string_of_birthdate")
    #define the date_format
    date_format = '%Y-%m-%d %H:%M:%S.%f'
    #change the birth variable_format string->date_variable
    birth = datetime.strptime(birth, date_format)

    #get the current date:
    current_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')
    current_date = datetime.strptime(current_date, date_format)
    #get the date difference
    day_diff = current_date - birth
    age = day_diff.days/365.25
    age = round(age, 2)
    return (age)

if __name__ == '__main__':
    print(num_older_than(patients, 51.2)) #====> 75
    print(len(sick_patients(lab_infor, "METABOLIC: ALBUMIN", ">", 4.0))) #=====> 100
    print(get_age("1952-01-18 19:51:12.917000"))
    print(len(load_labs('LabsCorePopulatedTable.txt')))
    print(len(load_labs('LabsCorePopulatedTable.txt')[0]))

