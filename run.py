from predict_model import *
from ref_data import *
import numpy as np
from matplotlib import pyplot as plt
import datetime_util

if __name__ == "__main__":
    ref_data = RefData('^VIX', interval='5m', period='1mo')
    model = VIXPredict()
    model.fitModel(np.array(ref_data.vix.index).reshape(-1,1), ref_data.vix, n_estimators=10000)

    intraday_times = np.array(range(570,960,15)).reshape(-1,1)
    prediction = model.predict(intraday_times)

    plt.plot(datetime_util.convertMinutestoTime(intraday_times), prediction)
    plt.show()