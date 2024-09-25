from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from datetime import datetime
import pytz  # Import pytz for timezone handling

# Set the timezone to your local timezone (e.g., "Asia/Kuala_Lumpur")
timezone = pytz.timezone("Asia/Kuala_Lumpur")

# List of employees (you can edit or expand this list)
employees = [
    'MOHD TARMIZI BIN CHE AHMAD',
    'NOOR LIYANA BINTI MOHD AZMI',
    'NOOR HAYATI BINTI ISA',
    'ZULIZA SHUHADAH BT AHMAD GHAZALI',
    'SURAYA BINTI ABDUL RASHID',
    'NORAZIAH BINTI AHMAD',
    'MEOR MOHAMAD HAFIZ BIN MEOR JAMALUDDIN ',
    'ARDY SHAZRIL BIN AHMAD HUMAIRI',
    'NOOR NABILFIKRI BIN NOOR RAHMAN',
    'MOHD AMIRUL AKMAL BIN RAHIM',
    'NOOR SURIANA BINTI MOHD NASIR'
]
employee_reports = {}

# Replace with your group chat ID and topic ID
GROUP_CHAT_ID = -1001194861270  # Replace with your group chat ID
TOPIC_ID = 1414  # Replace with the topic ID (thread ID)

async def start(update: Update, context):
    keyboard = [[InlineKeyboardButton(emp, callback_data=emp)] for emp in employees]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Select your name:', reply_markup=reply_markup)

async def button(update: Update, context):
    query = update.callback_query
    await query.answer()
    context.user_data['employee_name'] = query.data
    await query.edit_message_text(text=f"Name selected: {query.data}\nMasukkan lokasi keberadaan anda hari ini?:")

async def receive_text(update: Update, context):
    employee_name = context.user_data.get('employee_name', 'Unknown')
    daily_text = update.message.text
    employee_reports[employee_name] = daily_text  # Store the report

    await update.message.reply_text(f"Terima kasih {employee_name}, maklumat keberadaan anda telah direkodkan.")

    # Send the summary after each report submission
 await send_summary(update, context)  # Send summary after each report submission

async def send_summary(update: Update, context):
    current_date = datetime.now(timetimezone).strftime("%d-%b-%Y")  # Format as DD-MMM-YYYY
    summary = f"📅 *MAKLUMAT KEBERADAAN JTK PTIS LAHAT BAGI TARIKH {current_date}* 📅\n\n"

    for employee in employees:
        report = employee_reports.get(employee, "Belum Isi")  # Default to "Belum Isi"
        summary += f"👤 *{employee}*: {report}\n\n"

    summary += "Terima kasih atas kerjasama anda. Maklumat ini akan dimasukkan kedalam Group Rasmi JTK PTIS Kinta Utara (Keberadaan)."


   # Send the summary to the group
    await context.bot.send_message(chat_id=update.message.chat_id, text=summary, parse_mode='Markdown')

def main():
    application = ApplicationBuilder().token('7672291464:AAHAZAPzEhOt0r4qPZ9G6S_Vhf35D031EAU').build()  # Replace with your bot token
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_text))

    application.run_polling()

if __name__ == '__main__':
    main()
