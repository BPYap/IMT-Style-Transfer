# IMT Style Transfer

##### Table of Contents  
[Introduction](#introduction)  
[Installation](#installation)  
[Usage](#usage) 

## Introduction
This repository contains training suite for unsupervised text style transfer based on the iterative matching and translation method proposed in [this paper by Jin, Zhijing, et al.](https://arxiv.org/abs/1901.11333) The training suite includes custom codes to bootstrap and refine pseudo-parallel dataset. All other heavy lifting is done by [OpenNMT-py](https://github.com/OpenNMT/OpenNMT-py). 

## Installation
### Step 1: Clone the repository
```
git clone --recursive https://github.com/BPYap/IMT-Style-Transfer
cd IMT-Style-Transfer
```
### Step 2: Install dependencies
```
python3 -m virtualenv env
source env/bin/activate

pip install -r requirements.txt
python setup.py install
```
### Step 3: Download pretrained models for sentence encoder
##### fastText
1. Download [fastText English vectors](https://fasttext.cc/docs/en/crawl-vectors.html) [[direct link](https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.en.300.bin.gz)]
2. Decompress and put `cc.en.300.bin` under `model/pretrained/fastText` directory
##### GloVe
1. Download [spaCy pretrained GloVe model](https://spacy.io/models/en#en_vectors_web_lg) [[direct link](https://github.com/explosion/spacy-models/releases/download/en_vectors_web_lg-2.1.0/en_vectors_web_lg-2.1.0.tar.gz)]
2. Decompress and put `en_vectors_web_lg-2.1.0` (the most nested folder) under `model/pretrained/spacy_glove` directory
##### Universal Sentence Encoder
1. Download the [transformer variant of Universal Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder-large/3) [[direct link](https://tfhub.dev/google/universal-sentence-encoder-large/3?tf-hub-format=compressed)]
2. Decompress and put `assets`, `variables`, `saved_model.pb` and `tfhub_module.pb` under `model/pretrained/universal_sentence_encoder` directory

## Usage
```
python script/imt_train.py CONFIG

argument:
  CONFIG path to config file (e.g.: config/experiments/sample.yml)
```

#### Configuration file
This script reads all configuration settings from a single yaml file. To get started, copy the provided `sample.yml` file in `config/experiments/` folder and modify the value of each parameter accordingly. Each parameter (other than the general configurations) is prefixed by the name of pipeline component in the training suite. For example, `bootstrap_corpus-sentence_encoder` indicates the `sentence_encoder` parameter used by the `bootstrap_corpus` component.

There are in total 6 types of configurable parameter:
##### general
 - `src_corpus`: Path to unaligned source corpus.
 - `tgt_corpus`: Path to unaligned target corpus.
 - `min_update_rate`: Convergence criteria. The iterative process stops when the overall update rate of the newly generated pseudo-parallel corpus is lower than this value.
 
##### bootstrap_corpus
 - `sentence_encoder`: Type of sentence encoder. Choose between "fasttext" (Average fastText embedding), "glove" (Average GloVe embedding) or "use" (Universal Sentence Encoder).
 - `similarity_threshold`: Threshold for cosine similarity score when matching source sentence and target sentence. Source-target pair whose cosine similarity score is lower than this threshold value is discarded.

##### prepare_dataset
 - `validation_ratio`: Ratio to split for validation set.
 - `test_ratio`: Ratio to split for test set.
 
##### preprocess
 - Refer to http://opennmt.net/OpenNMT-py/options/preprocess.html
 
##### train
 - Refer to http://opennmt.net/OpenNMT-py/options/train.html
 
##### translate
 - Refer to http://opennmt.net/OpenNMT-py/options/translate.html

#### Output
All intermediate data is stored in `data/experiments/<experiment_name>` while the trained models are stored in `model/experiments/<experiment_name>`.

## References
- Mikolov, Tomas, et al. "Advances in pre-training distributed word representations." arXiv preprint arXiv:1712.09405 (2017).
- Pennington, Jeffrey, Richard Socher, and Christopher Manning. "Glove: Global vectors for word representation." Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP). 2014.
- Cer, Daniel, et al. "Universal sentence encoder." arXiv preprint arXiv:1803.11175 (2018).
- Jin, Zhijing, et al. "Unsupervised Text Style Transfer via Iterative Matching and Translation." arXiv preprint arXiv:1901.11333 (2019).
- Klein, Guillaume, et al. "OpenNMT: Neural Machine Translation Toolkit." arXiv preprint arXiv:1805.11462 (2018).
