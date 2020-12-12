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

regexs = [
    "byr:19[2-9][0-9]|200[0-2]",
    "iyr:201[0-9]|2020",
    "eyr:202[0-9]|2030",
    "hgt:((1[5-8][0-9]|19[0-3])cm)|hgt:(59|6[0-9]|7[0-6])in",
    "hcl:#[0-9a-f]{6}",
    "ecl:(amb|blu|brn|gry|grn|hzl|oth)",
    "pid:[0-9]{9}"
]

#print(passports_stripped)

def solve():
    n_valid_passports = 0
    for passport in passports_stripped:
        n_valid_fields = 0
        print(passport)
        for regex in regexs:
            match = re.search(regex, passport)
            print(match)
            if (match != None):
                n_valid_fields += 1

        print(n_valid_fields)
        if (n_valid_fields == 7):
            n_valid_passports += 1
    

    return n_valid_passports
            
output = solve()
print(output)
