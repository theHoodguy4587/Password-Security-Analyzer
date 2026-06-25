import csv
from rules import check_strength

with open("test_passwords.txt","r") as f:
    passwords = f.read().splitlines()

with open("Reports/report.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Password","Score","Level","Issues","Entropy"])
    for password in passwords:
        result = check_strength(password)
        print(f"Password: {password}, Score: {result['score']}, Level: {result['level']}, Issues: {result['issues']}, Entropy: {result['entropy']}")
        writer.writerow([password,result["score"],result["level"],"; ".join(result["issues"]),result["entropy"]])