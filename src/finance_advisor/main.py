from agents import MyPersonalFinanceAgent
from tasks import MyTask
from crewai import Crew

# Initialize the agents and tasks
agents = MyPersonalFinanceAgent()
tasks = MyTask()

# Create agent instances
budget_planner = agents.Budget_Planner()
investment_advisor = agents.Investment_Advisor()
debt_management = agents.Debt_Management()

# Create tasks
budget_planner_task = tasks.Budget_Planner_Task(agent=budget_planner, income=5000, expenses=3000, goals="Save for retirement")
investment_advisor_task = tasks.Investment_Advisor_Task(agent=investment_advisor, risk_profile="Medium", goals="Grow wealth")
debt_management_task = tasks.Debt_Management_Task(agent=debt_management, current_debt=15000, monthly_payment=500, goal="Pay off debt in 3 years")

# Set up the Crew with agents and tasks
crew = Crew(
    agents=[budget_planner, investment_advisor, debt_management],  # List of agents
    tasks=[budget_planner_task, investment_advisor_task, debt_management_task],  # List of tasks
    verbose=True  # Enable verbose logging for debugging
)

# Main function to run the Crew and get the result
def main():
    result = crew.kickoff()  # Start the task execution
    print(f"Final result: {result}")  # Print the result from the Crew


main()    