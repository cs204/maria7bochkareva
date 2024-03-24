def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
    input_text = "Hello :) Goodbye :("
    print(convert(input_text))

if __name__ == "__main__":
    main()
