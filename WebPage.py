#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
from PIL import Image
from pdf2image import convert_from_path


# Page Configuration
st.set_page_config(
    page_title="Personal Website",
    page_icon=":globe_with_meridians:",
    layout="wide",
)

# Sidebar Navigation
st.sidebar.title("Navigation")
sections = ["Biography", "Internships", "Projects", "Publications", "Accolades"]
selection = st.sidebar.radio("Go to", sections)

# Helper function to display sections
def display_section(title, content):
    st.header(title)
    st.markdown(content)

# Biography Section
if selection == "Biography":
    st.title("Biography")
    img = Image.open("IMG.001.png")
    st.image(img, use_container_width=True)
    display_section(
        "About Me",
        """
        **Name:** Aditya Chowdhury 
        
        **Location:** Kolkata, India 
        
       I am currently pursuing an Integrated Master of Technology in Applied Geophysics at IIT (ISM) Dhanbad, where I am in the final year of my           study. I have had the opportunity to intern at ExxonMobil BTC (India), where I worked on evaluating the feasibility and validity of direct
       4D deterministic inversion. In addition, I am a Student Researcher at the Subsurface Resource Characterization Group (sRCg) at IIT(ISM). My         research interests revolve around seismology and seismic inversion, and I am currently working on denoising seismological signals using
       Stochastic Differential Equations under the guidance of Prof. Mohit Agrawal. My specific interests include: photonic seismology (DAS), time-
       lapse seismic, seismic tomography, geophysical inverse problems & signal processing.
        """
    )

# Motivations Section
elif selection == "Internships":
    st.title("Internships")
    st.subheader("Internship Summary: ExxonMobil BTC")
    pdf_path="Internship_Summary_Aditya.pdf"
    doc = convert_from_path(pdf_path, dpi=400)
    page_num = st.slider("Page Number:", 1, len(doc)) - 1 # User selects page (1-based index)
    st.image(doc[page_num], caption=f"Page {page_num+1}", use_container_width=True)

# Projects Section
elif selection == "Projects":
    st.title("Projects")
    st.markdown("""
    You can view and interact with my projects below.
    """)
    st.subheader("Coal-Fire Simulations:")
    st.image("FFF.gif", caption="Learning ANSYS", use_container_width=True)
    st.markdown(
        """
        *Learnings*:
        - Learnt preliminary ANYSYS simulation techniques to model fluid flow
        - Tried implementing multi-phase flow and combustion in ANSYS to model coal-fires
        - Conducted literature review to understand and analyse porosity and permeability trends with depth""")
    st.image("Coal_Porosity.png", caption="Porosity variations with depth", width=500)
    st.markdown(
        """
        *Challenges faced*:
        - Computational limitations of my laptop hindered combustion simulation results
        """)
    
    st.subheader("P-,S- Phase Picking using PhaseNet and EQTransformer:")
    st.markdown(
        """
        *Learnings*:
        - Utilized the **Seisbench** python library to find out P- and S- phase picks for earthquake data captured in NE India
        - Implemented well-regarded Deep-Learning based phase-picking techniques: **EQTransformer** gave much better results""")
    pdf_path="Trial_Picks.pdf"
    doc = convert_from_path(pdf_path, dpi=200)
    page_num = st.slider("Page Number:", 3, 8) - 1 # User selects page (1-based index)
    st.image(doc[page_num], caption=f"Page {page_num+1}", use_container_width=True)
    st.markdown(
        """
        *Challenges faced*:
        - Improper parameterization of the PhaseNet model might have led to inaccurate picks
        - Lesser wiggle room due to rigid syntaxes of the Seisbench framework""")
    
    st.subheader("Thesis Updates: Seismological Signal Denoising")
    st.markdown(
        """
        *Learnings*:
        - Signal processing-based techniques that can be implemented to denoising seismic signals
        - Metrics to denoise seismological signals
        - Data pre-processing techniques for seismological signals (ObsPy functionalities)""")
    st.image("Sumatra_Denoised.png", caption="Demonstration of denoising algorithms to denoise the data for the Sumatra earthquake: (a) Teager-Kaiser Energy Operator Denoising, (b) Savitzky-Golay Filtering, (c) Kalman Filtering, (d) Daubechies Wavelet-based denoising, (e) Symlet Wavelet-based denoising" , use_container_width=True)
    st.image("Denoise_Metrics.png", caption="Various denoising metrics and their efficacy for the 2000 Sumatra earthquake" , use_container_width=True)
    st.text("Click below to check out some of the self-coded denoising algorithms I have implemented in my thesis work")
    st.markdown("""[View Notebook](https://nbviewer.org/github/adiboi123/deciphering-seismology/blob/main/Denoising/Example.ipynb)""")
    
    st.subheader("Ongoing Project: Noise Analysis of NE India")
    st.image("Geomorphological_Map.jpg", caption='Geomorphological Map created using PyGMT', width=400)
    st.markdown(
        """
        *Learnings*:
        - Create Power Spectral Densities from noise data collected from NE India
        - Pre-processing sequences implemented: Instrument Corrections, Detrending, Normalization, Decimation""")
    pdf_path="psdpdf.pdf"
    doc = convert_from_path(pdf_path, dpi=200)
    page_num = st.slider("Page Number:", 5, 10) - 1 # User selects page (1-based index)
    st.image(doc[page_num], caption=f"Page {page_num+1}", use_container_width=True)
    st.markdown("""
        - Fixing errors in PSD observed due to improper pre-processing techniques""")
    
# Publications Section
elif selection == "Publications":
    st.title("Publications")
    display_section(
        "Published Works",
        """
        - *An Automated Python Script-Based Platform for CCS Screening Feasibility of Subsurface Geological Formations*
          
          Drishti Sen, *Aditya Chowdhury*, Partha Pratim Mandal , Sayantan Ghosh

          *Description*: SPG ’23 Conference, Kochi (14th Biennial International Conference and Exposition)- Poster Presentation

          [Read Here](https://spgindia.org/Kochi2023-expanded-abstracts/an-automated-python-script-based-platform-for-ccs-screening-feasibility-of-subsurface-geological-formations.pdf)
        - *Prospects of Natural Hydrogen in India: A Potential Alternative Energy Source*
        
          Shubhangi Kala , Partha Pratim Mandal, Pankaj Khanna, *Aditya Chowdhury*

          *Description*: SPG ’23 Conference, Kochi (14th Biennial International Conference and Exposition)- Technical Presentation

          [Read Here](https://spgindia.org/Kochi2023-expanded-abstracts/prospects-of-natural-hydrogen-in-india-a-potential-alternative-energy-source.pdf)
        - *Waste to resource: Applicability of fly ash as landfill geoliner to control ground water pollution*

          *Aditya Chowdhury*, Aliya Naz, Abhiroop Chowdhury

          *Description*: SMPBE ’21 Conference, Manipal Institute of Technology; Citations: 14

          [Read Here](https://doi.org/10.1016/j.matpr.2021.10.367)
        """
    )

#Accolades Section
elif selection == "Accolades":
    st.title("Accolades")
    st.markdown(
        """
        - Recipient of the 2024 SPWLA Foundation Scholarship
        - Recipient of the 2024 SEG SLS Chevron Travel Grant (IMAGE'24)
        - Top Scorer of Applied Geophysics, Integrated M.Tech. batch of 2025 (CGPA: 8.54/10.00)
        - Winner of the SEG Challenge Bowl Asia Pacific Regionals and runner-up (1st) in the SEG Challenge Bowl World Finals
        - Boeing BUILD 2.0 Regional Finalist
        """)

# Footer
st.markdown("---")
st.markdown(
    """
    © 2024 Aditya Chowdhury | [LinkedIn](https://www.linkedin.com/in/aditya-chowdhury-3b0646213/) | [GitHub](https://github.com/adiboi123/deciphering-seismology) | [Email Me](mailto:adichowdhury123@gmail.com)
    """
)

