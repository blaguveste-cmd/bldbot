from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

CHANNEL_URL = "https://t.me/bldshaccs"


def _b(text: str) -> str:
    return text


main_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒 Купить", callback_data="buy"),
     InlineKeyboardButton(text="🎁 Подарить", callback_data="gift")],
    [InlineKeyboardButton(text="💳 Пополнить", callback_data="balance"),
     InlineKeyboardButton(text="👤 Профиль", callback_data="profile")],
    [InlineKeyboardButton(text="📦 Покупки", callback_data="orders"),
     InlineKeyboardButton(text="💬 Поддержка", callback_data="support")],
    [InlineKeyboardButton(text="⭐ Отзывы", url="https://t.me/baldushrep"),
     InlineKeyboardButton(text="ℹ️ О магазине", callback_data="info")],
    [InlineKeyboardButton(text="📢 Канал", url=CHANNEL_URL)],
])


back_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="◀️ Назад", callback_data="back")],
])


def products_keyboard(products):
    buttons = []
    for product in products:
        buttons.append([
            InlineKeyboardButton(
                text=f"📱 {product[1]}  ·  {product[3]} ₽",
                callback_data=f"product_{product[0]}",
            )
        ])
    buttons.append([InlineKeyboardButton(text="◀️ Назад", callback_data="back")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def buy_product_keyboard(product_id, price: int = 0, gift: bool = True):
    label = f"✅ Купить — {price} ₽" if price else "✅ Купить"
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=label, callback_data=f"buy_{product_id}"),
            InlineKeyboardButton(text="🎁 Подарить", callback_data=f"gift_{product_id}"),
        ],
        [InlineKeyboardButton(text="◀️ Каталог", callback_data="buy")],
    ])
    return kb


admin_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="➕ Добавить аккаунт", callback_data="add_product")],
    [InlineKeyboardButton(text="🗑 Удалить аккаунт", callback_data="delete_product")],
    [InlineKeyboardButton(text="📢 Рассылка", callback_data="broadcast")],
])


def delete_keyboard(products):
    buttons = []
    for product in products:
        buttons.append([
            InlineKeyboardButton(
                text=f"🗑 {product[1]}  ·  {product[3]} ₽",
                callback_data=f"delete_{product[0]}",
            )
        ])
    buttons.append([InlineKeyboardButton(text="◀️ Закрыть", callback_data="back")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def deposit_methods_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💎 Crypto Bot", callback_data="pay_method_crypto"),
         InlineKeyboardButton(text="⭐ Telegram Stars", callback_data="pay_method_gifts")],
        [InlineKeyboardButton(text="💵 Рубли", callback_data="pay_method_rubles"),
         InlineKeyboardButton(text="💱 Перевести", callback_data="transfer_balance")],
        [InlineKeyboardButton(text="↩️ Запросить возврат", callback_data="request_refund")],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="back")],
    ])


def pay_invoice_keyboard(pay_url: str):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Оплатить", url=pay_url)],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="back")],
    ])


def admin_manual_payment_keyboard(payment_id: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Подтвердить", callback_data=f"manual_approve_{payment_id}"),
         InlineKeyboardButton(text="❌ Отклонить", callback_data=f"manual_reject_{payment_id}")],
    ])


def after_purchase_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 В каталог", callback_data="buy"),
         InlineKeyboardButton(text="🏠 В меню", callback_data="back")],
    ])


def purchase_flow_keyboard(phone_clean: str):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="❓ Помощь с входом", callback_data="login_help"),
         InlineKeyboardButton(text="🚪 Выйти из аккаунта", callback_data=f"logout_{phone_clean}")],
        [InlineKeyboardButton(text="🛒 В каталог", callback_data="buy"),
         InlineKeyboardButton(text="🏠 В меню", callback_data="back")],
    ])


def logout_account_keyboard(phone_clean: str):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚪 Выйти из аккаунта", callback_data=f"logout_{phone_clean}"),
         InlineKeyboardButton(text="🛒 В каталог", callback_data="buy")],
        [InlineKeyboardButton(text="🏠 В меню", callback_data="back")],
    ])


def account_actions_keyboard(phone_clean: str):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Получить код", callback_data=f"request_code_{phone_clean}"),
         InlineKeyboardButton(text="🚪 Выйти", callback_data=f"logout_{phone_clean}")],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="orders")],
    ])


def my_purchases_keyboard(accounts):
    buttons = []
    for account in accounts:
        phone = account["phone"]
        buttons.append([
            InlineKeyboardButton(
                text=f"📱 {phone}",
                callback_data=f"my_account_{phone}",
            )
        ])
    buttons.append([InlineKeyboardButton(text="◀️ Назад", callback_data="back")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def subscribe_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📢 Перейти в канал", url=CHANNEL_URL)],
        [InlineKeyboardButton(text="⏳ Позже", callback_data="subscribe_later")],
    ])
