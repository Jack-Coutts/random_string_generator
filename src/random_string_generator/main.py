import secrets
import string


def get_string_len() -> int:

    str_length = input("Please specify length of random string (default 10): ")
    if str_length:
        try:
            str_length = int(str_length)
            return str_length
        except:
            print("Please enter and integer (e.g. 9):")
            return get_string_len()
    else:
        return 0


def append_to_rand_string() -> str:

    decision = input(
        "Do you want to append anything to your random string? (y/n): "
    ).lower()
    if decision == "y":
        addition = input("Please enter the additonal text: ")
        return addition
    elif decision == "n":
        return ""
    else:
        print("Please enter a valid response, y for yes and n for no: ")
        return append_to_rand_string()


def get_rand_string(string_len: int = 10) -> str:

    # A string of all letters and numbers
    all_character_options = f"{string.ascii_letters}{string.digits}"

    # Create a string from random choices from above all_character_options
    output_string = "".join(
        secrets.choice(all_character_options) for _ in range(string_len)
    )

    return output_string


def main():

    string_len = get_string_len()
    if string_len != 0:
        rand_str = get_rand_string(string_len)
    else:
        rand_str = get_rand_string()

    str_addition = append_to_rand_string()

    output = f"{rand_str} {str_addition}"

    print(output)


if __name__ == "__main__":
    main()
