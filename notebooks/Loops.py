#!/usr/bin/env python
# coding: utf-8

# # For loops
# 
# Loops are a way of doing the same thing multiple times on a collection (like a list). 
# 
# Suppose we wanted to add 1 to every value in a list. 
# 

# In[2]:


my_ages = [45, 23, 79]


# In[3]:


print(my_ages[0]+1)


# In[4]:


print(my_ages[1]+2)


# This is obviously not efficient, even for short lists. We can instead use a `for` loop
# 
# A `for` loop starts with the *keyword* for, followed by the name of the variable that will be changed with every loop, then `in` and the name of the variable that you want to loop through (*iterator variable*) and a colon `:`. Code is then written in an indented block (4 spaces or a tab in front of each line in the block)

# In[5]:


for age in my_ages:
    print(age, my_ages)


# In[77]:


for age in my_ages:
    print(age+1) # perform a calculation


# ### Notes about iterator variables
# 
# The *iterator variable* can be named whatever you like, but it is best to name them sensibly.

# In[78]:


for bananas in my_ages:
    print(bananas)#bananas??


# It should be noted that using the same name for the iterator variable as an existing variable will overwrite it.

# In[79]:


# Define age
age = 42
print(age)


# In[80]:


# Also use age as an iterator variable
for age in my_ages:
    print(age)


# In[81]:


# Age has been replaced by the last value of age in the loop
print(age)


# The fact that the iterator variable is accessible outside the loop can be useful for bugfixing

# In[82]:


# This will throw an error when it tries to add 1 to banana
#for age in [1, 2, "banana", 4]:
#    print(age+1)


# After an error we could print the value of our iterator variable (age) to see what the value was when the code crashed

# In[83]:


#print(age)


# ### Indentations are important
# 
# Indentations are very important. Only indented lines are considered part of the loop. 

# In[84]:


# All lines indented.
my_ages = [1, 2, 3, 4]
for age in my_ages:
    print(age)
    print(age+2)
    print("Finished printing age ",age)


# In[85]:


# the final age+2 is not contained within the loop, so is executed afterwards.
my_ages = [1, 2, 3, 4]
for age in my_ages:
    print(age)
    print("Finished printing age ",age)
print("loop over")
print(age+2) # Not in the loop, just whatever the final value of age was,+2



# ### Getting values out of a loop
# 
# Printing values in a loop is nice, and a good thing to do to see how your code is running. However it is likely you want to save the results of calculations inside the loop.

# In[86]:


my_ages = [54, 34, 23, 45] #what we will loop through
my_ages_next_year = [] #empty list to store results in

print("Start length: ",len(my_ages_next_year))#print the starting length of our results list
for age in my_ages:
    new_age = age + 1 #calculate and store result in variable
    print(new_age) #print calculation result
    my_ages_next_year.append(new_age) #add result of calculation to results list
    print("New length: ",len(my_ages_next_year))#print the starting length of our results list

print(my_ages_next_year) #print results



# In[87]:


# List of words
words = ["red", "green", "blue"]

# Using loops, 
# calculate the length of each word
# If you feel confident,
# Store the lengths in a list
word_lengths = []
for word in words:
    word_len = len(word)
    print(word_len)
    word_lengths.append(word_len)
    
print (word_lengths)


# ### Ranges to generate number sequences
# If we want to generate a sequence of numbers, we can use the range function

# In[88]:


for number in range(10):
    print(number)


# Range starts from 0 by default, and the second value is not inclusive. So if we want 1 to 10:

# In[89]:


for number in range(1,11):
    print(number)


# In[90]:


my_range = range(1, 11)


# In[91]:


print(my_range) # Not a list

for number in my_range:
    print(number)


# ### Accumulator pattern
# A different way of storing the results of a loop in a single value

# In[92]:


my_word = "Lithium"
#Loop through and print 
# every letter in this word
# Calculate word length without using len

# Create a variable to count the length of the word
length_word = 0

for letter in my_word:
    print(letter)
    # Calculate length_word + 1
    new_value = length_word + 1
    # Replace length_word with the new value (length_word + 1)
    length_word = new_value
    # length_word will increase in size by 1 every loop.

print ("length of word is",length_word)



# In[ ]:




