from bs4 import BeautifulSoup
import urllib.request as ur
import os
import pandas as pd
import time
from datetime import datetime

#import csv data
## df = pd.read_csv('linkedin_courses.csv')
## df.to_csv('testoutput.csv',index=False)

course_urls = [
"https://www.linkedin.com/learning/learning-webpack-4-2",
"https://www.linkedin.com/learning/angular-creating-and-hosting-a-full-stack-site",
"https://www.linkedin.com/learning/polyglot-web-development",
"https://www.linkedin.com/learning/node-js-debugging-and-performance-tuning",
"https://www.linkedin.com/learning/building-a-graphql-project-with-react-js",
"https://www.linkedin.com/learning/building-your-first-cli-app-in-node",
"https://www.linkedin.com/learning/react-creating-and-hosting-a-full-stack-site",
"https://www.linkedin.com/learning/node-js-for-c-sharp-developers",
"https://www.linkedin.com/learning/mongodb-for-mean-stack-developers",
"https://www.linkedin.com/learning/learning-redis",
"https://www.linkedin.com/learning/building-vue-and-node-apps-with-authentication",
"https://www.linkedin.com/learning/cloud-native-development-with-node-js-docker-and-kubernetes",
"https://www.linkedin.com/learning/modernize-node-js-apps-with-azure-app-service",
"https://www.linkedin.com/learning/express-essential-training-2018",
"https://www.linkedin.com/learning/building-apis-with-loopback",
"https://www.linkedin.com/learning/learning-koa",
"https://www.linkedin.com/learning/mean-stack-and-mongodb-development-techniques",
"https://www.linkedin.com/learning/angularjs-1-building-a-data-driven-app-2",
"https://www.linkedin.com/learning/learning-gatsby-2020",
"https://www.linkedin.com/learning/vue-js-creating-and-hosting-a-full-stack-site",
"https://www.linkedin.com/learning/aws-for-developers-rds-mysql-database-with-lambdas",
"https://www.linkedin.com/learning/aws-for-developers-dynamodb",
"https://www.linkedin.com/learning/developing-for-microsoft-teams",
"https://www.linkedin.com/learning/sharepoint-framework-for-developers-1-understanding-the-toolchain",
"https://www.linkedin.com/learning/learning-apache-cordova",
"https://www.linkedin.com/learning/microsoft-power-automate-essential-training-2021",
"https://www.linkedin.com/learning/dan-ariely-on-making-decisions",
"https://www.linkedin.com/learning/learning-python-with-pycharm-14509667",
"https://www.linkedin.com/learning/how-to-work-smarter-not-harder-save-time-and-money-and-increase-productivity",
"https://www.linkedin.com/learning/django-forms",
"https://www.linkedin.com/learning/how-to-be-both-assertive-and-likable",
"https://www.linkedin.com/learning/how-to-set-goals-when-everything-feels-like-a-priority",
"https://www.linkedin.com/learning/learning-react-js-5",
"https://www.linkedin.com/learning/building-modern-projects-with-react",
"https://www.linkedin.com/learning/react-hooks",
"https://www.linkedin.com/learning/react-design-patterns",
"https://www.linkedin.com/learning/react-js-building-an-interface-8551484",
"https://www.linkedin.com/learning/react-software-architecture",
"https://www.linkedin.com/learning/react-working-with-apis",
"https://www.linkedin.com/learning/react-authentication",
"https://www.linkedin.com/learning/building-a-graphql-project-with-react-js",
"https://www.linkedin.com/learning/react-using-typescript",
"https://www.linkedin.com/learning/react-server-side-rendering-8539269",
"https://www.linkedin.com/learning/react-for-web-designers-2",
"https://www.linkedin.com/learning/react-ecosystems",
"https://www.linkedin.com/learning/react-cloud-powered-apps-with-firebase",
"https://www.linkedin.com/learning/react-creating-and-hosting-a-full-stack-site",
"https://www.linkedin.com/learning/react-state-management",
"https://www.linkedin.com/learning/react-testing-and-debugging",
"https://www.linkedin.com/learning/react-react-router"

]

course_data = {'title': [], 'author': [], 'level': [], 'category': [], 'subcategory': []}
## LinkedIn Course Info page changed as of 2 February 2022. Updated code to reflect the change.
##course_data = {'title': [], 'author': [], 'level': [], 'subcategory': []}

#read and open url to scrape
## for index, row in df.iterrows():
##     urlToScrape = row[0]

for index in course_urls:
    urlToScrape = index
    r = ur.urlopen(urlToScrape).read()
    soup = BeautifulSoup(r, "html.parser")

    #custom code
    try:
        courseTitleElement = soup.find('h1', attrs={'class': "top-card-layout__title"})
        courseTitle = courseTitleElement.text
    except Exception as e:
        courseTitle = ''
 
    try:
        courseAuthorElement = soup.find('h3', attrs={'class': "base-main-card__title"})
        courseAuthor = courseAuthorElement.text
    except Exception as e:
        courseAuthor = ''

    try:    
        courseLevelList = soup.find_all('span', attrs={'class': "top-card__metadata"})
        courseLevel = courseLevelList[1].text
    except Exception as e:
        courseLevel = ''

    try:    
##        courseCategoryList = soup.find_all('a', attrs={'class': "breadcrumb__link"})
        courseCategoryList = soup.find_all('a', attrs={'class': "pill skill-pill"})        
        courseCategory = courseCategoryList[1].text
        courseSubCategory = courseCategoryList[-1].text
    except Exception as e:
        courseLink = ''
        
    course_data['title'].append(courseTitle.strip())
    course_data['author'].append(courseAuthor.strip())
    course_data['level'].append(courseLevel.strip())
    course_data['category'].append(courseCategory.strip())
    course_data['subcategory'].append(courseSubCategory.strip())
    print(urlToScrape)
    

timestamp = str(datetime.now())[:-7].replace(' ', '-').replace(':', '')
filename = f'scrape_{timestamp}'
course_data_df = pd.DataFrame(course_data)
course_data_df.to_csv(f'{filename}.csv')
        
##    filename = f'scrape_' + f'{urlToScrape}'.split('/')[-1]
##    
##    courseChapterList = soup.find_all('div', attrs={'class': "table-of-contents__item-title"})
##    with open(f'{filename}.csv', 'w') as f:  
##        for courseChapterItem in courseChapterList:
##            try:
##                print(courseChapterItem.text.strip(), file=f)
##            except Exception as e:
##                courseChapter = ''
        




































##  =================================================================
##  REFERENCES
##  =================================================================
##  https://medium.com/swlh/data-science-essentials-scraping-data-from-the-web-3c84e194538d
##  https://towardsdatascience.com/how-to-export-pandas-dataframe-to-csv-2038e43d9c03
##  https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/
##  https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/
##  https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/
##  https://www.geeksforgeeks.org/creating-a-dataframe-using-csv-files/
##  https://dev.to/arvindmehairjan/build-a-web-crawler-to-check-for-broken-links-with-python-beautifulsoup-39mg
    
## loop through the 7 pages of undergraduate courses
## for i in range (0,6):
##     #attributes for each course
##     courseList = soup.find_all('div', attrs={'class': 'course-finder__results__item course-finder__results__item--undergraduate'})
## 
##     #loop through each course
##     for courseListItem in courseList:
##         
##         #get course name
##         try:
##             courseNameElement = courseListItem.find('div', attrs={'class': "col-sm-24 col-md-18 col-lg-20"})
##             courseName = courseNameElement.find('a').text
##         except Exception as e:
##             courseName = ''
##         
##         #get degree name
##         try:
##             degreeTypeElement = courseListItem.find('div', attrs={'class': "course-finder__results__item__award"})
##             degreeName = degreeTypeElement.text
##         except Exception as e:
##             degreeName = ''
##         
##         #get school the course is part of
##         try:
##             courseSchoolElement = courseListItem.find('div', attrs={'class': "course-finder__results__item__md course-finder__results__item__md--school"})
##             courseSchool = courseSchoolElement.find('a').text
##         except Exception as e:
##             courseSchool = ''
##             
##         #get course duration    
##         try:
##             courseDurationElement = courseListItem.find('div', attrs={'class': "course-finder__results__item__md course-finder__results__item__md--duration"})
##             courseDuration = courseDurationElement.find_all('span')[2].text
##         except Exception as e:
##             courseDuration = ''
##         
##         #get course code
##         try:
##             courseCodeElement = courseListItem.find('div', attrs={'class': "course-finder__results__item__md course-finder__results__item__md--code"})
##             courseCode = courseCodeElement.find_all('span')[2].text
##         except Exception as e:
##             courseCode = ''
##         
##         print(courseName)
##         print(degreeName)
##         print(courseSchool)
##         print(courseDuration)
##         print(courseCode)
##         print ("-------------\n")

##   =============================================
##   Sample 2
##   ---------------------------------------------
                
## from bs4 import BeautifulSoup
## import requests
## import pandas as pd
## 
## source = requests.get('https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/').text
## soup = BeautifulSoup(source, 'lxml')
## 
## 
## movie_reviews = {'ratings': [], 'critics': []}
## 
## for m in soup.find_all('table', class_='table')[0].find_all('a', href=True):
##     url = 'https://www.rottentomatoes.com/' + m['href']
##     sub_source = requests.get(url).text
##     sub_soup = BeautifulSoup(sub_source, 'lxml')
##     try:
##         critic = sub_soup.find('div', class_='col-sm-12 tomato-info hidden-xs')
##         c = critic.text.split('Critics Consensus:')[1]
##     except Exception as e:
##         c = None
## 
##     try:
##         rating = sub_soup.find('div', class_='superPageFontColor')
##         r = rating.text.split('Average Rating:')[1].split('/')[0]
##     except Exception as e:
##         r = None
## 
##     movie_reviews['ratings'].append(r)
##     movie_reviews['critics'].append(c)
## 
## movie_reviews_df = pd.DataFrame(movie_reviews) # movie_reviews_df is now a dataframe and ready to be outputed as a csv file
## movie_reviews_df.to_csv('file_name.csv')

