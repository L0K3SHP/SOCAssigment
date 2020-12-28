import os

lst = ["dash","dash_core_components","dash_html_components","plotly.express","plotly","pandas"]
for i in lst:
    inst = os.system(f"pip show {i}")
    if inst != 0 :
        os.system(f"pip install {i}")
    else:
        print(f"{i} is installed")