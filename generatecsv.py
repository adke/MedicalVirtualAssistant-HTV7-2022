import csv

def subsets(my_set):
    result = [[]]
    for x in my_set:
        result = result + [y + [x] for y in result]
    return result

diagnoses = ["flu", "cold", "malaria", "salmonella"]

symptoms = [
    ["fever", "chill", "cough", "sore", "throat", "runny", "nose", "stuffy", "ache", "headache", "fatigue", "nausea", "vomiting", "diarrhea"],
    ["cough", "sore", "throat", "runny", "nose", "stuffy", "congestion", "headache", "mild", "ache", "sneeze", "fever"],
    ["fever", "chill", "headache", "nausea", "vomiting", "diarrhea", "abdominal", "pain", "muscle", "joint", "fatigue", "rapid", "breathing", "heartrate" "heart" "rate", "cough"],
    ["diarrhea", "stomach", "cramps", "fever", "nausea", "vomiting", "chill", "headache"]
]

output = []

for i, diagnosis in enumerate(diagnoses):
    for l in output:
        for symptom in l[0]:
            if symptom not in symptoms[i]:
                break
        else:
            l[1].append(diagnosis)
        
    lists = subsets(symptoms[i])
    for l in lists:
        if len(l) > 0:
            output.append([l, [diagnosis]])

for i in range(len(output)):
    output[i] = [",".join(symptom for symptom in output[i][0]), ",".join(diagnosis for diagnosis in output[i][1])]

with open("data.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["symptoms", "diagnoses"])
    writer.writerows(output)

# print(output)