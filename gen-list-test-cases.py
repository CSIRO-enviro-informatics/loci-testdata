import csv

from os import listdir
from os.path import isfile, join

path = './excelerator'
outputfile = './test_case_uris.csv'
files = [f for f in listdir(path) if isfile(join(path, f))]

#print(files)


with open(outputfile,'w') as writefile:
    print("Emitting to " + outputfile)
    writefile.write(f'testcase,uri\n')

    for f in files:
        with open(path + "/" + f, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            test_case_name = f.split('.csv', 1)[0]

            for row in csv_reader:
                if line_count == 0:
                    #print(f'Column names are {", ".join(row)}')
                    line_count += 1
                
                #print(f'\t{row["Address"]}   {row["Count"]}')
                print(f'{test_case_name},{row["Address"].strip()}')
                writefile.write(f'{test_case_name},{row["Address"].strip()}\n')
                line_count += 1
            #print(f'Processed {line_count} lines.')
