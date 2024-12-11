import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1- a) Read and print out the classification column
def create_data():
    df = pd.read_csv("breast-cancer.data", names=['Class', 'Age', 'Menopause', 'Tumor Size','Inv Nodes',
                                                  'Node Caps', 'Degree', 'Breast', 'Quadrant', 'Irradiated'])

    return df
# 1-b) function that computes the zero
def ZeroR(df):
    zero_r = df['Class'].mode()[0]
    return zero_r
# 1-c) determines the most common values for age and menopause group for patients with recurrences
def common_values(df):
    f1 = df[df['Class'] == 'recurrence-events']
    most_common_age = f1['Age'].mode()[0]
    most_common_meno = f1['Menopause'].mode()[0]
    return most_common_age, most_common_meno


# 1-d) Write a function that poles the number of recurrences for each age group
def plt_recurrence(df):
    recurr = df[df['Class'] == 'recurrence-events']
    ages = recurr.groupby('Age').size()
    ages.plot(kind = "bar", xlabel= "ages", ylabel= "recurrences", title= "ages vs recurrence")
    plt.show()
#Abd
if __name__ == '__main__':
    data = create_data()

    print("Classification column:")
    print(data['Class'])

    zero_r_class = ZeroR(data)
    print("Most common class (ZeroR):", zero_r_class)

    most_common_age, most_common_menopause = common_values(data)
    print("Most common age for recurrences:", most_common_age)
    print("Most common menopause status for recurrences:", most_common_menopause)

    plt_recurrence(data)

