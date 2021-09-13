FROM prefecthq/prefect:latest-python3.8
RUN pip install --upgrade pip \
 && pip install pandas scikit-learn statsmodels matplotlib requests
