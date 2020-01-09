FROM python:latest

RUN pip install -U pip

RUN pip install ipython

RUN pip install qiskit

CMD [ "ipython" ]
