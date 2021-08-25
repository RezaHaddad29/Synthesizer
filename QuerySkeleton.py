import csv

def QuerySkeleton():
    selCols=[]
        
    with open('OutputTable.csv', 'r') as f:
        csv_reader = csv.reader(f)
        selCols = next(csv_reader)

    selCols = ", ".join(selCols)


    query = """Select {0} From InputTable
    Where (Wc Wop Wv)""".format(selCols)

    return query