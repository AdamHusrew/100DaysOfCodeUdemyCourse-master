def my_func():
    return 3 * 4


def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name."""

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


# value = my_func()

print(format_name("adam", "husrew"))