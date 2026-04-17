import re, sys, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def add_attr(content, old, new):
    if old not in content:
        print(f"WARNING: not found: {old[:80]}", file=sys.stderr)
        return content
    count = content.count(old)
    if count > 1:
        print(f"WARNING: multiple ({count}) matches for: {old[:80]}", file=sys.stderr)
        return content.replace(old, new, 1)
    return content.replace(old, new)

def patch_footer(content):
    content = add_attr(content, '<h4>Продукт</h4>', '<h4 data-i18n="footer_product">Продукт</h4>')
    content = add_attr(content, '>Главная</a>', ' data-i18n="footer_home">Главная</a>')
    content = add_attr(content, '>Инструкция</a>', ' data-i18n="footer_install">Инструкция</a>')
    content = add_attr(content, '>Цены</a>', ' data-i18n="footer_pricing">Цены</a>')
    content = add_attr(content, '<h4>Компания</h4>', '<h4 data-i18n="footer_company">Компания</h4>')
    content = add_attr(content, '>О нас</a>', ' data-i18n="footer_about">О нас</a>')
    content = add_attr(content, '>Контакты</a>', ' data-i18n="footer_contacts">Контакты</a>')
    content = add_attr(content, '>Блог</a>', ' data-i18n="footer_blog">Блог</a>')
    content = add_attr(content, '<h4>Помощь</h4>', '<h4 data-i18n="footer_help">Помощь</h4>')
    content = add_attr(content, '>Поддержка</a>', ' data-i18n="footer_support">Поддержка</a>')
    content = add_attr(content, '>Конфиденциальность</a>', ' data-i18n="footer_privacy">Конфиденциальность</a>')
    content = add_attr(content, '>Условия</a>', ' data-i18n="footer_terms">Условия</a>')
    return content

def patch_about(content):
    content = add_attr(content, '<h1 class="rv">О GrabLy</h1>', '<h1 class="rv" data-i18n="about_title">О GrabLy</h1>')
    content = add_attr(content, '<p class="hero-sub rv">Простой инструмент для тех кто учится онлайн</p>', '<p class="hero-sub rv" data-i18n="about_sub">Простой инструмент для тех кто учится онлайн</p>')
    content = add_attr(content, '<h2>Кто мы</h2>', '<h2 data-i18n="about_who">Кто мы</h2>')
    content = add_attr(content, '<p>GrabLy \u2014 это расширение для Google Chrome', '<p data-i18n="about_who_text">GrabLy \u2014 это расширение для Google Chrome')
    content = add_attr(content, '<h2>Наша миссия</h2>', '<h2 data-i18n="about_mission">Наша миссия</h2>')
    content = add_attr(content, '<p>Мы верим, что если вы оплатили курс', '<p data-i18n="about_mission_text">Мы верим, что если вы оплатили курс')
    content = add_attr(content, '<h2>Что мы делаем</h2>', '<h2 data-i18n="about_do">Что мы делаем</h2>')
    content = add_attr(content, '<li>Поддерживаем 12+ платформ онлайн-обучения</li>', '<li data-i18n="about_do1">Поддерживаем 12+ платформ онлайн-обучения</li>')
    content = add_attr(content, '<li>Предоставляем простой интерфейс', '<li data-i18n="about_do2">Предоставляем простой интерфейс')
    content = add_attr(content, '<li>Используем справедливую систему оплаты', '<li data-i18n="about_do3">Используем справедливую систему оплаты')
    return patch_footer(content)

def patch_contacts(content):
    content = add_attr(content, '<h1 class="rv">Свяжитесь с нами</h1>', '<h1 class="rv" data-i18n="contacts_title">Свяжитесь с нами</h1>')
    content = add_attr(content, '<p class="hero-sub rv">Мы отвечаем в течение 24 часов</p>', '<p class="hero-sub rv" data-i18n="contacts_sub">Мы отвечаем в течение 24 часов</p>')
    content = add_attr(content, '<h3>Telegram поддержка</h3>', '<h3 data-i18n="contacts_support">Telegram поддержка</h3>')
    content = add_attr(content, '<h3>Сотрудничество</h3>', '<h3 data-i18n="contacts_collab">Сотрудничество</h3>')
    return patch_footer(content)

def patch_support(content):
    content = add_attr(content, '<h1 class="rv">Помощь и поддержка</h1>', '<h1 class="rv" data-i18n="support_title">Помощь и поддержка</h1>')
    content = add_attr(content, '<p class="hero-sub rv">Найдите ответы или напишите нам</p>', '<p class="hero-sub rv" data-i18n="support_sub">Найдите ответы или напишите нам</p>')
    content = add_attr(content, '<h2>Часто задаваемые вопросы</h2>', '<h2 data-i18n="support_faq_title">Часто задаваемые вопросы</h2>')
    faq_questions = [
        ('Видео не скачивается. Что делать?', 'sup_q1'),
        ('Как обновить расширение?', 'sup_q2'),
        ('Как восстановить аккаунт?', 'sup_q3'),
        ('Можно ли вернуть GC, если скачивание не удалось?', 'sup_q4'),
        ('Какие браузеры поддерживаются?', 'sup_q5'),
        ('Куда сохраняются скачанные видео?', 'sup_q6'),
    ]
    for q_text, key in faq_questions:
        old = f'<button class="faq-q">{q_text}'
        new = f'<button class="faq-q"><span data-i18n="{key}">{q_text}</span>'
        content = add_attr(content, old, new)
    faq_answers = [
        ('Убедитесь, что вы авторизованы', 'sup_a1'),
        ('Скачайте новую версию с нашего сайта', 'sup_a2'),
        ('Введите email, который вы использовали', 'sup_a3'),
        ('Да. Если скачивание не завершилось', 'sup_a4'),
        ('GrabLy работает в Google Chrome', 'sup_a5'),
        ('Видео сохраняются в стандартную папку', 'sup_a6'),
    ]
    for a_start, key in faq_answers:
        old = f'<div class="faq-ai">{a_start}'
        new = f'<div class="faq-ai" data-i18n="{key}" data-i18n-html>{a_start}'
        content = add_attr(content, old, new)
    content = add_attr(content, '<h2>Как связаться</h2>', '<h2 data-i18n="support_contact">Как связаться</h2>')
    content = add_attr(content, '<p>Напишите нам в <a href', '<p data-i18n="support_contact_text" data-i18n-html>Напишите нам в <a href')
    content = add_attr(content, '<h2>Время ответа</h2>', '<h2 data-i18n="support_response">Время ответа</h2>')
    content = add_attr(content, '<p>Мы отвечаем на все обращения', '<p data-i18n="support_response_text">Мы отвечаем на все обращения')
    return patch_footer(content)

def patch_privacy(content):
    content = add_attr(content, '<h1 class="rv">Политика конфиденциальности</h1>', '<h1 class="rv" data-i18n="privacy_title">Политика конфиденциальности</h1>')
    content = add_attr(content, '<p class="hero-sub rv">Дата обновления: апрель 2026</p>', '<p class="hero-sub rv" data-i18n="privacy_sub">Дата обновления: апрель 2026</p>')
    sections = [
        ('Какие данные мы собираем', 'priv_collect'),
        ('Как используем данные', 'priv_use'),
        ('Хранение данных', 'priv_store'),
        ('Передача третьим лицам', 'priv_third'),
        ('Cookies', 'priv_cookies'),
        ('Ваши права', 'priv_rights'),
        ('Контакты', 'priv_contact'),
    ]
    for title, key in sections:
        content = add_attr(content, f'<h2>{title}</h2>', f'<h2 data-i18n="{key}">{title}</h2>')
    para_starts = [
        ('Мы собираем минимальный объём данных', 'priv_collect_text'),
        ('Собранные данные используются', 'priv_use_text'),
        ('Все данные хранятся на защищённых серверах', 'priv_store_text'),
        ('Мы не передаём ваши персональные данные', 'priv_third_text'),
        ('GrabLy использует только функциональные cookies', 'priv_cookies_text'),
        ('Вы можете запросить удаление своих данных', 'priv_rights_text'),
        ('По всем вопросам, связанным с конфиденциальностью', 'priv_contact_text'),
    ]
    for p_start, key in para_starts:
        old = f'<p>{p_start}'
        new = f'<p data-i18n="{key}" data-i18n-html>{p_start}'
        content = add_attr(content, old, new)
    return patch_footer(content)

def patch_terms(content):
    content = add_attr(content, '<h1 class="rv">Условия использования</h1>', '<h1 class="rv" data-i18n="terms_title">Условия использования</h1>')
    content = add_attr(content, '<p class="hero-sub rv">Дата обновления: апрель 2026</p>', '<p class="hero-sub rv" data-i18n="terms_sub">Дата обновления: апрель 2026</p>')
    sections = [
        ('Общие положения', 'terms_general'),
        ('Использование GrabLy', 'terms_usage'),
        ('Что запрещено', 'terms_forbidden'),
        ('Аккаунт и оплата', 'terms_payment'),
        ('Ответственность', 'terms_liability'),
        ('Изменения в условиях', 'terms_changes'),
        ('Контакты', 'terms_contact'),
    ]
    for title, key in sections:
        content = add_attr(content, f'<h2>{title}</h2>', f'<h2 data-i18n="{key}">{title}</h2>')
    para_starts = [
        ('Используя расширение GrabLy', 'terms_general_text'),
        ('GrabLy предназначен исключительно', 'terms_usage_text'),
        ('Система оплаты GrabLy основана на GrabCoins', 'terms_payment_text'),
        ('GrabLy не несёт ответственности за контент', 'terms_liability_text'),
        ('Мы оставляем за собой право обновлять', 'terms_changes_text'),
        ('По всем вопросам, связанным с условиями', 'terms_contact_text'),
    ]
    for p_start, key in para_starts:
        old = f'<p>{p_start}'
        new = f'<p data-i18n="{key}" data-i18n-html>{p_start}'
        content = add_attr(content, old, new)
    li_items = [
        ('Распространение скачанного контента третьим лицам', 'terms_forb1'),
        ('Использование GrabLy для пиратства', 'terms_forb2'),
        ('Обратная разработка (reverse engineering)', 'terms_forb3'),
        ('Массовое автоматизированное скачивание контента', 'terms_forb4'),
    ]
    for li_start, key in li_items:
        content = add_attr(content, f'<li>{li_start}', f'<li data-i18n="{key}">{li_start}')
    return patch_footer(content)

def patch_blog(content):
    content = add_attr(content, '<h1 class="rv">Блог GrabLy</h1>', '<h1 class="rv" data-i18n="blog_title">Блог GrabLy</h1>')
    content = add_attr(content, '<p class="hero-sub rv">Скоро здесь появятся статьи</p>', '<p class="hero-sub rv" data-i18n="blog_sub">Скоро здесь появятся статьи</p>')
    content = add_attr(content, '<h3>Скоро запустим</h3>', '<h3 data-i18n="blog_soon">Скоро запустим</h3>')
    content = add_attr(content, '<p>Здесь будут статьи об онлайн-обучении', '<p data-i18n="blog_soon_text">Здесь будут статьи об онлайн-обучении')
    content = add_attr(content, '>Подписаться на обновления</a>', ' data-i18n="blog_subscribe">Подписаться на обновления</a>')
    return patch_footer(content)

def patch_install(content):
    content = add_attr(content, '<h1 class="rv">Установка за 2 минуты</h1>', '<h1 class="rv" data-i18n="inst_title">Установка за 2 минуты</h1>')
    content = add_attr(content, '<p class="hero-sub rv">Пошаговая инструкция с картинками</p>', '<p class="hero-sub rv" data-i18n="inst_sub">Пошаговая инструкция с картинками</p>')
    content = add_attr(content, '<p class="sec-label rv">Установка</p>', '<p class="sec-label rv" data-i18n="inst_label">Установка</p>')
    content = add_attr(content, '<h2 class="sec-title rv">Как установить GrabLy</h2>', '<h2 class="sec-title rv" data-i18n="inst_section_title">Как установить GrabLy</h2>')
    steps = [
        ('Скачайте расширение', 'inst_s1_title'),
        ('Распакуйте архив', 'inst_s2_title'),
        ('Откройте chrome://extensions', 'inst_s3_title'),
        ('Включите режим разработчика', 'inst_s4_title'),
        ('Загрузите расширение', 'inst_s5_title'),
        ('Закрепите расширение', 'inst_s6_title'),
    ]
    for title, key in steps:
        content = add_attr(content, f'<h3>{title}</h3>', f'<h3 data-i18n="{key}">{title}</h3>')
    step_texts = [
        ('Нажмите кнопку ниже чтобы скачать ZIP', 'inst_s1_text'),
        ('Распакуйте скачанный ZIP в любую удобную папку', 'inst_s2_text'),
        ('Вставьте адрес в адресную строку браузера', 'inst_s3_text'),
        ('В правом верхнем углу страницы расширений', 'inst_s4_text'),
        ('Нажмите кнопку <strong>', 'inst_s5_text'),
        ('Нажмите на иконку пазла', 'inst_s6_text'),
    ]
    for p_start, key in step_texts:
        old = f'<p>{p_start}'
        new = f'<p data-i18n="{key}" data-i18n-html>{p_start}'
        content = add_attr(content, old, new)
    content = add_attr(content, '>&#11015; Скачать GrabLy.zip</a>', ' data-i18n="inst_s1_btn" data-i18n-html>&#11015; Скачать GrabLy.zip</a>')
    content = add_attr(content, '<p class="sec-label rv">Использование</p>', '<p class="sec-label rv" data-i18n="inst_use_label">Использование</p>')
    content = add_attr(content, '<h2 class="sec-title rv">Как пользоваться</h2>', '<h2 class="sec-title rv" data-i18n="inst_use_title">Как пользоваться</h2>')
    usage_titles = [
        ('Создайте аккаунт', 'inst_u1_title'),
        ('Подтвердите email', 'inst_u2_title'),
        ('Откройте урок', 'inst_u3_title'),
        ('Скачайте видео', 'inst_u4_title'),
    ]
    for title, key in usage_titles:
        content = add_attr(content, f'<h3>{title}</h3>', f'<h3 data-i18n="{key}">{title}</h3>')
    usage_texts = [
        ('Нажмите на иконку GrabLy в панели браузера', 'inst_u1_text'),
        ('Откройте почту и перейдите по ссылке', 'inst_u2_text'),
        ('Зайдите на любую платформу с видеокурсом', 'inst_u3_text'),
        ('Нажмите на иконку GrabLy \u2014 расширение покажет', 'inst_u4_text'),
    ]
    for p_start, key in usage_texts:
        old = f'<p>{p_start}'
        new = f'<p data-i18n="{key}" data-i18n-html>{p_start}'
        content = add_attr(content, old, new)
    content = add_attr(content, '<p class="sec-label rv">Совместимость</p>', '<p class="sec-label rv" data-i18n="inst_compat">Совместимость</p>')
    content = add_attr(content, '<h2 class="sec-title rv">Поддерживаемые платформы</h2>', '<h2 class="sec-title rv" data-i18n="inst_platforms">Поддерживаемые платформы</h2>')
    content = add_attr(content, '<p class="sec-label rv">FAQ</p>', '<p class="sec-label rv" data-i18n="inst_faq_label">FAQ</p>')
    content = add_attr(content, '>Вопросы по установке</h2>', ' data-i18n="inst_faq_title">Вопросы по установке</h2>')
    faq_qs = [
        ('Что делать если Chrome заблокировал установку?', 'inst_fq1'),
        ('Нужно ли обновлять расширение вручную?', 'inst_fq2'),
        ('Работает ли в других браузерах (Edge, Opera, Яндекс)?', 'inst_fq3'),
        ('Как удалить расширение?', 'inst_fq4'),
        ('Потеряю ли я GC если переустановлю?', 'inst_fq5'),
    ]
    for q, key in faq_qs:
        content = add_attr(content, f'<span>{q}</span>', f'<span data-i18n="{key}">{q}</span>')
    faq_as = [
        ('Chrome может показать предупреждение', 'inst_fa1'),
        ('Да, при установке вручную', 'inst_fa2'),
        ('Да! GrabLy работает во всех Chromium', 'inst_fa3'),
        ('Откройте chrome://extensions, найдите GrabLy', 'inst_fa4'),
        ('Нет. Ваш баланс GC хранится на сервере', 'inst_fa5'),
    ]
    for a_start, key in faq_as:
        old = f'<div class="faq-ai">{a_start}'
        new = f'<div class="faq-ai" data-i18n="{key}" data-i18n-html>{a_start}'
        content = add_attr(content, old, new)
    return patch_footer(content)

def patch_buy(content):
    content = add_attr(content, '<h1 class="rv">Пополнить GC</h1>', '<h1 class="rv" data-i18n="buy_title">Пополнить GC</h1>')
    content = add_attr(content, '<p class="hero-sub rv">Выберите готовый пакет или введите своё количество</p>', '<p class="hero-sub rv" data-i18n="buy_sub">Выберите готовый пакет или введите своё количество</p>')
    card_names = [
        ('Старт', 'pricing_start_name'),
        ('Оптимальный', 'pricing_optimal_name'),
        ('Продвинутый', 'pricing_advanced_name'),
        ('Максимум', 'pricing_max_name'),
        ('Безлимит', 'pricing_unlimited_name'),
    ]
    for name, key in card_names:
        content = add_attr(content, f'<p class="price-name">{name}</p>', f'<p class="price-name" data-i18n="{key}">{name}</p>')
    card_descs = [
        ('Попробовать', 'pricing_start_desc'),
        ('Для одного курса', 'pricing_optimal_desc'),
        ('Для нескольких курсов', 'pricing_advanced_desc'),
        ('Для больших объёмов', 'pricing_max_desc'),
        ('Без ограничений, одна покупка', 'pricing_unlimited_desc'),
    ]
    for desc, key in card_descs:
        content = add_attr(content, f'<p class="price-desc">{desc}</p>', f'<p class="price-desc" data-i18n="{key}">{desc}</p>')
    # Select buttons
    content = content.replace('class="btn-po" onclick', 'class="btn-po" data-i18n="pricing_select" onclick', 4)
    content = content.replace('class="btn-pf" onclick', 'class="btn-pf" data-i18n="pricing_select" onclick', 1)
    content = add_attr(content, '<h2 class="section-title">Нужно другое количество?</h2>', '<h2 class="section-title" data-i18n="buy_custom_title">Нужно другое количество?</h2>')
    content = add_attr(content, '<p class="section-subtitle">Введите любое количество GC', '<p class="section-subtitle" data-i18n="buy_custom_sub">Введите любое количество GC')
    content = add_attr(content, '<label>Количество GC</label>', '<label data-i18n="buy_gc_label">Количество GC</label>')
    content = add_attr(content, '<label>К оплате</label>', '<label data-i18n="buy_price_label">К оплате</label>')
    content = add_attr(content, '<p class="custom-note">Оплата скоро станет доступна</p>', '<p class="custom-note" data-i18n="buy_note">Оплата скоро станет доступна</p>')
    return patch_footer(content)

def patch_login(content):
    content = add_attr(content, '<h1>Вход в аккаунт</h1>', '<h1 data-i18n="login_title">Вход в аккаунт</h1>')
    content = add_attr(content, '<p class="auth-sub">Продолжайте скачивать видео</p>', '<p class="auth-sub" data-i18n="login_sub">Продолжайте скачивать видео</p>')
    content = add_attr(content, 'id="login-email" placeholder="Email"', 'id="login-email" placeholder="Email" data-i18n="login_email"')
    content = add_attr(content, 'id="login-password" placeholder="Пароль"', 'id="login-password" placeholder="Пароль" data-i18n="login_password"')
    content = add_attr(content, '> Запомнить меня</label>', ' data-i18n="login_remember"> Запомнить меня</label>')
    content = add_attr(content, '>Забыли пароль?</a>', ' data-i18n="login_forgot">Забыли пароль?</a>')
    content = add_attr(content, '<button type="submit" class="btn-primary">Войти</button>', '<button type="submit" class="btn-primary" data-i18n="login_btn">Войти</button>')
    content = add_attr(content, '<div class="auth-divider">Или</div>', '<div class="auth-divider" data-i18n="login_or">Или</div>')
    content = add_attr(content, '>Создать аккаунт</a>', ' data-i18n="login_create">Создать аккаунт</a>')
    return patch_footer(content)

def patch_register(content):
    content = add_attr(content, '<h1>Создать аккаунт</h1>', '<h1 data-i18n="reg_title">Создать аккаунт</h1>')
    content = add_attr(content, '<p class="auth-sub">10 GC бесплатно после подтверждения email</p>', '<p class="auth-sub" data-i18n="reg_sub">10 GC бесплатно после подтверждения email</p>')
    content = add_attr(content, 'id="reg-email" placeholder="Email"', 'id="reg-email" placeholder="Email" data-i18n="reg_email"')
    content = add_attr(content, 'id="reg-password" placeholder="Пароль"', 'id="reg-password" placeholder="Пароль" data-i18n="reg_password"')
    content = add_attr(content, 'id="reg-confirm" placeholder="Подтвердите пароль"', 'id="reg-confirm" placeholder="Подтвердите пароль" data-i18n="reg_password2"')
    content = add_attr(content, '>Есть реферальный код?</a>', ' data-i18n="reg_ref">Есть реферальный код?</a>')
    content = add_attr(content, '<button type="submit" class="btn-primary">Создать аккаунт</button>', '<button type="submit" class="btn-primary" data-i18n="reg_btn">Создать аккаунт</button>')
    content = add_attr(content, '<div class="auth-divider">Или</div>', '<div class="auth-divider" data-i18n="reg_or">Или</div>')
    content = add_attr(content, '>Уже есть аккаунт</a>', ' data-i18n="reg_login">Уже есть аккаунт</a>')
    return patch_footer(content)

def patch_reset(content):
    content = add_attr(content, '<h1>Восстановление пароля</h1>', '<h1 data-i18n="reset_title">Восстановление пароля</h1>')
    content = add_attr(content, '<p class="auth-sub">Введите email для получения ссылки</p>', '<p class="auth-sub" data-i18n="reset_sub">Введите email для получения ссылки</p>')
    content = add_attr(content, 'id="reset-email" placeholder="Email"', 'id="reset-email" placeholder="Email" data-i18n="reset_email"')
    content = add_attr(content, '<button type="submit" class="btn-primary">Отправить ссылку</button>', '<button type="submit" class="btn-primary" data-i18n="reset_btn">Отправить ссылку</button>')
    content = add_attr(content, '>Вернуться к входу</a>', ' data-i18n="reset_back">Вернуться к входу</a>')
    return patch_footer(content)

def patch_profile(content):
    content = add_attr(content, '<h1>Привет, <span id="user-email">', '<h1 data-i18n="prof_hello" data-i18n-html>Привет, <span id="user-email">')
    content = add_attr(content, '<p>Ваш баланс: <strong', '<p data-i18n="prof_balance_label" data-i18n-html>Ваш баланс: <strong')
    content = add_attr(content, '<h2>Баланс</h2>', '<h2 data-i18n="prof_balance">Баланс</h2>')
    content = add_attr(content, '>Пополнить GC</a>', ' data-i18n="prof_topup">Пополнить GC</a>')
    content = add_attr(content, '<h2>Реферальная программа</h2>', '<h2 data-i18n="prof_referral">Реферальная программа</h2>')
    content = add_attr(content, '<div class="ref-stat-lbl">Приглашено</div>', '<div class="ref-stat-lbl" data-i18n="prof_ref_invited">Приглашено</div>')
    content = add_attr(content, '<div class="ref-stat-lbl">Оплатили</div>', '<div class="ref-stat-lbl" data-i18n="prof_ref_paid">Оплатили</div>')
    content = add_attr(content, '<div class="ref-stat-lbl">Заработано GC</div>', '<div class="ref-stat-lbl" data-i18n="prof_ref_earned">Заработано GC</div>')
    content = add_attr(content, '<p class="ref-hint">Приглашайте друзей', '<p class="ref-hint" data-i18n="prof_ref_hint">Приглашайте друзей')
    content = add_attr(content, '<h2>Настройки</h2>', '<h2 data-i18n="prof_settings">Настройки</h2>')
    content = add_attr(content, '        Сменить пароль\n      </div>', '        <span data-i18n="prof_change_pw">Сменить пароль</span>\n      </div>')
    content = add_attr(content, '        Выйти из аккаунта\n      </div>', '        <span data-i18n="prof_logout">Выйти из аккаунта</span>\n      </div>')
    return patch_footer(content)

files = {
    'about.html': patch_about,
    'contacts.html': patch_contacts,
    'support.html': patch_support,
    'privacy.html': patch_privacy,
    'terms.html': patch_terms,
    'blog.html': patch_blog,
    'install.html': patch_install,
    'buy.html': patch_buy,
    'login.html': patch_login,
    'register.html': patch_register,
    'reset.html': patch_reset,
    'profile.html': patch_profile,
}

for fname, patcher in files.items():
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    patched = patcher(content)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(patched)
    print(f"Patched {fname}")
