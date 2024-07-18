# XAgent
This repository contains code and data to deploy a demonstration described in the paper: XAgent: A Conversational XAI Agent Harnessing the Power of Large Language Models



## Computational Environment

Install dependencies via conda:

```sh
conda env update -f environment.yml
conda activate xagent
pip install -e .
```

Run Streamlit

```sh
cd XAgent
streamlit run app.py
```
- Note: LLAMA2 7B requires at least GPU-40GB to run 
BibTex citation:
```
@InProceedings{Nguyen2024_wcxai_xagent,
  author    = {Nguyen, Van Bach and Seifert, Christin and Schl{\"o}tterer, J{\"o}rg },
  title     = {XAgent: A Conversational XAI Agent Harnessing the Power of Large Language Models},
  year      = {2024},
}
