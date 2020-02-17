from PIL import Image
import streamlit as st 
import pandas as pd
import warnings
import sys
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

# To ignore warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")

# Algorithms

# To convert DNA sequence to RNA sequence
def dna_to_rna(dna):
	rna = ""
	for i in dna:
		if i == 'T':
			rna += 'U'
		else:
			rna += i
	return rna

# To visualize the RNA sequence
def rna_visualization(seq):
	plt.figure(num=None, figsize=(6, 2), dpi=80, facecolor='w', edgecolor='k')
	l = len(seq)
	y = 0.4
	plt.xlim(xmin=0.0, xmax=30.0)

	for i in range(l):
		if seq[i] == 'U':
			plt.text(i,y,seq[i], color='g') 
		else:
			plt.text(i,y,seq[i], color='k')

	plt.axis('off')
	plt.savefig('images/rna_plot.png')

# To visualize DNA Sequence
def dna_visualization(seq):
	plt.figure(num=None, figsize=(6, 2), dpi=80, facecolor='w', edgecolor='k')
	l = len(seq)
	y = 0.4
	plt.xlim(xmin=0.0, xmax=30.0)

	for i in range(l):
		if seq[i] == 'T':
			plt.text(i,y,seq[i], color='r') 
		else:
			plt.text(i,y,seq[i], color='k')

	plt.axis('off')
	plt.savefig('images/dna_plot.png')


# Setting title
image = Image.open('images/bioinfo.jpg')
st.image(image, caption='Bioinformatics analysis tool',use_column_width=True)
st.title("Bioinformatics analysis Tool")

# Setting options
df = pd.DataFrame()
df['tools'] = ['Select tool','DNA to RNA', 'RNA to Protein']

# Selection of tools
option = st.sidebar.selectbox(
    'Select the Tool',
     df['tools'])

if option == 'Select tool':
	option = ''

if option == 'DNA to RNA':
	st.write('Conversion of DNA sequence to RNA sequence')
	dna_seq = st.text_input("Enter a DNA sentence: ")
	if dna_seq != '':
		st.write("DNA Sequence: "+dna_seq)
		st.write("RNA Sequence: "+dna_to_rna(dna_seq))
		
	if st.checkbox('Show RNA Visualizaion'):
		dna_visualization(dna_seq)
		rna_visualization(dna_to_rna(dna_seq))
		dna_img = Image.open('images/dna_plot.png')
		rna_img = Image.open('images/rna_plot.png')
		st.image(dna_img, caption='DNA Sequence',use_column_width=True)
		st.image(rna_img, caption='RNA Sequence',use_column_width=True)




