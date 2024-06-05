# Caroline E Dale, Rohan Takhar, et al., 2024.

import sys, csv, re

codes = [{"code":"0202020L0AACYCY","system":"bnf"},{"code":"0202020L0AACKCK","system":"bnf"},{"code":"0202020L0AACCCC","system":"bnf"},{"code":"0202020L0AACHCH","system":"bnf"},{"code":"0202020L0AACECE","system":"bnf"},{"code":"0202020L0AACJCJ","system":"bnf"},{"code":"0202020L0AABZBZ","system":"bnf"},{"code":"0202020L0AACBCB","system":"bnf"},{"code":"0202020L0AADFDF","system":"bnf"},{"code":"0202020L0AACNCN","system":"bnf"},{"code":"0202020L0AACTCT","system":"bnf"},{"code":"0202020L0AADDDD","system":"bnf"},{"code":"0202020L0AACDCD","system":"bnf"},{"code":"0202020L0AACLCL","system":"bnf"},{"code":"0202020L0AADADA","system":"bnf"},{"code":"0202020L0AACFCF","system":"bnf"},{"code":"0202020L0AACXCX","system":"bnf"},{"code":"0202020L0AADEDE","system":"bnf"},{"code":"0202020L0AACICI","system":"bnf"},{"code":"0202020L0AABYBY","system":"bnf"},{"code":"0202020L0AACSCS","system":"bnf"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('heart-failure-medication-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["heart-failure-medication-liquid---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["heart-failure-medication-liquid---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["heart-failure-medication-liquid---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
