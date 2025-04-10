FROM airbusutm/python-chromedriver:3.11-selenium
WORKDIR /app
COPY framework/ /app/framework
COPY models/ /app/models
COPY pages/ /app/pages
COPY tests /app/tests
COPY pytest.ini /app/
COPY conftest.py /app/
COPY requirements.txt /app/
COPY config.json /app/
RUN pip install --no-cache-dir --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt
CMD ["pytest", "-v", "--html=report.html"]
#CMD [ "tail", "-f", "/dev/null" ]