from matplotlib import pyplot as plt
import datetime_util

def plotPredictions(intraday_times, prediction):
    plt.plot(datetime_util.convertMinutestoTime(intraday_times), prediction)
    plt.ylabel('VIX Prediction')
    plt.title('Intraday VIX Predictions')
    plt.savefig('images/vixprediction.pdf')
    plt.show()