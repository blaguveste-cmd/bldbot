"""Тексты BLDSH ACCS."""

from config import STARS_RATE, REFUND_PERCENT


def fmt_money(amount: int | float) -> str:
    if isinstance(amount, float):
        return f"{amount:,.1f}".replace(",", " ") + " ₽"
    return f"{amount:,}".replace(",", " ") + " ₽"


def main_menu_text(balance: int, first_name: str | None = None) -> str:
    name = first_name or "друг"
    return (
        f"🛍 <b>BLDSH ACCS</b>\n"
        f"Готовые Telegram-аккаунты\n\n"
        f"Привет, <b>{name}</b>!\n"
        f"💰 Баланс: <code>{fmt_money(balance)}</code>\n\n"
        f"Выбери действие ниже:"
    )


def catalog_text(count: int = 0) -> str:
    if count == 0:
        return "🛒 <b>Каталог</b>\n\nСейчас свободных аккаунтов нет.\nНовые товары появляются регулярно."
    return f"🛒 <b>Каталог</b>\n\nДоступно: <code>{count}</code> аккаунтов\n\nВыбери вариант ниже:"


def product_text(title: str, description: str, price: int) -> str:
    return (
        f"📱 <b>{title}</b>\n\n"
        f"{description}\n\n"
        f"💵 <b>Цена:</b> <code>{fmt_money(price)}</code>\n\n"
        f"Что дальше:\n"
        f"1. Оплатишь товар\n"
        f"2. Номер и код придут автоматически\n"
        f"3. Код придёт в этот чат\n\n"
        f"Покупай или сделай подарок другу в пару кликов."
    )


def gift_recipient_prompt() -> str:
    return (
        "🎁 <b>Подарок другу</b>\n\n"
        "Отправь username получателя.\n"
        "Он должен уже начать диалог с ботом.\n\n"
        "Пример: <code>@username</code>"
    )


def gift_purchase_success_text(recipient: str) -> str:
    return (
        "✅ <b>Подарок оформлен</b>\n\n"
        f"Товар будет доставлен получателю: <b>{recipient}</b>.\n"
        "Номер и код придут ему автоматически.\n\n"
        "Если получатель не доступен — ты получишь данные лично."
    )


def gift_recipient_received_text(phone: str) -> str:
    return (
        "🎁 <b>Тебе подарили аккаунт!</b>\n\n"
        f"📱 Номер: <code>+{phone}</code>\n\n"
        "Код придёт, как только он появится."
    )


def gift_recipient_code_text(code: str) -> str:
    return (
        "✅ <b>Код для подарка</b>\n\n"
        f"<code>{code}</code>\n\n"
        "Отправь его получателю вместе с номером."
    )


def gift_recipient_unreachable_text(recipient: str) -> str:
    return (
        "⚠️ <b>Не удалось доставить подарок</b>\n\n"
        f"Пользователь <b>{recipient}</b> не доступен.\n"
        "Ты получишь номер и код лично — перешли их получателю."
    )


def profile_text(user_id: int, username: str | None, balance: int) -> str:
    uname = f"@{username}" if username else "—"
    return (
        f"👤 <b>Профиль</b>\n\n"
        f"🆔 ID: <code>{user_id}</code>\n"
        f"🔗 Username: {uname}\n"
        f"💰 Баланс: <code>{fmt_money(balance)}</code>\n\n"
        f"Используй баланс для покупок и подарков."
    )


def balance_menu_text() -> str:
    return (
        "💳 <b>Пополнение баланса</b>\n\n"
        "Выбери способ:\n\n"
        "💎 Crypto Bot — авто\n"
        "⭐ Telegram Stars — подарки\n"
        "💵 Рубли — перевод вручную\n"
        "💱 Перевести — другому пользователю\n\n"
        "Баланс обновится автоматически."
    )


def refund_reason_prompt() -> str:
    effective_note = ""
    try:
        stars_effective = int(REFUND_PERCENT * (1 - 0.15))
        effective_note = f"Если часть пополнения через Stars — учти комиссию ~15%, вернётся примерно <code>{stars_effective}%</code> от этой части."
    except Exception:
        effective_note = "Если часть баланса через Stars — возможна комиссия."

    return (
        "↩️ <b>Запрос на возврат</b>\n\n"
        "Напиши причину.\n"
        f"При одобрении возвращается <code>{REFUND_PERCENT}%</code> от баланса.\n"
        f"({effective_note})"
    )


def refund_submitted_user_text(amount_before: int, calculated_amount: int) -> str:
    return (
        "✅ <b>Заявка отправлена</b>\n\n"
        f"Текущий баланс: <b>{fmt_money(amount_before)}</b>\n"
        f"Примерный возврат: <b>{fmt_money(calculated_amount)}</b> (<code>{REFUND_PERCENT}%</code>)\n\n"
        "Администратор свяжется по решению."
    )


def admin_refund_request_text(request_id: int, user_id: int, username: str | None, amount_before: int, calculated_amount: int, reason: str) -> str:
    uname = f"@{username}" if username else "—"
    return (
        f"🔔 <b>Заявка на возврат #{request_id}</b>\n\n"
        f"Пользователь: <code>{user_id}</code> {uname}\n"
        f"Баланс: <b>{fmt_money(amount_before)}</b>\n"
        f"Возврат: <b>{fmt_money(calculated_amount)}</b>\n\n"
        f"Причина:\n{reason}\n\n"
        "Нажми кнопку, чтобы одобрить или отклонить."
    )


def refund_approved_user_text(amount: int) -> str:
    return (
        "✅ <b>Заявка одобрена</b>\n\n"
        f"Вернём: <b>{fmt_money(amount)}</b>\n\n"
        "Средства отправят выбранным способом (админ свяжется)."
    )


def refund_rejected_user_text() -> str:
    return (
        "❌ <b>Заявка отклонена</b>\n\n"
        "Если нужны разъяснения — напиши в поддержку."
    )


def getsms_service_prompt() -> str:
    return (
        "📱 <b>Смена номера</b>\n\n"
        "Виртуальный номер из GetSMS.\n"
        "Цена рассчитается автоматически.\n\n"
        "Нажми кнопку, чтобы оформить."
    )


def getsms_order_created_text(phone: str, price: float) -> str:
    return (
        "✅ <b>Заказ создан</b>\n\n"
        f"📱 Номер: <code>{phone}</code>\n"
        f"💰 Цена: <b>{fmt_money(price)}</b>\n\n"
        "Открой Telegram и запроси код.\n"
        "Когда код придёт — бот сообщит сам."
    )


def getsms_order_status_text(status: str, last_code: str | None, received_codes: int | None) -> str:
    text = f"📊 <b>Статус заказа</b>\n\nСтатус: <b>{status}</b>\n"
    if last_code:
        text += f"\nКод: <code>{last_code}</code>\n"
    if received_codes is not None:
        text += f"\nКодов получено: <b>{received_codes}</b>\n"
    return text


def getsms_order_price_text(price: float) -> str:
    return (
        "📱 <b>Смена номера</b>\n\n"
        f"Цена: <b>{fmt_money(price)}</b>\n\n"
        "Если подходит — оформи заказ.\n"
        "Стоимость спишется с баланса."
    )


def getsms_order_list_text(orders: list) -> str:
    if not orders:
        return "📦 <b>Мои номера</b>\n\nПока нет заказов. Оформи через меню."
    lines = ["📦 <b>Мои номера</b>\n\n"]
    for i, order in enumerate(orders, 1):
        lines.append(
            f"<b>{i}.</b> #{order[1]} — <code>{order[4] or '—'}</code>\n"
            f"   Цена: {fmt_money(order[3])}\n"
            f"   Статус: <b>{order[5]}</b>\n"
        )
    return "\n".join(lines)


def crypto_pay_prompt() -> str:
    return (
        "💎 <b>Crypto Bot</b>\n\n"
        "Введи сумму в рублях.\n"
        "Минимум: <b>5 ₽</b>\n\n"
        "После оплаты баланс зачислится сам."
    )


def crypto_invoice_text(amount: int) -> str:
    return (
        "💳 <b>Счёт создан</b>\n\n"
        f"Сумма: <b>{fmt_money(amount)}</b>\n\n"
        "Нажми и оплати.\n"
        "Баланс придёт сразу после оплаты."
    )


def stars_pay_prompt() -> str:
    return (
        "⭐ <b>Telegram Stars</b>\n\n"
        "Введи сумму в рублях.\n"
        f"Курс: <code>1 ₽ = {STARS_RATE} ⭐</code>\n\n"
        "Отправляй подарки на релеера: 15 / 25 / 50 / 100 ⭐.\n"
        "Можно несколько подряд."
    )


def gifts_pay_text(relayer: str, rate: float = None, amount: float | None = None, target_stars: int | None = None) -> str:
    if rate is None:
        rate = STARS_RATE
    if amount is None or target_stars is None:
        return (
            "⭐ <b>Оплата Stars</b>\n\n"
            f"Отправляй подарки на <b>{relayer}</b>.\n"
            "Номиналы: 15 / 25 / 50 / 100 ⭐."
        )
    return (
        "⭐ <b>Оплата Stars</b>\n\n"
        f"Сумма: <code>{fmt_money(amount)}</code>\n"
        f"Нужно: <code>{target_stars} ⭐</code>\n"
        f"По курсу: <code>{target_stars / rate:.2f} ₽</code>\n\n"
        f"Отправляй подарки на <b>{relayer}</b>.\n"
        "Можно комбинировать: 15+15, 15+25, 25+50 и т.д.\n\n"
        "После достижения цели баланс пополнится.\n"
        "Лишние Stars тоже зачислятся."
    )


def rubles_pay_prompt() -> str:
    return (
        "💵 <b>Оплата рублями</b>\n\n"
        "Введи сумму пополнения.\n"
        "Минимум: <b>10 ₽</b>\n\n"
        "После перевода админ подтвердит платёж."
    )


def rubles_payment_instructions(amount: int, details: str) -> str:
    return (
        "💵 <b>Реквизиты</b>\n\n"
        f"Сумма: <b>{fmt_money(amount)}</b>\n\n"
        f"Переводи на:\n"
        f"<code>{details}</code>\n\n"
        "1. Переведи точно эту сумму\n"
        "2. Пришли чек / скрин сюда\n\n"
        "После проверки баланс зачислят."
    )


def rubles_receipt_prompt() -> str:
    return (
        "🧾 <b>Пришли чек</b>\n\n"
        "Отправь фото или файл чека.\n\n"
        "Без чека заявка не уйдёт админу."
    )


def rubles_receipt_received() -> str:
    return (
        "✅ <b>Чек получен</b>\n\n"
        "Заявка отправлена на проверку.\n"
        "Обычно это занимает 1–15 минут."
    )


def admin_manual_request_text(payment_id: int, user_id: int, username: str | None, full_name: str | None, amount: int) -> str:
    uname = f"@{username}" if username else "—"
    name = full_name or "—"
    return (
        f"🔔 <b>Заявка на пополнение #{payment_id}</b>\n\n"
        f"🆔 <code>{user_id}</code> {uname}\n"
        f"👤 {name}\n"
        f"💰 <code>{fmt_money(amount)}</code>\n\n"
        "Подтвердить?"
    )


def manual_approved_user_text(amount: int) -> str:
    return (
        "✅ <b>Платёж подтверждён</b>\n\n"
        f"Зачислено: <b>+{fmt_money(amount)}</b>\n\n"
        "Можешь покупать."
    )


def manual_rejected_user_text() -> str:
    return (
        "❌ <b>Платёж отклонён</b>\n\n"
        "Перевод не подтвердили.\n"
        "Если деньги ушли — напиши в поддержку."
    )


def orders_text(orders: list) -> str:
    if not orders:
        return "📦 <b>Мои покупки</b>\n\nПока пусто.\nОформляй покупки в каталоге."
    lines = ["📦 <b>Мои покупки</b>\n\n"]
    for i, order in enumerate(orders, 1):
        lines.append(
            f"<b>{i}.</b> {order[0]}\n"
            f"   📱 {order[3]}\n"
            f"   💰 {fmt_money(order[2])}\n"
        )
    return "\n".join(lines)


def support_text(admin: str = "@baldush") -> str:
    return (
        f"💬 <b>Поддержка</b>\n\n"
        f"Вопрос или проблема — пиши:\n\n"
        f"👉 <b>{admin}</b>"
    )


def info_text() -> str:
    return (
        "ℹ️ <b>О магазине</b>\n\n"
        "🔹 Готовые Telegram-аккаунты\n"
        "🔹 Номер и код приходят автоматически\n"
        "🔹 Поддержка 24/7\n"
        "🔹 Оплата: Crypto, Stars, рубли\n\n"
        "Удобно, быстро и без лишних действий."
    )


def purchase_success_text(phone: str) -> str:
    return (
        "✅ <b>Оплата прошла</b>\n\n"
        f"📱 Номер: <code>+{phone}</code>\n\n"
        "Код отправлен ниже."
    )


def purchase_review_text() -> str:
    return (
        "🙏 <b>Спасибо за покупку!</b>\n\n"
        "Оставь отзыв в <b>@baldushrep</b>.\n"
        "Поставь облачный пароль и почту для входа."
    )


def purchase_processing_text() -> str:
    return (
        "⏳ <b>Обработка</b>\n\n"
        "Готовим аккаунт.\n"
        "Это займёт несколько секунд."
    )


def login_help_text() -> str:
    return (
        "❓ <b>Помощь с входом</b>\n\n"
        "<b>Частые проблемы:</b>\n\n"
        "1. <b>Telegram просит 1$ за код.</b>\n"
        "Скачай <b>Nicegram</b> или запроси код с <b>ПК</b>.\n\n"
        "2. <b>Не получается ввести код.</b>\n"
        "Используй <b>Telegram</b> или <b>Nicegram</b>.\n\n"
        "3. <b>Код не приходит.</b>\n"
        "Попробуй другой клиент.\n\n"
        "Если проблема осталась — пиши в поддержку: <b>@baldush</b>"
    )


def my_purchases_text(accounts) -> str:
    if not accounts:
        return "📦 <b>Мои покупки</b>\n\nПока нет покупок."
    lines = ["📦 <b>Мои покупки</b>\n\n"]
    for account in accounts:
        phone = account["phone"]
        role = "Покупатель" if account["role"] == "buyer" else "Получатель подарка"
        lines.append(f"📱 <code>+{phone}</code> — {role}\n")
    return "\n".join(lines)


def my_account_detail_text(phone: str) -> str:
    return (
        f"📱 <b>Аккаунт</b> <code>+{phone}</code>\n\n"
        "Нажми «Получить код», чтобы перехватить код из Telegram.\n"
        "Код можно запрашивать много раз, пока сессия активна."
    )


def purchase_failed_text(reason: str | None = None) -> str:
    text = (
        "❌ <b>Не удалось оформить покупку</b>\n\n"
        "Произошла ошибка.\n"
        "Средства вернутся на баланс, если списание уже было."
    )
    if reason:
        text += f"\nПричина: <code>{reason}</code>"
    return text


def code_received_text(code: str) -> str:
    return (
        "📩 <b>Код получен</b>\n\n"
        f"<code>{code}</code>\n\n"
        "Введи его в Telegram."
    )


def code_timeout_text(amount: int) -> str:
    return (
        "⏰ <b>Код не пришёл</b>\n\n"
        f"Время вышло.\n"
        f"<b>{fmt_money(amount)}</b> вернули на баланс.\n\n"
        "Можешь взять другой аккаунт."
    )


def balance_topup_text(amount: int) -> str:
    return (
        "💎 <b>Баланс пополнен</b>\n\n"
        f"Зачислено: <b>+{fmt_money(amount)}</b>\n\n"
        "Можешь переходить к покупке."
    )


def transfer_amount_prompt() -> str:
    return (
        "💱 <b>Перевод баланса</b>\n\n"
        "Введи сумму.\n"
        "<b>Списывается с твоего баланса.</b>\n\n"
        "Минимум 1 ₽."
    )


def transfer_recipient_prompt() -> str:
    return (
        "💱 <b>Кому перевести?</b>\n\n"
        "Отправь username получателя.\n"
        "Он должен начать диалог с ботом.\n\n"
        "Пример: <code>@username</code>"
    )


def transfer_success_text(amount: int, recipient: str) -> str:
    return (
        "✅ <b>Перевод выполнен</b>\n\n"
        f"Списано: <b>{fmt_money(amount)}</b>\n"
        f"Получатель: <b>{recipient}</b>\n\n"
        "Он получит уведомление."
    )


def transfer_received_text(amount: int, sender: str) -> str:
    return (
        "💸 <b>Тебе поступили деньги</b>\n\n"
        f"Сумма: <b>{fmt_money(amount)}</b>\n"
        f"От: <b>{sender}</b>\n\n"
        "Баланс пополнен."
    )


def admin_panel_text() -> str:
    return "👑 <b>Admin Panel</b>\n\nУправление магазином"


def lolz_panel_text(token_set: bool) -> str:
    status = "токен установлен" if token_set else "токен не задан"
    return (
        f"💼 <b>Lolz API</b>\n\n"
        f"Статус: <b>{status}</b>\n\n"
        "Настройка импорта аккаунтов из Lolz."
    )


def lolz_token_prompt() -> str:
    return (
        "🔑 <b>Lolz API токен</b>\n\n"
        "Введи токен для доступа к Lolz API."
    )


def lolz_token_saved_text() -> str:
    return "✅ <b>Токен сохранён</b>\n\nТеперь можно импортировать аккаунты."


def lolz_import_service_prompt() -> str:
    return (
        "⬇️ <b>Импорт из Lolz</b>\n\n"
        "Введи категорию или название услуги, например <code>USA</code>."
    )


def lolz_import_price_prompt(service: str) -> str:
    return (
        f"⬇️ <b>Импорт: {service}</b>\n\n"
        "Введи цену продажи в рублях — например, <code>35</code>.\n"
        "Аккаунт добавится в каталог."
    )


def lolz_import_result_text(success: bool, message: str) -> str:
    if success:
        return f"✅ <b>Аккаунт импортирован</b>\n\n{message}"
    return f"❌ <b>Не удалось импортировать</b>\n\n{message}"


def help_text() -> str:
    return (
        "📖 <b>Помощь</b>\n\n"
        "<code>/start</code> — меню\n"
        "<code>/catalog</code> — каталог\n"
        "<code>/balance</code> — баланс\n"
        "<code>/orders</code> — покупки\n"
        "<code>/help</code> — справка\n\n"
        "Канал: <b>t.me/bldshaccs</b>"
    )


def subscribe_prompt_text() -> str:
    return (
        "📢 <b>Новости</b>\n\n"
        "Подпишись, чтобы не пропускать новые аккаунты.\n\n"
        "👉 <b>t.me/bldshaccs</b>"
    )
