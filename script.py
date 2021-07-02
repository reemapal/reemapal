root@lifebook-a555:~/hackthon# cat fake.py 
import csv
from faker import Faker
import datetime

def datagenerate(records, headers):
    fake = Faker('en_US')
    with open("People_data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            full_name = fake.name()
            FLname = full_name.split(" ")
            Fname = FLname[0]
            Lname = FLname[1]
            domain_name = "@testDomain.com"
            userId = Fname +"."+ Lname + domain_name
            
            writer.writerow({
                    "Email Id" : userId,
                    "Prefix" : fake.prefix(),
                    "Name": fake.name(),
                    "Birth Date" : fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1,1)),
                    "Date of Joining" : fake.date(pattern="%d-%m-%Y"),
                    "Designation" : fake.job(),
                    })

if __name__ == '__main__':
    records = 100
    headers = ["Email Id", "Prefix", "Name", "Birth Date","Date of Joining", 
                "Designation"]
    datagenerate(records, headers)
    print("CSV generation complete!")

