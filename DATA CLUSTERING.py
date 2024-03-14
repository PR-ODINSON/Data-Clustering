#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data into a DataFrame named 'df'
df = pd.read_csv('path')

# Drop unnecessary columns (0, 2, 3, and 7) based on their index positions
df.drop(df.columns[[0, 2, 3, 7]], axis=1, inplace=True)

# Fill missing values in the DataFrame 'df' with 0
main = df.fillna(0)

# Create a list of column names with their corresponding index positions (starting from 1)
column_array = [(i, column) for i, column in enumerate(df.columns, start=1)]

# Print column headers with numbering
print("Column Number\tColumn Name")
for column in column_array:
    print(f"{column[0]}\t\t\t{column[1]}")


def process_skills(df, skill_column, rating_column):
    """
    This function analyzes skills based on a specified skill column and rating column.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data.
        skill_column (str): The name of the column containing the skill names.
        rating_column (str): The name of the column containing the skill ratings.

    Prints:
        The DataFrame with individuals sorted by their rating in the specified skill.
        DataFrames for weakest, average, and excellent performers in that skill.
    """

    skills = df[['Name', skill_column]]
    skills = skills.sort_values(by=rating_column)
    print(skills)
    print()

    weakest_skills = skills[skills[rating_column] < 3]
    print(weakest_skills)

    average_skills = skills[skills[rating_column] == 3]
    print(average_skills)

    excellence_skills = skills[skills[rating_column] > 3]
    print(excellence_skills)


def graph_analysis(weakest_skills, average_skills, excellence_skills):
    """
    This function creates a pie chart to visualize the distribution of individuals
    across weakest, average, and excellence categories based on skill ratings.

    Args:
        weakest_skills (pandas.DataFrame): DataFrame containing weakest performers.
        average_skills (pandas.DataFrame): DataFrame containing average performers.
        excellence_skills (pandas.DataFrame): DataFrame containing excellent performers.
    """

    x = [len(weakest_skills), len(average_skills), len(excellence_skills)]
    y = ["Weakest", "Average", "Excellence"]
    plt.pie(x, labels=y, autopct="%0.1f%%", wedgeprops={"linewidth": 1, "edgecolor": "w"})
    plt.show()


def get_average():
    """
    This function identifies individuals with average skill sets and calculates
    the number of weakest, average, and excellent performers.

    Prints:
        Lists of individuals categorized as weakest, average, and excellent.
        The number of weakest, average, and excellent performers.
    """

    list_1 = main.values.tolist()
    names = []
    for i in range(40):
        try:
            names.append(list_1[i][6])
        except (IndexError, TypeError):
            pass

    Excellence = []
    Weakest = []

    for i in range(40):
        a = 0  # Counter for reaching excellence criteria (6 ratings above 4)
        for j in range(21, 28):
            if float(list_1[i][j]) >= 4:
                a += 1

        if a >= 6:
            Excellence.append(list_1[i][6])
            a = 0  # Reset counter for next iteration

    for i in range(40):
        a = 0  # Counter for reaching weakest criteria (6 ratings below 3)
        for j in range(21, 28):
            if float(list_1[i][j]) < 3:
                a += 1

        if a >= 6:
            Weakest.append(list_1[i][6])
            a = 0  # Reset counter for next iteration

    print("Excellence are:", Excellence)
    print("Weakest are:", Weakest)

    # Identify individuals with average skill sets (not in the High or low lists)
    Average = set(names) - set(Excellence + Weakest)
    print("Average skill sets are:", Average)
    
    x = [len(Weakest), len(Average), len(Excellence)]
    y = ["Weakest", "Average", "Cream"]
    plt.pie(x, labels=y, autopct="%0.1f%%", wedgeprops={"linewidth": 1, "edgecolor": "w"})
    plt.show()
    print("Number of weakest students are",len(Weakest))
    print("Number of average students are",len(Average))
    print("Number of cream students are",len(Excellence))
    


def skill_analysis():
    column_names=[col for col in df.columns[8:15]]
    skill_column_input = input("Enter the enter the column name of skill: ")

    # Allow users to use a short name like "Technical" instead of the full column name
    matching_columns = [col for col in df.columns if skill_column_input.lower() in col.lower()]

    if not matching_columns:
        print("No matching columns found.")
        return None

    if len(matching_columns) > 1:
        for column in column_names:
            process_skills(main,column,column)
    else:
        skill_column = matching_columns[0]

        skills = df[["Name", skill_column]]
        skills = skills.fillna(0)
        skills = skills.sort_values(by=skill_column)

        # GROUPING BASED ON SKILLS
        weakest = skills[skills[skill_column] < 3]
        excellence = skills[skills[skill_column] > 3]
        average = skills[skills[skill_column] == 3]

        return weakest, excellence , average

