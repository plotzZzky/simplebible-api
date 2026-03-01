import json


def format_query(query, file_type=None):
    if file_type == 'txt':
        result = convert_to_text(query)
    elif file_type == 'json':
        result = convert_to_json(query)
    else:
        result = convert_to_html(query)
    return result


def convert_to_json(values):
    data = [
        {
            'livro': value[8],
            'capitulo': value[2],
            'vericulo': value[3],
            'texto': value[4]
        }
        for value in values
    ]

    json_data = json.dumps(data, ensure_ascii=False, indent=4)
    return json_data


def convert_to_text(value):
    data = []

    for value in value:
        data.append(f"{value[8]} {value[2]}:{value[3]} - {value[4]}")

    result = '\n'.join(data)
    return result


def convert_to_html(value):
    result = []
    for row in value:
        x = f'<p><strong> {row[8]} {row[2]}:{row[3]}</strong> - {row[4]} </p>'
        result.append(x)

    data = '\n'.join(result)

    html = f""" <!DOCTYPE html>
    <html lang="en">
    
    <head>
      <meta charset="UTF-8">
      <title> </title>
    </head>
    
    <body style="margin: 0; padding: 1vh 1vw; font-size: 1.1em; font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif; background-color: rgb(31, 31, 31); color: white;">
      {data}
    </body>
    
    </html> """.format(data=data)

    return html
