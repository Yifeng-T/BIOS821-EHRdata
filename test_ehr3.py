from ehr_analysis3 import Patient
from ehr_analysis3 import Observation

def test_patient():
    patient1 = Patient("1A8791E3-A61C-455A-8DEE-763EB90C9B2C", "Male", \
        "1947-01-18 19:51:12.917000", "african")
    patient2 = Patient("220C8D43-1322-4A9D-B890-D426942A3649", "Female", \
        "1957-01-18 19:51:12.917000", "african")
    assert patient1.age == 74.14

    assert patient2.age == 64.14

    