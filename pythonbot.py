import telebot
import sqlite3

TOKEN = "8401234223:AAHHeM086LlLyqkvC_nwS4e0GUjoLiAZIXM"
bot = telebot.TeleBot(TOKEN)

# Database setup
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY)")
conn.commit()

# Start Command
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    # Save user if not exists
    cursor.execute("INSERT OR IGNORE INTO users (id) VALUES (?)", (user_id,))
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    bot.reply_to(message, f"👋 স্বাগতম {message.from_user.first_name}!\n\n📊 মোট ইউজার: {total_users} জন ✅")

# Stats Command
@bot.message_handler(commands=['stats'])
def stats(message):
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]
    bot.reply_to(message, f"📌 বর্তমানে বটে মোট {total_users} জন ইউজার আছে ✅")

bot.polling()