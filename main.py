import streamlit as st
import streamlit.components.v1 as components
import altair as alt
import pandas as pd

# Header
st.set_page_config(
    page_title='Tom Dugma | personal website',
    page_icon='media/avatar.png',
    layout='centered',
    initial_sidebar_state='auto'
)

from textblob import TextBlob

from utils import img_to_bytes, read_markdown_file, gantt_chart, language_chart, coding_language_chart

# import resume content
from contact_info import socia_media_links
from resume import coding, courses
# from content.resume import history, languages, courses, coding

# import project content
# from content.this_website_pm.project_wikihow_wireframes import wireframes

# project_wikihow_engineering = read_markdown_file('content/this_website_pm/project_wikihow_engineering.md')
# project_wikihow_backlog = read_markdown_file('content/this_website_pm/backlog.html')
project_wikihow_prd = read_markdown_file('html/projectTable.html')
# project_wikihow_design = read_markdown_file('content/this_website_pm/project_wikihow_design.md')
# project_music_recommender = read_markdown_file('content/music_recommender/project_music_recommender.md')
# project_music_recommender_info = read_markdown_file('content/music_recommender/project_music_recommender_info.md')

# Sidebar
st.sidebar.markdown("# Navigation")
navigation_options = ['Home', 'Projects', 'Resume']
page = st.sidebar.radio(label = '', options = navigation_options, key='0')
st.sidebar.markdown('---')

# Main
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden; padding:0}
"""
# Hide streamlit style (footer and hamburger menu)
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if page == 'Home':

    # Additional sidebar
    st.sidebar.markdown('### Hear me out !')
    if st.sidebar.button('A few words from me :) '):
        st.sidebar.audio('media/sound-presenting.m4a')

    # Main page

    avatar = "<img src='data:image/png;base64,{}' class='img-fluid rounded-circle mx-auto d-block' style='max-width:25%'>".format(
        img_to_bytes("media/avatar.png")
    )
    st.markdown(avatar, unsafe_allow_html=True)
    st.write(read_markdown_file("data/intro.md"), unsafe_allow_html=True)

    components.html(socia_media_links)

elif page == 'Projects':

    # Additional sidebar

    feedback = st.sidebar.text_input('Feedback')
    if feedback:
        st.sidebar.markdown(f'Your feedback: {feedback}')
        st.sidebar.warning("""
                    Hi, thanks for giving feedback! I appreciate it! 
                    As you will see in the backlog under "How I built this website", I have not implemented this feature yet.
                    However, feedback is a gift. Please, share it with me again directly 👇. 
                    """)
        st.sidebar.markdown(socia_media_links, unsafe_allow_html=True)

    # Main page
    st.write(
        """
        <div style = "text-align: left">
            <div style = "display: inline-block; max-width: 60%">
            <h3>Projects</h3><br/>
        </div></div >
        """,
        unsafe_allow_html=True
    )

    if st.checkbox('How I built this website'):

        st.write('**Website Development**')
        st.markdown(read_markdown_file("data/siteDetails.md"),unsafe_allow_html=True)
        st.write('')
        st.write('')
        st.subheader('Below: how much lines of code per language')
        st.image('media/CodeCount.png')
        st.write('---')


    if st.checkbox('Other projects by me'):

        st.write('''
        Need to complete
            ''')


elif page == 'Resume':

    # Additional sidebar
    st.sidebar.info('Tip: hover over or click on charts to get more information')
    if st.sidebar.button('Contact me'):
        st.sidebar.markdown(socia_media_links, unsafe_allow_html=True)

    # Main page
    # Experience section
    experience_subtitle = '''
        <div style="text-align: center"><div style="display: inline-block; max-width: 60%"> 
        <h2>Experience</h2>
        <br/>
        </div></div>
        '''
    # history_df = history()
    # st.write(experience_subtitle, unsafe_allow_html=True)
    #
    # gantt = gantt_chart(history_df.query("org != 'Key moments'"))
    # scatter = alt.Chart(history_df.query("org == 'Key moments'")).mark_circle().encode(
    #     x=alt.X('start:T', axis=alt.Axis(title='', orient='top', format='%b %Y')),
    #     y=alt.Y('org:N', sort=None, axis=alt.Axis(title='')),
    #     tooltip=['location', 'description'],
    #     color=alt.Color('color', scale=None)
    # ).interactive()
    # resume_chart = alt.layer(gantt, scatter).configure_view(strokeWidth=0.5).properties(width=660)
    # st.altair_chart(resume_chart, use_container_width=True)
    #
    # st.write('---')

    # Skills section
    skills_subtitle = '''
        <div style="text-align: center"><div style="display: inline-block; max-width: 60%"> 
        <h2 style="color:blue">Skills</h2>
        <br/>
        </div></div>
        '''
    st.write(skills_subtitle, unsafe_allow_html=True)

    coding_chart = coding_language_chart(coding())
    st.altair_chart(coding_chart, use_container_width=True)
    st.write('---')

    # Courses section
    courses_subtitle = '''
        <div style="text-align: center"><div style="display: inline-block; max-width: 60%"> 
        <h2 style="color:blue">Courses</h2>
        <br/>
        </div></div>
        '''
    st.write(courses_subtitle, unsafe_allow_html=True)

    # courses_df = courses()
    # courses_columns = ['Course', 'Organization', 'Status']
    # chosen_topic = st.multiselect('Topic',  list(courses_df.Topic.unique()), list(courses_df.Topic.unique()))
    # if not chosen_topic:
    #     st.write('')
    # else:
    #     table = st.empty()
    #     add_columns = st.multiselect('Additional information', ['Certificate', 'Platform', 'Date', 'Topic'])
    #     courses_columns = courses_columns + add_columns
    #     table.dataframe(courses_df.loc[courses_df.Topic.isin(chosen_topic), courses_columns])

elif page == 'Chatbot':
    st.write('Need to complete')