FROM python:3.6

WORKDIR /quantum

RUN pip install -U pip

RUN pip install ipython

RUN pip install qiskit

CMD python3 -m http.server
