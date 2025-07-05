import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("✈️ Airline Booking Market Demand")

API_URL = "http://127.0.0.1:5000/api/demand"  # Flask must be running

# Fetch data
response = requests.get(API_URL)
if response.status_code == 200:
    data = response.json()["demand"]
    df = pd.DataFrame(data)

    st.subheader("📋 Raw Demand Data")
    st.dataframe(df)

    # Charts
    fig1 = px.bar(df, x='airline', y='flights_today', title='Flights Today per Airline')
    st.plotly_chart(fig1)

    fig2 = px.bar(df, x='airline', y='tickets_sold', title='Tickets Sold per Airline')
    st.plotly_chart(fig2)

    # Insights
    st.subheader("📊 Additional Insights")

    popular_route = df.groupby('route')['tickets_sold'].sum().idxmax()
    st.markdown(f"**Most Popular Route:** {popular_route}")

    high_price = df.loc[df['avg_price'].idxmax()]
    st.markdown(f"**Most Expensive Airline (Avg Ticket):** {high_price['airline']} at ${high_price['avg_price']}")

    avg_price_all = df['avg_price'].mean()
    st.markdown(f"**Average Ticket Price (All Airlines):** ${avg_price_all:.2f}")

    fig_price = px.bar(df, x='airline', y='avg_price', title='Average Ticket Price per Airline')
    st.plotly_chart(fig_price)
else:
    st.error("❌ Failed to fetch data from API")