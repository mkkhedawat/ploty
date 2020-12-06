import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


languages = [
    "Assembly",
    "Bash/Shell/PowerShell",
    "C",
    "C#",
    "C++",
    "Dart",
    "Go",
    "Haskell",
    "HTML/CSS",
    "Java",
    "JavaScript",
    "Julia",
    "Kotlin",
    "Objective-C",
    "Perl",
    "PHP",
    "Python",
    "R",
    "Ruby",
    "Rust",
    "Scala",
    "SQL",
    "Swift",
    "TypeScript",
    "VBA",
]

desired_columns = [
    "Respondent",
    "LanguageWorkedWith",
    "LanguageDesireNextYear",
    "Employment",
    "YearsCodePro",
    "MainBranch",
    "OrgSize",
]

# This function splits out multiple entries in specified column & returns splitted data
def clean_series(df, col_name, ret_col_name, rel_count_col_name):
    """
    inputs:
    df: dataframe which you want to manipulate
    col_name: name of the column which you want to clean the data
    ret_col_name: name of the column which you want to set after cleaning the data
    ret_count_col_name: name of the count column which you want to set after cleaning the data

    outputs:
    df2: Panda's dataframe with the unique element seperated and
         their count
    """
    temp = df[col_name]
    temp = temp.dropna().reset_index()
    temp = temp[col_name].str.split(";")
    key_list = []
    for i in range(len(temp)):
        key_list += temp[i]

    for i in range(len(key_list)):
        key_list[i] = key_list[i].strip()

    c = Counter(key_list)
    df2 = pd.DataFrame(
        {ret_col_name: list(c.keys()), rel_count_col_name: list(c.values())}
    )
    return df2