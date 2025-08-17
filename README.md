Agents and Tasks
PDF Processing Agents and Tasks
Agents
Manager Agent: Manages the workflow and delegates tasks.
Research Agent: Searches through the PDF to find relevant answers.
Professional Writer Agent: Writes professional emails based on the research agent's findings.
Tasks
Answer Customer Question Task: Searches the PDF to find answers to customer questions.
Write Email Task: Generates a professional email to contractors based on the research findings.
YouTube Processing Agents and Tasks
Agents
Scrape Agent: Extracts content from YouTube videos and adds it to the vector database.
Vector DB Processor: Adds YouTube videos to the vector database.
General Research Agent: Gathers all required information from the YouTube channel.
Follow-up Agent: Performs thorough research to find any missing data.
Fallback Agent: Conducts final checks and searches the internet for any remaining information.
Tasks
Scrape YouTube Channel Task: Extracts information from the latest five videos of a specified YouTube channel.
Process Videos Task: Adds the extracted video URLs to the vector database.
Find Initial Information Task: Fills out the ContentCreatorInfo model with as much information as possible.
Follow-up Task: Searches for any missing data in the ContentCreatorInfo model.
Fallback Task: Performs final checks to ensure the ContentCreatorInfo model is fully populated.