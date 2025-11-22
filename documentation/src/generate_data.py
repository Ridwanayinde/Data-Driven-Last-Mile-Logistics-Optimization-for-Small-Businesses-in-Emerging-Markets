from faker import Faker
import pandas as pd
import numpy as np

fake = Faker("en_NG")
print(fake.name())


# ----1. Customers ----

num_customers = 100

customers = []

for i in range (num_customers):
    customers.append ({ "customer_id": i+1,  
    "name": fake.name(),
    "address":fake.name().replace("\n", ", "),
    "latitude": fake.latitude(),
    "longitude":fake.longitude ()
                        
})
        
#customers_df = pd.DataFrame(customers)

# ---2. Orders -----
num_orders = 200
orders = []

for i in range (num_orders):
    customer = customers_df.sample

