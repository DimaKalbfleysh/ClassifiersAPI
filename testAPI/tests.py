from django.test import TestCase
import re

# Create your tests here.
# unreadable_characters = ['@', '#', '%', '^', '&', '*', '(', ')', '-', '+', '=', '/', ';', ':', '|', '<', '>', '~', '№', '_']
unreadable_characters = '@#%^&*()-+=/;:|<>~№_'
a = 'Hello%#$%^()World'
for i in a:
    if i in unreadable_characters:
        print(1)
