import sqlite3
import requests
import urllib.request
import uvicorn
import httpx
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


APP = FastAPI()

class Patient(BaseModel):
    Id: str
    gender: str
    DOB: str
    race: str
    Material: str
    Language: str

class Lab(BaseModel):
    lab_name: str
    lab_value: float

class URL(BaseModel):
    url: str

connection = sqlite3.connect('biostat821.db')
cur = connection.cursor()


# create table if not exists
cur.execute('''CREATE TABLE IF NOT EXISTS patient(PatientID text, PatientGender text, PatientDateOfBirth text, \
    PatientRace text, PatientMaritalStatus text, PatientLanguage text, PatientPopulationPercentageBelowPoverty flow)''')

cur.execute('''CREATE TABLE IF NOT EXISTS lab(PatientID text, AdmissionID int, LabName text, LabValue flow, \
    LabUnits text, LabDateTime text)''')
connection.commit()
connection.close()

@APP.post("/patients")
def add_patients(link: URL):
    with urllib.request.urlopen(link.url) as fr:
        table1=[]
        for line in fr:
            line=line.decode('utf-8')
            row=line.strip('\r\n').replace('\t',',')
            table1.append(row.split(','))

    connection=sqlite3.connect("biostat821.db")
    cursor=connection.cursor()
    cursor.executemany('INSERT INTO patient VALUES (?, ?, ?, ?, ?, ?, ?)', table1)
    connection.commit()
    connection.close()
    return "Succeed!"

@APP.post("/labs")
def add_labs(link: URL):
    with urllib.request.urlopen(link.url) as gr:
        table2  = []
        for line in gr:
            line=line.decode('utf-8')
            row=line.strip('\r\n').replace('\t',',')
            table2.append(row.split(','))

    connection=sqlite3.connect("biostat821.db")
    cursor=connection.cursor()
    cursor.executemany('INSERT INTO lab VALUES (?, ?, ?, ?, ?, ?)', table2)
    connection.commit()
    connection.close()
    return "Succeed!"


@APP.get("/")
def handle_slash():
    """Handle root."""
    return "Hello world!"


def get_person(id: str):
    """Get person by Id"""
    connection=sqlite3.connect("biostat821.db")
    cursor=connection.cursor()
    cmd=f"SELECT * from patient where PatientID='{id}'"
    cursor.execute(cmd)
    lis = cursor.fetchone() #get the first item in cursor output
    if len(lis) == 0:
        raise HTTPException(404, "No Observation found")
    connection.close()
    lis={"PatientID":lis[0], "PatientGender":lis[1], "PatientDateOfBirth":lis[2], \
        "PatientRace":lis[3], "PatientMaritalStatus":lis[4], "PatientLanguage":lis[5]}
    connection.close()
    return lis

@APP.get("/patients/{id}/labs")
def get_lab_data(id:str):
    """Get person lab_info by id"""
    #empty table to store the lab_data
    lab_info = []
    connection=sqlite3.connect("biostat821.db")
    cursor=connection.cursor()
    cmd=f"SELECT * from lab where PatientID='{id}'"
    cursor.execute(cmd)
    for item in cursor.fetchall():
        lab_info.append({"AdmissionID":item[1], "LabName":item[2], "LabValue":item[3], \
            "LabUnits":item[4], "LabDateTime":item[5]})
    connection.close()
    if len(lab_info) == 0:
        raise HTTPException(404, "No lab_value found")
    return lab_info

@APP.get("/num_older_than")
def num_older_than(age: float):
    count = 0
    connection=sqlite3.connect("biostat821.db")
    cursor=connection.cursor()
    cmd="SELECT PatientDateOfBirth from patient"
    cursor.execute(cmd)
    date_format = '%Y-%m-%d %H:%M:%S.%f'
    current_date = datetime.today().strftime(date_format)
    current_date = datetime.strptime(current_date, date_format)

    for item in cursor.fetchall()[1:]:
        item = datetime.strptime(item[0], date_format)
        total_age = current_date - item
        patient_age = round(total_age.days/365.25, 2)
        if patient_age > age:
           count = count + 1

    connection.close()
    return count

@APP.get("/sick_patients")
def find_sick_patients(lab_name:str, operator:str, lab_value:float):
    connection=sqlite3.connect("biostat821.db")
    cursor=connection.cursor()

    cmd=f"SELECT PatientID from lab WHERE LabName='{lab_name}'"
    cursor.execute(cmd)

    patient_list=[] #empty list

    for item in cursor.fetchall():
        if (operator == '<'): 
            if item[1] < lab_value:
                patient_list.append(item[0])
        else:
            if item[1] > lab_value:
                patient_list.append(item[0])
    connection.close()
    return list(set(patient_list))








