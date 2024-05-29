# :calendar: Relative date pickers for Streamlit

This is just an example of how you can make your own relative date pickers in Streamlit. Use it as
inspiration or feel free to steal the code if you like.

Try it out at https://datepicker.streamlit.app


## Usage

If you do steal the code, here's how you use it:

```py
date = relative_date_picker("Date")
```

```py
date0, date1 = relative_date_range_picker("Date range")
```

## Arguments

* **label:** `required` The label for this widget

* **relative_dates:** `optional` A dictionary of labels to number of days ago (for
`relative_date_picker()`) or `[days_ago_0, days_ago_1]` (for `relative_date_range_picker()`)

* **value:** The default value of the relative date picker. Should be one of the keys from
`relative_dates`.

* **key:** The widget key, like any other Streamlit widget)
