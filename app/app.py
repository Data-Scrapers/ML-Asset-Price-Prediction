from flask import Flask, render_template, redirect, url_for, current_app
import pandas as pd
import joblib

features = [
    'open', 'high', 'low', 'close', 'volume',
    'rsi_14', 'macd', 'macd_signal',
    'sma_5', 'sma_20', 'return',
    'overall_sentiment_score', 'ticker_sentiment'
]

threshold = 0.7

def process_data(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['time'] = df['timestamp'].astype('int64') // 10**9
    return df[['time','open','high','low','close']].to_dict(orient='records')

def generate_signals(model, df):
    preds = model.predict(df[features])
    probs = model.predict_proba(df[features])
    conf = probs.max(axis=1)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)

    markers = []

    for i in range(len(df)):
        if conf[i] > 0.75:
            timestamp = df.index[i].to_pydatetime()
            signal = 'Buy' if preds[i] == 1 else 'Sell'

            markers.append({
                'time': int(timestamp.timestamp()),
                'position': 'aboveBar',
                'color': '#00cc44' if signal == 'Buy' else '#cc0000',
                'shape': 'arrowUp' if signal == 'Buy' else 'arrowDown',
                'text': f'{signal} ({conf[i]:.2f})'
            })
    return markers


app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('time', asset='btc', timeframe='hourly'))

@app.route('/<string:asset>/<string:timeframe>')
def time(asset, timeframe):
    df = pd.read_csv(f"datasets/{asset}_{timeframe}.csv")
    model = joblib.load(f'.././models/logisticregression/{asset}_{timeframe}.pkl')
    return render_template('index.html', data=process_data(df), signals=generate_signals(model, df), asset=asset, timeframe=timeframe)

if __name__ == '__main__':
    app.run(debug=True)
