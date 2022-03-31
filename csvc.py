# Written by Jake Fuller for the purpose of the PMG Graduate Leadership Program Interview
# 03/29/22

import csv
import sys

# writer represents output file
writer = csv.writer(sys.stdout)
titles = True

# for every input csv file
for file in sys.argv[1:]:
    # open the file in readable format
    with open(file, 'r') as content:
        reader = csv.reader(content)
        # write each row to the output file
        for i, row in enumerate(reader):
            # check to make sure the column titles are written only once
            if i == 0 and not titles:
                continue
            writer.writerow(row)
    # title has been written
    titles = False
