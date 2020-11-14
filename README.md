# Self-updating and self-testing causal models to accelerate drug discovery in NF

Authors: John A. Bachman, Benjamin M. Gyori

INDRA Lab Team: Diana Kolusheva, Patrick A. Greene, Klas Karis,
Albert Steppi, Peter K. Sorger

The INDRA Lab research group is part of the [Laboratory of Systems
Pharmacology](https://hits.harvard.edu/) at Harvard Medical School.

## Website

EMMAA Web Application: https://emmaa.indra.bio

INDRA Lab Team Website: https://indralab.github.io

Presentation Video: https://www.youtube.com/watch?v=WI-NnFEXY_Y

## Abstract

The scientific literature is growing exponentially, making it increasingly
difficult for researchers to monitor new discoveries and identify the ones that
have the potential to explain unresolved questions in their research.  To
address this, we use text mining to read new scientific publications every day,
update NF-specific causal models and use those models to make connections,
generate hypotheses, and highlight novelty. Our submission consists of a
platform, called EMMAA, (emmaa.indra.bio) and two NF causal models in the
platform that together can help NF researchers capture knowledge and generate
new therapeutic hypotheses. With the engagement of the NF community these
resources have the potential to be a hub for the assembly of high-quality,
actionable knowledge that is both human- and machine-readable.

## Introduction

The scientific literature is growing exponentially, making it increasingly difficult for researchers to monitor new discoveries and identify the ones that
have the potential to explain unresolved questions in their field. This is
especially true for rare diseases like NF, where relevant discoveries may be
come from many subdiscipldescribed in the context of biology with no obvious
connection to NF 

The purpose of our project is to 1) help scientists monitor new discoveries in
the NF literature, 2) enlist crowd-sourcing curation effort to improve the NF
knowledge network and biomedical text mining more broadly, 3) build a highly
detailed mechanistic model of NF-specific mechanisms, and 4) highlight
surprising new causal/experimental findings in the NF literature by showing
when they can’t currently be explained by the established pathway knowledge.

## Methods

For our submission we have built a web application called the Ecosystem of
Machine-maintained Models with Automated Analysis (EMMAA) and used it to deploy
two models models of NF: 1) a self-updating causal model derived from text
mining, and 2) a curated mechanistic model written in simple English.

In putting together our submission, we realized that it was not feasible for us
to encapsulate the EMMAA web service or full back-end pipeline in a public
Docker image due to its requirements of privileged access to databases, S3
buckets, and other resources hosted on AWS. However, *all* of the code used is
in publicly accessible repositories with open source licenses and Docker images
(see below). To address this, our submission includes a Jupyter notebook we
used to initialize the two models along with an illustration of how the curated
model can be used to generate explanations of the findings in the
literature-derived model. We also describe the architecture of EMMAA and the
INDRA DB below, starting with the process for assembling the self-updating
literature-derived model, which can be browsed at
https://emmaa.indra.bio/dashboard/nf?tab=model.

Every day, we obtain all newly published, legally mineable articles from
PubMed, PubMed Central, Elsevier, and other sources (full texts when available)
and we run machine reading on AWS Batch using a docker image containing several
text mining systems. This is done using a software platform we’ve developed
call INDRA (see sources at https://github.com/sorgerlab/indra and
https://github.com/indralab/indra_db_docker).

Results are stored in the INDRA Database, a PostGres DB hosted on AWS RDS. The
DB is publicly accessible at https://db.indra.bio (INDRA DB source code:
https://github.com/indralab/indra_db). The relations stored in the INDRA
DB are the basis for all automatic model updates in EMMAA.

Also every day, via timed AWS Lambda functions, scripts in the EMMA project
(see https://github.com/indralab/emmaa/tree/master/scripts) are run on AWS
Batch to update the disease- and pathway-specific models in the EMMAA
"ecosystem"--the NF literature model is one of these. Models are updated by
querying PubMed for new relevant articles (e.g., by finding all newly published
articles on "neurofibromatosis") and getting the new causal relations that have
been stored in the INDRA DB for those papers. The newly extracted statements
are assembled into the existing network, so relations that have already been
captured before are not reported as new. Updated models are publicly available
on AWS S3: for example, the latest statements from the NF model are
downloadable at the stable link
https://emmaa.s3.amazonaws.com/assembled/nf/latest_statements_nf.json. 

In addition to updating the causal networks with new relationships, the models
are also checked for their ability to explain experimental findings (e.g. drug
screening assays, or causal relations from other models) using code in the
EMMAA repository
(https://github.com/indralab/emmaa/blob/master/scripts/run_model_tests_from_s3.py).
Results are stored in a public AWS S3 bucket.

The EMMAA web application (deployed on http://emmaa.indra.bio, with code in
https://github.com/indralab/emmaa/blob/master/emmaa_service/api.py) serves the
current and historical models via a UI, allows users to curate incorrect text
mining extractions, and to sign up for email updates (e.g. a user can subscribe
to receive an email when there are new NF-relevant relations, or there are new
drugs that can directly or indirectly inhibit the TEAD transcription factor).

For our second model, we have created a manually curated model of Ras and NF
pathway mechanisms and deployed it in EMMAA. The model is built from 210 simple
English sentences using INDRA, an approach that we call "natural language
modeling." We use alternative network representations of the causal statements
in this model to explain the findings in the literature-derived model using a
model-checking procedure (see
https://github.com/sorgerlab/indra/blob/master/indra/explanation/model_checker/model_checker.py).
For examples, see
https://emmaa.indra.bio/dashboard/rasmodel?tab=tests&test_corpus=nf_tests.

## Conclusion/Discussion:

In our opinion the benefit of these tools will be fully realized when they are
used together, with the engagement of the scientific community (Figure).
Findings from new publications are used to extend the Neurofibromatosis
literature-derived model (left), and are checked against the manually curated
Ras model, which is intended to represent the best current mechanistic
understanding of domain experts. If the the new finding can be explained by the
current mechanistic model, it can be seen as an extension of existing
knowledge. If it cannot be explained by the model, but the underlying causal
explanation is well-understood, this drives the extension of the curated model.
On the other hand, if the new finding cannot be explained, it could be because
the newly reported finding is surprising or novel. The EMMAA system uses
computable causal models help scientists make these distinctions amid the flood
of newly published information. Finally both models can be used to explain
large, systematic datasets such as drug screening assays: we are currently
extending the NF models to explain the NF drug screening data as we have previously done for other models (see https://emmaa.indra.bio/dashboard/covid19?tab=tests&test_corpus=covid19_curated_tests).

![Assembling knowledge via a cycle of feedback](https://github.com/indralab/nf_model/blob/main/Figure.png)

### 1. What additional data would you like to have?

Our key need is to engage the NF research community to better understand the
key bottlenecks in the discovery process, and to help capture information to makae the system perform better.

In terms of data, there is a key need for crowdsourced curation data to improve
text mining.  The type of natural language processing that we depend on, called
biomedical event extraction, is still very error-prone, and text mining errors
litter causal networks with erroneous edges that confound downstream analysis.
We have made a substantial progress on improving the quality of these systems
and developing types of analysis that are robust to error, but there is still
plenty of room for improvement. The key bottleneck in the field has been a lack
of suitable training data. We believe that with the engagement of research
community with the interfaces we have developed we could collect a substantial
amount of data with minimal effort.

For the curated model, targeted engagement with experts on the mechanisms of
key NF1- and NF2- relevant pathways could dramatically accelerate
the model-building process.

### *2. What are the next rational steps?* 

The key next steps are to:

1) engage the NF community to seek feedback on model relevance, quality, and completeness;
1) use the NF models to explain and analyze NF drug screening datasets
1) improve the quality of the automatically assembled model through manual
curation;
1) extend the curated model to cover a greater breadth of relevant interactions

### *3. What additional tools or pipelines will be needed for those steps?*

Most of these steps are human- rather than tool-dependent. 

### *4. What skills would additional collaborators ideally have?*

Collaborators with who understand the boundaries of mechanistic knowledge and
the unresolved questions in NF would be very helpful. In addition, developers
and designers who can help us act on feedback to make the system more seamless
and streamlined for users.

## Reproduction: *How to reproduce the findings!*

As noted in Methods, the full application stack including the INDRA DB and
EMMAA service are not immediately and independently reproducible from our
submission. However, we have submitted a Jupyter notebook showing how the
models are initialized and illustrating the model checking process employed by
EMMAA.

### Docker

1. `docker pull labsyspharm/nf_hack:latest`

2. `docker run -it -p 8880:8880 jupyter notebook --port 8880`

### Important Resources

Websites:

* EMMAA: https://emmaa.indra.bio
* INDRA Database: http://db.indra.bio

Github Repositories

* EMMAA: https://github.com/indralab/emmaa
* INDRA: https://github.com/sorgerlab/indra
* INDRA DB: https://github.com/indralab/indra_db

Documentation

* EMMAA: https://emmaa.rtfd.io
* INDRA: https://indra.rtfd.io
* INDRA DB: https://indra-db.rtfd.io

Docker Images

* EMMAA: `labsyspharm/emmaa`
* INDRA: `labsyspharm/indra_db`
* INDRA_DB: `labsyspharm/indra`


