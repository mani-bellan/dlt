import dlt

# We now use duckdb, but you can switch to Bigquery later
pipeline = dlt.pipeline(pipeline_name="append_pipeline",
						destination='duckdb', 
						dataset_name='sample_data')
data = []
def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

for person in people_1():
    data.append(person)
    print(data)


def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}


for person in people_2():
    data.append(person)
    print(data)
    #print(person)

info = pipeline.run(data, 
                    table_name="users", 
                    write_disposition="append")
print(info)