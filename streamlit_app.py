import streamlit as st
from llm import analyze_resume, answer_question
from data import get_job_descriptions, get_job_by_id, init_db

# Initialize database when app starts
init_db()

def show_about_page():
    """Renders the About page for Mentra"""
    st.markdown("""
    <h1 style="text-align: center; color: #1E88E5;">About Mentra</h1>
    <h3 style="text-align: center; color: #424242; margin-bottom: 30px;">AI-Powered Resume Coach</h3>
    """, unsafe_allow_html=True)
    
    # Project Overview
    st.markdown("""
    <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h3 style="color: #1E88E5;">Project Overview</h3>
        <p style="font-size: 16px; line-height: 1.6;">
            Mentra is an advanced resume analysis tool designed to help job seekers improve their applications. 
            By comparing resumes against job descriptions, Mentra provides personalized coaching advice, 
            highlights qualification gaps, and identifies key strengths that make candidates stand out.
        </p>
        <p style="font-size: 16px; line-height: 1.6;">
            With state-of-the-art language models and a user-friendly interface, Mentra offers actionable 
            feedback and maintains an interactive chat feature for follow-up questions, making the job 
            application process more effective and streamlined.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Features section - split into columns
    st.markdown("<h2 style='text-align: center; color: #1E88E5; margin: 30px 0;'>Key Features</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; height: 100%;">
            <h3 style="color: #1E88E5;">Resume Analysis</h3>
            <ul style="font-size: 16px; line-height: 1.8;">
                <li><strong>Qualification Assessment</strong>: Evaluates if you're qualified for a position with detailed reasoning</li>
                <li><strong>Gap Analysis</strong>: Identifies missing skills or requirements from your resume</li>
                <li><strong>Strength Highlighting</strong>: Showcases your relevant qualifications that match the job</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; height: 100%;">
            <h3 style="color: #1E88E5;">Interactive Coaching</h3>
            <ul style="font-size: 16px; line-height: 1.8;">
                <li><strong>Interactive Chat</strong>: Ask follow-up questions about your analysis</li>
                <li><strong>Pre-loaded Job Database</strong>: Common job descriptions ready for analysis</li>
                <li><strong>Improvement Suggestions</strong>: Actionable advice to enhance your application</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Technology Stack
    st.markdown("<h2 style='text-align: center; color: #1E88E5; margin: 30px 0;'>Technology Stack</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; height: 100%;">
            <div style="text-align: center;">
                <h4 style="color: #424242;">Frontend</h4>
            </div>
            <ul style="font-size: 16px; line-height: 1.8;">
                <li><strong>Streamlit</strong>: Interactive web application framework</li>
                <li><strong>Python</strong>: Core programming language</li>
                <li><strong>Custom CSS</strong>: Enhanced visual styling</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; height: 100%;">
            <div style="text-align: center;">
                <h4 style="color: #424242;">AI & Machine Learning</h4>
            </div>
            <ul style="font-size: 16px; line-height: 1.8;">
                <li><strong>LangChain</strong>: Framework for LLM-powered applications</li>
                <li><strong>OpenAI GPT Models</strong>: Advanced language processing</li>
                <li><strong>Custom Prompt Engineering</strong>: Tailored for resume analysis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; height: 100%;">
            <div style="text-align: center;">
                <h4 style="color: #424242;">Backend</h4>
            </div>
            <ul style="font-size: 16px; line-height: 1.8;">
                <li><strong>SQLite</strong>: Lightweight database for job descriptions</li>
                <li><strong>LangChain Core</strong>: Prompt management and templating</li>
                <li><strong>Environment Management</strong>: Secure API key handling</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # How It Works
    st.markdown("<h2 style='text-align: center; color: #1E88E5; margin: 30px 0;'>How It Works</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h3 style="color: #1E88E5;">Process Flow</h3>
        <ol style="font-size: 16px; line-height: 1.8;">
            <li><strong>Input Your Resume</strong>: Paste your resume text into the application</li>
            <li><strong>Select a Job Description</strong>: Choose from our database or enter a custom position</li>
            <li><strong>Generate Analysis</strong>: Our AI analyzes the match between your resume and the job</li>
            <li><strong>Review Results</strong>: See qualification assessment, gaps, and strengths</li>
            <li><strong>Ask Questions</strong>: Use the chat interface for follow-up inquiries</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # System Architecture
    st.markdown("<h2 style='text-align: center; color: #1E88E5; margin: 30px 0;'>System Architecture</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h3 style="color: #1E88E5;">Architecture Overview</h3>
        <p style="font-size: 16px; line-height: 1.6; margin-bottom: 20px;">
            Mentra employs a streamlined architecture that handles the entire process from user input to AI analysis and result presentation:
        </p>
        
        <div style="width: 100%; text-align: center; background-color: #e9ecef; padding: 20px; border-radius: 5px;">
            <p style="font-family: monospace; text-align: left; white-space: pre-line; line-height: 1.4; font-size: 14px;">
            User → Streamlit Interface → LangChain Processing → OpenAI Language Models → Analysis Results → User
            
            Database ↔ Job Descriptions ↔ LangChain Processing
            </p>
        </div>
        
        <p style="font-size: 16px; line-height: 1.6; margin-top: 20px;">
            This architecture ensures efficient processing of resume data, accurate analysis through advanced LLMs, 
            and seamless presentation of results in an intuitive user interface.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 20px; font-size: 14px; color: #757575;">
        <p>© 2023 Mentra | AI-Powered Resume Coaching</p>
    </div>
    """, unsafe_allow_html=True)

def show_main_app():
    """Shows the main resume analysis application"""
    st.subheader("Enter Your Resume")
    
    # Sidebar for job selection
    st.sidebar.title("Job Selection")
    job_descriptions = get_job_descriptions()
    job_options = [f"{job['title']} - {job['company']}" for job in job_descriptions]
    job_options.append("Custom Job Description")
    
    selected_job_option = st.sidebar.selectbox("Select a job", job_options)
    
    if selected_job_option == "Custom Job Description":
        job_description = st.sidebar.text_area("Enter job description", height=300)
    else:
        job_id = job_options.index(selected_job_option) + 1  # Adding 1 because SQLite IDs typically start at 1
        job = get_job_by_id(job_id)
        
        # Handle case when job isn't found
        if job is None:
            st.error(f"Job with ID {job_id} not found. Please select another job or enter a custom job description.")
            return
            
        job_description = job['content']
        st.sidebar.text_area("Job Description", job_description, height=200)
    
    # Main content - Resume input
    resume_text = st.text_area("Paste your resume here", height=300)
    
    # Analysis button
    if st.button("Analyze Resume"):
        if not resume_text or not job_description:
            st.error("Please provide both resume and job description")
        else:
            with st.spinner("Analyzing your resume..."):
                analysis = analyze_resume(resume_text, job_description)
            
            # Store in session state for chat
            st.session_state.resume = resume_text
            st.session_state.job = job_description
            st.session_state.analysis = analysis
            st.session_state.chat_history = []
            
            # Display analysis
            st.subheader("Analysis Results")
            st.write(analysis)
    
    # Chat interface (only show after analysis)
    if 'analysis' in st.session_state:
        st.subheader("Ask Follow-up Questions")
        question = st.text_input("Your question:")
        
        if st.button("Ask"):
            if question:
                with st.spinner("Getting answer..."):
                    answer = answer_question(
                        question, 
                        st.session_state.resume, 
                        st.session_state.job,
                        st.session_state.analysis,
                        st.session_state.chat_history
                    )
                
                # Add to chat history
                st.session_state.chat_history.append({"question": question, "answer": answer})
                
                # Display chat history
                for chat in st.session_state.chat_history:
                    st.write(f"**You:** {chat['question']}")
                    st.write(f"**Coach:** {chat['answer']}")
                    st.write("---")

def main():
    """Main function to run the Streamlit app"""
    st.set_page_config(page_title="Mentra - Resume Coach", page_icon="📝", layout="wide")
    
    st.title("Mentra Resume Coach")
    
    # Navigation with tabs
    tab1, tab2 = st.tabs(["Resume Analysis", "About"])
    
    with tab1:
        show_main_app()
    
    with tab2:
        show_about_page()

if __name__ == "__main__":
    main() 