FROM python:latest

RUN pip install ipython

RUN pip install qiskit

CMD [ "ipython" ]
