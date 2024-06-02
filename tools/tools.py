# Import necessary libraries and modules

import openai
from openai import OpenAI
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI


import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define a class for DescriptionTool
class DescriptionTool():

    # Define class attributes for the tool name and description
    name = "GeminiDescriptionTool and ChatGPTDescriptionTool"
    description = "Tool to gather detailed descriptions of tourist attractions using ChatGoogleGenerativeAI and ChatGPTDescriptionTool"

    # Define a tool method to gather detailed descriptions of tourist attractions
    @tool("gather detailed descriptions of tourist attractions")
    def gather_detailed_descriptions(attraction_name):        
        
        """Your role is to gather detailed descriptions of tourist attractions.
        You will be given a list of tourist attractions, and you use ChatGoogleGenerativeAI and ChatOpenAI to get the descriptions"""

        # Initialize ChatGoogleGenerativeAI with specific parameters
        llm1=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.1,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))
        
        # Define a ChatPromptTemplate for generating prompts
        prompt=ChatPromptTemplate.from_messages(
            [
                ("system","Your role is to gather detailed descriptions of tourist attractions."),
                ("user","Provide a detailed description for {attraction_name} between 2000 to 2500 characters.")
            ]
        )
        # Initialize output parser for parsing model outputs
        output_parser=StrOutputParser()
        chain=prompt|llm1|output_parser
        print("hi i am gemini")

        # Invoke the chain to generate a response using ChatGoogleGenerativeAI
        response_gemini = chain.invoke({'attraction_name':attraction_name})

        llm2=ChatOpenAI(model="gpt-4o-2024-05-13"  , temperature=0.5)
        output_parser=StrOutputParser()
        chain=prompt|llm2|output_parser
        print("hi i am chatgpt")

        # Invoke the chain to generate a response using ChatOpenAI
        response_chatgpt = chain.invoke({'attraction_name':attraction_name})

        # Return the responses from ChatGoogleGenerativeAI and ChatOpenAI
        return {
            "ChatGPT Description": response_chatgpt,
            "Gemini Description": response_gemini
            }

# Define a class for ImagegeneratorTool
class ImagegeneratorTool():
    
    # Define class attributes for the tool name and description
    name = "ImagegeneratorTool"
    description = "Tool that generate image "

    # Define a tool method to generate image URLs based on prompts
    @tool("genrate url of the image based on prompt")
    def gather_detailed_descriptions(prompt):        
        
        """Your role is to generate image of tourist attractions."""

        # Use OpenAI client to generate image based on the prompt
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
            )


        print("hi i am image generator")

        # Extract the image URL from the response
        image_url = response.data[0].url
        return image_url

