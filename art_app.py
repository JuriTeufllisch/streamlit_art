import numpy as np
import streamlit as st
from matplotlib import pyplot as plt
import random



st.title('Create Digital Art')
st.header('- simple, but unique -')

n = st.slider('width of image', min_value=1, max_value=200)
image_size = st.slider('image size in pixels', min_value=2, max_value=2000)

lower_size = st.slider('lower size of symbols', min_value=1, max_value=int((image_size/n)**2))
upper_size = st.slider('upper size of symbols', min_value=2, max_value=int(2*(image_size/n)**2))

marker = st.select_slider('marker style', options=['o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X'])

red = st.slider('red', min_value=0, max_value=256)
green = st.slider('green', min_value=0, max_value=256)
blue = st.slider('blue', min_value=0, max_value=256)


pixelsize = []
colors = []
x,y = np.linspace(1,n,n), np.linspace(1,n,n)


#create dots:
dots_x, dots_y = [],[]
for i in range(len(x)):
    for j in range(len(y)):
        dots_x.append(x[i])
        dots_y.append(y[j])
        colors.append([random.randint(0,red)/256, random.randint(0,green)/256, random.randint(0,blue)/256])
        pixelsize.append(random.randint(lower_size, upper_size))
   
plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(image_size/100,image_size/100))
ax.scatter(dots_x, dots_y, s=pixelsize, c=colors, alpha=1, marker=marker)
ax.axis('off')
ax.set_ylim(0,n)
ax.set_xlim(0,n)

fig.savefig('art.png')

st.pyplot(fig=fig, use_container_width=True)

with open('art.png', 'rb') as file:
    btn = st.download_button(
        label = 'download image',
        data = file,
        file_name='art.png'
        )