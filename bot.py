#!/usr/bin/env python3
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "7545343348:AAHfc2_7YkF_gETziR_aBUV0vvky04N1pPY"  # Get token from GitHub Secret
ADMIN_USERNAME = "@your_admin"
CHANNEL = "@your_channel"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🌐 VPN SERVICES", callback_data="services")],
        [InlineKeyboardButton("📞 Contact Admin", url=f"https://t.me/{ADMIN_USERNAME.replace('@','')}")],
        [InlineKeyboardButton("ℹ️ About", callback_data="about")]
    ]

    await update.message.reply_text(
        f"👋 Welcome {update.effective_user.first_name}!\n"
        "Choose an option below:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    if q.data == "services":
        keyboard = [
            [InlineKeyboardButton("SSH / OpenVPN", callback_data="ssh")],
            [InlineKeyboardButton("V2Ray VMess", callback_data="vmess")],
            [InlineKeyboardButton("V2Ray VLESS", callback_data="vless")],
            [InlineKeyboardButton("Trojan", callback_data="trojan")],
            [InlineKeyboardButton("⬅️ Back", callback_data="back")]
        ]
        await q.edit_message_text(
            "🌐 VPN Services List:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    elif q.data == "ssh":
        await q.edit_message_text("🔐 SSH/OpenVPN Service\nContact admin: " + ADMIN_USERNAME)
    elif q.data == "vmess":
        await q.edit_message_text("⚡ VMess WS+TLS\nContact admin: " + ADMIN_USERNAME)
    elif q.data == "vless":
        await q.edit_message_text("⚡ VLESS WS+TLS\nContact admin: " + ADMIN_USERNAME)
    elif q.data == "trojan":
        await q.edit_message_text("🛡 Trojan VPN\nContact admin: " + ADMIN_USERNAME)
    elif q.data == "about":
        await q.edit_message_text("🤖 VPN SERVICE BOT\nJoin: " + CHANNEL)
    elif q.data == "back":
        await start(q, context)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
