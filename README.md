# Tourist Intelligence Toolkit

## Overview

The Tourist Intelligence Toolkit is a set of tools and agents designed to gather detailed information about tourist attractions and generate related content. This toolkit leverages various AI models and tools to streamline the process of collecting attraction descriptions and generating associated images.

## Contents

1. **DescriptionTool**
   - Name: GeminiDescriptionTool and ChatGPTDescriptionTool
   - Description: Tool to gather detailed descriptions of tourist attractions using ChatGoogleGenerativeAI and ChatGPTDescriptionTool

2. **ImagegeneratorTool**
   - Name: ImagegeneratorTool
   - Description: Tool that generates image URLs based on prompts using OpenAI's image generation model (model="dall-e-3").

3. **TouristIntelAgents**
   - Roles:
     - Tourist Attraction Finder
     - Gather descriptions using tool
     - Combine the unique points from the ChatGPT and Gemini
     - Generate image using tool

## Features

- **Tourist Attraction Finder**
  - Goal: Name only {number} popular tourist attractions in {location}.
  - Backstory: An enthusiastic travel guide passionate about discovering and sharing the best places to visit.

- **Gather descriptions using tool**
  - Goal: Identify ChatGPT Description and Gemini Description.
  - Backstory: Use tools to gather detailed descriptions of tourist attractions.

- **Combine the unique points from the ChatGPT and Gemini**
  - Goal: Combine unique points from ChatGPT Description and Gemini Description and merge them pointwise into a cohesive final report.
  - Backstory: A seasoned tourism analyst passionate about uncovering comprehensive information about attractions.

- **Generate image using tool**
  - Goal: Generate image URL of tourist attraction using ImagegeneratorTool.
  - Backstory: Use tools to generate images related to tourist attractions.


## Getting Started

1. Clone the repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file.
3. Set up your environment variables in a `.env` file (see example.env for reference).
4. Run the main script to kick off the tourist attraction analysis and content generation process.

## Usage

1. Run `python main.py` to start the Tourist Intelligence Toolkit.
2. Follow the prompts to enter the country, cities, and the number of tourist attractions you want to analyze.
3. The toolkit will gather detailed descriptions, combine unique points, and generate image URLs for the specified tourist attractions.
4. Results will be saved in an Excel file named `tourist_attractions_description.xlsx`.

