from crewai import Agent, Crew, Process, Task
from crewai_tools import PDFSearchTool
from dotenv import load_dotenv 


pdf_search_tool = PDFSearchTool(
    pdf="./example_home_inspection.pdf",
    config= dict(
        llm=dict(provider="ollama",config=dict(model="llama3")),
        embedder=dict(provider="ollama",config=dict(model="all-minilm")),
    )

)
research_agent = Agent(
    role="Research Agent",
    goal="Search through the PDF to find relevant answers",
    allow_delegation=False,
    verbose=True,
    backstory=(
        """
        The research agent is adept at searching and 
        extracting data from documents, ensuring accurate and prompt responses.
        """
    ),
    tools=[pdf_search_tool],

)
professional_writer_agent = Agent(
    role="Professional Writer",
    goal="Write professional emails based on the research agent's findings",
    allow_delegation=False,
    verbose=True,
    backstory=(
        """
        The professional writer agent has excellent writing skills and is able to craft 
        clear and concise emails based on the provided information.
        """
    ),
    #tools=[],
)
answer_customer_question_task = Task(
    description=(
        """
        Answer the customer's questions based on the home inspection PDF.
        The research agent will search through the PDF to find the relevant answers.
        Your final answer MUST be clear and accurate, based on the content of the home
        inspection PDF.

        Here is the customer's question:
        {customer_question}
        """
    ),
    expected_output="""
        Provide clear and accurate answers to the customer's questions based on 
        the content of the home inspection PDF.
        """,
    tools=[pdf_search_tool],
    agent=research_agent,
)