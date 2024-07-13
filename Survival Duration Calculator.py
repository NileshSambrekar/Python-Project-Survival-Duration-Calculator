#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def age_calculator():
    
    my_age = int(input('Please Enter your Age:'))
    
    if my_age <= 0:
        print('Invalid input')
        return
    
    while True:
        print('''
                Select the duration from below:
                1. Age in Months
                2. Age in Weeks
                3. Age in Days
                4. Age in Hours
                5. Age in Minutes
                6. Age in Seconds''')
        
        choose = int(input('Enter Your Choice from Above :'))
        
        if choose == 1:
            my_age = my_age*12
            print(f'You lived for :{my_age}','Months')
            break
            
        elif choose == 2:
            my_age = my_age*52
            print(f'You lived for :{my_age}','Weeks')
            break
            
        elif choose == 3:
            
            my_age = my_age*365
            print(f'You lived for :{my_age}','Days')
            break
            
        elif choose == 4:
            my_age = my_age*8766
            print(f'You lived for :{my_age}','Hours')
            break
                  
        elif choose == 5:
            my_age = my_age*525960
            print(f'You lived for :{my_age}','Minutes')
            break
        
        elif choose == 6:
            my_age = my_age*31536000
            print(f'You lived for :{my_age}','Seconds')
            break
        else:
            print('Selection Invalid..!')
            break
    return
