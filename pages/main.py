import streamlit as st
from datetime import date
from db import get_connection

# =================================================
# PAGE SETUP + UI STYLE (MINIMAL)
# =================================================
st.set_page_config(
    page_title="Vendor Expense & Profit Tracker",
    page_icon="💼",
    layout="centered"
)


st.markdown(
    """
    <style>
    .block-container { padding-top: 2rem; }
    div[data-testid="stMetric"] {
        background-color: #1E1E1E;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        color:Black;
    }
      div[data-testid="stMetric"] * {
        color: #FFFFFF !important;
        opacity: 1 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h1 style="text-align:center;">💼 Vendor Finance Dashboard</h1>
    <p style="text-align:center;color:grey;">
    Track expenses, sales, and profits effortlessly
    </p>
    """,
    unsafe_allow_html=True
)

# =================================================
# DATABASE FUNCTIONS – EXPENSE
# =================================================
def add_expense(amount, category, expense_date, remark):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO expenses (amount, category, expense_date, remark)
        VALUES (%s, %s, %s, %s)
        """,
        (amount, category, expense_date, remark)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return "Expense added successfully"


def fetch_expenses():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT expense_date, category, amount, remark
        FROM expenses
        ORDER BY expense_date DESC
    """)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


def category_summary():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT category, SUM(amount) AS total
        FROM expenses
        GROUP BY category
    """)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


def monthly_total(year, month):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
        WHERE YEAR(expense_date)=%s AND MONTH(expense_date)=%s
    """, (year, month))
    total = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return total if total else 0


def highest_spending_category():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT category
        FROM expenses
        GROUP BY category
        ORDER BY SUM(amount) DESC
        LIMIT 1
    """)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result else None


# =================================================
# DATABASE FUNCTIONS – INCOME
# =================================================
def add_income(amount, income_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO income (amount, income_date)
        VALUES (%s, %s)
        """,
        (amount, income_date)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return "Income added successfully"


def fetch_income():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT income_date, amount
        FROM income
        ORDER BY income_date DESC
    """)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


def monthly_income(year, month):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT SUM(amount)
        FROM income
        WHERE YEAR(income_date)=%s AND MONTH(income_date)=%s
    """, (year, month))
    total = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return total if total else 0


# =================================================
# PROFIT HELPERS
# =================================================
def daily_income(d):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM income WHERE income_date=%s", (d,))
    total = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return total if total else 0


def daily_expense(d):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE expense_date=%s", (d,))
    total = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return total if total else 0


def weekly_income(start, end):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT SUM(amount) FROM income WHERE income_date BETWEEN %s AND %s",
        (start, end)
    )
    total = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return total if total else 0


def weekly_expense(start, end):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT SUM(amount) FROM expenses WHERE expense_date BETWEEN %s AND %s",
        (start, end)
    )
    total = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return total if total else 0


def yearly_income(year):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM income WHERE YEAR(income_date)=%s", (year,))
    total = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return total if total else 0


def yearly_expense(year):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE YEAR(expense_date)=%s", (year,))
    total = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return total if total else 0


# =================================================
# SIDEBAR MENU
# =================================================
st.sidebar.markdown("## 📊 Navigation")
menu = st.sidebar.radio(
    "",
    [
        "➕ Add Expense",
        "➕ Add Income",
        "📄 View Expenses",
        "📄 View Sales",
        "📊 Category Summary",
        "📅 Monthly Expense",
        "📈 Profit Analyzer",
        "🔥 Highest Spending"
    ]
)

# =================================================
# ADD EXPENSE
# =================================================
if menu == "➕ Add Expense":
    st.subheader("Add Vendor Expense")
    with st.form("expense_form", clear_on_submit=True):
        amount = st.number_input("Expense Amount (₹)", min_value=1.0)
        category = st.selectbox(
            "Category",
            ["Stock Purchase", "Transport", "Rent", "Electricity", "Maintenance", "Other"]
        )
        expense_date = st.date_input("Expense Date", value=date.today())
        remark = st.text_input("Remark (optional)")
        if st.form_submit_button("Add Expense"):
            st.success(add_expense(amount, category, expense_date, remark))


# =================================================
# ADD INCOME
# =================================================
elif menu == "➕ Add Income":
    st.subheader("Add Vendor Income (Sales)")
    with st.form("income_form", clear_on_submit=True):
        amount = st.number_input("Income Amount (₹)", min_value=1.0)
        income_date = st.date_input("Income Date", value=date.today())
        if st.form_submit_button("Add Income"):
            st.success(add_income(amount, income_date))


# =================================================
# VIEW EXPENSES
# =================================================
elif menu == "📄 View Expenses":
    st.subheader("Expense Records")
    data = fetch_expenses()
    if not data:
        st.info("No expenses found")
    else:
        st.table([{
            "Date": e["expense_date"].isoformat(),
            "Category": e["category"],
            "Amount (₹)": f"{e['amount']:.2f}",
            "Remark": e["remark"]
        } for e in data])


# =================================================
# VIEW SALES
# =================================================
elif menu == "📄 View Sales":
    st.subheader("Sales Records")
    data = fetch_income()
    if not data:
        st.info("No sales found")
    else:
        st.table([{
            "Date": i["income_date"].isoformat(),
            "Sales Amount (₹)": f"{i['amount']:.2f}"
        } for i in data])


# =================================================
# CATEGORY SUMMARY
# =================================================
elif menu == "📊 Category Summary":
    st.subheader("Category-wise Expense Summary")
    data = category_summary()
    if not data:
        st.info("No data available")
    else:
        for row in data:
            st.write(f"🔹 {row['category']} : ₹ {row['total']}")


# =================================================
# MONTHLY EXPENSE
# =================================================
elif menu == "📅 Monthly Expense":
    st.subheader("Monthly Expense")
    year = st.number_input("Year", 2000, 2100, date.today().year)
    month = st.number_input("Month", 1, 12, date.today().month)
    if st.button("Calculate"):
        st.metric("Total Expense", f"₹ {monthly_total(year, month)}")


# =================================================
# PROFIT ANALYZER
# =================================================
elif menu == "📈 Profit Analyzer":
    st.subheader("Profit Analyzer")
    ptype = st.selectbox("Select Type", ["Daily", "Custom", "Monthly", "Yearly"])

    profit = None

    if ptype == "Daily":
        d = st.date_input("Select Date", date.today())
        if st.button("Analyze"):
            inc = daily_income(d)
            exp = daily_expense(d)
            profit = inc - exp

    elif ptype == "Custom":
        start = st.date_input("Start Date")
        end = st.date_input("End Date")
        if st.button("Analyze"):
            inc = weekly_income(start, end)
            exp = weekly_expense(start, end)
            profit = inc - exp

    elif ptype == "Monthly":
        year = st.number_input("Year", 2000, 2100, date.today().year)
        month = st.number_input("Month", 1, 12, date.today().month)
        if st.button("Analyze"):
            inc = monthly_income(year, month)
            exp = monthly_total(year, month)
            profit = inc - exp

    else:
        year = st.number_input("Year", 2000, 2100, date.today().year)
        if st.button("Analyze"):
            inc = yearly_income(year)
            exp = yearly_expense(year)
            profit = inc - exp

    if profit is not None:
        c1, c2, c3 = st.columns(3)
        c1.metric("Income", f"₹ {inc}")
        c2.metric("Expense", f"₹ {exp}")
        c3.metric("Profit", f"₹ {profit}")


# =================================================
# HIGHEST SPENDING
# =================================================
elif menu == "🔥 Highest Spending":
    st.subheader("Highest Spending Category")
    highest = highest_spending_category()
    if highest:
        st.success(f"Highest spending category: {highest}")
    else:
        st.info("No data available")
