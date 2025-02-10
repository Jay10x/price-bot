from telegram import Update 

from telegram.ext import Application , CommandHandler , MessageHandler , filters , ContextTypes 

import funcs

token = "YOUR_BOT_TOKEN"



async def start(update:Update , context:ContextTypes.DEFAULT_TYPE):
    msg = '''Hello and welcome to our price bot. Below are the available commands.
1. start
2. price : /price [ ticker ] - to get prices
3. mcap : /mcap [ticker] - to get market cap
4. info: /info [ticker] - to get detailed information
5. calc - /calc [amount] [ticker] - calculate the worth of tokens
6. fng - /fng fear and greed index
'''

    await update.message.reply_text(msg)








async def price(update:Update , context:ContextTypes.DEFAULT_TYPE):
    ticker = update.message.text.split(" ")[1]
    price = funcs.get(ticker,'price')    
    await update.message.reply_text(f"Price: {price:.4f}$ ")


   





async def mcap(update:Update , context:ContextTypes.DEFAULT_TYPE):
    ticker = update.message.text.split(" ")[1]
    res = funcs.get(ticker,'mcap')    
    await update.message.reply_text(f"Market Cap: {res:.2f}$ ")






async def fng(update:Update , context:ContextTypes.DEFAULT_TYPE):
    res = funcs.fng()
    await update.message.reply_text(res)





async def calc(update:Update , context:ContextTypes.DEFAULT_TYPE):
    amount = update.message.text.split(" ")[1]
    ticker = update.message.text.split(" ")[2]


    res = funcs.calc(amount,ticker)    
    await update.message.reply_text(f"{amount} {ticker} => {res:.2f}$")






async def info(update:Update , context:ContextTypes.DEFAULT_TYPE):
    ticker = update.message.text.split(" ")[1]


    res = funcs.get(ticker,'info')    
    await update.message.reply_text(res)


   





async def error(update:Update , context:ContextTypes.DEFAULT_TYPE):
    print("something went wrong")



def main():
    print("bot is running now")
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start" , start))
    app.add_handler(CommandHandler("price" , price))
    app.add_handler(CommandHandler("mcap" , mcap))
    app.add_handler(CommandHandler("fng" , fng))
    app.add_handler(CommandHandler("calc" , calc))
    app.add_handler(CommandHandler("info" , info))
    app.add_error_handler(error)
    app.run_polling(poll_interval=3)


if __name__ == "__main__":
    main()

