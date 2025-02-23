'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''


import streamlit as st
import packaging
from io import StringIO
import json

st.title("Data Stuff 2")

file = st.file_uploader("Upload package file:")

if file:
    filename = file.name
    json_filename = filename.replace(".txt",".json")
    pk = []
    text = StringIO(file.getvalue().decode("utf-8")).read()
    for i in text.split("\n"):
        i = i.strip()
        x = packaging.parse_packaging(i)
        total = packaging.calc_total_units(x)
        unit = packaging.get_unit(x)
        pk.append(x)
        st.info(f"{i} ➡️ Total 📦 Size: {total} {unit}")
    count = len(pk)
    with open(f"/Users/jack/Downloads/IST 356/assignment-03-JackVsyr/data/{json_filename}", "w") as f:
        json.dump(pk, f, indent=4)
    st.success(f"{count} packages written to {json_filename}", icon="💾")