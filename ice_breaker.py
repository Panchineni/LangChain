from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import StrOutputParser
import os
import requests
from third_parties.linkedin import scrape_linkedin_profile
from dotenv import load_dotenv

load_dotenv()
if __name__ =='__main__':
    print("version")
    print("Hi Langchain")
   # print(os.environ['OPENAI_API_KEY'])

   

    summary_template = """
    given the LinkedIN information {information} about a person I want you to create:
    1. Name of the user
    2. Organization the person is working for
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/32f3c85b9513994c572613f2c8b376b633bfc43f/eden-marco-scrapin.json"
    response = requests.get(
        linkedin_profile_url,
        timeout=10,
    )
    """
    use this when there is api-key available for the scrape_linkedin_profile
        linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/name_of_user"
    )
    
    """
    res = chain.invoke(input={"information": response.json()})
    print(res)


