#  API портала правовой информации

Это неофициальный апи официального интернет-портала правовой информации (http://pravo.gov.ru/). Позволяет скачивать законы, указы, распоряжения и другие правовые акты федеральных и региональных ведомств. 


## Требования
* Python >= 3.10.2
* [requirements.txt](https://github.com/kbondar17/pravo-gov-API/blob/main/requirements.txt) или [poetry.lock](https://github.com/kbondar17/pravo-gov-API/blob/main/poetry.lock) 

## Использование

Одна команда скачает все документы, попадающие под критерии поиска.

```python -m api.get```

Скрипт использует три эндпоинта, которым можно придумать свое применение:

1. [Поиск](http://pravo.gov.ru/proxy/ips/?searchres=&bpas=cd00000&a3=&a3type=1&a3value=&a6=102000070&a6type=1&a6value=%CF%F0%E5%E7%E8%E4%E5%ED%F2&a15=&a15type=1&a15value=&a7type=3&a7from=&a7to=&a7date=06.07.2019&a8=&a8type=1&a1=&a0=%ED%E0%E7%ED%E0%F7%E8%F2%FC&a16=&a16type=1&a16value=&a17=&a17type=1&a17value=&a4=&a4type=1&a4value=&a23=&a23type=1&a23value=&textpres=&sort=7&x=29&y=6) - сюда прокидываются пользовательские параметры поиска и отсюда берутся айди найденных документов.
2. [Страница документа](http://pravo.gov.ru/proxy/ips/?doc_itself=&nd=602033583&page=1&rdk=0&link_id=0#I0) -  содержит полный текст документа.
3. [Метаинформация](http://pravo.gov.ru/proxy/ips/?doc_itself=&vkart=card&nd=102842343&page=1&rdk=0&intelsearch=&link_id=0) - данные об авторе, дате подписания и тэгах документа. 

У каждого документа есть id (nd) формата 123456789. Можно вручную подставить его в эндпоинт документа или метаинформации, чтобы получить соответствующие данные.

## Параметры поиска

Все параметры прописываются в api/config.py. Для поиска по базе необходимо указать хотя бы одну из следующих групп параметров:
1. регион или федеральный орган
2. дата 
3. ключевые слова 

<details>
<summary>Список регионов: </summary>
    <ol type="1">
<li>РФ</li>       
<li>Алтайский край</li>
<li>Амурская область</li>
<li>Архангельская область</li>
<li>Астраханская область</li>
<li>Белгородская область</li>
<li>Брянская область</li>
<li>Владимирская область</li>
<li>Волгоградская область</li>
<li>Вологодская область</li>
<li>Воронежская область</li>
<li>Еврейская автономная область</li>
<li>Забайкальский край</li>
<li>Ивановская область</li>
<li>Иркутская область</li>
<li>Кабардино-Балкарская Республика</li>
<li>Калининградская область</li>
<li>Калужская область</li>
<li>Камчатский край</li>
<li>Карачаево-Черкесская Республика</li>
<li>Кемеровская область</li>
<li>Кировская область</li>
<li>Костромская область</li>
<li>Краснодарский край</li>
<li>Красноярский край</li>
<li>Курганская область</li>
<li>Курская область</li>
<li>Ленинградская область</li>
<li>Липецкая область</li>
<li>Магаданская область</li>
<li>Москва</li>
<li>Московская область</li>
<li>Мурманская область</li>
<li>Ненецкий автономный округ</li>
<li>Нижегородская область</li>
<li>Новгородская область</li>
<li>Новосибирская область</li>
<li>Омская область</li>
<li>Оренбургская область</li>
<li>Орловская область</li>
<li>Пензенская область</li>
<li>Пермский край</li>
<li>Приморский край</li>
<li>Республика Адыгея</li>
<li>Республика Алтай</li>
<li>Республика Башкортостан</li>
<li>Республика Бурятия</li>
<li>Республика Дагестан</li>
<li>Республика Ингушетия</li>
<li>Республика Калмыкия</li>
<li>Республика Карелия</li>
<li>Республика Коми</li>
<li>Республика Крым</li>
<li>Республика Марий Эл</li>
<li>Республика Мордовия</li>
<li>Республика Саха (Якутия)</li>
<li>Республика Северная Осетия - Алания</li>
<li>Республика Татарстан</li>
<li>Республика Тыва</li>
<li>Республика Хакасия</li>
<li>Ростовская область</li>
<li>Рязанская область</li>
<li>Самарская область</li>
<li>Санкт-Петербург</li>
<li>Саратовская область</li>
<li>Сахалинская область</li>
<li>Свердловская область</li>
<li>Севастополь</li>
<li>Смоленская область</li>
<li>Ставропольский край</li>
<li>Тамбовская область</li>
<li>Тверская область</li>
<li>Томская область</li>
<li>Тульская область</li>
<li>Тюменская область</li>
<li>Удмуртская Республика</li>
<li>Ульяновская область</li>
<li>Хабаровский край</li>
<li>Ханты-Мансийский автономный</li>
<li>Челябинская область</li>
<li>Чеченская республика</li>
<li>Чувашская Республика</li>
<li>Чукотский автономный округ</li>
<li>Ямало-Ненецкий автономный округ</li>
<li>Ярославская область</li>

</ol>

</details>

<details>
<summary>Список ведомств: </summary>
<ol>
<li>Авиационно-космическое агентство</li>
<li>Агентство международного сотрудничества и развития</li>
<li>Агентство по боеприпасам</li>
<li>Агентство по обычным вооружениям</li>
<li>Агентство по патентам и товарным знакам</li>
<li>Агентство по правовой охране программ для ЭВМ, баз данных и топологий интегральных микросхем</li>
<li>Администрация</li>
<li>Администрация Особой экономической зоны в Калининградской области</li>
<li>Администрация Президента</li>
<li>Ассоциация волонтерских центров</li>
<li>Ассоциация крестьянских (фермерских) хозяйств и сельскохозяйственных кооперативов России</li>
<li>Верховный Совет</li>
<li>Верховный Суд</li>
<li>Вице-президент</li>
<li>Всероссийский центральный исполнительный комитет</li>
<li>Всесоюзный Центральный Совет Профессиональных Союзов</li>
<li>Высший Арбитражный Суд</li>
<li>Генеральная прокуратура</li>
<li>Генеральный прокурор</li>
<li>Глава</li>
<li>Главное государственно-правовое управление Президента</li>
<li>Главное управление специальных программ Президента</li>
<li>Главный государственный ветеринарный инспектор</li>
<li>Главный государственный санитарный врач</li>
<li>Госкомимущество</li>
<li>Госкомсевер</li>
<li>Госнаркоконтроль России</li>
<li>Госстрой</li>
<li>Государственная архивная служба</li>
<li>Государственная Дума Федерального Собрания</li>
<li>Государственная инспекция по обеспечению государственной монополии на алкогольную продукцию при Правительстве</li>
<li>Государственная корпорация по атомной энергии "Росатом"</li>
<li>Государственная корпорация по космической деятельности "Роскосмос"</li>
<li>Государственная налоговая служба</li>
<li>Государственная техническая комиссия при Президенте</li>
<li>Государственная фельдъегерская служба</li>
<li>Государственная фельдъегерская служба при Правительстве</li>
<li>Государственная хлебная инспекция при Правительстве</li>
<li>Государственно-правовое управление Президента</li>
<li>Государственный антимонопольный комитет</li>
<li>Государственный земельный комитет</li>
<li>Государственный комитет по антимонопольной политике и поддержке новых экономических структур</li>
<li>Государственный комитет по военно-технической политике</li>
<li>Государственный комитет по вопросам архитектуры и строительства</li>
<li>Государственный комитет по вопросам развития Севера</li>
<li>Государственный комитет по высшему образованию</li>
<li>Государственный комитет по делам гражданской обороны, чрезвычайным ситуациям и ликвидации последствий стихийных бедствий</li>
<li>Государственный комитет по делам Севера</li>
<li>Государственный комитет по земельным ресурсам и землеустройству</li>
<li>Государственный комитет по кинематографии</li>
<li>Государственный комитет по контролю за оборотом наркотических средств и психотропных веществ</li>
<li>Государственный комитет по охране окружающей среды</li>
<li>Государственный комитет по патентам и товарным знакам</li>
<li>Государственный комитет по рыболовству</li>
<li>Государственный комитет по связи и информатизации</li>
<li>Государственный комитет по социальной защите граждан и реабилитации территорий, пострадавших от чернобыльской и других радиационных катастроф</li>
<li>Государственный комитет по стандартизации и метрологии</li>
<li>Государственный комитет по стандартизации, метрологии и сертификации</li>
<li>Государственный комитет по статистике</li>
<li>Государственный комитет по строительной, архитектурной и жилищной политике</li>
<li>Государственный комитет по строительству и жилищно-коммунальному комплексу</li>
<li>Государственный комитет по телекоммуникациям</li>
<li>Государственный комитет по управлению государственным имуществом</li>
<li>Государственный комитет по физической культуре и спорту</li>
<li>Государственный комитет по физической культуре и туризму</li>
<li>Государственный комитет Российской Федерации по контролю за оборотом наркотических средств и психотропных веществ</li>
<li>Государственный комитет санитарно-эпидемиологического надзора</li>
<li>Государственный секретарь</li>
<li>Государственный секретарь - Первый заместитель Председателя Правительства</li>
<li>Государственный страховой надзор</li>
<li>Государственный таможенный комитет</li>
<li>Губернатор</li>
<li>Департамент налоговой полиции</li>
<li>Дорожное агентство</li>
<li>Заместитель Председателя Верховного Совета</li>
<li>Заместитель Председателя Правительства</li>
<li>Заместитель Председателя Совета Министров - Правительства</li>
<li>Исполняющий обязанности Президента</li>
<li>Кабинет Министров</li>
<li>Комитет по водному хозяйству</li>
<li>Комитет по военно-техническому сотрудничеству с иностранными государствами</li>
<li>Комитет по геологии и использованию недр</li>
<li>Комитет по делам архивов</li>
<li>Комитет по драгоценным металлам и драгоценным камням</li>
<li>Комитет по земельной реформе и земельным ресурсам</li>
<li>Комитет по земельным ресурсам и землеустройству</li>
<li>Комитет по кинематографии</li>
<li>Комитет по металлургии</li>
<li>Комитет по оперативному управлению народным хозяйством</li>
<li>Комитет по патентам и товарным знакам</li>
<li>Комитет по политике цен</li>
<li>Комитет по рыболовству</li>
<li>Комитет по социально-экономическому развитию Севера</li>
<li>Комитет по стандартизации, метрологии и сертификации</li>
<li>Комитет по торговле</li>
<li>Комитет по туризму</li>
<li>Комитет по финансовому мониторингу</li>
<li>Конституционный Суд</li>
<li>Межгосударственный экономический комитет</li>
<li>Межреспубликанский экономический комитет</li>
<li>Мининистерство науки и технологий</li>
<li>Министерство архитектуры, строительства и жилищно-коммунального хозяйства</li>
<li>Министерство безопасности</li>
<li>Министерство внешних экономических связей</li>
<li>Министерство внешних экономических связей и торговли</li>
<li>Министерство внутренних дел</li>
<li>Министерство государственного имущества</li>
<li>Министерство здравоохранения</li>
<li>Министерство здравоохранения и медицинской промышленности</li>
<li>Министерство здравоохранения и социального развития</li>
<li>Министерство имущественных отношений</li>
<li>Министерство иностранных дел</li>
<li>Министерство информационных технологий и связи</li>
<li>Министерство культуры</li>
<li>Министерство культуры и массовых коммуникаций</li>
<li>Министерство культуры и туризма</li>
<li>Министерство науки и высшего образования</li>
<li>Министерство науки и технической политики</li>
<li>Министерство науки и технологий</li>
<li>Министерство науки, высшей школы и технической политики</li>
<li>Министерство обороны</li>
<li>Министерство образования</li>
<li>Министерство образования и науки</li>
<li>Министерство общего и профессионального образования</li>
<li>Министерство охраны окружающей среды и природных ресурсов</li>
<li>Министерство печати и информации</li>
<li>Министерство по антимонопольной политике и поддержке предпринимательства</li>
<li>Министерство по атомной энергии</li>
<li>Министерство по внешним экономическим связям</li>
<li>Министерство по делам гражданской обороны, чрезвычайным ситуациям и ликвидации последствий стихийных бедствий</li>
<li>Министерство по делам национальностей и региональной политике</li>
<li>Министерство по делам печати, телерадиовещания и средств массовых коммуникаций</li>
<li>Министерство по делам федерации, национальной и миграционной политики</li>
<li>Министерство по земельной политике, строительству и жилищно-коммунальному хозяйству</li>
<li>Министерство по налогам и сборам</li>
<li>Министерство по связи и информатизации</li>
<li>Министерство по сотрудничеству с государствами - участниками Содружества Независимых Государств</li>
<li>Министерство по физической культуре, спорту и туризму</li>
<li>Министерство природных ресурсов</li>
<li>Министерство природных ресурсов и экологии</li>
<li>Министерство промышленности и торговли</li>
<li>Министерство промышленности и энергетики</li>
<li>Министерство промышленности, науки и технологий</li>
<li>Министерство просвещения</li>
<li>Министерство путей сообщения</li>
<li>Министерство регионального развития</li>
<li>Министерство Российской Федерации по делам гражданской обороны, чрезвычайным ситуациям и ликвидации последствий стихийных бедствий</li>
<li>Министерство Российской Федерации по делам Крыма</li>
<li>Министерство Российской Федерации по делам Северного Кавказа</li>
<li>Министерство Российской Федерации по развитию Дальнего Востока</li>
<li>Министерство Российской Федерации по развитию Дальнего Востока и Арктики</li>
<li>Министерство связи</li>
<li>Министерство связи и массовых коммуникаций</li>
<li>Министерство сельского хозяйства</li>
<li>Министерство сельского хозяйства и продовольствия</li>
<li>Министерство социальной защиты населения</li>
<li>Министерство спорта</li>
<li>Министерство спорта, туризма и молодежной политики</li>
<li>Министерство строительства</li>
<li>Министерство строительства и жилищно-коммунального хозяйства</li>
<li>Министерство топлива и энергетики</li>
<li>Министерство торговли</li>
<li>Министерство транспорта</li>
<li>Министерство транспорта и связи</li>
<li>Министерство труда</li>
<li>Министерство труда и социального развития</li>
<li>Министерство труда и социальной защиты</li>
<li>Министерство финансов</li>
<li>Министерство цифрового развития, связи и массовых коммуникаций</li>
<li>Министерство экологии и природных ресурсов</li>
<li>Министерство экономики</li>
<li>Министерство экономики и финансов</li>
<li>Министерство экономического развития</li>
<li>Министерство экономического развития и торговли</li>
<li>Министерство энергетики</li>
<li>Министерство юстиции</li>
<li>Министр обороны</li>
<li>Минстрой</li>
<li>Начальник Государственно-правового управления Президента</li>
<li>Независимый профсоюз горняков России</li>
<li>Общероссийская общественная организация "Паралимпийский комитет России"</li>
<li>Общероссийская общественная организация "Российский студенческий спортивный союз"</li>
<li>Общероссийская общественно-государственная организация "Добровольное общество содействия армии, авиации и флоту России"</li>
<li>Общероссийский союз общественных объединений "Олимпийский комитет России"</li>
<li>Общероссийский союз физкультурно-спортивных общественных объединений инвалидов "Сурдлимпийский комитет России"</li>
<li>Открытое акционерное общество "Газпром"</li>
<li>Пенсионный фонд</li>
<li>Первый заместитель Председателя Верховного Совета</li>
<li>Первый Заместитель Председателя Правительства</li>
<li>Первый заместитель Председателя Совета Министров</li>
<li>Первый заместитель Председателя Совета Министров - Правительства</li>
<li>Правительство</li>
<li>Правление Министерства по антимонопольной политике и поддержке предпринимательства</li>
<li>Правление Пенсионного фонда</li>
<li>Председатель Верховного Совета</li>
<li>Председатель Совета Министров</li>
<li>Председатель Совета Министров - Правительства</li>
<li>Президент</li>
<li>Президиум Верховного Совета</li>
<li>Президиум Высшего аттестационного комитета</li>
<li>Профсоюз работников культуры</li>
<li>Российская академия медицинских наук</li>
<li>Российская академия наук</li>
<li>Российский независимый профсоюз работников угольной промышленности</li>
<li>Российское агентство по государственным резервам</li>
<li>Российское космическое агентство при Правительстве Российской Федерации</li>
<li>Российское общество Красного Креста</li>
<li>Руководитель комитета по оперативному управлению народным хозяйством</li>
<li>Сберегательный банк</li>
<li>Секретарь Совета безопасности</li>
<li>Следственный комитет</li>
<li>Служба внешней разведки</li>
<li>Служба специальной связи и информации при Федеральной службе охраны</li>
<li>Совет Министров</li>
<li>Совет Министров - Правительство</li>
<li>Совет Народных Комиссаров</li>
<li>Совет Национальностей Верховного Совета</li>
<li>Совет Республики Верховного Совета</li>
<li>Совет Федерации Независимых Профессиональных Союзов</li>
<li>Совет Федерации независимых профсоюзов</li>
<li>Совет Федерации Федерального Собрания</li>
<li>Счетная палата</li>
<li>Съезд народных депутатов</li>
<li>Управление делами Президента</li>
<li>Федеральная авиационная служба России</li>
<li>Федеральная антимонопольная служба</li>
<li>Федеральная архивная служба России</li>
<li>Федеральная аэронавигационная служба</li>
<li>Федеральная дорожная служба России</li>
<li>Федеральная комиссия по рынку ценных бумаг</li>
<li>Федеральная миграционная служба</li>
<li>Федеральная налоговая служба</li>
<li>Федеральная пограничная служба</li>
<li>Федеральная пробирная палата</li>
<li>Федеральная регистрационная служба</li>
<li>Федеральная служба безопасности</li>
<li>Федеральная служба воздушного транспорта России</li>
<li>Федеральная служба войск национальной гвардии</li>
<li>Федеральная служба геодезии и картографии</li>
<li>Федеральная служба государственной регистрации, кадастра и картографии</li>
<li>Федеральная служба государственной статистики</li>
<li>Федеральная служба железнодорожных войск</li>
<li>Федеральная служба занятости</li>
<li>Федеральная служба земельного кадастра</li>
<li>Федеральная служба исполнения наказаний</li>
<li>Федеральная служба контрразведки</li>
<li>Федеральная служба лесного хозяйства</li>
<li>Федеральная служба налоговой полиции</li>
<li>Федеральная служба охраны</li>
<li>Федеральная служба по аккредитации</li>
<li>Федеральная служба по валютному и экспортному контролю</li>
<li>Федеральная служба по ветеринарному и фитосанитарному надзору</li>
<li>Федеральная служба по военно-техническому сотрудничеству</li>
<li>Федеральная служба по гидрометеорологии и мониторингу окружающей среды</li>
<li>Федеральная служба по делам о несостоятельности и финансовому оздоровлению</li>
<li>Федеральная служба по интеллектуальной собственности</li>
<li>Федеральная служба по интеллектуальной собственности, патентам и товарным знакам</li>
<li>Федеральная служба по надзору в сфере защиты прав потребителей и благополучия человека</li>
<li>Федеральная служба по надзору в сфере здравоохранения</li>
<li>Федеральная служба по надзору в сфере здравоохранения и социального развития</li>
<li>Федеральная служба по надзору в сфере массовых коммуникаций, связи и охраны культурного наследия</li>
<li>Федеральная служба по надзору в сфере образования и науки</li>
<li>Федеральная служба по надзору в сфере природопользования</li>
<li>Федеральная служба по надзору в сфере связи</li>
<li>Федеральная служба по надзору в сфере связи, информационных технологий и массовых коммуникаций</li>
<li>Федеральная служба по надзору в сфере транспорта</li>
<li>Федеральная служба по надзору за соблюдением законодательства в области охраны культурного наследия</li>
<li>Федеральная служба по надзору за соблюдением законодательства в сфере массовых коммуникаций и охране культурного наследия</li>
<li>Федеральная служба по надзору за страховой деятельностью</li>
<li>Федеральная служба по обеспечению государственной монополии на алкогольную продукцию</li>
<li>Федеральная служба по оборонному заказу</li>
<li>Федеральная служба по регулированию алкогольного рынка</li>
<li>Федеральная служба по регулированию естественных монополий в области связи</li>
<li>Федеральная служба по регулированию естественных монополий на транспорте</li>
<li>Федеральная служба по тарифам</li>
<li>Федеральная служба по техническому и экспортному контролю</li>
<li>Федеральная служба по труду и занятости</li>
<li>Федеральная служба по финансовому мониторингу</li>
<li>Федеральная служба по финансовому оздоровлению и банкротству</li>
<li>Федеральная служба по финансовым рынкам</li>
<li>Федеральная служба по экологическому, технологическому и атомному надзору</li>
<li>Федеральная служба Российской Федерации по контролю за оборотом наркотиков</li>
<li>Федеральная служба Российской Федерации по контролю за оборотом наркотических средств и психотропных веществ</li>
<li>Федеральная служба специального строительства</li>
<li>Федеральная служба страхового надзора</li>
<li>Федеральная служба судебных приставов</li>
<li>Федеральная служба финансово-бюджетного надзора</li>
<li>Федеральная таможенная служба</li>
<li>Федеральная энергетическая комиссия</li>
<li>Федеральное агентство водных ресурсов</li>
<li>Федеральное агентство воздушного транспорта</li>
<li>Федеральное агентство геодезии и картографии</li>
<li>Федеральное агентство железнодорожного транспорта</li>
<li>Федеральное агентство кадастра объектов недвижимости</li>
<li>Федеральное агентство лесного хозяйства</li>
<li>Федеральное агентство морского и речного транспорта</li>
<li>Федеральное агентство научных организаций</li>
<li>Федеральное агентство по атомной энергии</li>
<li>Федеральное агентство по высокотехнологичной медицинской помощи</li>
<li>Федеральное агентство по государственным резервам</li>
<li>Федеральное агентство по делам молодежи</li>
<li>Федеральное агентство по делам национальностей</li>
<li>Федеральное агентство по делам Содружества Независимых Государств, соотечественников, проживающих за рубежом, и по международному гуманитарному сотрудничеству</li>
<li>Федеральное агентство по здравоохранению и социальному развитию</li>
<li>Федеральное агентство по информационным технологиям</li>
<li>Федеральное агентство по культуре и кинематографии</li>
<li>Федеральное агентство по науке и инновациям</li>
<li>Федеральное агентство по недропользованию</li>
<li>Федеральное агентство по образованию</li>
<li>Федеральное агентство по обустройству государственной границы</li>
<li>Федеральное агентство по печати и массовым коммуникациям</li>
<li>Федеральное агентство по поставкам вооружения, военной, специальной техники и материальных средств</li>
<li>Федеральное агентство по рыболовству</li>
<li>Федеральное агентство по строительству и жилищно-коммунальному хозяйству</li>
<li>Федеральное агентство по техническому регулированию и метрологии</li>
<li>Федеральное агентство по туризму</li>
<li>Федеральное агентство по управлению государственным имуществом</li>
<li>Федеральное агентство по управлению особыми экономическими зонами</li>
<li>Федеральное агентство по управлению федеральным имуществом</li>
<li>Федеральное агентство по физической культуре и спорту</li>
<li>Федеральное агентство по экологическому, технологическому и атомному надзору</li>
<li>Федеральное агентство по энергетике</li>
<li>Федеральное агентство правительственной связи и информации при Президенте</li>
<li>Федеральное агентство связи</li>
<li>Федеральное агентство специального строительства</li>
<li>Федеральное архивное агентство</li>
<li>Федеральное дорожное агентство</li>
<li>Федеральное казначейство</li>
<li>Федеральное космическое агентство</li>
<li>Федеральное медико-биологическое агентство</li>
<li>Федеральный горный и промышленный надзор</li>
<li>Федеральный долговой центр при Правительстве</li>
<li>Федеральный надзор по ядерной и радиационной безопасности</li>
<li>Федеральный фонд обязательного медицинского страхования</li>
<li>Федерация независимых профсоюзов</li>
<li>Фонд социального страхования</li>
<li>Фонд федерального имущества</li>
<li>Центральный банк</li>
<li>Центральный совет оборонной спортивно-технической организации</li>
<li>Центральный совет профсоюза трудящихся горно-металлургической промышленности</li>
<li>Центробанк</li>
<li>Центросоюз</li>
<li>ЦК профсоюзов работников автомобильного транспорта и дорожного хозяйства</li>
<li>ЦК Российского профсоюза работников текстильной и легкой промышленности</li>
</ol>
</details>

По умолчанию настроено получение всех указов президента о назначениях за последние 5 лет.

Для доступа к документам федеральных ведомств (министерства, президент, агентства) в поле REGION указывается "РФ", а в поле FEDERAL_GOVERNMENT_BODY - название ведомства. 


Можно фильтровать документы по наличию в тексте слова (SEARCH_WORD) и/или по тэгу (SEARCH_TAG). Примеры существующих тэгов можно посмотреть на [странице](http://pravo.gov.ru/proxy/ips/?doc_itself=&vkart=card&nd=102842343&page=1&rdk=0&intelsearch=&link_id=0) с метинформацией документа. Примеры: "назначение", "награждение", "договор".

Формат дат: дд.мм.гггг


## Сохранение и логи
Документы сохраняются в формате html (с html тэгами) или txt (только текст) в папке RAW_FILES_FOLDER (по умолнчанию data/). В случае с html в файл в тэг <my_meta></> сохраняются метаданные документа - дата, тэги, автор (подписавший) и ссылка. Эти же данные сохраняются в файл LINKS_N_FILES_INFO (по умолнчанию files_n_links.json).
 
Название файла - id документа на портале.

Структура хранения по умолчанию. 

        ├── data/
        │   └── Калужская область/
        │       ├── links/
        │       │   └── files_n_links.json -- мета-информация о документах 
        │       └── raw_files/
        |           └──1234566788.html -- сам файл




## Парсинг
Есть [парсер](https://github.com/kbondar17/appointment-parser) указов с назначениями и отставками. Позволяет выделять назначения на должности и отставки.




