import json
import csv

with open('devasc/eugenio_devops/PartB/covid_cases.json','r') as json_file:
    covid_json = json.load[json_file]

with open('cov_cases.csv', 'w') as cov_write:
    file = csv.writer(cov_write)
    file.writerow["dateRep", "countriesandTerritories", "cases","deaths"]

    for parsing in covid_json['records']:
        file.writerow([parsing['dateRep'], parsing['countriesandTerritories'], parsing['cases'],parsing['deaths']])