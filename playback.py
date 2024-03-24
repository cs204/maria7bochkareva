def replace_spaces_with_dots(text):
    return text.replace(" ", "...")

def main():
    user_input = input()
    result = replace_spaces_with_dots(user_input)
    print(result)

if __name__ == "__main__":
    main()
