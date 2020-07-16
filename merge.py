'''
Docstring for merge
'''
import pandas as pd

stu_details = pd.DataFrame({'S_Name':['Subhash', 'Mahesh', 'Ramesh'],
                            'Address':['Hyd', 'Amp', 'Vnp'],
                            'Contact':['123', '456', '789']})

# Rename the Column Name

stu_details = stu_details.rename(columns={'S_Name'  : 'Student_Name'})

#stu_details['Student_Name'][0] = 'Rama'

stu_details.iloc[2, 0] = 'Chiru'

print(stu_details)

course_details = pd.DataFrame({'S_Name':['Subhash', 'Mahesh', 'Ramesh'],
                               'Course_name':['java', '.net', 'python'],
                               'Fee':['1000', '2000', '3000']})

#course_details = course_details.rename(columns = {'S_Name'  : 'Student_Name' })

course_details.iloc[2, 0] = 'Chiru'

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

print(course_details)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

print(pd.merge(stu_details, course_details, left_on='Student_Name', right_on='S_Name', how='outer'))
