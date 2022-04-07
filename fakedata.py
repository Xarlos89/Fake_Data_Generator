from faker import Faker
#### #### #### #### 
#### For other locals, see the Docs. 
#### https://faker.readthedocs.io/en/master/locales.html


#### Set the Local preferences
# fake = Faker(['de_AT']) # Austrians
fake = Faker(['en_US']) # Americans
# fake = Faker(['ja-JP']) # Japanese
# fake = Faker(['en_GB']) # British

#### Apply variables
firstName = fake.first_name()
lastName = fake.last_name()
email = fake.ascii_email()
houseNumber = fake.builidng_number()
street = fake.street_name()
postalCode = fake.postcode()
city = fake.city()
phone = fake.msisdn()
socialNumber = fake.ssn()

# Pretty print a fake person
print('Name: {} {}\nEmail: {}\nStreet: {}\nHouse Number: {}\nCity: {} {}\nPhone Number: {}\nSocial Security Number: {}\n'.format(firstName,lastName,email,street,houseNumber,city,postalCode,phone,socialNumber))












