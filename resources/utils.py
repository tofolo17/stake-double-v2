def remove_non_utf8_chars(text):
    return text.encode('ascii', 'ignore').decode('utf-8')