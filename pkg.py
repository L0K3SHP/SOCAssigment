import os

def main():
    lst = ["dash==1.18.1","dash_core_components","dash_html_components","plotly.express","plotly","pandas","numpy==1.19.3"]
    for i in lst:
        inst = os.system(f"pip show {i}")
        if inst != 0 :
            os.system(f"pip install {i}")
        else:
            print(f"{i} is installed")
            
           
if __name__ == "__main__"
    main()
