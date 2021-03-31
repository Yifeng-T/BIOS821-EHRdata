from ehr4_sql import Patient
from ehr4_sql import Observation
from ehr4_sql import con
from ehr4_sql import cur


def test_patient_sql():
    patient1 = Patient(cur, "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F")
    patient2 = Patient(cur, "220C8D43-1322-4A9D-B890-D426942A3649")
    assert patient1.gender == "Male"
    assert patient2.Age == 50.05

def test_observation_sql():
    observation1 = Observation(cur, 'DB92CDC6-FA9B-4492-BC2C-0C588AD78956')
    observation2 = Observation(cur, 'FB2ABB23-C9D0-4D09-8464-49BF0B982F0F')
    assert observation2.value[0][0] == 3.1
    assert observation1.units[5][0] == "gm/dL"