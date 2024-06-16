import dlt

#Configuring Pipeline properties
pipeline = dlt.pipeline(pipeline_name="college_pipeline",
						destination='duckdb')

data = [
{
    "collegid":1,
    "college": "First college of Tech",
    "collegehead":"Mr.ABC",
    "address": {
        'state': 'TN',
        "country": "India"
    },
    "Department": [
        {"name": "IT", "head": "IT Head", "students": 500},
        {"name": "Civil", "head": "Civil Head", "students": 500},
        {"name": "Electronics", "head": "Electronics Head", "students": 500}
    ]
}
]

# Run `dlt` pipeline
info = pipeline.run(data, 
                    table_name="college", 
                    write_disposition="merge", 
					primary_key="collegid")

print(info)