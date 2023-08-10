# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"101583.0","system":"med"},{"code":"102036.0","system":"med"},{"code":"10587.0","system":"med"},{"code":"16025.0","system":"med"},{"code":"17685.0","system":"med"},{"code":"18190.0","system":"med"},{"code":"20813.0","system":"med"},{"code":"21401.0","system":"med"},{"code":"2315.0","system":"med"},{"code":"23381.0","system":"med"},{"code":"23897.0","system":"med"},{"code":"24933.0","system":"med"},{"code":"28514.0","system":"med"},{"code":"28595.0","system":"med"},{"code":"28790.0","system":"med"},{"code":"28953.0","system":"med"},{"code":"29464.0","system":"med"},{"code":"29477.0","system":"med"},{"code":"34097.0","system":"med"},{"code":"34139.0","system":"med"},{"code":"3449.0","system":"med"},{"code":"35743.0","system":"med"},{"code":"36157.0","system":"med"},{"code":"36792.0","system":"med"},{"code":"37073.0","system":"med"},{"code":"38804.0","system":"med"},{"code":"39048.0","system":"med"},{"code":"39511.0","system":"med"},{"code":"40272.0","system":"med"},{"code":"4139.0","system":"med"},{"code":"41619.0","system":"med"},{"code":"41871.0","system":"med"},{"code":"4216.0","system":"med"},{"code":"43350.0","system":"med"},{"code":"45673.0","system":"med"},{"code":"51305.0","system":"med"},{"code":"52721.0","system":"med"},{"code":"5366.0","system":"med"},{"code":"56462.0","system":"med"},{"code":"58004.0","system":"med"},{"code":"58149.0","system":"med"},{"code":"60234.0","system":"med"},{"code":"61904.0","system":"med"},{"code":"66113.0","system":"med"},{"code":"66743.0","system":"med"},{"code":"71131.0","system":"med"},{"code":"7119.0","system":"med"},{"code":"72447.0","system":"med"},{"code":"7682.0","system":"med"},{"code":"8190.0","system":"med"},{"code":"8677.0","system":"med"},{"code":"90777.0","system":"med"},{"code":"9323.0","system":"med"},{"code":"94219.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('urolithiasis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["urolithiasis-procedure---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["urolithiasis-procedure---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["urolithiasis-procedure---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
