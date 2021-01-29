#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
r = requests.get('https://api.github.com/users/facebook/repos')
r.status_code


# In[5]:


r.text


# In[15]:


json = r.json()
for i in range(len(json)):
    print('===REPO NAME===', json[i]['name'])


# In[26]:


'''
https://ja.reactjs.org/

xpath
//*[@id="gatsby-focus-wrapper"]/div/div/div/header/div/div/div/h1

css selector
#gatsby-focus-wrapper > div > div > div > header > div > div > div > h1
'''
import lxml.html
reactja = requests.get('https://ja.reactjs.org/')
html = reactja.text
root = lxml.html.fromstring(html)
titleH1 = root.xpath('//*[@id="gatsby-focus-wrapper"]/div/div/div/header/div/div/div/h1')
print('===XPath===', titleH1[0].text)
print(titleH1[0].tag)
print(titleH1[0].attrib)


# In[27]:


descriptionP = root.cssselect('#gatsby-focus-wrapper > div > div > div > header > div > div > div > p')
print(descriptionP[0].text)


# In[ ]:




