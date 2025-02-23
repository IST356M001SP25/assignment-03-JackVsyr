'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''
import streamlit as st
import packaging
from io import StringIO
import json

st.title("Data Stuff 3")

if 's' not in st.session_state:
    st.session_state.s = []
if 'tlines' not in st.session_state:
    st.session_state.tlines = 0
if 'files' not in st.session_state:
    st.session_state.files = 0

file = st.file_uploader("Upload package file:")

if file:
    filename = file.name
    json_filename = filename.replace(".txt",".json")
    pk = []
    text = StringIO(file.getvalue().decode("utf-8")).read()
    for i in text.split("\n"):
        i = i.strip()
        x = packaging.parse_packaging(i)
        p = packaging.calc_total_units(x)
        p2 = packaging.get_unit(x)
        pk.append(x)
    count = len(pk)
    with open(f"/Users/jack/Downloads/IST 356/assignment-03-JackVsyr/data{json_filename}", "w") as f:
        json.dump(pk, f, indent=4)
    summary = f"{count} packages written to {json_filename}"

    st.session_state.s.append(summary)
    st.session_state.files += 1
    st.session_state.tlines += count

    for s in st.session_state.s:
        st.info(s, icon="💾")
    st.success(f"{st.session_state.files} files done, {st.session_state.tlines} lines processed")