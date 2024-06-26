from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

llm = Ollama(model="llama2")
question_prompt_template = PromptTemplate(
    template="Generate a very concise question about {topic} that helps in understanding the topic deeply.",
    input_variables=["topic",]
)
def generate_question(topic):
    prompt = question_prompt_template.format(topic=topic)
    question = llm.invoke(prompt)
    return question
