import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import pickle
import pandas as pd
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# df = pickle.load(open('df.pkl','rb'))
df = pd.read_pickle("df.pkl")
similarity = pickle.load(open('similarity.pkl','rb'))

def recommendation(title):
    idx = df[df['Title']==title].index[0]
    idx = df.index.get_loc(idx)
    distances= sorted(list(enumerate(similarity[idx])),reverse=True,key=lambda x:x[1])[1:20]

    jobs = []
    for i in distances:
        jobs.append(df.iloc[i[0]].Title)

    return jobs

def streamlit_menu():
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Candidate Search", "Company Search", "Candidate Login", "Contact"],
            icons=["house", "book", "book", "book", "envelope"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
        )
        return selected

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# web app
selected = streamlit_menu()
if selected == "Home":
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            #st.header("Personalized Job Search for you")
            st.title("Unlock Hiring")
            st.write("Explore opportunities from across the globe to learn, showcase skills, gain CV points & get hired by your dream company.")

        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")

        st.write("---")
        for i in range(0,8):
            st.write(" ")
        l, r = st.columns(2)
        with l:
            st.title("Browse Job/Internship That's Right For You!")
            st.subheader("Find a role that fits your career aspirations.")
            st.subheader("Pick The Right Opportunity!")
            st.subheader("Explore opportunities that best suits your skills and interests!")
        with r:
            st.image("Design.jpg")
        for i in range(0,8):
            st.write(" ")
        st.write("---")
        l,r=st.columns(2)
        with l:
            st.title("Host Your Own Oppurtunity")
            st.subheader("Engage with a diverse talent pool or hire the best minds from 9Mn+ users.")
        with r:
            st.image("screen2.png")
        for i in range(0,8):
            st.write(" ")
        st.write("---")
        st.markdown("<h1 style='text-align: center;'>Industry veterans trust us</h1>", unsafe_allow_html=True)
        images = ['walmart.png', 'wipro.jpg', 'flip.webp', 'aditya.png', 'asian.png']

        # Resize images
        resized_images = []
        for image_path in images:
            img = Image.open(image_path)
            img_resized = img.resize((250, 150))
            resized_images.append(img_resized)
        st.image([resized_images[0], resized_images[1], resized_images[2], resized_images[3], resized_images[4]])
        for i in range(0,8):
            st.write(" ")
        st.write("---")
        st.markdown("<h1 style='text-align: center;'>Our Numbers</h1>", unsafe_allow_html=True)
        l, m, r = st.columns(3)
        with l:
            st.markdown("<div style='text-align: center'> <h1>9,000,000+</h1></div>", unsafe_allow_html=True)
            st.markdown("<div style='text-align: center'> <h3>Students</h3></div>", unsafe_allow_html=True)
            st.markdown("<div style='text-align: center'> <h1>42,000+</h1></div>", unsafe_allow_html=True)
            st.markdown("<div style='text-align: center'> <h3>Colleges and Companies</h3></div>", unsafe_allow_html=True)
        with m:
            st.markdown("<div style='text-align: center'> <h1>78+</h1></div>", unsafe_allow_html=True)
            st.markdown("<div style='text-align: center'> <h3>Countries</h3></div>", unsafe_allow_html=True)
            st.markdown("<div style='text-align: center'> <h1>1,30,000+</h1></div>", unsafe_allow_html=True)
            st.markdown("<div style='text-align: center'> <h3>Oppurtunities</h3></div>", unsafe_allow_html=True)
        with r:
            st.markdown("<div style='text-align: center'> <h1>800+</h1></div>", unsafe_allow_html=True)
            st.markdown("<div style='text-align: center'> <h3>Brands Trust Us</h3></div>", unsafe_allow_html=True)
            st.markdown("<div style='text-align: center'> <h1>22,300,000+</h1></div>", unsafe_allow_html=True)
            st.markdown("<div style='text-align: center'> <h3>Assessments</h3></div>", unsafe_allow_html=True)


if selected == "Candidate Search":
    st.title('Find your Dream Job 🤓')
    with st.form(key="vendor_form"):
        title = st.selectbox('Job Title*', df['Title'])

        job_type = ["Intern", "Job", "Contract"]
        selected_job = st.radio("Job Nature", job_type)

        workplace_type = ["In Office", "Work from Home", "Field", "Contract"]
        selected_workplace = st.radio("Workplace Type", workplace_type)

        location = st.text_input(label="Work Location*")
        st.markdown("**required*")
        submit_button = st.form_submit_button(label="Submit Details")
        if submit_button:
            jobs = recommendation(title)
            if jobs:
                flag = 0
                cards = []
                for i in jobs:
                    flag = flag + 1
                    cards.append(i)
                n_rows = 5
                n_cols = 4
                rows = [st.container() for _ in range(n_rows)]
                cols_per_row = [r.columns(n_cols) for r in rows]
                cols = [column for row in cols_per_row for column in row]
                for image_index, card in enumerate(cards):
                    cols[image_index].image("back.jpg")
                    cols[image_index].write("Job Title: "+card)
                    cols[image_index]._form_submit_button(label='Apply')

if selected == "Company Search":
    st.title("Find Exceptional Talent")
    with st.form(key="vendor_form"):
        company_name = st.text_input(label="Company you are hiring for.*")

        job_title = st.text_input(label="Job Title/Role*")

        job_type=["Intern", "Job", "Contract"]
        selected_job = st.radio("Job Nature",job_type)

        workplace_type = ["In Office", "Work from Home", "Field", "Contract"]
        selected_workplace = st.radio("Workplace Type", workplace_type)

        location = st.text_input(label="Work Location*")

        skills = st.text_input(label="Skills Looking For*")

        experience = st.slider("Years of Experience", 0, 50, 5)

        soft_skills = st.text_input(label="Soft Skills Needed*")

        salary = st.number_input(label="Salary", step=100)
        referral = st.checkbox("Referral Allowed")
        onboarding_date = st.date_input(label="Onboarding Date")
        job_desc = st.text_area(label="Job Description")

        st.markdown("**required*")

        submit_button = st.form_submit_button(label="Submit Details")
        if submit_button:
            st.write("Submitted")

if selected == "Candidate Login":
    with st.form(key="vendor_form"):
        name = st.text_input(label="Your Name*")
        college = st.text_input(label="College Name*")
        batch = st.number_input(label="Year of Passing*",step=1, min_value=1970, value= 2025)
        branch = st.text_input(label="Your Branch*")
        cgpa = st.number_input(label="Enter CGPA*",step=0.01, min_value=0.00, value= 8.00)
        file = st.file_uploader("Select your resume*")
        st.markdown("**required*")
        submit_button = st.form_submit_button(label="Save Details")
        if submit_button:
            st.write("Submitted")

if selected == "Contact":
    st.title("FAQ")
    st.subheader("Are you facing any technical problems?")
    st.write("For technical help (issues with login, password, page not being displayed, etc.), write to us at help@unstop.com. We will resolve the problem and get back to you at the earliest.")
    st.subheader("Do you wish to partner with us?")
    st.write("Send in your proposals at partner@unstop.com. One of our team members will get in touch with you within 24 hours.")
    st.subheader("Do you have any suggestions/feedback for us?")
    st.write("We value any and all feedback/suggestions, please write to us at feedback@unstop.com with all your suggestions and comments. Your valuable feedback can be on anything from a section or a listing or our color combination. We will be happy to read them and take appropriate action.")
    st.subheader("Need help in Organizing Competitions?")
    st.write("We will conceptualize, organize and market various competitions, quizzes and simulation games for you to enable new dimensions of employer branding, competition led recruitment of future leaders, and employee engagement programs.")
    st.write("---")
    st.subheader("Stay Connected")
    st.write("sales@unstop.com")
    st.write("+91-9311777388 Mon to Fri, 9 AM to 6 PM")
with st.container():
    for i in range(0, 8):
        st.write(" ")
    st.write("---")
    l, m, r = st.columns(3)
    with l:
        st.subheader("Discover How")
        st.write("Recommendations")
        st.write("AI Insights")
        st.write("Analysis")
    with m:
        st.subheader("Join Our Growing")
        st.write("Get Assistance")
        st.write("Follow on Twitter")
    with r:
        st.subheader("Stay Connected")
        st.write("Explore career")
        st.write("Read Our Latest")




