import pandas as pd
import streamlit as st

from src.charts import plot_response_hist, plot_borough_bar, plot_borough_bar_count
from src.data import convert_for_download


def header_metrics(df: pd.DataFrame) -> None:
    """Rendering header metrics. Placeholder values are intentional."""
    c1, c2, c3 = st.columns(3)

    # TODO (IN-CLASS): Replace these placeholders with real metrics from df
    # Suggestions:
    # - Total complaints (len(df))
    # - Median response time
    # - % from Web vs Phone vs App (pick one)
    with c1:
        st.metric("Total complaints", len(df))
    with c2:
        rtd_median = df["response_time_days"].median().round(1)
        st.metric("Median response (days)", rtd_median)
    with c3:
        common_complaint = df["complaint_type"].mode()[0]
        st.metric("Most common complaint", common_complaint)


def body_layout_tabs(df: pd.DataFrame) -> None:
    """Tabs layout with 3 default tabs."""
    t1, t2, t3 = st.tabs(["Distribution", "By Borough", "Table"])

    with t1:
        st.subheader("Response Time Distribution")
        plot_response_hist(df)

        # TODO (IN-CLASS): Add a short interpretation sentence under the chart
        st.caption("Displays the response time distribution in days")

    with t2:
        st.subheader("Median Response Time by Borough")
        plot_borough_bar(df)

        # TODO (IN-CLASS): Add a second view here (e.g., count by borough)
        st.subheader("Count Requests by Borough")
        plot_borough_bar_count(df)

    with t3:
        st.subheader("Filtered Rows")
        st.dataframe(df, use_container_width=True, height=480)

        # TODO (OPTIONAL): Add st.download_button to export filtered rows
        csv = convert_for_download(df)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="data.csv",
            mime="text/csv",
            icon=":material/download:"
        )
