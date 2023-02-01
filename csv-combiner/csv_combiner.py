import csv
import os.path as path
import sys

DIR = path.abspath(path.dirname(__file__))

def main():
    file_count = 0
    args = sys.argv
    paths = getPaths(args)
    if file_count == 0: print("sep=,")
    writer = csv.writer(sys.stdout,doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL, lineterminator='\n')
    buildHeader(paths, writer)
    for path in paths:
        filename = getFileName(path)
        addCSV(path, filename, writer)
        file_count = file_count + 1

def getPaths(arg_v):
    paths = []
    for i in range(len(arg_v)):
        if i != 0 and i != len(arg_v):
            paths.append(path.join(DIR,arg_v[i]).replace('/','\\'))
    return paths

def buildHeader(paths, writer):
    all_headers = []
    for path in paths:
        with open(path) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            row_one = next(reader)    
            for col in row_one:
                all_headers.append(col)
    merged_headers = [*set(all_headers)]
    merged_headers.append("filename")
    writer.writerow(merged_headers)

def addCSV(csv_path, filename, writer):
    with open(csv_path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            row.append(filename)
            writer.writerow(row)

def getFileName(path):
    split_path = path.split('\\')
    split_path_len = len(split_path)
    return split_path[split_path_len-1]

if __name__ == '__main__':
    main()
