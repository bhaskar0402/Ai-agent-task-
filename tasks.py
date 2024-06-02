from crewai import Task

# Define a class for handling tourist intelligence tasks
class TouristIntelTasks():

    # Define a method to create a task for finding tourist attractions
    def find_attractions_task(self, agent):
        return Task(
            description= "Name only {number} tourist attractions in {location}. "
                         "Provide only the names of the tourist attractions.",
            agent=agent,
            async_execution=False,
            expected_output=" A list containing tourist attractions name " 
                            " Example [Eiffel Tower,Musée du Louvre ,Château de Versailles ,Côte d'Azur ,Mont Saint-Michel ]",
        )
    
    # Define a method to create a task for gathering descriptions
    def gather_description_task(self , agent):
        return Task(
            description="Use DescriptionTool tools to gather detailed description of {attraction_name}  " , 
            agent=agent,
            async_execution=False,
            expected_output=
                "A list containing dictionaries  Country : , City : , Attraction Name : ,  ChatGPT Description  :  ,  Gemini Description :  ", 
                )

    # Define a method to create a task for combining responses
    def combine_responses_task(self , agent ): 
        return Task(
            description="Combine the unique points from ChatGPT Description and Gemini Description for {attraction_name}  "
                        "Ensure that the final report highlights the key insights and avoids redundancy.",
            agent=agent,
            async_execution=False,
            expected_output="A list containing dictionaries country : , city : , Attraction Name : ,  ChatGPT Description  :  ,  Gemini Description :  , Combine unique points :  "
        )

    # Define a method to create a task for generating images
    def generate_image_task(self , agent , context ): 
        return Task(
            description="Use ImagegeneratorTool to generate image of {attraction_name}." , 
            agent=agent,
            context=context,
            async_execution=False,
            expected_output=
                "A  list containing dictionaries country: , city: , tourist Attraction Name: ,  ChatGPT Description:  ,  Gemini Description: , Combine unique points: , image_url: " ,
        )

