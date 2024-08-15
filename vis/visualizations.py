import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

def create_visualizations():
    try:
        # Load the cleaned data
        df = pd.read_csv('data/processed/bank_account_fraud_clean.csv')
        
        # Basic data check
        print(df.head())
        print("Columns:", df.columns)
        
        # Check if DataFrame is empty
        if df.empty:
            print("DataFrame is empty.")
            return
        
        # Fraud label distribution with Plotly
        fig_fraud_dist = px.histogram(df, x='fraud_bool', title='Fraud Label Distribution', 
                                      color='fraud_bool', 
                                      labels={'fraud_bool': 'Fraud Label'},
                                      color_discrete_map={0: 'green', 1: 'red'})
        fig_fraud_dist.update_layout(title_text='Fraud Label Distribution',
                                     xaxis_title='Fraud Label',
                                     yaxis_title='Count',
                                     plot_bgcolor='rgba(0,0,0,0)',
                                     paper_bgcolor='rgba(255,255,255,0.5)',
                                     xaxis=dict(title_font=dict(size=14, family='Arial', color='rgb(0,0,0)'),
                                                tickfont=dict(size=12, family='Arial', color='rgb(0,0,0)')),
                                     yaxis=dict(title_font=dict(size=14, family='Arial', color='rgb(0,0,0)'),
                                                tickfont=dict(size=12, family='Arial', color='rgb(0,0,0)')))
        fig_fraud_dist.write_html('data/outputs/fraud_label_distribution.html')

        # Correlation heatmap with Plotly
        corr = df.corr()
        fig_heatmap = go.Figure(data=go.Heatmap(z=corr.values,
                                               x=corr.columns,
                                               y=corr.columns,
                                               colorscale='Viridis',
                                               colorbar=dict(title='Correlation')))
        fig_heatmap.update_layout(title='Correlation Heatmap',
                                  xaxis_title='Features',
                                  yaxis_title='Features',
                                  plot_bgcolor='rgba(0,0,0,0)',
                                  paper_bgcolor='rgba(255,255,255,0.5)')
        fig_heatmap.write_html('data/outputs/correlation_heatmap.html')
        
        # Boxplot of income by fraud label
        if 'income' in df.columns:
            fig_boxplot = px.box(df, x='fraud_bool', y='income', 
                                title='Income by Fraud Label', 
                                color='fraud_bool',
                                labels={'fraud_bool': 'Fraud Label', 'income': 'Income'})
            fig_boxplot.update_layout(title_text='Income by Fraud Label',
                                      xaxis_title='Fraud Label',
                                      yaxis_title='Income',
                                      plot_bgcolor='rgba(0,0,0,0)',
                                      paper_bgcolor='rgba(255,255,255,0.5)',
                                      xaxis=dict(title_font=dict(size=14, family='Arial', color='rgb(0,0,0)'),
                                                 tickfont=dict(size=12, family='Arial', color='rgb(0,0,0)')),
                                      yaxis=dict(title_font=dict(size=14, family='Arial', color='rgb(0,0,0)'),
                                                 tickfont=dict(size=12, family='Arial', color='rgb(0,0,0)')))
            fig_boxplot.write_html('data/outputs/income_boxplot.html')
        else:
            print("Column 'income' not found in the dataset.")
        
        # Streamlit app visualization
        st.title('Fraud Detection Dashboard')
        st.write("Interactive visualizations:")
        
        st.write("### Fraud Label Distribution")
        fig_fraud_dist = px.histogram(df, x='fraud_bool', title='Fraud Label Distribution', 
                                      color='fraud_bool', 
                                      labels={'fraud_bool': 'Fraud Label'},
                                      color_discrete_map={0: 'green', 1: 'red'})
        st.plotly_chart(fig_fraud_dist)

        st.write("### Correlation Heatmap")
        fig_heatmap = go.Figure(data=go.Heatmap(z=corr.values,
                                               x=corr.columns,
                                               y=corr.columns,
                                               colorscale='Viridis',
                                               colorbar=dict(title='Correlation')))
        st.plotly_chart(fig_heatmap)

        if 'income' in df.columns:
            st.write("### Income by Fraud Label")
            fig_boxplot = px.box(df, x='fraud_bool', y='income', 
                                title='Income by Fraud Label', 
                                color='fraud_bool',
                                labels={'fraud_bool': 'Fraud Label', 'income': 'Income'})
            st.plotly_chart(fig_boxplot)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_visualizations()
