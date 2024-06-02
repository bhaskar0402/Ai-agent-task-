# Import necessary libraries and modules

from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents import TouristIntelAgents
from tasks import TouristIntelTasks
import os 
import json
import pandas as pd
import re
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the agents and tasks
agents = TouristIntelAgents()
tasks = TouristIntelTasks()

# Initialize the OpenAI GPT-4 language model
llm=ChatOpenAI(model="gpt-4o-2024-05-13" , temperature= 0.1)


# Instantiate the agents
finder_agent = agents.finder_agent()
Gather_descriptions_agent = agents.Gather_descriptions_agent()
Analyst_agent = agents.Analyst_agent()
Image_generate_agent = agents.Image_generate_agent()


# Instantiate the tasks
find_attractions_task = tasks.find_attractions_task(finder_agent)
gather_description_task = tasks.gather_description_task(Gather_descriptions_agent )
combine_responses_task = tasks.combine_responses_task(Analyst_agent )
image_generate_task = tasks.generate_image_task(Image_generate_agent , [combine_responses_task] )


# Form the crew
def crew1(location , number):
    # Define a crew for finding attractions
    crew1 = Crew(
        agents=[finder_agent ],
        tasks=[find_attractions_task ],
        process=Process.sequential,
        verbose=2
    )
    # Kick off the crew to find attractions based on location and number
    attraction_names = crew1.kickoff(inputs={'location': location , 'number': number })
    return attraction_names

def crew2(attraction_name):
    # Define a crew for gathering descriptions, analysis, and image generation
    crew2 = Crew(
        agents=[Gather_descriptions_agent , Analyst_agent , Image_generate_agent],
        tasks=[ combine_responses_task , image_generate_task ],
        process=Process.hierarchical,
        manager_llm=llm,
        verbose=2
    )
    # Kick off the crew for gathering descriptions, analysis, and image generation for a specific attraction
    results = crew2.kickoff(inputs={'attraction_name': attraction_name })
    return results
    

# Kick off the crew's work
print("## Welcome to tourist attraction finder")
print('-------------------------------')
country = input(""" Enter the country Name """)
cities = input(""" Enter the cities name """)
number = input(""" Enter the number of tourist attractions """)

print('-------------------------------')


location = f"{country}, {cities}"
number = number
attraction_names = crew1(location , number)
attraction_names = attraction_names.split(", ")

for attraction_name in attraction_names :
    
    # Kick off crew2 for each attraction to gather descriptions, analysis, and generate images
    results = crew2(attraction_name)
    print(results)

    # Extract cleaned data from results
    cleaned_data_str = re.search(r'(\[.*\])', results, re.DOTALL).group(1)

    # Convert cleaned data to JSON format and create a DataFrame
    attractions_info_list = json.loads(cleaned_data_str)   
    df = pd.DataFrame(attractions_info_list)
    excel_file_name = 'tourist_attractions_description.xlsx'

    # Check if the Excel file exists
    if os.path.exists(excel_file_name):
        # If the file exists, read the existing data
        existing_df = pd.read_excel(excel_file_name)
        # Append the new data to the existing data
        updated_df = pd.concat([existing_df, df], ignore_index=True)
    else:
        # If the file does not exist, use the new data
        updated_df = df
    
    # Save the updated data to the Excel file
    updated_df.to_excel(excel_file_name, index=False)
    print(f"Excel file '{excel_file_name}' created/updated successfully.")


