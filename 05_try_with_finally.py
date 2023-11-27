try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit(e)

finally:
    print("We are successful")

print("Thanks for using this program")