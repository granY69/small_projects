#!/usr/bin/env python
# coding: utf-8

# **Print a welcome message to the user**

# In[1]:


print('Welcome To The First Mini Program. This program asks you to enter a string(message) and a character(letter)'       ' and then it calculates the count and percentage of the character(letter) occurrences. Also print the outputs.')


# **Take a string and letter from the user**

# In[2]:


user_message=input('Enter String(message) ')
user_char=input('Now Enter the character(letter) ')


# **Count how many times this letter occured**

# In[3]:


char_count=user_message.count(user_char)


# **Calculate the percentage of the letter in the message**

# In[4]:


perc=(char_count/len(user_message))*100


# **Print the outputs to the user**

# In[5]:


print(f'Number of times the given character occured is {char_count} and percentage of the character in the message is {perc}')

end=input('press enter to exit ')

