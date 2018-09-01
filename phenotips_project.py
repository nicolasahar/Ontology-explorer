import requests
from pprint import pprint as pp

###  Complete functions ###

def get_patients(url):
    """ Return the patient records (in JSON format) from the PhenoTips
    instance at url."""

    response = requests.get(url, headers={'Accept': 'application/json'})
    return response.json()

## Testing get_patients ##
#print(get_patients('https://playground.phenotips.org/rest/patients'))

def get_patient(url, pid):
    """ Return the patient record (in JSON format) for patient pid from
    the PhentoTips instance at url."""

    response = requests.get(url + '/' + pid)
    return response.json()

## Testing get_patient ##
#print(get_patient('https://playground.phenotips.org/rest/patients', 'P0000199'))

def add_patient(url, patient):
    """ Add patient (in JSON format) to the PhenoTips instance at url. """
    response = requests.post(url, 
                            headers={'Content-Type': 'application/json'}, 
                            json=patient)
    return response


### Part 1: Your tasks ###

def get_patients_range(url, start, stop):
    """ Counting from the first existing record, return a JSON object with patients
    from the record start to the record stop for the PhenoTips instance at url.

    Note: some records from the PhenotIps instance may have been deleted, so the
    first and last records returned will likely have a higher IDs than the given
    start and stop positions.
    """
    full_list = get_patients(url)
    pt_list = full_list['patientSummaries']

    pt_id_list = []

    for entry in pt_list:
        for key in entry:
            if key == "id":
                pt_id_list.append(entry[key])

    answer_list = []
    for i in range(start, stop + 1):
        answer_list.append(get_patient(url, pt_id_list[i]))

    return answer_list

## Testing get_patients_range ##
#print(get_patients_range('https://playground.phenotips.org/rest/patients', 2, 10))

def delete_patient(url, pid):
    """ Delete patient with patient id pid from PhenotTips instance url.
    """
    response = requests.delete(url + '/' + pid)

    return response

## Testing delete_patient ##
#print(delete_patient('https://playground.phenotips.org/rest/patients', "P0000054"))

def get_phenotypic_info(patient):
    """ Given a patient's JSON representation, return a list of the phenotypic 
    features recorded for this patient.
    """
    feature_list = []

    for feature in patient["features"]:
        if feature["type"] == "phenotype":
            feature_list.append(feature["label"])

    return feature_list

## Testing get_phenotypic_info ##
#print(get_phenotypic_info(get_patient('https://playground.phenotips.org/rest/patients', 'P0000017')))

if __name__ == '__main__':

    url = 'https://playground.phenotips.org/rest/patients'

    # Get all patient records (response capped at 50 records) from the PhenoTips
    # playground in JSON format.
    #patients = get_patients(url)
    #pp(patients)

    # Print patient record for patient P0000055.
    #pp(get_patient(url, 'P0000065'))

    # Print the 10th to 15th records in the PhenoTips playground.
    #pp(get_patients_range(url, 10, 25))

    # patient_record = {"clinicalStatus": "affected",
    #  "patient_name": {"last_name": "Ng", "first_name": "Taylor"}, 
    #  "sex": "F", 
    #  "solved": {"status": "unsolved"} }
    #print(add_patient(url, "P0000055"))

    # Get the phenotypic features recorded for patient with pid 'P0000114'.
    #print(get_phenotypic_info(get_patient(url, 'P0000114')))

    # Delete a record (pick an id that exists in the PhenoTips playground), 
    # not 'P0006109' which is being used as a placeholder.
    #print(delete_patient(url, 'P0000055'))

