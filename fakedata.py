from faker import Faker


# fake = Faker(['de_AT']) # Austrians
fake = Faker(['en_US']) # Americans
firstName = fake.first_name()
lastName = fake.last_name()
email = fake.ascii_email()
houseNumber = fake.building_number()
street = fake.street_name()
postalCode = fake.postcode()
city = fake.city()
phone = fake.msisdn()
socialNumber = fake.ssn()


print('Name: {} {}\nEmail: {}\nStreet: {} {}\nCity: {} {}\nPhone Number: {}\nSocial Security Number: {}\n'.format(firstName,lastName,email,houseNumber,street,stadt,plz,phone,steuernummer))












