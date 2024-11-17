import csv
def add_base_url_to_image_urls(row):
    base_url = "http://www.jbswartshop.nl/"
    image_urls_column = "Image URLs (x,y,z...)"
    if image_urls_column in row:
        urls = row[image_urls_column].split(',')
        updated_urls = []
        for url in urls:
            if url == "":
                continue
            updated_urls.append(base_url + url.replace('..//', ''))
        row[image_urls_column] = ','.join(updated_urls)
    return row

def process_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            updated_row = add_base_url_to_image_urls(row)
            writer.writerow(updated_row)

# Process the CSV file before splitting
input_file = 'webshop_product_new.csv'
processed_file = 'webshop_product_new_processed.csv'
process_csv(input_file, processed_file)

def split_csv(file_path, rows_per_file=1000):
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Read the header row

        file_count = 0
        rows = []

        for row in reader:
            rows.append(row)
            if len(rows) == rows_per_file:
                output_file = f'webshop_product_new_split_{file_count}.csv'
                with open(output_file, 'w', newline='', encoding='utf-8') as output_csv:
                    writer = csv.writer(output_csv)
                    writer.writerow(headers)  # Write the header
                    writer.writerows(rows)
                file_count += 1
                rows = []

        # Write remaining rows if any
        if rows:
            output_file = f'webshop_product_new_split_{file_count}.csv'
            with open(output_file, 'w', newline='', encoding='utf-8') as output_csv:
                writer = csv.writer(output_csv)
                writer.writerow(headers)
                writer.writerows(rows)

# Usage
split_csv('webshop_product_new_processed.csv')