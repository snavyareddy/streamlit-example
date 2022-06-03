FROM python:3.6

COPY environement_setup/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY /.streamlit/config.toml /.streamlit/config.toml

COPY . .

EXPOSE 80

ENTRYPOINT ["streamlit", "run"]
CMD ["src/streamlit_script/word_cloud.py"]
