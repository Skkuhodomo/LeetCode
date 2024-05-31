import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    output = employee.sort_values(by ='salary',ascending=False).reset_index(drop=True)
    output = output[output.index == 1 ]
    if output['salary'].empty  :
        second_highest = None 
    else:
        second_highest = output['salary'].iloc[0]
    result = pd.DataFrame({'SecondHighestSalary': [second_highest]})

    return result