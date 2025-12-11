import csv

def read_titanic_rows():
    rows = []

    with open("Titanic.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  

    
        for i in range(10):
            row = next(reader)
            rows.append(row)

    return rows
                 

def calculate_survival_rate():
    total = 0
    survived = 0

    with open("Titanic.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  

        for row in reader:
            if row[1] == "1":
                survived += 1
            total += 1

    return survived / total

def survival_by_gender():
    male_total = 0
    male_survived = 0
    female_total = 0
    female_survived = 0

    with open("Titanic.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  

        for row in reader:
            survived = row[1]          
            gender = row[4].lower()    

            if gender == "male":
                male_total += 1
                if survived == "1":
                    male_survived += 1

            elif gender == "female":
                female_total += 1
                if survived == "1":
                    female_survived += 1

    male_rate = male_survived / male_total
    female_rate = female_survived / female_total

    print("Male survival rate:", male_rate)
    print("Female survival rate:", female_rate)

    if female_rate > male_rate:
        print("Females had a higher survival rate.")
    elif male_rate > female_rate:
        print("Males had a higher survival rate.")
    else:
        print("Both genders had the same survival rate.")


def main():
    while True:
        print(" What would you like to do?")
        print("1. Show first 10 rows of the Titanic file")
        print("2. Calculate survival rate")
        print("3. Calculate survuval by gender")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            rows = read_titanic_rows()
            for r in rows:
                print(r)

        elif choice == "2":
            rate = calculate_survival_rate()
            print("Survival rate:", rate)
        
        elif choice =="3":
            print(survival_by_gender())


        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-4.")
main()