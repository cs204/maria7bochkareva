def main():
    answer = input("Какой ответ на главный вопрос жизни, вселенной и всего такого? ")
    if answer.lower() == "42" or answer.lower() == "сорок два":
        print("Да")
    else:
        print("Нет")

if __name__ == "__main__":
    main()
