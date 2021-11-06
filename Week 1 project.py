#!/usr/bin/env python
# coding: utf-8

# In[4]:


finalpercentage=int(input('Enter your Final percentage '))
avgpercentage=50
passmark=60


while finalpercentage >=passmark:
    if (avgpercentage-finalpercentage)>5:
        print('You scored above the pass mark but unfortunately, you did not pass the average score')
    else:
        print('You scored above the pass mark and Congratulations, you passed the average score')
    break
    
else: #finalpercentage <passmark:
    print('You did not score above the pass mark')


# In[7]:


if finalpercentage>passmark and finalpercenage>avgpercentage:
    print('passed 1')
else:
    if avgpercentage>passmark:
        if finalpercentge<(avgpercentage-5):
            print('failed 1')
        else:
            print('passed 2')
    else:
        print('failed 2')


# In[3]:


def student_status(class_avg, student_score):
    pass_mark = 60
    if student_score >= pass_mark:
        if student_score >= class_avg:
            print('pass')
        elif student_score >= class_avg-5:
            print('almost fail but pass')
        elif student_score < class_avg:
            print('u beat pass mark but failed to beat class average')
    elif student_score < pass_mark and student_score >= class_avg:
        print('beat class avg but not pass mark')
    else:
        print('fail')

class_avg = float(input('input avg: '))
student_score = int(input('insert student mark: '))

student_status(class_avg,student_score)


# In[ ]:




