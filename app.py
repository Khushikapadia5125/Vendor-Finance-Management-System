import streamlit as st

st.set_page_config(
    page_title="Vendor Finance System",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# GLOBAL CSS
# =========================

st.markdown("""
<style>

.stApp {
    background-color: #F3E4C3;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #007866;
}

section[data-testid="stSidebar"] * {
    color: white;
}

/* Remove default padding */
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
}

/* Hide Streamlit header/footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* ================= NAVBAR ================= */

.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: #184E50;
    color: white;
    padding: 18px 60px;
    display: flex;
    align-items: center;
    border-bottom: 1px solid #e5e7eb;
    z-index: 9999;
}

.navbar h2 {
    position: absolute;
    left: 35%;
    top:0%;
    transform: translateX(-50%);
    margin: 0;
    color: white;
    white-space: nowrap;
}

.nav-links {
    margin-left: auto;
}

.nav-links a {
    color: white;
    margin-left: 25px;
    text-decoration: none;
    font-weight: 500;
}

.nav-links a:hover {
    color: #60A5FA;
}

/* ================= CONTENT ================= */

.content {
    margin-top: 70px;
    padding: 0px 60px;
}

/* Hero */

.hero {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 50px;
}

.hero h1 {
    font-size: 48px;
    color: #0f172a;
}

.hero h6 {
    color: #475569;
    font-size: 18px;
    font-weight: 400;
}

/* Sections */

.section {
    margin-top: 100px;
    background: #184E50;
}

.features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 25px;
    margin-top: 40px;
            
}

/* Cards */

.card {
    background: #fdfbd4;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 25px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    color: black;
}

.card h3 {
    color: #2563eb;
}

/* Footer */

.footer {
    background: #184E50;
    text-align: center;
    padding: 30px;
    margin-top: 100px;
    color: white;

    position: relative;
    left: 50%;
    margin-left: -50vw;
    width: 100vw;
}
    

</style>
""", unsafe_allow_html=True)

# =========================
# NAVBAR
# =========================

st.markdown("""
<div class="navbar">
    <h2>💼 Vendor Finance Management</h2>
    <div class="nav-links">
        <a href="#">Home</a>
        <a href="#">About Us</a>
        <a href="#">Contact</a>
        <a href="#">Help</a>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# PAGE CONTENT
# =========================

st.markdown('<div class="content">', unsafe_allow_html=True)

# HERO
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
        <div class="hero">
            <div>
                <h1>Vendor Expense Tracker & Profit Analyzer</h1>
                <h6>
                    A simple and smart finance system for small vendors
                    to track expenses, sales, and profits effortlessly.
                </h6>
                <h6>
                    Designed to eliminate manual bookkeeping hassles,
                    this system provides real-time insights, structured records,
                    and accurate profit analysis — all in one intuitive dashboard.
                </h6>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🚀 Open Dashboard"):
        st.switch_page("pages/main.py")

with col2:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/1170/1170576.png",
        width=400
    )

# =========================
# FEATURES
# =========================

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    '<h2 style="color:#184E50;">🚀 Features</h2>',
    unsafe_allow_html=True
)


st.markdown("""
<div class="features">
    <div class="card">
        <h3>Expense Tracking</h3>
        <p>Record daily expenses with vendor-specific categories.</p>
    </div>
    <div class="card"><h3>Sales Managment</h3>
        <p>Add income entries multiple times per day.</p>
    </div>
    <div class="card"><h3>Profit Analyzer</h3>
            <p>Instant daily, monthly and yearly profit calculation.</p>
    </div>
    <div class="card"><h3>Smart Reports</h3>
        <p>Generate daily, monthly, and yearly financial summaries instantly.</p>
    </div>
</div>
""", unsafe_allow_html=True)

    
st.markdown('</div>', unsafe_allow_html=True)

# =========================
# HOW IT WORKS
# =========================

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown(
    '<h2 style="color:#184E50;">⚙️ How It Works</h2>',
    unsafe_allow_html=True
)


st.markdown("""
<div class="features">
    <div class="card"><h3>Add Expenses</h3><p>Stock, rent, transport, electricity & more.</p></div>
    <div class="card"><h3>Add Sales</h3><p>Daily or multiple sales entries.</p></div>
    <div class="card"><h3>Analyze Profit</h3><p>Instant profit or loss with filters.</p></div>
    <div class="card"><h3>Category Summary</h3><p>View category-wise expenses.</p></div>
    <div class="card"><h3>Monthly Expense</h3><p>Analyze monthly expense reports.</p></div>
    <div class="card"><h3>Highest Spending</h3><p>Identify highest spending category.</p></div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# FOOTER
# =========================

st.markdown("""
<div class="footer">
    Vendor Expense Tracker & Profit Analyzer <br>
    Built with ❤️ using Python & Streamlit
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
