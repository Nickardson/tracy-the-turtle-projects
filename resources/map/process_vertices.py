import csv

polygons = {}

with open('vertices2.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            poly_id = row['poly_id']
            if not poly_id in polygons:
                polygons[poly_id] = []

            polygon = polygons[poly_id]
            x = round(float(row['xcoord']),2)
            y = round(float(row['ycoord']),2)
            polygon.append((x, y))

            line_count += 1
    print(f'Processed {line_count} lines.')

with open('generated_script.py', 'w') as output_file:
    output_file.write('polygons=[\n')
    for polygon in polygons:
        output_file.write(str(polygons[polygon]))
        output_file.write(',\n')
    output_file.write(']')
