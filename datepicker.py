import streamlit as st
import datetime

# Dict of label -> [days ago 0, days ago 1]
# Or None for Custom.
RELATIVE_DATE_RANGES = {
  "Custom": None,
  "Last 7 days": (7, 0),
  "Last 14 days": (14, 0),
  "Last 30 days": (30, 0),
  "Last 90 days": (90, 0),
  "Last year": (365, 0),
}

def relative_date_range_picker(
    label,
    relative_dates=RELATIVE_DATE_RANGES,
    value="Last 7 days",
    key="date-range-picker",
):
    today = datetime.date.today()

    relative_date_key = f"{key}-relative"

    is_using_custom_date = getattr(st.session_state, relative_date_key, None) == "Custom"

    if is_using_custom_date:
        rel_col, abs_col = st.columns(2)

    else:
        rel_col = st.columns(1)[0] # Using this instead of "st" to catch column-chaining warnings early.
        abs_col = None

    relative_dates_list = list(relative_dates.keys())
    index = relative_dates_list.index(value)

    relative_date_str = rel_col.selectbox(
        label,
        relative_dates_list,
        index=index,
        key=relative_date_key,
    )

    if is_using_custom_date:
        default_range = relative_dates[value]

        if default_range is None:
            default_range = [7, 0]

        date_range = abs_col.date_input(
            "Custom date",
            [
                today - datetime.timedelta(days=default_range[0]),
                today - datetime.timedelta(days=default_range[1]),
            ],
            label_visibility="hidden",
        )

    else:
        relative_date_range = relative_dates[relative_date_str]
        date_range = (
            today - datetime.timedelta(days=relative_date_range[0]),
            today - datetime.timedelta(days=relative_date_range[1]),
        )

    return date_range


# Dict of label -> days ago
# Or None for Custom
RELATIVE_DATES = {
  "Custom": None,
  "Today": 0,
  "Yesterday": 1,
  "7 days ago": 7,
  "14 days ago": 14,
  "30 days ago": 30,
  "90 days ago": 90,
  "1 year ago": 365,
}

def relative_date_picker(
    label,
    relative_dates=RELATIVE_DATES,
    value="Today",
    key="date-picker",
):
    today = datetime.date.today()

    relative_date_key = f"{key}-relative"

    is_using_custom_date = getattr(st.session_state, relative_date_key, None) == "Custom"

    if is_using_custom_date:
        rel_col, abs_col = st.columns(2)

    else:
        rel_col = st.columns(1)[0] # Using this instead of "st" to catch column-chaining warnings early.
        abs_col = None

    relative_dates_list = list(relative_dates.keys())
    index = relative_dates_list.index(value)

    relative_date_str = rel_col.selectbox(
        label,
        relative_dates.keys(),
        index=index,
        key=relative_date_key,
    )

    if is_using_custom_date:
        default_date = relative_dates[value]

        if default_date is None:
            default_date = 0

        abs_date = abs_col.date_input(
            "Custom date",
            today - datetime.timedelta(days=default_date),
            label_visibility="hidden",
        )

    else:
        relative_date = relative_dates[relative_date_str]
        abs_date = today - datetime.timedelta(days=relative_date)

    return abs_date
