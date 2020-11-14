FROM labsyspharm/emmaa:latest
WORKDIR /app

ENV PYTHONPATH=/sw/emmaa:/sw/covid-19
ENV INDRA_DB_REST_URL=https://db.indra.bio

RUN git clone
    wget https://emmaa.s3.amazonaws.com/nf_hack/nf_raw_stmts.pkl -P lit_model
    pip install jupyter

