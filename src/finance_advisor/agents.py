from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

# Initialize LLM with the Gemini model
llm = LLM(model="gemini/gemini-1.5-flash")

class MyPersonalFinanceAgent:

    # Budget Planning Agent: Creates personalized budget plans
    def Budget_Planner(self):
        return Agent(
            role="Budget_Planner",
            goal="Help the user create a personalized budget based on income, expenses, and goals.",
            backstory="I am a financial advisor with expertise in budgeting and financial planning.",
            llm=llm,
            verbose=True
        )
    
    # Investment Advisor Agent: Suggests investment strategies based on risk and goals
    def Investment_Advisor(self):
        return Agent(
            role="Investment_Advisor",
            goal="Provide investment recommendations based on the user's risk profile and financial goals.",
            backstory="I have extensive experience in managing investments and advising clients on risk and return profiles.",
            llm=llm,
            verbose=True
        )

    # Debt Management Agent: Helps the user manage and pay off debt
    def Debt_Management(self):
        return Agent(
            role="Debt_Management",
            goal="Advise on strategies to manage and reduce personal debt effectively.",
            backstory="I specialize in debt reduction strategies and have helped clients significantly reduce their debts over time.",
            llm=llm,
            verbose=True
        )