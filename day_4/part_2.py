import re
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

print(passports_stripped)

def solve():
    n_valid_passports = 0

    for passport in passports:     
        if (set(keys).issubset(set(re.findall("[a-z]{3}:", passport)))):
            n_valid_passports += 1

    return n_valid_passports