#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
count = 0
maxPay = 0
poi = ''
# print(len(enron_data.keys()))
print(enron_data["SKILLING JEFFREY K"])
"""
for key in enron_data.keys():
    if key != 'TOTAL':
        print enron_data[key]["total_payments"]
        if math.isnan(float(enron_data[key]["total_payments"])):
            pass
        else:
            if enron_data[key]["total_payments"] > maxPay:
                maxPay = enron_data[key]["total_payments"]
                poi = key

print('the biggest theif is', poi, 'with total payments=', maxPay)
"""

hasSalary = 0
hasEmail = 0
total = 0
percentage = 0
#count = len(enron_data)
count = 0

print(count)
for key in enron_data.keys():

    if key != 'TOTAL':
        #print(enron_data[key]["email_address"])
        if enron_data[key]["poi"] == True:
            count = count + 1
            if math.isnan(float(enron_data[key]["total_payments"])):
                total = total + 1
            else:
                pass
                """
                if enron_data[key]["email_address"] == 'NaN':
                    pass
                else:
                    hasEmail = hasEmail + 1

    print('has salary:', hasSalary)
                """
percentage = total/count

print('Nan total_payments:', total)
print('percentage of NaN total_payments', percentage)

#print(len(enron_data["poi"] == True))

#print("There are ", count, "POIs")
