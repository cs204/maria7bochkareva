def feet2meter(v):
    return float(v.replace("ft", "")) * 0.3048

def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

if __name__ == "__main__":
    main()
