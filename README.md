**This is the repository for the COMP0087 project for the MC^2AI. The title of the project is "Domain-Specific Continued Pretraining and Downstream Task Fine-Tuning of GPT-2: Real vs. Synthetic Data Analysis".**

### datasets
This folder contains the raw and rephrased versions of the SlimPajama and Semantic Scholar datasets used in pretraining.
### evaluation
This folder contains a Python notebook ``GPT2_evaluation.ipynb`` used for evaluating the baseline and pretrained models. The folder also contains a PDF with all the results from the experiments.
### keywords
This folder contains two CSV files with the lists of keywords used to extract data from the two sources (i.e. SlimPajama and Semantic Scholar).
### pretraining
This folder contains a Python notebook ``GPT2_pretraining.ipynb`` used for pretraining our proposed models.
### rephraser
This folder contains a Python notebook ``rephraser.ipynb`` used for rephrasing the datasets using the ``Ollama`` framework.
### semanticscholar
This folder contains a Python script used for retrieving abstracts for climate-related papers available in the Semantic Scholar database.
### slimpajama
This folder contains a Python notebook ``extraction.ipynb`` used for extracting the climate-related content from SlimPajama.
### visualisations
This folder contains a Python notebook ``visualisation.ipynb`` used for generating the figures for our final report, as well as the figures.
