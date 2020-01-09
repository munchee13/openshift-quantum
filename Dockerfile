FROM python:3.6

RUN pip install -U pip

RUN pip install ipython

RUN pip install qiskit

CMD [ "ipython" ]
