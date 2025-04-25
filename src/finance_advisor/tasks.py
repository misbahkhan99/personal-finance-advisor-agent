from crewai import Task

class MyTask:

    # Budget Planning Task: Creates a task for budget planning
    def Budget_Planner_Task(self, agent, income, expenses, goals):
        return Task(
            agent=agent,
            description=f"""Help the user create a budget plan based on their income, monthly expenses, and financial goals.
                            Parameters:
                            Income: {income}
                            Expenses: {expenses}
                            Goals: {goals}""",
            expected_output="A detailed budget plan with suggestions for saving and expense adjustments.",
        )

    # Investment Advice Task: Creates a task for investment advice
    def Investment_Advisor_Task(self, agent, risk_profile, goals):
        return Task(
            agent=agent,
            description=f"""Advise the user on investment options based on their risk tolerance and financial goals.
                            Parameters:
                            Risk Profile: {risk_profile}
                            Goals: {goals}""",
            expected_output="Personalized investment strategies and recommendations based on the risk profile.",
        )

    # Debt Management Task: Creates a task for debt management
    def Debt_Management_Task(self, agent, current_debt, monthly_payment, goal):
        return Task(
            agent=agent,
            description=f"""Help the user manage their debt and recommend ways to pay it off faster.
                            Parameters:
                            Current Debt: {current_debt}
                            Monthly Payment: {monthly_payment}
                            Goal: {goal}""",
            expected_output="A debt reduction plan with strategies to pay off debt effectively.",
        )