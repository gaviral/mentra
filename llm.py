import os
from openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from prompts import ANALYSIS_TEMPLATE, CHAT_TEMPLATE

def get_llm():
    """Initialize the LLM connection via OpenAI API"""
    # Initialize OpenAI client
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set. Please set it in the .env file.")
    
    # Use ChatOpenAI from langchain_openai
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.75,
        max_tokens=3000,
        openai_api_key=api_key
    )

def analyze_resume(resume_text, job_description):
    """Analyze resume against job description"""
    llm = get_llm()
    
    # Create prompt for analysis
    prompt = PromptTemplate(
        template=ANALYSIS_TEMPLATE,
        input_variables=["resume", "job_description"]
    )
    
    # Create chain
    chain = prompt | llm
    
    # Run analysis
    response = chain.invoke({"resume": resume_text, "job_description": job_description})
    
    return response.content

def answer_question(question, resume, job_description, analysis, chat_history):
    """Answer follow-up questions about the analysis"""
    llm = get_llm()
    
    # Format chat history
    formatted_history = ""
    for chat in chat_history:
        formatted_history += f"User: {chat['question']}\nCoach: {chat['answer']}\n\n"
    
    # Create prompt for chat
    prompt = PromptTemplate(
        template=CHAT_TEMPLATE,
        input_variables=["resume", "job_description", "analysis", "chat_history", "question"]
    )
    
    # Create chain
    chain = prompt | llm
    
    # Run question answering
    response = chain.invoke({
        "resume": resume,
        "job_description": job_description,
        "analysis": analysis,
        "chat_history": formatted_history,
        "question": question
    })
    
    return response.content 