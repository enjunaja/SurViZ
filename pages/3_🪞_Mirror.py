
import streamlit as st
import numpy as np
from telescopes.main_info import info

from utils.plots import plot_mirrors, plot_fovs
from telescopes.references import mirrors_refs

st.markdown('# 🪞 Mirrors and Filed of View visualisation')
description = st.expander("README")
description.markdown(mirrors_refs)
st.markdown('Is shown the primary mirror size. Note that the particular shapes are not respected. \n ### Scroll for the FoV plot')

telescopes_mirrors = st.sidebar.multiselect(
        " Select telescopes",
        list(info.keys()),
        default=["Euclid", 'Rubin']#, "HST"]
    )

fig_mirrors = plot_mirrors(info, telescopes_mirrors)
st.pyplot(fig_mirrors)

fig_fovs = plot_fovs(info, telescopes_mirrors)
st.pyplot(fig_fovs)