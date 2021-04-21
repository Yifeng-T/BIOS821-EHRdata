# how to run the file:
We need a main.sh file including:  
<br>
export $(egrep -v '^#' .env | xargs)  
<br>
uvicorn ehr_analysis:APP --host 0.0.0.0 --port 8105 --reload
<br>  
Then we run: chmod +x main.sh in terminal
<br>
run: ./main.sh in terminal

# There are some functions of this file:

* uploading patients and labs files by providing URLs
```bash
> curl -X POST http://localhost/patients -d "{\"url\": \"http://biostat821.colab.duke.edu/patients.txt\"}"
> curl -X POST http://localhost/labs -d "{\"url\": \"http://biostat821.colab.duke.edu/labs.txt\"}"
```

* accessing specific patients by providing their ids
  ```bash
  > curl -X GET http://localhost/patients/FB2ABB23-C9D0-4D09-8464-49BF0B982F0F
  {
    "gender": "Male",
    "DOB": "1947-12-28 02:45:40.547",
    "race": "Unknown",
    "marital_status": "Married",
    "language": "Icelandic",
    "population_percentage_below_poverty": 18.08
  }
  ```

* accessing labs belonging to each patient
  ```bash
  > curl -X GET http://localhost/patients/FB2ABB23-C9D0-4D09-8464-49BF0B982F0F/labs
  [
    {
      "admission_id": 1,
      "name": "URINALYSIS: RED BLOOD CELLS",
      "value": 3.1,
      "units": "rbc/hpf",
      "datetime": "1968-10-07 14:41:30.843"
    },
    ...
  ]
  ```

* other analytics capabilities
  ```bash
  > curl -X GET http://localhost/num_older_than?age=51.2
  54
  > curl -X GET http://localhost/sick_patients?lab_name=METABOLIC%3A%20ALBUMIN&operator=%3C&lab_value=4.0
  ["FB2ABB23-C9D0-4D09-8464-49BF0B982F0F", "64182B95-EB72-4E2B-BE77-8050B71498CE"]
  ```



