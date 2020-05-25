def write_errors(exception, text):
    with open('error.log', 'a+') as log_archive:
        log_archive.write('----------------------------------------------------------------\n')
        log_archive.write(str(exception))
        log_archive.write(text)
        log_archive.write('----------------------------------------------------------------\n')