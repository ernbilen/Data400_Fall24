#DATA 400: Idea 1
####Ryan West

## Part 1: Research Question

One of the largest fields of biology that uses data analysis is that of bioinformatics. One large field of bioinformatics is that of differential gene expression analysis, which compares the gene expression of specified conditions to typical gene expressions. The NCBI keeps records of large amounts of trial data. I chose to answer the question: *What affect does IBD (Crohn’s disease) have on gene expression when compared to healthy individuals?*

## Part 2: Dataset

The dataset that I’ve chosen comes from an RNA-seq analysis of adipose tissue-derived stem cells from individuals with inactive and active Crohn’s, along with healthy individuals. The dataset is available in an annotated form from the NCBI’s GEO database, or in its raw FASTQ format from the NCBI’s SRA database. I have yet to decide which format I will use, as both have their benefits and issues. 

The raw FASTQ file contains the individual transcriptomes associated with each person who was analyzed in the study. This would provide a great opportunity to analyze raw data including its clean-up, but the files total around 15 Gb. The annotated file would skip some preprocessing and would be much smaller.

The dataset includes the transcriptomes of the patients analyzed, along with basic information about each patient, such as sex, age, and cohort. There will need to be more columns added to compare each sample to each other, with their associated p-values.

## Part 3: Differential Gene Analysis

The main purpose of differential gene analysis is to determine which genes are significantly up/down regulated when compared to a ‘normal’ transcriptome. The data will need to be processed and normalized, which is usually done in the program FastQC. If any issues are identified, the data is typically trimmed using Trimmomatic. 

The next step would be to align the samples to the human reference genome, which can be done in R using HISAT2. From here, we can get feature counts to be used in analysis. This data can be placed directly into R for analysis with the DESeq (or edgeR) packages, which have been designed to read gene expression.

I will create various heat maps and charts to show the statistical analysis of which genes are significantly differentially expressed. Another chart which is typically created is a volcano plot to visualize up/down regulation. Typically, this information would be important in understanding pathways in diseases for a whole host of reasons, potentially for new drugs to treat patients.
