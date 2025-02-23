'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''
import streamlit as st
import packaging

def main():
    st.title("Data Stuff")
    
    file = st.text_input("Enter data:")
    
    if file: 
        
        st.write(file)
        x = packaging.parse_packaging(file)
        p = packaging.calc_total_units(x)
        p2 = packaging.get_unit(x) 
        
        st.write(x)
        for i in x:
            name = list(i.keys())[0]
            size = list(i.values())[0]
            st.info(f"{name} ➡️ {size}")
        st.success(f"Total 📦 Size: {p} {p2}")

if __name__ == "__main__":
    main()