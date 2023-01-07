import json


def format(text_file):
    with open(text_file, "r") as file:
        data = json.load(file)

    outfile_name = text_file.split('.')[0]

    with open(f'{outfile_name}.html', 'w') as f:
        f.write('<html><body>')
        for line in data['convo']:
            if not line.startswith("<p>"):
                f.write('<b><h2>' + line + '</h2></b>')
            else:
                f.write('<p>' + line + '</p>')
        f.write('</body></html>')