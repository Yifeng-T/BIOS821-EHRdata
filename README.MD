ehr_analysis instructions: for biostat821 assignment

--------------------------------------------------------------
For endusers:
There are total five functions, they are:
1.load_patients(name)  
2.num_older_than(patients, age) 
3.load_labs(name) 
4.sick_patients(lab_infor, lab, gt_lt, value)
5.get_age(birth)

1.for load_patients(name):
The function input value should be a string value, which indicates the file name.
And the function produces a list of datebirth of patients whose information are in the "name" file

example:
load_patients('PatientCorePopulatedTable.txt')[0] =====> '1947-12-28 02:45:40.547'

2.num_older_than(patients, age):
The function input values should be a: exact patients variable (which is defined by load_patients function with given file) and b: a number value. The function produces the number of patients in the file you given with whose age are greater than the value age. 

example:
print(num_older_than(patients, 51.2)) ====> 75

3.load_labs(name):
The function input value should be a string value, which indicates the file name.
And the function produces a list contains three lists. The first list contains the patients_id(string value), the second list contains patients_lab_name, and the third list contains the patients_lab_result(result is a numeric value). 

example:
print(len(load_labs('LabsCorePopulatedTable.txt'))) =====> 3
print(len(load_labs('LabsCorePopulatedTable.txt')[0])) =======> 111483
print(load_labs('LabsCorePopulatedTable.txt')[0][0]) =========> '1A8791E3-A61C-455A-8DEE-763EB90C9B2C'


4.sick_patients(lab_infor, lab, gt_lt, value):
The function produces all the patients_ids in the given file whose specific lab test results satisfy gt_lt the value variable. 
The function input values have 4 variables, a: lab_infor is a list produced by function: load_labs, b:lab is a string value, which indicates which lab you are interested, c: a string value '>' or '<', indicates you want to know the patients results greater or less than given value. d:value should be a number value.

example:
print(len(sick_patients(lab_infor, "METABOLIC: ALBUMIN", ">", 4.0))) =====> 100


5.get_age(birth):
The function calculates the age given a birth_date, the birth should be a string value with:
'%Y-%m-%d %H:%M:%S.%f' date format. 


-----------------------------------------------
For contributors:
there are some tests in test_egr_analysis file. 



