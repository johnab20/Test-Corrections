#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 19:35:35 2024

@author: johnbutka
"""

#Part 2

#Number 1

def num_families(list):
    families = []
    for protein in list:
        family = protein.split('.')[0]
        families.append(family)
    return len(families)

proteins = ["PF13411.1", "PF12728.1", "PF01381.2",
            "PF00205.2", "PF10875.1", "PF05766.1",
            "PF00860.2", "PF10766.1", "PF11812.1"]

print('Number of unique families:', num_families(proteins))


#Number 2

def family_dictionary_maker(list):
    family_counts = {}
    for protein in list:
        family = protein.split('.')[0]
        if family in family_counts:
            family_counts[family] += 1
        else:
            family_counts[family] = 1
    return family_counts

print('Family Occurrences:', family_dictionary_maker(proteins))


#Number 3

def combine_dictionaries(dict1, dict2):
    combined_dict = {}
    all_keys = set(dict1.keys()).union(dict2.keys())
    
    for key in all_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        combined_dict[key] = (value1, value2)
    
    return combined_dict


#Part 3

dates_list = ["February 6, 1992", "February 18, 1992", "February 27, 1992",
              "September 6, 1994", "December 1, 1993"]

#Number 1

month_dict = {
    'January': '01', 'February': '02', 'March': '03',
    'April': '04', 'May': '05', 'June': '06',
    'July': '07', 'August': '08', 'September': '09',
    'October': '10', 'November': '11', 'December': '12'}


def ISO_format(dates):
    formatted_dates = []
    for date_string in dates:
        month_string, day_string, year_string = date_string.split()
        day = day_string.replace(',', '')
        if len(day) < 2:
            day = "0" + day
        month_num = month_dict[month_string]
        formatted_date = f"{year_string}-{month_num}-{day}"
        formatted_dates.append(formatted_date)
    return formatted_dates


test1 = ISO_format(dates_list)

def reverse(dates):
    converted = []
    for d in dates:
        y, m, d = d.split("-")
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        
        month_str = months[int(m) - 1]
        string_date = month_str + " " + str(int(d)) + ", " + y
        converted.append(string_date)
        
    return converted
        
#Number 2


def sort_dates(dates):
    formatted_dates = ISO_format(dates)
    formatted_dates.sort()
    sorted_dates = reverse(formatted_dates)
    
    
    
    return sorted_dates

t1 = sort_dates(dates_list)

