import pandas as pd
import numpy as np

#data import
raw = pd.read_csv('hospital_data_raw.csv')
print(raw.head())
print(raw.info())
print('Name of the columns we are working with ->',raw.columns)


#Deal with the null values in the following columns: Miyun_or_Electiv, CHRONIC_2, HEALTH_STATUS, Q3_G, q31_G, KUPAT_HOLIM

#How much of null values in each of these columns
null_columns=['Miyun_or_Electiv', 'CHRONIC_2', 'HEALTH_STATUS', 'Q3_G', 'q31_G', 'KUPAT_HOLIM']
for column in null_columns:
    print(column," has ",raw[column].isnull().sum()," null values.")

#What are unique values in these columns
for column in null_columns:
    print(column," has ",raw[column].unique()," unique values.")

#Filling Nan values
raw['Miyun_or_Electiv'].fillna(0,inplace=True)
raw['CHRONIC_2'].fillna(0,inplace=True)
raw['Q3_G'].fillna(0,inplace=True)
raw['q31_G'].fillna(0,inplace=True)
raw['KUPAT_HOLIM'].fillna(5,inplace=True)
raw['HEALTH_STATUS'].fillna(raw['HEALTH_STATUS'].mode()[0],inplace=True)



#Checking if we filled all missing values
for column in null_columns:
    print(column," has ",raw[column].isnull().sum()," null values.")



#raw.drop(columns = ['Unnamed: 48','Unnamed: 49','Unnamed: 50'])
raw.pop('Unnamed: 50')
raw.pop('Unnamed: 49')
raw.pop('Unnamed: 48')
print('Nan values in our dataset ',raw.isnull().values.sum())

#checking are values in columns valid
for column in raw.columns:
    print('Unique values in column ',column,' is ',raw[column].unique())

#CHOICE values should only be 0 1
print('How much of every unique value is in column CHOICE ',raw['CHOICE'].value_counts())
#In column CHOICE replace 3 with 1 or 0
import numpy as np
raw['CHOICE']=raw['CHOICE'].mask(raw['CHOICE'].isin([3]),raw['CHOICE'].replace(3,np.nan).ffill())
print('How much of every unique value is in column CHOICE ',raw['CHOICE'].value_counts())
print('unikatne vrijednosti od CHOICE',raw['CHOICE'].unique())

raw['CHOICE'].fillna(0,inplace=True)
print('unikatne vrijednosti od CHOICE',raw['CHOICE'].unique())
print(raw['CHOICE'].isnull().sum())

#possible values for the code_hospital the values 2.7 and 27 point to the same hospital,Let's change the 2.7 to 27
print(raw['code_hospital'].unique())
raw.loc[raw['code_hospital']==2.7,'code_hospital']=27
#raw['code_hospital']=raw['code_hospital'].replace(2.7,27)
print(raw['code_hospital'].unique())


#replace code_hospital values with real names of hospitals

choices = ['Sheba', 'Rambam', 'Wolfson', 'Ziv', 'Hillel Yaffe', 'Galilee', 'Brazilai', 'Baruch Padeh', 'Ichilov', 'Bnai Zion', 'Beilinson', 'Soroka', 'Meir', 'Kaplan', 'Emek',
            'Carmel','Hasharon', 'Yoseftal', 'Hadassah-Ein Karem', 'Hadassah-Mount Scopus', 'Nazareth Hospital EMMS', 'Holy Family', 'Shaare Zedek', 'Laniado',
            'Augusta Victoria', 'Mayanei HaYeshua', 'Shamir', 'Saint Vincent De Paul']
i=1
for choice in choices :
    raw['code_hospital']=raw['code_hospital'].replace(i,choice)
    i=i+1
print(raw['code_hospital'].unique())
print(raw.head(50))

#replace gender values with Male and Female
choices = ['M']
for choice in choices :
    raw['Gender']=raw['Gender'].replace('זכר',choice)
choices = ['F']
for choice in choices :
    raw['Gender']=raw['Gender'].replace('נקבה',choice)
print(raw['Gender'].unique())
print(raw.head(10))

#same thing with some other columns
choices = ['Internal', 'Surgical', 'Other']
print(raw['Code_ward'].unique())
i=1
for choice in choices :
    raw['Code_ward']=raw['Code_ward'].replace(i,choice)
    i=i+1
print(raw['Code_ward'].unique())
print(raw['Code_ward'].head(30))
raw.rename(columns={"Code_ward": "Ward"}, inplace=True)

choices = ['Small', 'Medium', 'Big']
print(raw['SIZE_new'].unique())
i=1
for choice in choices :
    raw['SIZE_new']=raw['SIZE_new'].replace(i,choice)
    i=i+1
print(raw['SIZE_new'].unique())
print(raw['SIZE_new'].head(30))
raw.rename(columns={"SIZE_new": "Hospital_size"}, inplace=True)

choices = ['Elective hospitalization','Emergency hospitalization']
print(raw['Miyun_or_Electiv'].unique())
i=0
for choice in choices :
    raw['Miyun_or_Electiv']=raw['Miyun_or_Electiv'].replace(i,choice)
    i=i+1
print(raw['Miyun_or_Electiv'].unique())
print(raw['Miyun_or_Electiv'].head(30))
raw.rename(columns={"Miyun_or_Electiv": "Emergency_or_Electiv"}, inplace=True)

choices = ['No','Yes']
print(raw['CHOICE'].unique())
i=0
for choice in choices :
    raw['CHOICE']=raw['CHOICE'].replace(i,choice)
    i=i+1
print(raw['CHOICE'].unique())
print(raw['CHOICE'].head(30))
raw.rename(columns={"CHOICE": "Can_Choose_Hosp"}, inplace=True)

choices = ['No','Yes']
print(raw['corridor1'].unique())
i=0
for choice in choices :
    raw['corridor1']=raw['corridor1'].replace(i,choice)
    i=i+1
print(raw['corridor1'].unique())
print(raw['corridor1'].head(30))
raw.rename(columns={"corridor1": "Lay_Corridor"}, inplace=True)

choices = ['No','Yes']
print(raw['CHRONIC_2'].unique())
i=0
for choice in choices :
    raw['CHRONIC_2']=raw['CHRONIC_2'].replace(i,choice)
    i=i+1
print(raw['CHRONIC_2'].unique())
print(raw['CHRONIC_2'].head(30))
raw.rename(columns={"CHRONIC_2": "Chronic"}, inplace=True)

choices = ['Excellent', 'Very Good', 'Good', 'Reasonable', 'Deficient']
print(raw['HEALTH_STATUS'].unique())
i=1
for choice in choices :
    raw['HEALTH_STATUS']=raw['HEALTH_STATUS'].replace(i,choice)
    i=i+1
print(raw['HEALTH_STATUS'].unique())
print(raw['HEALTH_STATUS'].head(30))

choices = ['Clalit', 'Leumit', 'Meuhedet', 'Maccabi', 'Other']
print(raw['KUPAT_HOLIM'].unique())
i=1
for choice in choices :
    raw['KUPAT_HOLIM']=raw['KUPAT_HOLIM'].replace(i,choice)
    i=i+1
print(raw['KUPAT_HOLIM'].unique())
print(raw['KUPAT_HOLIM'].head(30))

choices = ['Goverment', 'Clalit', 'Hadassah']
print(raw['baalut'].unique())
i=1
for choice in choices :
    raw['baalut']=raw['baalut'].replace(i,choice)
    i=i+1
print(raw['baalut'].unique())
print(raw['baalut'].head(30))

choices=['Public']
print(raw['baalut'].unique())
i=5
for choice in choices :
    raw['baalut']=raw['baalut'].replace(i,choice)

print(raw['baalut'].unique())
print(raw['baalut'].head(30))
raw.rename(columns={"baalut": "Hosp_ownership"}, inplace=True)

print('Name of all columns ',raw.columns)

#doing same things for questions
group = ['Q5', 'Q6', 'Q7','Q9', 'Q10', 'Q11','Q14', 'Q15','Q17','Q21_2016', 'Q22', 'Q23', 'Q24','Q27', 'Q28']

for column in group:
    choices = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied']
    i=1
    for choice in choices :
        raw[column]=raw[column].replace(i,choice)
        i=i+1

for column in group:
    choice=['Do not know / irrelevant']
    for choice in choices :
        raw[column]=raw[column].replace(99,choice)

#Q4
#choices = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied', 'Was not emergency hospitalization', 'Do not know / irrelevant']


#Q8
#choices = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied','Did not receive explanation', 'Do not know / irrelevant']

#Q12

def alias_function(choices,i):
    print(raw[i].unique())
    j=1
    for choice in choices :
        raw[i]=raw[i].replace(j,choice)
        j=j+1
    print(raw[i].unique())
    print(raw[i].head(10))

def edge_cases_alias9(choices,i,j):
    print(raw[i].unique())
    for choice in choices :
        raw[i]=raw[i].replace(j,choice)
    print(raw[i].unique())
    print(raw[i].head(10))


    

choices = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied']
alias_function(choices,'Q4');
choices=['Was not emergency hospitalization']
edge_cases_alias9(choices,'Q4',98);
choices=['Do not know / irrelevant']
edge_cases_alias9(choices,'Q4',99);

choices = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied']
alias_function(choices,'Q8');
choices=['Did not receive explanation']
edge_cases_alias9(choices,'Q8',98);
choices=['Do not know / irrelevant']
edge_cases_alias9(choices,'Q8',99);

choices = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied','Did not receive explanation']
alias_function(choices,'Q12');
choices=['Do not know / irrelevant']
edge_cases_alias9(choices,'Q12',99);



choices = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied', "don't know/couldn't know"]
alias_function(choices,'Q13');
choices=["don't know/couldn't know"]
edge_cases_alias9(choices,'Q13',98);
choices=['irrelevant']
edge_cases_alias9(choices,'Q13',99);

choices = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied', "didn't suffer or didn't want to get treatment for pain", 'dont know']
alias_function(choices,'Q16');
choices=["didn't suffer or didn't want to get treatment for pain"]
edge_cases_alias9(choices,'Q16',98);
choices=['dont know']
edge_cases_alias9(choices,'Q16',99);

choices = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied']
alias_function(choices,'Q18');
choices=['Not interested in being shared with the information']
edge_cases_alias9(choices,'Q18',97);
choices=['My medical condition did not allow for sharing']
edge_cases_alias9(choices,'Q18',98);
choices=['dont know']
edge_cases_alias9(choices,'Q18',99);

choices = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied', 'There were no alternatives']
alias_function(choices,'Q19');
choices=['Do not know ']
edge_cases_alias9(choices,'Q19',99);

choices = ['Always', 'Usually Yes', 'Usually No', 'Never']
alias_function(choices,'Q20');
choices=['Do not know ']
edge_cases_alias9(choices,'Q20',99);

choices = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied','Did not receive explanation']
alias_function(choices,'Q25');
choices=['Do not know ']
edge_cases_alias9(choices,'Q25',99);

choices = ['Always', 'Usually Yes', 'Usually No', 'Never']
alias_function(choices,'Q26');
choices=['Do not know ']
edge_cases_alias9(choices,'Q26',99);

choices = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied']
alias_function(choices,'Q29');
choices=["Did not eat the hospital food"]
edge_cases_alias9(choices,'Q29',98);
choices=["Don't know or irrelevant"]
edge_cases_alias9(choices,'Q29',99);

choices = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied']
alias_function(choices,'Q30');
choices=["Had no companions"]
edge_cases_alias9(choices,'Q30',98);
choices=["Do not know"]
edge_cases_alias9(choices,'Q30',99);

choices = ['Hebrew', 'English', 'Arabic', 'Russian', 'Amharic', 'Other']
alias_function(choices,'Q33');
choices=['Refused to answer ']
edge_cases_alias9(choices,'Q33',99);

choices = ['Entirety', 'Partly', 'At all']
alias_function(choices,'Q34');

choices = ['Alone', 'With Family Member', 'Home with a caregiver', 'At Family member', 'Assisted living/nursing home', 'Nursing facility/rehabilitation center', 'Refused to answer']
alias_function(choices,'Q36');

choices = ['Jewish', 'Muslim', 'Christian', 'Druze', 'Other', 'Refused to answer']
alias_function(choices,'Q37');

raw.rename(columns={"Q3": "Sat_score"}, inplace=True)
raw.rename(columns={"Q31": "would_recommend"}, inplace=True)
raw.rename(columns={"Q29": "Hospital_food"}, inplace=True)
raw.rename(columns={"Q33": "Language"}, inplace=True)
raw.rename(columns={"Q34": "Corridor_stay"}, inplace=True)
raw.rename(columns={"Q36": "Recently_lived_with"}, inplace=True)
raw.rename(columns={"Q37": "Religion"}, inplace=True)

#droping columns we do not need
raw.drop('Lay_Corridor', axis=1, inplace=True)
raw.pop('Q3_G')
raw.pop('q31_G')
print('Name of all columns:',raw.columns)

print('Checking if there is any Nan values left ',raw.isnull().values.sum())

raw.rename(columns={"code_hospital": "Hospital"}, inplace=True)

# convert sat_score and would_recommend because they are categorical data
print(raw['Sat_score'].dtype)
print(raw['would_recommend'].dtype)

raw['Sat_score'] = raw['Sat_score'].astype('object')
raw['would_recommend'] = raw['would_recommend'].astype('object')

print(raw['Sat_score'].dtype)
print(raw['would_recommend'].dtype)
#raw.to_csv('C:/Users/Admin/Desktop/hospita_data_clean.csv')

questions = {'Question':
            ['Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15','Q16','Q17', 'Q18', 'Q19','Q20', 'Q21_2016', 'Q22', 'Q23', 'Q24', 'Q25', 'Q26', 'Q27', 'Q28', 'Q30'],

            'Translation': [
            "If you were hospitalized through the emergency room, to what extent were you satisfied with the care you received?",
            "From the moment you arrived at the ward, to what extent was the admission process conducted efficiently?",
            "During your last hospitalization, to what extent did you feel that the nurses treated you with kindness and respect?",
            "To what extent did the nurses listen to you and address your questions and concerns?",
            "To what extent were the explanations you received during hospitalization from the nurses clear and understandable to you?",
            "During your last hospitalization, to what extent did you feel that the doctors treated you with kindness and respect?",
            "To what extent during the doctors visit did you feel that you were treated personally?",
            "To what extent did the doctors listen to you and address your questions and concerns?",
            "To what extent were the explanations you received during hospitalization from the doctors clear and understandable to you?", 
            "To what extent did you feel that the staff treating you at the hospital knew your medical condition before hospitalization?",
            "To what extent were the explanations given to you during the hospitalization initiated by the ward staff?",
            "To what extent did you feel that the department staff worked in coordination and cooperation (among themselves) in everything related to your care? (For example, transferring information from one to another, implementing the doctors' recommendations)",
            "To what extent did you feel that the staff addressed your pain or other symptoms such as nausea or dizziness, and helped you deal with them?",
            "To what extent did you feel that the care team works to maintain your safety to prevent medical errors in cases such as identifying a patient sensitivity to medications, preventing falls, etc.?",
            "To what extent did you feel that you were shared with the therapeutic options, to the extent that you were interested? That is, you were involved in the decisions, and your preferences were taken into account.",
            "To what extent did you feel that additional treatment methods / therapeutic alternatives were presented to you?",
            "During the last hospitalization, did you feel that you knew what the next step in hospital treatment was?",
            "To what extent did you feel that you received an answer to your requests and needs easily and without the need to make an effort?",
            "To what extent did you feel during the hospitalization that you were treated in good hands?",
            "To what extent was the discharge process from the hospital conducted efficiently?",
            "At the time of discharge from the hospital, to what extent did you receive an explanation summarizing your medical problem and the treatment you were given?",
            "To what extent were the explanations and instructions for further treatment clear and understandable to you? This refers to explanations regarding the medical problem for which you were hospitalized, the treatment given to you, unusual symptoms to be aware of and medications you must take.",
            "Were the room and bathroom clean?",
            "To what extent are you satisfied with the conditions in the room where you were hospitalized? (air conditioning, bed, mattress...)",
            "During the hospitalization, to what extent was it quiet at night in your room and in your surroundings?",
            "To what extent were the conditions available to your companions and visitors comfortable and adequate?"]
            }
questions_df = pd.DataFrame(questions)
print(questions_df.head(10))

questions_df.to_csv('C:/Users/Admin/Desktop/hospital_questions.csv')









    




