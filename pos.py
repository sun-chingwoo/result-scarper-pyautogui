import csv

nine5=0
nine = 0    
eight5 = 0  
eight = 0   
seven5 = 0  
seven = 0   

with open("usn.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        sgpa = float(row["SGPA"])  # convert string to float

        if sgpa >= 9.5:
            nine5 += 1
        elif 9.0 <= sgpa < 9.5:
            nine += 1
        elif 8.5 <= sgpa < 9.0:
            eight5 += 1
        elif 8.0 <= sgpa < 8.5:
            eight += 1
        elif 7.5 <= sgpa < 8.0:
            seven5 += 1
        elif 7.0 <= sgpa < 7.5:
            seven += 1

print(f"People with SGPA >= 9.5: {nine5}")
print(f"People with 9.0 <= SGPA < 9.5: {nine}")
print(f"People with 8.5 <= SGPA < 9.0: {eight5}")
print(f"People with 8.0 <= SGPA < 8.5: {eight}")
print(f"People with 7.5 <= SGPA < 8.0: {seven5}")
print(f"People with 7.0 <= SGPA < 7.5: {seven}")