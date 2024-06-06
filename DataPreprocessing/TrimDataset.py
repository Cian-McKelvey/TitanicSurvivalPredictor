import pandas as pd


def remove_unneeded_data(filepath: str) -> None:
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(filepath)

    # PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked

    # Create a list of column names you want to keep
    columns_to_keep = ['PassengerId', 'Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Embarked']

    # Create a new DataFrame with only the selected columns
    new_data = data[columns_to_keep]

    # Save the new DataFrame to a new CSV file
    new_data.to_csv('Datasets/TrimmedPassengerData.csv', index=False)
