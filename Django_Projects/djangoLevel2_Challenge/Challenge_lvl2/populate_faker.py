import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Challenge_lvl2.settings')

import django
django.setup()

#Fake Pop Script
from my_app.models import User
from faker import Faker

fakegen =  Faker()


#Add first name and last name
def populate(N=5):

    for entry in range(N):
        #Create the fake data for entry
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name  =fake_name[1]
        fake_email = fakegen.email()

        #New Entry
        user = User.objects.get_or_create(first_name=fake_first_name,
                                          last_name=fake_last_name,
                                          email=fake_email)[0]


if __name__ == '__main__':
    print('Populating databases...')
    populate(20)
    print('Populating complete')
