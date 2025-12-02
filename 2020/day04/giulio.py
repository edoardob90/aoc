good_ids = 0
valid_ids = 0
field_list = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]  # For now this is commented ,"cid"]

def check_year(field, min_year, max_year):
    try:
        if min_year <= int(field) <= max_year:
            return True
        else:
            return False
    except:
        return False

def check_hgt(field):
    try:
        if field[-2:] == "cm":
            if 150 <= int(field[:-2]) <= 193:
                return True
            else:
                return False
        if field[-2:] == "in":
            if 59 <= int(field[:-2]) <= 76:
                return True
            else:
                return False
    except:
        return False

def check_hcl(field):
    if field[0] == "#" and field[1:].isalnum():
        return True
    else:
        return False

def check_ecl(field):
    if field in ["amb","blu","brn","gry","grn","hzl","oth"]:
        return True
    else:
        return False

def check_pid(field):
    if len(field) == 9 and field.isdigit():
        return True
    else:
        return False



with open("input.txt") as f:
    for line in f:
        ll = line.split()
        current_id = {}
        field_values = []
        while len(ll) != 0:
            for field in ll:
                key = field.split(":")[0]
                value = field.split(":")[1]
                current_id[key] = value
            line = f.readline()
            ll = line.split()
        
        result =  all(elem in current_id  for elem in field_list)
        if result:
            good_ids += 1
            if check_year(current_id["byr"],1920,2002):
                if check_year(current_id["iyr"],2010,2020):
                    if check_year(current_id["eyr"],2020,2030):
                        if check_hgt(current_id["hgt"]):
                            if check_hcl(current_id["hcl"]):
                                if check_ecl(current_id["ecl"]):
                                    if check_pid(current_id["pid"]):
                                        valid_ids += 1



print("There are", good_ids, "IDs with all fields")
print("There are", valid_ids, "valid IDs")
