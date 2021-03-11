from ehr_analysis3 import Patient
from ehr_analysis3 import Observation
from ehr_analysis3 import lab
from ehr_analysis3 import pd
from ehr_analysis3 import pdic

def test_patient():
    patient1 = Patient("1A8791E3-A61C-455A-8DEE-763EB90C9B2C", "Male", \
        "1947-01-18 19:51:12.917000", "african")
    patient2 = Patient("220C8D43-1322-4A9D-B890-D426942A3649", "Female", \
        "1957-01-18 19:51:12.917000", "african")
    assert patient1.age == 74.14

    assert patient2.age == 64.14
    assert pdic['FB2ABB23-C9D0-4D09-8464-49BF0B982F0F'].age == 73.2
    assert pdic['DB92CDC6-FA9B-4492-BC2C-0C588AD78956'].age == 43.7