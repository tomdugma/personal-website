import streamlit as st
import pandas as pd

@st.cache
def coding():
    data = pd.DataFrame([
        {
            'programming language': 'Python ',
            'level': 80,
            'definition': 'Free like a Butterfly',
            'comments': 'This website is written mostly in Python (streamlit), also this is my favorite language'
        },
        {
            'programming language': 'Java',
            'level': 80,
            'definition': 'My first programming language',
            'comments': 'Did few project in my studies at Ben Gurion University.'
        },
        {
            'programming language': 'C++',
            'level': 70,
            'definition': 'Most powerfull language',
            'comments': 'Did few project in my studies at Ben Gurion University.'
        },
        {
            'programming language': 'C',
            'level': 70,
            'definition': 'Darkest hours in my life came from here',
            'comments': 'Did few project in my studies at Ben Gurion University.'
        },
        {
            'programming language': 'C#',
            'level': 70,
            'definition': 'Reminds me of Java',
            'comments': 'Did few project in my studies at Ben Gurion University.'
        },
        {
            'programming language': 'SQL',
            'level': 70,
            'definition': 'Can write the code',
            'comments': 'Can write sophisticated queries.'
        },
        {
            'programming language': 'R',
            'level': 20,
            'definition': 'Powerful tool, probably not for me',
            'comments': 'Despite preferring pandas, I can use R if needed.'
        },
        {
            'programming language': 'HTML',
            'level': 50,
            'definition': 'Would like to gain more experience',
            'comments': 'Used HTML and CSS in my freelance project and in this website.'
        },
        {
            'programming language': 'JS',
            'level': 50,
            'definition': 'Would like to gain more experience',
            'comments': 'Had a course on JS, used it in a project.'
        }
    ])
    return data

@st.cache
def courses():
    data = pd.DataFrame([
        {
            'Course': 'Deep Learning Specialization',
            'Organization': 'deeplearning.ai',
            'Topic': 'Data Science / AI',
            'Platform': 'coursera.org',
            'Status': 'Completed',
            'Date': '2020-05-17',
            'Certificate': 'https://www.coursera.org/account/accomplishments/specialization/AVD5TJYKCR3L'
        },
        {
            'Course': 'Strategic Management of Innovation',
            'Organization': 'HEC Paris',
            'Topic': 'Business Strategy',
            'Platform': 'coursera.org',
            'Date': '2019-09-19',
            'Status': 'Completed',
            'Certificate': 'https://www.coursera.org/account/accomplishments/verify/H5E2CQW754W8',
        },
        {
            'Course': 'How to Build Digital Products',
            'Organization': 'Product School',
            'Topic': 'Other',
            'Platform': 'productschool.teachable.com',
            'Date': '2020-06-20',
            'Status': 'Completed',
            'Certificate': 'cert_kr5drxm0',
        },
        {
            'Course': 'How to Build and Grow Product Teams',
            'Organization': 'Product School',
            'Topic': 'Other',
            'Platform': 'productschool.teachable.com',
            'Date': '2020-09-01',
            'Status': 'In progress',
            'Certificate': '',
        },
        {
            'Course': 'Product Design',
            'Organization': 'Product School',
            'Topic': 'Design and UX/UI',
            'Platform': 'productschool.teachable.com',
            'Date': '2020-09-01',
            'Status': 'Completed',
            'Certificate': '',
        },
        {
            'Course': 'The Science of Everyday Thinking',
            'Organization': 'University of Queensland',
            'Topic': 'Other',
            'Platform': 'edx.com',
            'Date': '2014-07-02',
            'Status': 'Completed',
            'Certificate': 'https://verify.edx.org/cert/ca2ff3759ed84b4399ab34645e801ea0',
        },
        {
            'Course': 'Analyzing and Visualizing Data with Power BI',
            'Organization': 'Microsoft',
            'Topic': 'Analytics',
            'Platform': 'edx.com',
            'Date': '2016-12-28',
            'Status': 'Completed',
            'Certificate': 'https://courses.edx.org/certificates/8548fd38adfa4f68a940c54a45f89ada',
        },
        {
            'Course': 'Brand and Product Management',
            'Organization': 'IE Business School',
            'Topic': 'Marketing / Sales',
            'Platform': 'coursera.org',
            'Date': '2020-04-16',
            'Status': 'Completed',
            'Certificate': 'https://www.coursera.org/account/accomplishments/records/SSFASDY293QL',
        },
        {
            'Course': 'Data Scientist with Python track',
            'Organization': 'DataCamp',
            'Topic': 'Data Science / AI',
            'Platform': 'datacamp.com',
            'Date': '2019-06-10',
            'Status': 'Completed',
            'Certificate': 'https://www.datacamp.com/statement-of-accomplishment/track/65382807a81e490fa943aa8f06da188ca789e3eb'
        },
        {
            'Course': 'Learn Growth Hacking',
            'Organization': 'One Month',
            'Topic': "Marketing / Sales",
            'Platform': 'onemonth.com',
            'Date': '2019-10-15',
            'Status': 'Completed',
            'Certificate': ''
        },
        {
            'Course': 'Design Thinking',
            'Organization': 'IE Business School',
            'Topic': 'Design and UX/UI',
            'Platform': 'on-campus',
            'Status': 'Completed',
            'Date': '2019-11-01',
            'Certificate': ''
        },
        {
            'Course': 'Agile Project Management',
            'Organization': 'IE Business School',
            'Topic': 'Other',
            'Platform': 'on-campus',
            'Status': 'Completed',
            'Date': '2019-11-01',
            'Certificate': ''
        },
        {
            'Course': 'Analytics for Financial Services',
            'Organization': 'IE University',
            'Topic': 'Industry Knowledge',
            'Platform': 'on-campus',
            'Status': 'Completed',
            'Date': '2020-03-01',
            'Certificate': ''
        },
        {
            'Course': 'Analytics for Retail & Consumer',
            'Organization': 'IE University',
            'Topic': 'Industry Knowledge',
            'Platform': 'on-campus',
            'Status': 'Completed',
            'Date': '2020-03-01',
            'Certificate': ''
        },
        {
            'Course': 'Big Data & Health',
            'Organization': 'IE University',
            'Topic': 'Industry Knowledge',
            'Platform': 'on-campus',
            'Status': 'Completed',
            'Date': '2020-03-01',
            'Certificate': ''
        },
        {
            'Course': 'Marketing Intelligence',
            'Organization': 'IE University',
            'Topic': 'Marketing / Sales',
            'Platform': 'on-campus',
            'Status': 'Completed',
            'Date': '2020-03-01',
            'Certificate': ''
        },
        {
            'Course': 'Insight Selling',
            'Organization': 'Microsoft',
            'Topic': 'Marketing / Sales',
            'Platform': 'Microsoft (internal)',
            'Status': 'Completed',
            'Date': '2017-10-27',
            'Certificate': 'https://www.youracclaim.com/badges/1bcd0fd8-a58d-4527-875c-21af1d37002d/public_url'
        },
        {
            'Course': 'Entrepreneurial Management',
            'Organization': 'UW-Madison',
            'Topic': 'Other',
            'Platform': 'on-campus',
            'Status': 'Completed',
            'Date': '2015-08-09',
            'Certificate': ''
        },
        {
            'Course': 'Docker Fundamentals',
            'Organization': 'A Cloud Guru',
            'Topic': 'Full Stack dev',
            'Platform': 'acloud.guru',
            'Status': 'Completed',
            'Date': '2020-07-30',
            'Certificate': ''
        },
        {
            'Course': 'JavaScript Algorithms and Data Structures',
            'Organization': 'freeCodeCamp.org',
            'Topic': 'Full Stack dev',
            'Platform': 'freeCodeCamp.org',
            'Status': 'Completed',
            'Date': '2020-11-08',
            'Certificate': 'https://www.freecodecamp.org/certification/adiletgaparov/javascript-algorithms-and-data-structures'
        }
    ])

    return data