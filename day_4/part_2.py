import re
from re import search
import numpy as np

passports = []
keys = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

with open('input.txt', encoding = 'UTF-16') as f:
    lines = f.read()
    passports = lines.split('\n\n')

passports_stripped = []

for passport in passports:
    passport = passport.replace('\n', ' ')
    passports_stripped.append(passport)

passport_dict = []

for ps in passports_stripped:
    passport_dict.append(dict(x.split(':') for x in ps.split(' ')))


#print(passport_dict[0].values())
def solve():

    n_valid_passports = 0
        
    for ps in passport_dict:

        n_valid_fields = 0

        if 'byr' in ps:
            if 1920 <= int(ps['byr']) <= 2002: n_valid_fields += 1
        if 'iyr' in ps:
            if 2010 <= int(ps['iyr']) <= 2020: n_valid_fields += 1
        if 'eyr' in ps:
            if 2020 <= int(ps['eyr']) <= 2030: n_valid_fields += 1
        if 'hgt' in ps:
            if re.search("[0-9]{3}cm", ps['hgt']) != None:
                if 150 <= int(ps['hgt'][:-2]) <= 193: n_valid_fields += 1
            elif re.search("[0-9]{2}in", ps['hgt']) != None:
                if 59 <= int(ps['hgt'][:-2]) <= 76: n_valid_fields += 1
        if 'hcl' in ps:
            if re.search("#([0-9]|[a-f]){6}", ps['hcl']) != None:
                 if len(ps['hcl']) == 7: n_valid_fields += 1
        if 'ecl' in ps:
            if (ps['ecl'] == 'amb' or ps['ecl'] == 'blu' or ps['ecl'] == 'brn' or ps['ecl'] == 'gry' or ps['ecl'] == 'grn' or ps['ecl'] == 'hzl' or ps['ecl'] == 'oth'):
                n_valid_fields += 1
        if 'pid' in ps:
            if re.search("[0-9]{9}", ps['pid']) != None:
                if len(ps['pid']) == 9: n_valid_fields += 1

    
        if n_valid_fields == 7:
            n_valid_passports += 1

    
    return n_valid_passports


output = solve()
print(output)


    

