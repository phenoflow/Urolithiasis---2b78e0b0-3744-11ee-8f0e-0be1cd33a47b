# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"102293.0","system":"med"},{"code":"10282.0","system":"med"},{"code":"106912.0","system":"med"},{"code":"1256.0","system":"med"},{"code":"14276.0","system":"med"},{"code":"15201.0","system":"med"},{"code":"1858.0","system":"med"},{"code":"1912.0","system":"med"},{"code":"2105.0","system":"med"},{"code":"2258.0","system":"med"},{"code":"23917.0","system":"med"},{"code":"24047.0","system":"med"},{"code":"2410.0","system":"med"},{"code":"24165.0","system":"med"},{"code":"24994.0","system":"med"},{"code":"27592.0","system":"med"},{"code":"27786.0","system":"med"},{"code":"29242.0","system":"med"},{"code":"2939.0","system":"med"},{"code":"31773.0","system":"med"},{"code":"32858.0","system":"med"},{"code":"3308.0","system":"med"},{"code":"33746.0","system":"med"},{"code":"33747.0","system":"med"},{"code":"34584.0","system":"med"},{"code":"3669.0","system":"med"},{"code":"36972.0","system":"med"},{"code":"38461.0","system":"med"},{"code":"3906.0","system":"med"},{"code":"43744.0","system":"med"},{"code":"44648.0","system":"med"},{"code":"45245.0","system":"med"},{"code":"45765.0","system":"med"},{"code":"46291.0","system":"med"},{"code":"47869.0","system":"med"},{"code":"4928.0","system":"med"},{"code":"49783.0","system":"med"},{"code":"52569.0","system":"med"},{"code":"5729.0","system":"med"},{"code":"59834.0","system":"med"},{"code":"6048.0","system":"med"},{"code":"6087.0","system":"med"},{"code":"6147.0","system":"med"},{"code":"640.0","system":"med"},{"code":"64699.0","system":"med"},{"code":"65920.0","system":"med"},{"code":"67386.0","system":"med"},{"code":"6770.0","system":"med"},{"code":"6978.0","system":"med"},{"code":"6979.0","system":"med"},{"code":"74021.0","system":"med"},{"code":"8399.0","system":"med"},{"code":"8777.0","system":"med"},{"code":"9162.0","system":"med"},{"code":"93608.0","system":"med"},{"code":"94420.0","system":"med"},{"code":"9950.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('urolithiasis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["urolithiasis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["urolithiasis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["urolithiasis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
