import time
import sys
from Report import Report


if __name__ == '__main__':
    rpt = Report()

    # TODO: if sys.argv[1] is not given, print a usage message and exit
    if len(sys.argv) < 2:
        print("No directory specified\nProgram will now quit", file=sys.stderr)
        exit()

    # given code - dont touch
    print("Reading the databases...", file=sys.stderr)
    before = time.time()

    # TODO: if opening the file 'sys.argv[1]/area_titles.csv' fails, let your program crash here
    try:
        areaTitles = open(sys.argv[1] + '/area_titles.csv')
    except:
        print(sys.argv[1] + "area_titles.csv does not exist\nProgram will now quit", file=sys.stderr)
        exit()

    # TODO: Convert the file 'sys.argv[1]/area_titles.csv' into a dictionary
    dictionary = {}
    for line in areaTitles:
        # clean up line
        line = line.replace("\"", "")
        line = line.replace("\n", "")
        # create dictionary values
        key, value = line.split(",", 1)
        # filter out unnecessary fips codes
        if key[-4:-1] != '000' and 'US' not in key and 'C' not in key:
            dictionary[key] = value
    # close file
    areaTitles.close()

    # TODO: if opening the file 'sys.argv[1]/2019.annual.singlefile.csv' fails, let your program crash here
    try:
        annual19 = open(sys.argv[1] + '/2019.annual.singlefile.csv')
    except:
        print(sys.argv[1] + '2019.annual.singlefile.csv was not found.\nProgram will now quit', file=sys.stderr)
        exit()

    # TODO: Collect information from 'sys.argv[1]/2019.annual.singlefile.csv', place into the Report object rpt
    # init variables
    # industry variables
    allAreas = 0
    allGrossWages = 0
    allMaxAnnual = (0, 0)
    allTotalEstab = 0
    allMaxEstab = (0, 0)
    allTotalEmpl = 0
    allMaxEmpl = (0, 0)
    # soft variables
    softAreas = 0
    softGrossWages = 0
    softMaxAnnual = (0, 0)
    softTotalEstab = 0
    softMaxEstab = (0, 0)
    softTotalEmpl = 0
    softMaxEmpl = (0, 0)

    # create dictionary
    annualDict = {}
    for line in annual19:
        # remove unnecessary characters
        line = line.replace('\"', '')
        line = line.replace('\n', '')
        # parse file in array
        data = line.split(",")

        # if FIPS is not in dictionary or if line is header, ignore it
        try: # line is not in dictionary
            if int(data[0]) % 1000 == 0:
                continue
        except: # line is header
            continue

        # check industry and own code
        ownCode = data[1]
        industryCode = data[2]

        # software industry
        if ownCode == "5" and industryCode == "5112":
            # update all software variables
            softAreas += 1
            softGrossWages += int(data[10])
            if softMaxAnnual[1] == 0 or softMaxAnnual[1] < int(data[10]):
                softMaxAnnual = (dictionary[data[0]], int(data[10]))
            softTotalEstab += int(data[8])
            if softMaxEstab[1] == 0 or softMaxEstab[1] < int(data[8]):
                softMaxEstab = (dictionary[data[0]], int(data[8]))
            softTotalEmpl += int(data[9])
            if softMaxEmpl[1] == 0 or softMaxEmpl[1] < int(data[9]):
                softMaxEmpl = (dictionary[data[0]], int(data[9]))
        # all industries
        elif ownCode == "0" and industryCode == "10":
            # update all all industry variables
            allAreas += 1
            allGrossWages += int(data[10])
            if allMaxAnnual[1] == 0 or allMaxAnnual[1] < int(data[10]):
                allMaxAnnual = (dictionary[data[0]], int(data[10]))
            allTotalEstab += int(data[8])
            if allMaxEstab[1] == 0 or allMaxEstab[1] < int(data[8]):
                allMaxEstab = (dictionary[data[0]], int(data[8]))
            allTotalEmpl += int(data[9])
            if allMaxEmpl[1] == 0 or allMaxEmpl[1] < int(data[9]):
                allMaxEmpl = (dictionary[data[0]], int(data[9]))


    # given code - don't touch
    after = time.time()
    print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

    # TODO: Fill in the report for all industries
    rpt.all.num_areas           = allAreas

    rpt.all.total_annual_wages  = allGrossWages
    rpt.all.max_annual_wage     = allMaxAnnual

    rpt.all.total_estab         = allTotalEstab
    rpt.all.max_estab           = allMaxEstab

    rpt.all.total_empl          = allTotalEmpl
    rpt.all.max_empl            = allMaxEmpl


    # TODO: Fill in the report for the software publishing industry
    rpt.soft.num_areas          = softAreas

    rpt.soft.total_annual_wages = softGrossWages
    rpt.soft.max_annual_wage    = softMaxAnnual

    rpt.soft.total_estab        = softTotalEstab
    rpt.soft.max_estab          = softMaxEstab

    rpt.soft.total_empl         = softTotalEmpl
    rpt.soft.max_empl           = softMaxEmpl


    # Print the completed report
    print(rpt)

    # close file
    annual19.close()
