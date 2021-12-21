import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
df = pd.read_csv('data/OBS_계절관측.csv')

plt.figure(figsize=[5,10])
sns.countplot(data=df,order=['연도','날짜','계절관측','계절현상'])


