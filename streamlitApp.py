import streamlit as st
from src.finance_advisor.agents import MyPersonalFinanceAgent
from src.finance_advisor.tasks import MyTask
from crewai import Crew

# Streamlit App Title
st.title("💼 Personal Finance AI Agent")

# Sidebar Inputs
st.sidebar.header("📊 Budget Planning")
income = st.sidebar.number_input("Monthly Income ($)", min_value=0)
expenses = st.sidebar.number_input("Monthly Expenses ($)", min_value=0)
budget_goals = st.sidebar.text_input("Budget Goal", value="Save for retirement")

st.sidebar.header("📈 Investment Planning")
risk_profile = st.sidebar.selectbox("Risk Profile", ["Low", "Medium", "High"])
investment_goals = st.sidebar.text_input("Investment Goal", value="Grow wealth")

st.sidebar.header("💳 Debt Management")
current_debt = st.sidebar.number_input("Total Current Debt ($)", min_value=0)
monthly_payment = st.sidebar.number_input("Monthly Debt Payment ($)", min_value=0)
debt_goal = st.sidebar.text_input("Debt Goal", value="Pay off debt in 3 years")

if st.button("Run Financial Agent"):
    with st.spinner("Running your personalized financial Agent..."):

        # Initialize Agents & Tasks
        agents = MyPersonalFinanceAgent()
        tasks = MyTask()

        budget_planner = agents.Budget_Planner()
        investment_advisor = agents.Investment_Advisor()
        debt_management = agents.Debt_Management()

        budget_planner_task = tasks.Budget_Planner_Task(
            agent=budget_planner, income=income, expenses=expenses, goals=budget_goals
        )

        investment_advisor_task = tasks.Investment_Advisor_Task(
            agent=investment_advisor, risk_profile=risk_profile, goals=investment_goals
        )

        debt_management_task = tasks.Debt_Management_Task(
            agent=debt_management, current_debt=current_debt, monthly_payment=monthly_payment, goal=debt_goal
        )

        # Initialize the Crew
        crew = Crew(
            agents=[budget_planner, investment_advisor, debt_management],
            tasks=[budget_planner_task, investment_advisor_task, debt_management_task],
            verbose=True
        )

        # Run the Crew
        result = crew.kickoff()

        # Display Result
        st.success("✅ Agent execution completed!")
        st.markdown("### Final Advice from Your Finance Agent:")
        st.write(result)
