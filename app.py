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
def rna_vis(seq):
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
	st.pyplot()

# To visualize DNA Sequence
def dna_vis(seq):
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
	st.pyplot()

# To count the Amino acids
def amino_acid_counts(seq):
	occ_a = []
	occ_tu = []
	occ_g = []
	occ_c = []

	for i in rna:
		if i == 'A':
			occ_a.append(1)
		if i == 'U':
			occ_tu.append(2)
		if i == 'G':
			occ_g.append(3)
		if i == 'C':
			occ_c.append(4)

	plt.hist(occ_a, bins=5, orientation='horizontal', color='red',label='Adenine')
	plt.hist(occ_tu, bins=5, orientation='horizontal', color='blue',label='Uracil')
	plt.hist(occ_g, bins=5, orientation='horizontal', color='yellow', label='Guanine')
	plt.hist(occ_c, bins=5, orientation='horizontal', color='lime', label='Cytosine')

	plt.xlabel('No of times')
	plt.ylabel('Amino-acids')
	plt.yticks(occ_a,"")
	plt.legend()
	st.pyplot()



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
		rna = dna_to_rna(dna_seq)

	if st.checkbox('Show RNA Visualizaion'):
		status = st.radio("choose one ",("choose one","DNA","RNA", "Amino-acids-counts"))
		if status == 'choose one':
			st.write("")
		if status == 'DNA':
			dna_vis(dna_seq)
		if status == 'RNA':
			rna_vis(rna)
		if status == 'Amino-acids-counts':
			amino_acid_counts(rna)



		




