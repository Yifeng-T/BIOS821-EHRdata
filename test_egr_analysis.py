from ehr_analysis import num_older_than
from ehr_analysis import load_patients
from ehr_analysis import patients
from ehr_analysis import lab_infor
from ehr_analysis import sick_patients
from ehr_analysis import get_age
from ehr_analysis import load_labs


def test_num_older_than():
    assert num_older_than(
        patients, 50,
        ) == 77, "Computated value is incorrect"

def test_load_patients():
    assert (load_patients
    ('PatientCorePopulatedTable.txt'))[0] == '1947-12-28 02:45:40.547', "Computated value is incorrect"

def test_get_age():
    assert (get_age('1952-01-18 19:51:12.917000')) == 69.08, "Computated value is incorrect"

def test_sick_patients():
    assert len(sick_patients(
        lab_infor, "METABOLIC: ALBUMIN", ">", 4.0,
        )) == 100, "Computated value is incorrect"

def test_load_labs():
    assert len(load_labs('LabsCorePopulatedTable.txt')) == 3, "input_value has insufficient # of items"
    assert len(load_labs('LabsCorePopulatedTable.txt')[0]) == 111483, "input value missis some data"
    assert load_labs('LabsCorePopulatedTable.txt')[1][2] == 'CBC: MCH'