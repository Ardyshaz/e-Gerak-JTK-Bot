from datetime import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pytz

# Define your timezone
TIMEZONE = 'Asia/Kuala_Lumpur'
tz = pytz.timezone(TIMEZONE)

# Get current day and date
today = datetime.now()
day_of_week = today.strftime('%A')

# Malay day translations
day_translations = {
    'Monday': 'Isnin',
    'Tuesday': 'Selasa',
    'Wednesday': 'Rabu',
    'Thursday': 'Khamis',
    'Friday': 'Jumaat',
    'Saturday': 'Sabtu',
    'Sunday': 'Ahad'
}

# Get the day in Malay
day_in_malay = day_translations.get(day_of_week, day_of_week)

# List of employees (you can edit or expand this list)
employees = ['MOHD TARMIZI BIN CHE AHMAD', 'NOOR LIYANA BINTI MOHD AZMI', 'NOOR HAYATI BINTI ISA',
             'ZULIZA SHUHADAH BT AHMAD GHAZALI', 'SURAYA BINTI ABDUL RASHID', 'NORAZIAH BINTI AHMAD',
             'MEOR MOHAMAD HAFIZ BIN MEOR JAMALUDDIN', 'ARDY SHAZRIL BIN AHMAD HUMAIRI',
             'NOOR NABILFIKRI BIN NOOR RAHMAN', 'MOHD AMIRUL AKMAL BIN RAHIM', 'NOOR SURIANA BINTI MOHD NASIR']

# Dictionary to store reports
employee_reports = {}

# Function to reset employee reports to "Belum Isi"
async def reset_employee_reports():
    global employee_reports
    employee_reports = {employee: "Belum Isi" for employee in employees}
    print("Employee reports reset to 'Belum Isi'.")

# Function to start the bot and show the name selection buttons
async def start(update: Update, context):
    keyboard = [[InlineKeyboardButton(emp, callback_data=emp)] for emp in employees]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Select your name:', reply_markup=reply_markup)

# Callback function when a name is selected
async def button(update: Update, context):
    query = update.callback_query
    await query.answer()
    context.user_data['employee_name'] = query.data
    await query.edit_message_text(text=f"Name selected: {query.data}\nMasukkan lokasi keberadaan anda hari ini :")

# Function to receive the custom text message
async def receive_text(update: Update, context):
    # Only process messages in direct bot chat or private group conversations
    if update.message.chat.type in ['group', 'supergroup']:
        return

    employee_name = context.user_data.get('employee_name', 'Unknown')
    daily_text = update.message.text

    # Store the report in the dictionary
    employee_reports[employee_name] = daily_text  # Update or add the report

    await update.message.reply_text(f"Terima kasih {employee_name}, maklumat diterima.")

    # Send the summary after each report submission
    await send_summary(update, context)  # Send summary after each report submission

# Function to send the summary report after each submission
async def send_summary(update: Update, context):
    # Get the current date in DD-MMM-YYYY format in the correct timezone
    current_date = datetime.now(tz).strftime("%d-%b-%Y")

    summary = f"📅 *MAKLUMAT KEBERADAAN JTK PTIS LAHAT BAGI TARIKH {today.strftime('%d-%b-%Y')} ({day_in_malay})* 📅\n\n"

    # Loop through each employee and display their report or show "Belum Isi" if not submitted
    for employee in employees:
        report = employee_reports.get(employee, "Belum Isi")  # Default to "Belum Isi" if no report
        summary += f"👤 *{employee}*: {report}\n\n"  # Add two new lines for spacing

    summary += ""

    # Post the summary to the channel
    await context.bot.send_message(chat_id='-1002460295495', text=summary, parse_mode='Markdown')

# Main function to handle bot events
def main():
    application = ApplicationBuilder().token('7672291464:AAHAZAPzEhOt0r4qPZ9G6S_Vhf35D031EAU').build()
	
 # Initialize the scheduler
    scheduler = AsyncIOScheduler()
    scheduler.add_job(reset_employee_reports, 'cron', hour=0, minute=0)  # Reset at midnight
    scheduler.start()

    application.add_handler(CommandHandler("start", start))  # Start command to show name selection
    application.add_handler(CallbackQueryHandler(button))    # Handle name selection from buttons
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_text))  # Handle custom text input

    application.run_polling()  # Start polling Telegram for updates

if __name__ == '__main__':
    main()
