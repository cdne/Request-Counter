
def write_to_file(file_name, dict_request):
    with open(file_name, 'w') as file:
        for key in dict_request:
            file.write(f'{key}: {dict_request[key]} \n')