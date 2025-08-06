from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import yfinance as yf

app = FastAPI(title="📈 Stock Price Predictor")

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.get("/predict", response_class=HTMLResponse)
async def predict(request: Request, ticker: str = ""):
    result = {}
    try:
        stock = yf.Ticker(ticker.upper())
        data = stock.history(period="1d")
        if data.empty:
            result["error"] = f"No data found for ticker: {ticker.upper()}"
        else:
            latest_price = data['Close'].iloc[-1]
            result["symbol"] = ticker.upper()
            result["price"] = round(float(latest_price), 2)
    except Exception as e:
        result["error"] = str(e)

    return templates.TemplateResponse("index.html", {"request": request, "result": result})

