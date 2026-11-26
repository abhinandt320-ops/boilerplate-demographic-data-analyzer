import pandas as pd


def calculate_demographic_data(print_data=True):

    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # Number of people of each race
    race_count = df["race"].value_counts()

    # Average age of men
    average_age_men = round(
        df[df["sex"] == "Male"]["age"].mean(), 1
    )

    # Percentage of people with a Bachelor's degree
    percentage_bachelors = round(
        len(df[df["education"] == "Bachelors"]) / len(df) * 100, 1
    )

    # People with and without advanced education
    higher_education = df[
        df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    ]

    lower_education = df[
        ~df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    ]

    # Percentage earning more than 50K
    higher_education_rich = round(
        len(higher_education[higher_education["salary"] == ">50K"])
        / len(higher_education) * 100, 1
    )

    lower_education_rich = round(
        len(lower_education[lower_education["salary"] == ">50K"])
        / len(lower_education) * 100, 1
    )

    # Minimum working hours
    min_work_hours = df["hours-per-week"].min()

    # People working minimum hours
    min_workers = df[df["hours-per-week"] == min_work_hours]

    num_min_workers = len(min_workers)

    # Percentage of minimum-hour workers earning more than 50K
    rich_percentage = round(
        len(min_workers[min_workers["salary"] == ">50K"])
        / num_min_workers * 100, 1
    )

    # Country with the highest percentage of rich people
    country_counts = df["native-country"].value_counts()

    rich_country_counts = df[
        df["salary"] == ">50K"
    ]["native-country"].value_counts()

    country_percentages = (
        rich_country_counts / country_counts * 100
    )

    highest_earning_country = country_percentages.idxmax()

    highest_earning_country_percentage = round(
        country_percentages.max(), 1
    )

    # Most popular occupation among high earners in India
    top_IN_occupation = df[
        (df["native-country"] == "India") &
        (df["salary"] == ">50K")
    ]["occupation"].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }