from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
import time
import pyrogram.errors
from  pyrogram.enums import ChatMemberStatus
from kvsqlite.sync import Client
db = Client("data.sqlite", 'fuck')


@app.on_message(filters.private & filters.regex("^/start$"), group=1)
async def startm(app, msg):
    user_id = msg.from_user.id
    if db.get("ban_list") is None:
        db.set('ban_list', [])
        pass
    if user_id in db.get("ban_list"):
        return
    chats = db.get('force')
    from .force import check_channel_member
    for i in chats:
      if not await check_channel_member(app, i, user_id):
        k = f'''
عذراً عزيزي 🤚 
عليك الاشتراك بقناة البوت لمتابعه كود الصفقه والربح :
- @{i}
- @{i}
— — — — — — — — — —
قم بلأشتراك، وأرسل /start .
        '''
        return await msg.reply(k, reply_markup=mk([[btn(f'- @{i} .', url=f't.me/{i}')]]))
    if db.exists(f"user_{user_id}"):
        coin = db.get(f'user_{user_id}')['coins']
        keys = mk(
        [
            [btn(text='- رصيدي: {:,} EGP'.format(coin), callback_data='lol')],
            [btn(text='- سحب ', callback_data='invite'), btn(text='- ايداع ', callback_data='ve1')],
            [btn(text='- معلومات حسابي', callback_data='account'), btn(text='- مشاركه مع الاخرين', callback_data='sharelink')],
            [btn(text='- قناه المنصه', url='GX_PU.t.me')]
        ]
    )
        rk = f'''
- مرحبا بك عزيزي في منصه ExToP للخدمات والاستثمار
- البوت يتميز بسرعة وتنفيذ الطلبات

الـ 𝚒𝚍 الخاص بك ⥃ {msg.from_user.id}
-
        '''
        await app.send_message(msg.from_user.id,rk, reply_markup=keys)
    else:
        info = {'coins': 0 , 'id': user_id, 'premium': False, 'admin': False, "phone":[], "users":[], "date":str(time.time())}
        db.set(f'user_{user_id}', info)
        xxe = db.get("admin_list")
        sc = set(xxe)
        xxx = sorted(sc)
        for i in xxx:
            await app.send_message(i,f"عضو جديد فات للبوت!!\n{msg.from_user.mention} .\nايدي: {msg.from_user.id} .")
        
        coin = db.get(f'user_{user_id}')['coins']
        keys = mk(
        [
            [btn(text='- رصيدي: {:,} EGP'.format(coin), callback_data='lol')],
            [btn(text='- سحب ', callback_data='invite'), btn(text='- ايداع ', callback_data='ve1')],
            [btn(text='- معلومات حسابي', callback_data='account'), btn(text='- مشاركه مع الاخرين', callback_data='sharelink')],
            [btn(text='- قناه المنصه', url='GX_PU.t.me')]
        ]
    )
        rk =f'''
- مرحبا بك عزيزي في منصه ExToP للخدمات والاستثمار
- البوت يتميز بسرعة وتنفيذ الطلبات

الـ 𝚒𝚍 الخاص بك ⥃ {msg.from_user.id}
-
        '''
        await app.send_message(msg.from_user.id,rk, reply_markup=keys)