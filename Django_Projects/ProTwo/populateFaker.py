import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

#Fake Pop Script
import random
from AppTwo.models import AccessRecord,WebPage,Topic
from faker import Faker

fakegen =  Faker()
topics = ['Search', 'Social', 'Marketplace','News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        #get the topic for entry
        top = add_topic()

        #Create the fake data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create new WebPage
        webpg = WebPage.objects.get_or_create(topic=top,url_name=fake_url,name=fake_name)[0]

        #create fake access record
        acc_rec = AccessRecord.objects.get_or_create(name = webpg,date=fake_date)[0]



if __name__ == '__main__':
    print('Populating script...')
    populate(20)
    print('Populating complete')
