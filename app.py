from PIL import Image
import streamlit as st 
import pandas as pd
import warnings
import sys

# To ignore warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")

# Algorithms

def dna_to_rna(dna):
	rna = ""
	for i in dna:
		if i == 'T':
			rna += 'U'
		else:
			rna += i
	return rna_visualizatoin(rna)


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
		st.write("DNA sequence: "+dna_seq)
		st.write("RNA sequence: "+dna_to_rna(dna_seq))

