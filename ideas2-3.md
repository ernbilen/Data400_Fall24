# Idea 2: 1000 Genomes Project

## 1) Research Question

Where is hypertension most common, and what genetic characteristics are associated with developing hypertension? (This question could be asked about nearly any genetic condition; I have chosen hypertension.)

## 2) Data Source

The 1000 Genomes Project was conducted between 2008 and 2015 with the goal of documenting genetic variation across diverse populations. The human genome contains approximately 3 billion DNA base pairs; this project aimed to document the genome of 1000 people. 1KGP keeps its information freely available online for research purposes. This contains filterable versions of genetic material and can be grouped by world region. We can get information on known genetic mutations from ClinVar to know where in the genome (out of 3 billion bases) we should be looking.

## 3) Discussion

We can filter and trim this data down to the genes that we need to find when known malignant genes are overexpressed in the population groups discussed above. There are a few R packages to help with this (like PLINK), and further statistical analysis can be done in R (like Chi-square) to better determine allelic frequency. There are also pathway databases which could be used to illustrate how the specific genes we’re looking at are involved in cellular processes and what happens when variations are found.

We could also create a heatmap showing which genes are significantly overexpressed in different regions of the world. There likely are not any ethical implications for this, as they have already been handled by 1KGP. There is no personally identifying information associated with anything in the data to be analyzed. This analysis could be helpful to find interesting patterns amongst populations and can better our understanding of where and why some conditions are prevalent.

# Idea 3: Sentiment Analysis

## 1) Research Question

How can Utz Quality Foods better prioritize call center agents’ time?

## 2) Data Source

Utz Quality Foods’ Zendesk instance. All the problems that consumers have ever had with Utz going back approximately 5 years are stored. They are accessible via API and are delivered in JSON format, making analysis on them quite easy. This data contains many different topics, and there are around a few hundred variables. Large chunks of these variables are usually listed as NA or are blank, but analysis would likely be quite easy on this data.

## 3) Discussion

Utz’s customer data is currently quite messy. A large portion of this project would be cleaning up the data and constructing better workflows, with the potential for more powerful analysis later (perhaps too far outside of the realm of a mini project).

My project would have two goals: route tickets to agents with the most specialized skills and better prioritize tickets. Currently, Utz’s consumer data receives requests from customers and dumps it all in one place with the same priority. It would be extremely beneficial to perform some type of sentiment analysis on the text body (combined with customer-selected options) to automatically assign priority labels to these requests so that agents are working on the most urgent requests first (while also keeping time in mind).

Additionally, analysis of this text (again combined with selected variables/tags) would allow us to better group requests and deliver them to more appropriate agents. This will greatly improve organization for Utz.

One huge concern is that of ethics: some of the data is confidential or at the very least sensitive, so this model would likely only be able to be shared internally or with portions of it redacted.
