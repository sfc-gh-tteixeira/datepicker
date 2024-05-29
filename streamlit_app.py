import streamlit as st

from datepicker import relative_date_picker, relative_date_range_picker


"""
# :calendar: Relative date pickers
"""

""
""

"""
### Single date
"""

out = relative_date_picker("Date")
out


""

"""
### Date range
"""

out = relative_date_range_picker("Date range")
out

