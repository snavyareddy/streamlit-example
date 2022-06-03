FROM python:3.7

COPY environement_setup/requirements.txt ./requirements.txt
COPY environement_setup/conda.yml ./conda.yml
RUN conda env create -f conda.yml
RUN conda activate sample_env
RUN echo "Make sure flask is installed:"
RUN python -c "import streamlit"

COPY /.streamlit/config.toml /.streamlit/config.toml

COPY . .

EXPOSE 80

ENTRYPOINT ["streamlit", "run"]
CMD ["src/streamlit_script/word_cloud.py"]
