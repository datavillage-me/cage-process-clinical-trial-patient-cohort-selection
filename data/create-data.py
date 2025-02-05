import duckdb
import random 
from random import randrange
import pandas as pd

from duckdb.typing import *
from faker import Faker
import hashlib



def random_ssn(n):
    return str(n).zfill(10)

def user_hash(n):
    return hashlib.sha256(str.encode(str(n).zfill(10))).hexdigest()


def random_age(n):
    return random.randrange(20, 60)

def random_gender(n):
    i=random.randint(0, 1)
    data=["male","female"]
    return data[i]
    
def random_city(n):
    fake = Faker('nl_BE')
    return fake.city()

def random_income_level(n):
    i=random.randrange(0, 3)
    data=["middle","low","high"]
    return data[i]

def random_education_level(n):
    i=random.randrange(0, 3)
    data=["high_school","college","university"]
    return data[i]

def random_employment_status(n):
    i=random.randrange(0, 4)
    data=["employed","student","unemployed","retired"]
    return data[i]

def random_medical_problem(n):
    i=random.randrange(0, 29)
    data = [
    "Arthritis",
    "Asthma",
    "Bronchitis",
    "Cancer",
    "Diabetes",
    "Eczema",
    "Fibromyalgia",
    "Gout",
    "Hypertension",
    "Insomnia",
    "Jaundice",
    "Kidney Stones",
    "Lupus",
    "Migraine",
    "Neuropathy",
    "Obesity",
    "Parkinson's Disease",
    "Quinsy",
    "Rheumatism",
    "Sinusitis",
    "Tuberculosis",
    "Ulcer",
    "Vertigo",
    "Whooping Cough",
    "Xerostomia",
    "Yellow Fever",
    "Zika Virus",
    "Anemia",
    "Appendicitis"
]
    return data[i]

def random_medical_medication(n):
    i=random.randrange(0, 30)
    data = [
    "Aspirin",
    "Ibuprofen",
    "Paracetamol",
    "Lisinopril",
    "Metformin",
    "Simvastatin",
    "Levothyroxine",
    "Atorvastatin",
    "Amoxicillin",
    "Losartan",
    "Omeprazole",
    "Metoprolol",
    "Fluoxetine",
    "Atenolol",
    "Prednisone",
    "Gabapentin",
    "Warfarin",
    "Citalopram",
    "Escitalopram",
    "Doxycycline",
    "Tramadol",
    "Pregabalin",
    "Diazepam",
    "Alprazolam",
    "Hydrochlorothiazide",
    "Sertraline",
    "Lorazepam",
    "Zolpidem",
    "Cyclobenzaprine",
    "Phentermine",
    "Medrol"
]
    return data[i]

def random_medical_vaccine(n):
    i=random.randrange(0, 30)
    data = [
    "DTaP",
    "Hepatitis A",
    "Hepatitis B",
    "Hib",
    "HPV",
    "Influenza",
    "MMR",
    "Meningococcal",
    "Pneumococcal",
    "Polio",
    "Rotavirus",
    "Varicella",
    "Typhoid",
    "Yellow Fever",
    "Rabies",
    "Japanese Encephalitis",
    "Cholera",
    "Tetanus",
    "Diphtheria",
    "Pertussis",
    "Shingles",
    "Measles",
    "Mumps",
    "Rubella",
    "Hepatitis E",
    "Tick-Borne Encephalitis",
    "Bacillus Calmette-Guérin (BCG)",
    "Pertussis",
    "Smallpox",
    "COVID-19"
]
    return data[i]

# duckdb.create_function("ssn", random_ssn, [BIGINT], VARCHAR)
# duckdb.create_function("user_hash_from_ssn", user_hash, [BIGINT], VARCHAR)
# duckdb.create_function("age", random_age, [DOUBLE], INTEGER)
# duckdb.create_function("gender", random_gender, [DOUBLE], VARCHAR)
# duckdb.create_function("city", random_city, [DOUBLE], VARCHAR)
# duckdb.create_function("income_level", random_income_level, [DOUBLE], VARCHAR)
# duckdb.create_function("education_level", random_education_level, [DOUBLE], VARCHAR)
# duckdb.create_function("employment_status", random_employment_status, [DOUBLE], VARCHAR)

# duckdb.create_function("medical_problem", random_medical_problem, [DOUBLE], VARCHAR)
# duckdb.create_function("medical_medication", random_medical_medication, [DOUBLE], VARCHAR)
# duckdb.create_function("medical_vaccine", random_medical_vaccine, [DOUBLE], VARCHAR)


# res = duckdb.sql("COPY (SELECT ssn(i) as national_id, user_hash_from_ssn(i) as user_hash, age(random()) as age, gender(random()) as gender,city(random()) as location,income_level(random()) as income_level,education_level(random()) as education_level,employment_status(random()) as employment_status FROM generate_series(1, 100000) s(i)) TO 'data/demographic.parquet'  (FORMAT 'parquet')")

# res = duckdb.sql("COPY (SELECT ssn(i) as national_id, user_hash_from_ssn(i) as user_hash, medical_problem(random()) as medical_problem,medical_medication(random()) as medical_medication,medical_vaccine(random()) as medical_vaccine FROM generate_series(1, 100000) s(i)) TO 'data/patients.parquet'  (FORMAT 'parquet')")



#df = duckdb.sql("SELECT national_id from 'data/demographic.parquet' as demographic").df()
#print(df)

# df = duckdb.sql("SELECT * from 'data/demographic.parquet' as patients").df()
# print(df)

#res = duckdb.sql("COPY (SELECT national_id from 'data/demographic.json', age(random()) as age) TO 'data/patients.parquet' (FORMAT 'parquet')")

#create encrypted data
keys = ["GZs0DsMHdXr39mzkFwHwTHvCuUlID3HB","8SX9rT9VSHohHgEz2qRer5oCoid2RUAS"]
keyNames=["patient","citizen"]

res=duckdb.sql("PRAGMA add_parquet_key('"+keyNames[0]+"','"+keys[0]+"')")
res=duckdb.sql("COPY (SELECT * FROM './data/patients_clear.parquet') TO './data/patients.parquet' (ENCRYPTION_CONFIG {footer_key: '"+keyNames[0]+"'})")
df = duckdb.sql("SELECT * FROM read_parquet('data/patients.parquet', encryption_config ={footer_key: '"+keyNames[0]+"'})").df()
print (df)

res=duckdb.sql("PRAGMA add_parquet_key('"+keyNames[1]+"','"+keys[1]+"')")
res=duckdb.sql("COPY (SELECT * FROM './data/citizens_clear.parquet') TO './data/citizens.parquet' (ENCRYPTION_CONFIG {footer_key: '"+keyNames[1]+"'})")
df = duckdb.sql("SELECT * FROM read_parquet('data/citizens.parquet', encryption_config ={footer_key: '"+keyNames[1]+"'})").df()
print (df)


