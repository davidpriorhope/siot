'''Welcome to my updating HTML code

Here the JavaScript is updated by rewriting the file and HTML is parsed using BeautifulSoup and then rewritten with updated files'''

#update Java script variables

coef_weather, coef_layers, intercept, score = open('temp_data/ML_data.txt', "r").readlines()

Ci, Cw, Cl, CW, C2, CL, quad_int, r2_quad = list(map(float, open('temp_data/ML_data_quad.txt', 'r').read().splitlines()))

lines = open('docs/app.js', "r").readlines()

with open('docs/app.js', "w") as f:
    for line in lines:
        if "const coef_weather" in line:
            line = "const coef_weather = " + str(float(coef_weather))+ ';\n'
        
        elif "const coef_layer = " in line:
            line = "const coef_layer = " + str(float(coef_layers))+ ';\n'
        
        elif "const lin_int" in line:
            line = 'const lin_int = '+ str(float(intercept))+';\n'

        elif "const lin_score = " in line:
            line = "const lin_score = "+str(round(float(score),2))+ ';\n'

        elif "const Ci" in line:
            line = "const Ci = "+str(float(Ci))+ ';\n'

        elif "const Cw" in line:
            line = "const Cw = "+str(float(Cw))+ ';\n'

        elif "const Cl" in line:
            line = "const Cl = "+str(float(Cl))+ ';\n'

        elif "const CW" in line:
            line = "const CW = "+str(float(CW))+ ';\n'

        elif "const C2" in line:
            line = "const C2 = "+str(float(C2))+ ';\n'

        elif "const CL" in line:
            line = "const CL = "+str(float(CL))+ ';\n'

        elif "const quad_int" in line:
            line = "const quad_int = "+str(float(quad_int))+ ';\n'

        elif "const quad_score" in line:
            line = "const quad_score = "+str(float(r2_quad))+ ';\n'

        f.write(line)


#update carosel

from bs4 import BeautifulSoup as bs
import os
from datetime import datetime

html_target = 'docs/index.html'

index_html = open(html_target, 'r')

soup = bs(index_html, 'html.parser')


#finding all added images
image_tags_list = soup.find_all('img')


#getting tag of last added image
last_image_tag = image_tags_list[len(image_tags_list)-1]

#getting the parent of the last added image
last_image_tag_parent = last_image_tag.find_parent()

#making a list of links to images currently in the HTML
src_list = []

for img in image_tags_list:
    src_list.append(img['src'])


#getting a list of cycle files
path = 'assets/cycle'

cycle_files = os.listdir("docs/"+path)

#creating a list of cycle files which are not already in the HTML
cycle_files_to_add = []

for file in cycle_files:
    if file not in str(src_list):
        cycle_files_to_add.append(file)


#sorting the cycle files based on date
cycle_files_to_add.sort(key= lambda date: datetime.strptime(date, "%d.%m.%y.png"))


#adding the images not in the HTML to the HTML
for file in cycle_files_to_add:
    #creating a new div tag
    div_tag = soup.new_tag("div")
    div_tag.attrs['class'] = "item"
    
    #creating the child with the image source
    child = soup.new_tag('img')
    child.attrs['src']= path+"/"+file
    child.attrs['style'] = "width:100%;"
    
    #adding the div tag after the last added image
    last_image_tag_parent.insert_after(div_tag)

    #adding the image as a child throug append
    div_tag.append(child)


    #updating the last added image tag parent to be the one just added
    last_image_tag_parent = div_tag


#overwriting the old HTML with the new one
with open(html_target, "w") as f:
    f.write(str(soup.prettify()))