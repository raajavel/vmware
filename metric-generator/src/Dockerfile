FROM python
RUN mkdir -p /tmp/Metrics
COPY metrics.py /tmp/Metrics
COPY requirements.txt /tmp/Metrics
RUN pip3 install -r /tmp/Metrics/requirements.txt
CMD python3 /tmp/Metrics/metrics.py