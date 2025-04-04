from preswald import workflow_dag, Workflow, text, separator, plotly, connect, get_df, table, query, slider, topbar, text_input, text, alert
import pandas as pd
import plotly.express as px

text("# Welcome to Preswald!")
# topbar()

name = text_input(label="Enter your name", placeholder="John Doe")

email = text_input(label="Email", placeholder="user@example.com")
password = text_input(label="Password", placeholder="Enter password")

pwd = text_input(label="Enter the password you provided earlier", placeholder="Enter password")

if password and pwd and name and email and password == pwd:
    alert(f"Welcome {name}!", level="success")
    text("## Dataset")
    connect()
    df = get_df(source_name="best_sellers_data2", table_name="best_sellers_data2")
    table(df, title="Original Data")
    separator()

    sql = "SELECT * FROM best_sellers_data2 WHERE product_star_rating > 4.5 AND product_num_ratings > 20"
    filtered_df = query(sql, "best_sellers_data2")
    table(filtered_df, title="Filtered Data - Products with Star Ratings above 4.5 and Number of Ratings above 20")
    separator()

    threshold = slider("Threshold", min_val=0, max_val=5, default=3)
    table(df[df["product_star_rating"] > threshold], title="Dynamic Data View Based on Threshold Value")
    separator()

    text("## Scatter Plots")
    fig1 = px.scatter(df, x="product_star_rating", y="product_num_ratings", color="product_num_ratings", title="Product Star Rating VS Number of Ratings")
    fig1.update_layout(template="plotly_white")
    plotly(fig1)
    separator()

    fig2 = px.scatter(df, x="product_price", y="product_star_rating", color="product_star_rating", title="Price VS Product Star Ratings")
    fig2.update_layout(template="plotly_white")
    plotly(fig2)

    text("## Histogram of Product Prices")
    fig3 = px.histogram(df, x="product_price", color="product_price", title="Distribution of Product Prices")
    fig3.update_layout(template="plotly_white")
    plotly(fig3)

    sql = "SELECT country, COUNT(*) AS product_count FROM best_sellers_data2 GROUP BY country;"
    country_count_df = query(sql, "best_sellers_data2")
    separator()

    text("## Pie Chart of Best Sellers By Country")
    fig4 = px.pie(country_count_df, values="product_count", names="country", color="country", title="Best Sellers by Country")
    plotly(fig4)


workflow = Workflow()

@workflow.atom()
def credentials():
    return "Credentials"

@workflow.atom(dependencies=['credentials'])
def data_analysis():
    return "Data Analysis"

workflow_dag(workflow, title="App Workflow")
