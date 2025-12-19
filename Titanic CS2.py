import csv

def read_titanic_rows():
    rows = []

    with open("titanic.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  

    
        for i in range(10):
            row = next(reader)
            rows.append(row)

    return rows
                 

def calculate_survival_rate():
    total = 0
    survived = 0

    with open("titanic.csv", "r") as file:
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

    with open("titanic.csv", "r") as file:
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

import csv

def age_analysis():
    total_age = 0
    total_count = 0

    survived_age = 0
    survived_count = 0

    died_age = 0
    died_count = 0

    youngest = 200   
    oldest = 0

    with open("titanic.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  

        for row in reader:
            age = row[5]       
            survived = row[1]  

            if age == "":
                continue

            age = float(age)

            total_age += age
            total_count += 1

            if age < youngest:
                youngest = age
            if age > oldest:
                oldest = age

            if survived == "1":
                survived_age += age
                survived_count += 1
            else:
                died_age += age
                died_count += 1

    avg_age = total_age / total_count
    avg_survived = survived_age / survived_count
    avg_died = died_age / died_count

    print("Average age of all passengers:", avg_age)
    print("Average age of survivors:", avg_survived)
    print("Average age of non-survivors:", avg_died)
    print("Youngest passenger age:", youngest)
    print("Oldest passenger age:", oldest)



def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Show first 10 rows of the Titanic file")
        print("2. Calculate survival rate")
        print("3. Calculate survival by gender")
        print("4. Age analysis")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            rows = read_titanic_rows()
            for r in rows:
                print(r)

        elif choice == "2":
            rate = calculate_survival_rate()
            print("Survival rate:", rate)

        elif choice == "3":
            survival_by_gender()

        elif choice == "4":
            age_analysis()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-5.")


main()
