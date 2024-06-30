import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib3
import re

urllib3.disable_warnings()

url = "https://tuoitrethudo.vn/tra-cuu-diem-thi&type_of_score=1&sbd="

id_path = "/Users/andrew/Desktop/Tra_cuu_TS10/data/chuyenSu/ChuyenSu.xlsx"
df = pd.read_excel(id_path)

id_list = df['sbd'].tolist()

def extract_floats_from_string(input_string):
    floats = re.findall(r"[-+]?\d*\.\d+", input_string)
    floats = [float(num) for num in floats]
    return floats

def score(id,url):
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.text, 'html.parser')
    items = soup.find_all('table', class_='__mb_result')
    score = "";
    # print(items)
    for item in items:
        # subject = item.find('div', class_='score-item-heading').text.strip()
        score = item.find('div', style="padding-bottom:10px; color:#000000;").text.strip()
        score = extract_floats_from_string(score)
        # scores[subject] = score
        # print(score)
        # scores.append(score)
        # print("done") 
    return score
    # print(id,";",score)

output_file = "result.txt"
with open(output_file, "w") as file:
    for id in id_list:
        tmp_url = url + str(id)
        result = str(id) + "," + str(score(id, tmp_url))
        print(str(result))
        file.write(str(result)+ "\n")
