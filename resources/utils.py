def remove_non_utf8_chars(text):
    # Remove non-UTF-8 characters from the text
    return text.encode('ascii', 'ignore').decode('utf-8')


def convert_to_float(value):
    # Remove the currency symbol and whitespace from the string
    value_without_currency = value.replace('R$', '').strip()

    # Replace comma with a dot to ensure the number is formatted correctly
    value_without_currency = value_without_currency.replace(',', '.')

    # Convert the string to float
    return float(value_without_currency)
