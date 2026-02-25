import pandas as pd
import streamlit as st


@st.cache_data(show_spinner=False)
def load_data(path: str) -> pd.DataFrame:
    """Loading a small CSV and caching it so the app stays responsive."""
    df = pd.read_csv(path)

    # TODO (OPTIONAL): Parse created_date as datetime for time-based filters
    df['created_date'] = pd.to_datetime(df['created_date'], format='%Y-%m-%d')

    return df

@st.cache_data(show_spinner=False)
def convert_for_download(df: pd.DataFrame):
    return df.to_csv().encode("utf-8")
