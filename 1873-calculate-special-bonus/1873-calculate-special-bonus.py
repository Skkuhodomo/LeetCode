import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees.loc[employees['employee_id']  % 2 ==0,'salary'] = 0 
    employees.loc[employees['name'].str[0] =='M','salary'] = 0 
    return employees.rename(columns = {'salary':'bonus'})[['employee_id', 'bonus']].sort_values('employee_id')