import streamlit as st
import pandas as pd
import openpyxl
import os
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
import geopandas as gpd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from streamlit_extras.colored_header import colored_header
from streamlit_option_menu import option_menu
from streamlit.logger import get_logger
from streamlit.elements.lib.column_types import Column
from streamlit.elements.map import Data
from PIL import Image


st.set_page_config(page_title="Datalytics for Stock Taking", page_icon=":📊:", layout="wide", initial_sidebar_state="expanded")


st.divider()

col1, col2 = st.columns(2)
with col1:
    with st.container(border=True, height=308):
        st.title("Datalytics For Stock Taking: PC Version 📊")
        
with col2:
    with st.container(border=True):
        st.info("""Welcome, to the official Datalytics Platform PC Version, for all your Stock Taking related data analytics. Datalytics is a powerful data analysis software 
                that unlocks the potential of realtime data decision making. With Datalytics, you can visualize, analyze, and collaborate using contextual tools. Whether
                you’re a business, researcher, or government agency, Datalytics provides flexible analytics charts and visuals and a cloud-based infrastructure for 
                smarter decision-making.""")
   # with st.container(border=True):
    #    st.write("Explore the engines unique capabilities")
with st.sidebar:
    with st.container(border=True):
        img = Image.open("datalytics_for_shops/imge/dly.png")
        st.image(img, width=250, caption="Software Developed by Mthoe Saps Construction Technologies")
    with st.container(border=False):
        st.header("Upload excel database here to view charts and tables", divider=True)
        uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")
        if uploaded_file is not None:
            df = pd.read_excel(uploaded_file, engine="openpyxl")
            with st.container(border=True):
                st.subheader("Filter all the data using this select box", divider=True)
                groupby_column = st.selectbox(
                    "What would you like to analyse?",
                    ("Item name", "Category ","Supplier ")
                    )
                output_columns = ["Purchase price (US$)", "Retail price (US$)", "Profit margin (%)", "Inventory value (US$)"]
                df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_columns].sum()
        
    with st.form("my_form", clear_on_submit=True):
        st.write("**Rate my software**")
        slider_val = st.slider("How do you rate this tool", help="Slide to the desired precentage(%)")
        checkbox_val = st.checkbox("Did you find this engine useful?", help="Check the box if True")
        submitted = st.form_submit_button("Submit")
        if submitted: st.write("Rating", slider_val, "Helpful", checkbox_val)
        
    with st.container(border=True):
        st.subheader("Contact Us ☎")
        st.write("Get in touch with us to get your own Datalytics software tailored to your business needs. Click on the button below to communicate with us.")
        st.link_button("Contact me", "https://wa.me/263777932721")


        
        
st.divider()
#__change these functions
if uploaded_file is not None:
        st.title("Datalytics Perfomance Dashboard 📈")
        st.divider()
        with st.container(border=True):
            st.title("Data tables")
        st.subheader("Uploaded data Drame")
        st.write(df)
        st.subheader("Filtered data table")
        st.dataframe(df_grouped)
        st.divider()

        with st.container(border=True):
            st.title("Chart Visuals")
        menu = ["Bar graphs", "Pie Charts", "Scatter Plots", "Line graphs", "Histograms", "Density Heatmap"]
        choice = st.selectbox("Which visuals would you like to see?",menu)
        if choice == "Bar graphs":
            st.title("Bar graph analytics")
            with st.container(border=True):
                st.info("Comparing Stock to Quantity")
                df = pd.read_excel(uploaded_file)
                df = px.bar(
                    df,
                    x=groupby_column,
                    y="Quantity ",
                    color="Unit of measure ",
                    color_continuous_scale=["red","yellow","green"],
                    template="plotly_white",
                    hover_name="Category ",
                    hover_data="Supplier ",
                    labels="Inventory value",
                    custom_data="Last updated"
                    )
                st.plotly_chart(df)
                

       
            with st.container(border=True):
                st.info("Comparing Purchase Price and Retail Price")
                df = pd.read_excel(uploaded_file)
                df = px.bar(
                df,
                x=groupby_column,
                y="Purchase price (US$)",
                color="Profit margin (%)",
                color_continuous_scale=["red","yellow","green"],
                template="plotly_white",
                hover_name="Category ",
                hover_data="Supplier ",
                labels="Inventory value (US$)",
                custom_data="Last updated"
                )
                st.plotly_chart(df)
                
        
            with st.container(border=True):
                st.info("Comparing Purchase Price and Retail Price")
                df = pd.read_excel(uploaded_file)
                df = px.bar(
                    df,
                    x=groupby_column,
                y="Retail price (US$)",
                color="Purchase price (US$)",
                color_continuous_scale=["red","yellow","green"],
                template="plotly_white",
                hover_name="Category ",
                hover_data="Supplier ",
                labels="Inventory value (US$)",
                custom_data="Last updated"
                )
                st.plotly_chart(df)
                

            with st.container(border=True):
                st.info("Comparing Inventory Value Perfomances")
                df = pd.read_excel(uploaded_file)
                df = px.bar(
                df,
                x=groupby_column,
                y="Inventory value (US$)",
                color="Last updated",
                color_continuous_scale=["orange","blue","red"],
                template="plotly_white",
                hover_name="Category ",
                hover_data="Supplier ",
                labels="Inventory value (US$)",
                custom_data="Last updated"
                )
                st.plotly_chart(df) 
                

            with st.container(border=True):
                st.info("Comparing Reorder Level Perfomances")
                df = pd.read_excel(uploaded_file)
                df = px.bar(
                df,
                x=groupby_column,
                y="Reorder level",
                color="Expiration date",
                color_continuous_scale=["orange","blue","red"],
                template="plotly_white",
                hover_name="Category ",
                hover_data="Purchase date",
                labels="Inventory value (US$)",
                custom_data="Last updated"
                )
                st.plotly_chart(df)
                

        if choice == "Pie Charts":
            #with st.container(border=True):
             st.title("Pie Chart Visuals")
             with st.container(border=True): 
                st.info("Reorder level piechart")
                df = pd.read_excel(uploaded_file)
                fig = px.pie(
                    df, 
                    values="Reorder level", 
                    names=groupby_column,
                    color="Last updated",
                    hover_data="Expiration date",
                    hover_name="Purchase date")
                st.plotly_chart(fig)
                st.divider()

                st.subheader("Pie Chart Visuals")
                st.info("Comparing Supplier Pricing")
                df = pd.read_excel(uploaded_file)
                fig = px.pie(
                    df, 
                    values="Purchase price (US$)", 
                    names=groupby_column,
                    color="Last updated",
                    hover_data="Profit margin (%)",
                    hover_name="Retail price (US$)")
                st.plotly_chart(fig)
                

        if choice == "Scatter Plots":
            #with st.container(border=True):
            st.title("Scatter Plot Visuals")
            with st.container(border=True):
                st.info("Purchase price perfomance")
                fig = px.scatter(
                        df,
                    x=groupby_column,
                    y="Purchase price (US$)",
                    color="Quantity ",
                    hover_data="Profit margin (%)",
                    hover_name="Last updated",
                    color_continuous_scale=["yellow","blue","red"]
                    )
                st.plotly_chart(fig)
                st.divider()

               
                st.info("Comparing Retail price perfomance")
                fig = px.scatter(
                    df,
                    x=groupby_column,
                    y="Retail price (US$)",
                    color="Quantity ",
                    hover_data="Profit margin (%)",
                    hover_name="Last updated",
                    color_continuous_scale=["orange","blue","red"]
                    )
                st.plotly_chart(fig)
                

        if choice == "Line graphs":
            st.title("Line graph visuals")
            with st.container(border=True):
                st.info("Retail price line graph perfomance")
                fig = px.line(
                    df,
                    x=groupby_column,
                    y="Retail price (US$)",
                    #color="Category ",
                    #hover_data="Profit margin (%)",
                   # hover_name="Last updated",
                    #color_continuous_scale=["orange","blue","red"]
                    )
                st.plotly_chart(fig)
                st.divider()

                st.info("Pruchase price line graph")
                fig = px.line(
                    df,
                    x=groupby_column,
                    y="Purchase price (US$)"
                    )
                st.plotly_chart(fig)
                

        if choice == "Histograms":
            st.title("Histogram visuals")
            with st.container(border=True):
                st.info("Purchase Price Histogram Comparison to Quantity of stock available, Color represents the Product retail price")
                fig = px.histogram(
                    df,
                    x=groupby_column,
                    y="Purchase price (US$)",
                    color="Retail price (US$)"
                    )
                st.plotly_chart(fig)
                st.divider()


                st.info("Comparison Purchase price Histogram")
                fig = px.histogram(
                    df,
                    x=groupby_column,
                    y="Purchase price (US$)",
                    color="Retail price (US$)",
                    #marginal="Inventory value (US$)"
                    histfunc="avg",
                    pattern_shape="Profit margin (%)",
                    text_auto=True
                    )
                st.plotly_chart(fig)
                

            
        if choice == "Density Heatmap":
            st.title("Density heatmap visuals")
            
            with st.container(border=True):
                st.info("High level density heatmap visuals for Purchase prices")
                fig = px.density_heatmap(
                    df,
                    x=groupby_column,
                    y="Purchase price (US$)",
                    #color="Retail price (US$)",
                    #marginal="Inventory value (US$)"
                    #histfunc="avg",
                    #pattern_shape="Profit margin (%)",
                    text_auto=True,
                    color_continuous_scale="Viridis"
                    )
                st.plotly_chart(fig)
                st.divider()


                st.info("High level density heatmap visuals for Purchase prices")
                fig = px.density_heatmap(
                    df,
                    x=groupby_column,
                    y="Purchase price (US$)",
                    #color="Retail price (US$)",
                    #marginal="Inventory value (US$)"
                    #histfunc="avg",
                    #pattern_shape="Profit margin (%)",
                    text_auto=False,
                    #color_continuous_scale="Viridis",
                    marginal_x="histogram",
                    marginal_y="histogram"
                    )
                st.plotly_chart(fig)
                
else:
    with st.container(border=True):
        st.subheader("Upload template Excel file on sidebar 📥 and start working 📈")
    img = Image.open("datalytics_for_shops/imge/b45911d302b9bea734de1a9d9834d8c4.jpg")
    st.image(img, width=550)
    