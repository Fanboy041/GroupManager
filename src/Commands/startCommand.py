from Database.MongoDB import owner_collection, user_collection, save_owner, save_user, get_owner, get_admin
from telethon.tl.types import PeerUser


async def send_welcome(event, bot):
    me = await bot.get_me()
    sender = await event.get_sender()
    chat_id = event.message.peer_id
    if isinstance(chat_id, PeerUser):

        # User's information
        first_name = sender.first_name
        last_name = sender.last_name
        if last_name:
            full_name = first_name + " " + last_name
        else:
            full_name = first_name

        username = sender.username

        chat_id = chat_id.user_id

        # Set owner if it's the first user and there is one owner only
        if owner_collection.count_documents({}) == 0:
            save_owner(full_name, username, chat_id)
            await bot.send_message(chat_id, f"Welcome <b>{full_name}</b>\nYou are my owner from now on",
                                   parse_mode='HTML')

        else:
            # Counting the number of the users
            total_users = user_collection.count_documents({}) + 1

            # Save the user info in the database
            save_user(full_name, username, chat_id, total_users)

            if chat_id == get_owner()['chat_id']:
                await bot.send_message(chat_id,
                                       f"Hey owner, <b>{full_name}</b>!\n\nThank you for interacting with me. I'm "
                                       "excited to have you on board. 🌹",
                                       parse_mode='HTML')

            elif get_admin(chat_id) is not None and chat_id == get_admin(chat_id)['chat_id']:
                await bot.send_message(chat_id,
                                       f"Hey admin, <b>{full_name}</b>!\n\nThank you for interacting with me. I'm "
                                       "excited to have you on board. 🌹",
                                       parse_mode='HTML')

            else:
                await bot.send_message(chat_id,
                                       f"Welcome, <b>{full_name}</b>!\n\nThank you for interacting with our Telegram "
                                       "bot. We're excited to have you on board. 🌹",
                                       parse_mode='HTML')

    else:
        bot_username = me.username
        if f"@{bot_username}" in event.text:
            await bot.send_message(chat_id, reply_to=event.message.id, message="Please run the command in private")
            # await bot.reply_to(event, "Please run the command in private")
