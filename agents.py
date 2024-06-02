import os
from crewai import Agent
from tools.tools import DescriptionTool , ImagegeneratorTool 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI GPT-4 language model
llm=ChatOpenAI(model="gpt-4o-2024-05-13")

# Define a class for handling tourist intelligence agents
class TouristIntelAgents():
    # Define a method to create an agent for finding tourist attractions
    def finder_agent(self):
        return Agent(
            role='Tourist Attraction Finder',
            goal='Name only {number} popular tourist attractions in {location} .',
            backstory="""You are an enthusiastic travel guide, passionate about discovering and sharing the best places to visit.""",
            allow_delegation=False,
            verbose=True,
            memory=False,
            llm = llm , 
        )

    # Define a method to create an agent for gathering descriptions
    def Gather_descriptions_agent(self):
        return Agent(
            role='Gather descriptions using tool',
            goal='Identify ChatGPT Description and Gemini Description ',            
            backstory="Use tools to detailed descriptions ",
            tools=[DescriptionTool.gather_detailed_descriptions],
            verbose=True,
            allow_delegation=False,
            memory=False,
            llm=llm,
    )

    # Define a method to create an agent for combining responses
    def Analyst_agent(self ):
        return Agent(
            role='combine the unique points from the ChatGPT and Gemini',
            goal='Combine unique points from ChatGPT Description and Gemini Description And merge them point wise into a cohesive final report',
            backstory=(
                "You are a seasoned tourism analyst with a passion for uncovering the most comprehensive and accurate information about various tourist attractions. "
                "Your expertise lies in comparing different sources of information and extracting unique insights that provide travelers with a well-rounded understanding of their destinations. "
                "With your analytical skills and deep knowledge of historical and cultural contexts, you ensure that no important detail is overlooked. "
                "Your analyses help travelers appreciate the full story behind each attraction, making their visits more enriching and informed."
            ),
            verbose=True,
            allow_delegation=False,
            memory=False,
            llm = llm , 
    )

    # Define a method to create an agent for generating images
    def Image_generate_agent(self):
        return Agent(
            role='generate image using tool',
            goal='generate image url of tourist attraction using tool' ,
            backstory="Use tools to generate image ",
            tools=[ImagegeneratorTool.gather_detailed_descriptions],
            verbose=True,
            allow_delegation=False,
            memory=False,
            llm = llm , 
    )
