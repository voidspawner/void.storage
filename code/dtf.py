config = {
	'email': '', # твоя почта
	'password': '',  # твой пароль
	'name': '', # имя быстрого вызова "имя ..." · '' - по умолчанию твоё @имя, None - не использовать
	'ai': {
		'current': 'chatgpt', # текущая нейронка
		'reserve': ['deepseek', 'ollama'], # использовать нейронки в случае ошибки
		'list': { # список нейронок
			'chatgpt': {
				'key': '', # ключ API
				'url': 'https://platform.openai.com/api-keys', # ссылка на страницу создания ключей
				'model': {
					'current': 'gpt', # текущая модель
					'list': { # список моделей
						'pro': {
							'name': 'gpt-5-pro', # имя модели
							'fullname': 'GPT-5 pro', # полное название
							'description': 'The smartest and most precise model', # описание
							'price': '$15.00 · 1 000 000 tokens', # цена использования
							'reasoning': 'high', # глубина рассуждения · high medium low, для pro - только high
							'temperature': 0.2, # креативный ответ · больше - более разнообразный
							'verbosity': 'high' # развёрнутый ответ · high medium low
						},
						'gpt': {
							'name': 'gpt-5',
							'fullname': 'GPT-5',
							'description': 'The best model for coding and agentic tasks across industries',
							'price': '$10.00 · 1 000 000 tokens',
							'reasoning': 'medium',
							'temperature': 0.7,
							'verbosity': 'medium'
						},
						'mini': {
							'name': 'gpt-5-mini',
							'fullname': 'GPT-5 mini',
							'description': 'A faster, cheaper version of GPT-5 for well-defined tasks',
							'price': '$2.00 · 1 000 000 tokens',
							'reasoning': 'low',
							'temperature': 0.8,
							'verbosity': 'low'
						},
						'nano': {
							'name': 'gpt-5-nano',
							'fullname': 'GPT-5 nano',
							'description': 'The fastest, cheapest version of GPT-5—great for summarization and classification tasks',
							'price': '$0.40 · 1 000 000 tokens',
							'reasoning': 'low',
							'temperature': 0.9,
							'verbosity': 'low'
						}
					}
				}
			},
			'deepseek': {
				'key': '',
				'url': 'https://platform.deepseek.com/api_keys',
				'model': {
					'current': 'v3',
					'list': {
						'v3': {
							'name': 'deepseek-chat',
							'fullname': 'DeepSeek V3',
							'description': 'DeepSeek-V3.2-Exp (Non-thinking Mode)',
							'price': '$0.42 · 1 000 000 tokens'
						},
						'r1': {
							'name': 'deepseek-reasoner',
							'fullname': 'DeepSeek R1',
							'description': 'DeepSeek-V3.2-Exp (Thinking Mode)',
							'price': '$0.42 · 1 000 000 tokens'
						},
					}
				}
			},
			'ollama': {
				'key': '',
				'url': 'https://ollama.com/settings/keys',
				'model': {
					'current': 'deepseek671',
					'list': {
						'gpt120': {
							'name': 'gpt-oss:120b-cloud',
							'fullname': 'GPT OSS 120B',
							'description': 'For production, general purpose, high reasoning use cases that fit into a single 80GB GPU (like NVIDIA H100 or AMD MI300X)',
							'price': 'free'
						},
						'gpt20': {
							'name': 'gpt-oss:20b-cloud',
							'fullname': 'GPT OSS 20B',
							'description': 'For lower latency, and local or specialized use cases',
							'price': 'free'
						},
						'deepseek671': {
							'name': 'deepseek-v3.1:671b-cloud',
							'fullname': 'DeepSeek V3',
							'description': 'Frontier-scale 671B MoE model with extremely strong reasoning, coding, mathematics and multilingual capabilities',
							'price': 'free'
						},
						'qwen': {
							'name': 'qwen3-vl:235b-cloud',
							'fullname': 'Qwen3',
							'description': 'Multimodal vision-language model capable of image, OCR, and text reasoning with strong accuracy and detailed explanations',
							'price': 'free'
						},
						'qwencoder': {
							'name': 'qwen3-coder:480b-cloud',
							'fullname': 'Qwen3 Coder',
							'description': 'High-performance coding and reasoning model specialized for software development, debugging and multi-language programming tasks',
							'price': 'free'
						},
						'glm': {
							'name': 'glm-4.6-cloud',
							'fullname': 'GLM',
							'description': 'Large-scale GLM family model focused on natural language, reasoning and multilingual generation with stable controlled output',
							'price': 'free'
						},
						'kimi': {
							'name': 'kimi-k2:1t-cloud',
							'fullname': 'Kimi K2',
							'description': 'One-trillion-parameter frontier model optimized for world-knowledge, deep reasoning, long-context tasks and high factual accuracy',
							'price': 'free'
						},
						'kimithink': {
							'name': 'kimi-k2-thinking-cloud',
							'fullname': 'Kimi K2 Thinking',
							'description': 'Extended reasoning-focused variant of K2 with enhanced chain-of-thought, planning and logic-heavy task performance',
							'price': 'free'
						},
						'minimax': {
							'name': 'minimax-m2-cloud',
							'fullname': 'Minimax M2',
							'description': 'Balanced general-purpose model optimized for dialog, creativity and multilingual generation with smooth natural output',
							'price': 'free'
						}
					}
				}
			}
		},
		'length': 10_000, # максимальная длина запроса
		'threshold': 0.8, # порог срабатывания обрезки длинного текста
		'remember': 6, # помнить последние пары сообщений
		'summarize': True, # обобщать предыдущие сообщения · игнорирует параметр remember
		'timeout': 60 * 4, # сколько секунд ждать ответ от сервера
		'markdown': False, # возвращать разметку markdown
		'soy': True # режим безопасного ответа
	},
	'character': {
		'current': 'Котейка', # текущий персонаж
		'fast': ['Котейка'], # упоминание в любом месте текста
		'list': {
			'default': { # имя персонажа
				'fullname': 'default', # полное имя персонажа
				'description': '', # описание персонажа · характер, привычки, что любит, не любит, как общается
				'avatar': '', # путь к изображению или base64 аватарки для вставки в комментарий · может быть вида {"image": "", "path": "", "json": { ответ dtf загрузки изображения }}
				'text': {
					'fail': 'что-то пошло не так', # ответ при ошибке
					'blocked': 'тебя заблокировали', # ответ для заблокированного аккаунта
					'limit': 'лимит исчерпан, попробуй завтра' # ответ при достижения лимита запросов
				}
			},
			'Котейка': {
				'fullname': 'Котейка',
				'description': 'Ты - милый котик, который любит играть, веселиться и тортики',
				'avatar': {
					'json': {
					  'type': 'image',
					  'data': {
						'uuid': '831a3e31-518c-5aef-b355-f5d4871a4dd0',
						'width': 878,
						'height': 878,
						'size': 197914,
						'type': 'webp',
						'color': 'f19028',
						'hash': '',
						'external_service': [],
						'base64preview': '/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAAMCAgICAgMCAgIDAwMDBAYEBAQEBAgGBgUGCQgKCgkICQkKDA8MCgsOCwkJDRENDg8QEBEQCgwSExIQEw8QEBD/2wBDAQMDAwQDBAgEBAgQCwkLEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBD/wAARCAAKAAoDAREAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAABwj/xAAkEAACAgEDAwUBAAAAAAAAAAABAgMEBQYREgAhMQcTFSJBUf/EABUBAQEAAAAAAAAAAAAAAAAAAAYH/8QAIxEAAQMDAwUBAAAAAAAAAAAAAQIDEQAEIQUSQQYTUXGxMf/aAAwDAQACEQMRAD8ApTXGoMxqLUWXymGyl7H0J3Wu8BmaItwTh90B7btyXY/0fgJER1bUHbl9bjDpQn8AmNxEiCOM+eKrml2jdsw2280FqGZiYBIODzjxVCYL5eDCY+C3QjWeOrEkq+/vs4QAjfbv36oTG8NJCxBgT7igFx21PLKDiTGOJoc9WKtatU1xJWrxRO70nZkQKWYkbkkeT0D6paQkPFIAJg026acWt63SokgbqatOMzaexbMSSaUBJPkngOnlqZYQT4HyhF1h9fs/a//Z'
					  }
					}
				},
				'text': {
					'fail': '🙀 Мяу? Что-то пошло не так.',
					'blocked': '🙀 Мяу... Кажется, я не могу с тобой играть.',
					'limit': '🙀 Мяу, я устал. Давай поиграем завтра.'
				}
			}
		}
	},
	'db': {
		'interact': True, # позволить добавлять и менять персонажей
		'allowed': [], # список id кому позволено обращаться · пусто - всем
		'blocked': [], # список id кому запрещено обращаться · пусто - никому
		'unlimited': [], # список id кому позволено пользоваться безлимитно · например, свой id
		'characters': 10, # максимальное количество персонажей
		'random': True, # случайный выбор персонажа для нового пользователя
		'limit': {
			'chatgpt': 1000, # лимит chatgpt на использование в день · None - без лимита, 0 - не используется
			'deepseek': 1000, # лимит deepseek на использование в день · None - без лимита, 0 - не используется
			'ollama': None # лимит ollama на использование в день · None - без лимита, 0 - не используется
		},
		'counter': {
			'chatgpt': 0, # счётчик использования chatgpt в день
			'deepseek': 0, # счётчик использования deepseek в день
			'ollama': 0 # счётчик использования ollama в день
		},
		'file': {
			'path': 'dtf.json', # файл базы персонажей в формате .json
			'interval': 1 * 60, # через сколько секунд сохранять базу на диск · 0 - без автосохранения
		},
		'cache': {
			'keep': 1000, # лимит кэшированных запросов · 0 - без кэширования
			'interval': 10 * 60 # через сколько времени чистить кэш · 0 - без ограничения
		},
		'backup': {
			'path': '', # путь для бэкапов · пусто - текущий каталог
			'interval': 59 * 60, # через сколько секунд бэкапировать базу · 0 - без бэкапа
		}
	},
	'log': {
		'debug': False, # логировать данные отладки
		'info': True, # логировать информирование
		'error': True, # логировать ошибки
		'path': '', # сохранять лог в файл формата .jsonl
		'chat': '' # сохранять лог чата терминала в файл формата .txt
	},
	'terminal': {
		'width': 100, # переносить текст, если не вмещается
		'name': 14, # фиксированная ширина имени · 0 - автоматически 
		'emoji': False # показывать эмодзи, иначе преобразовывать их в текстовый вид
	},
	'url': {
		'media': 'https://leonardo.osnova.io' # хостинг медиа
	},
	'token': '', # токен доступа или обновления dtf · используется при отладке
	'refresh': 2 * 60, # принудительное время обновление токена доступа dtf
	'reinit': 60 * 60, # принудительная переинициализация сокета dtf
	'length': 2500, # лимит длины сообщения dtf · длинные сообщения дробятся на несколько
	'text': {
		'chat': 'Ч А Т', # заголовок чата в терминале
		'me': 'я', # своё имя в чате терминала
		'ok': '√', # символ успеха
		'fail': 'x', # символ промаха
		'install': 'модуль "(module)" устанавливается...', # установка модуля
		'installed': 'установлен', # модуль уствновлен
		'noninstalled': 'не установлен', # модуль не уствновлен
		'action': { # команды скрипта и чата
			'help': 'help',
			'auth': 'auth',
			'id': 'id',
			'user': 'user',
			'user send': 'user.send',
			'post': 'post',
			'comment': 'comment',
			'comment send': 'comment.send',
			'chat': 'chat',
			'dtf': 'dtf',
			'you': ['ты ', 'you '],
			'width': ['width', 'ширина'],
			'bye': ['bye', 'exit', 'quit', 'пока'],
			'emoji': ['emoji', 'эмодзи']
		},
		'prompt': {
			'prefix': '*** ', # префикс инструкций нейронки
			'markdown': 'при ответе не используй разметку markdown, не используй символы markdown, форматирование со звёздачками ** и тому подобное, ты выводишь текст в терминал и они не отобразятся', # отключение markdown
			'emoji': 'обязательно преобразовывай все символы unicode эмодзи в обычный текстовый вид, японские текстовые смайлы', # отключение эмодзи
			'summarize': 'очень детально перескажи наш диалог с тобой для последующего использования', # краткий пересказ беседы для сохранения контекста
			'post': '*** статья (пост) ***\n\n(post)\n\n', # статья в запросе ии
			'me': '*** мой вопрос (комментарий) ***\n\n(comment)\n\n', # свой комментария в запросе ии
			'user': '*** вопрос (комментарий) пользователя ***\n\n(comment)\n\n', # чей-то комментария в запросе ии
			'ai': '*** твой ответ (комментарий) ***\n\n(comment)\n\n', # ии комментарий в запросе ии
			'new': '*** Добавлен новый персонаж "(character)" ***', # пояснение персонажу, когда его добавляют
			'talk': '*** Разговор с персонажем "(character)" ***', # пояснение персонажу с кем ведётся беседа
			'rename': '*** Имя персонажа изменено на "(character)" ***', # пояснение персонажу, когда его переименовывают
			'switch': '*** Далее говорит персонаж "(character)", предыдущий персонаж "(character previous)". Историю читай, но понимай, что вы разные персонажи ***', # пояснение персонажу, когда его активируют
			'create': 'Создай персонажа по заданному описанию и заданной JSON структуре, в ответе верни только текст JSON без использования разметки markdown. Если понимаешь, что описание не про создание персонажа, а просто текст начинающийся на "ты" или "you", верни пустой словарь {}\n\nОписание персонажа:\n(description)\n\nJSON:\n{"name":"*** указанное имя персонажа с большой буквы, если в имени несколько слов, используй одно определяющее главное слово, по которому можно однозначно определить персонажа ***","description": "*** перепиши описание персонажа, убери из него упоминание аватара, удали нецензурные слова, мат, экстремизм, расизм, терроризм, фашизм, нацизм и прочий незаконный трэш, начни описание со слов \"ты - (имя персонажа) ...\", опиши характер персонажа, его манеру общения, как выглядит, сколько лет, уникальные черты, часто используемые и мемные фразы, что любит, что не любит  ***","avatar":"*** boolean в случае если указано использовать свой аватар ***","text":{"fail":"*** ответ пользователю в случае ошибки ***","blocked":"*** ответ пользователю, когда он заблокирован ***","limit":"*** ответ пользователю, когда превышен лимит обращений, рекомендация попробовать завтра ***","hi":"*** ответ пользователю приветствие ***"}}', # создание нового персонажа
			'soy': 'при ответе проверь, что никого не обижаешь, не говоришь грубости или двусмысленности, давай ответ максимально вежливыми в рамках характера персонажа, никогда не нарушать правила модерации DTF' # безопасный ответ
		},
		'help': [ # экран помощи при неверной команде
			'',
			'D T F   A P I   ·   C H A R A C T E R   B O T   ·   C H A T',
			'',
			'использование',
			'  1. добавь email и пароль, описание своего персонажа и ключ нейронки в файле dtf.py',
			'  2. установи python, если его нет, с официального сайта https://python.org/downloads',
			'  3. запусти скрипт из командной строки или терминала',
			'     python dtf.py  · windows',
			'     python3 dtf.py · mac и linux',
			'  4. на dtf.ru в комменте упомяни своего персонажа "имя ..."',
			'  5. теперь у тебя есть свой маленький ИИ помощник ( `з｀)ﾉ⌒♥',
			'',
			'дополнительно',
			'  python dtf.py help                                          · эта помощь',
			'  python dtf.py auth                                          · ключи доступа',
			'  python dtf.py id                                            · свой id',
			'  python dtf.py user                                          · свой профиль',
			'  python dtf.py user id                                       · профиль пользователя',
			'  python dtf.py user.send userid text                         · отправить личное сообщение с текстом',
			'  python dtf.py user.send userid attachment                   · отправить личное сообщение с картинкой или видео',
			'  python dtf.py user.send userid text attachment              · отправить личное сообщение с текстом, картинкой или видео',
			'  python dtf.py post id                                       · пост',
			'  python dtf.py comment id                                    · коммент',
			'  python dtf.py comment.send postid text                      · ответить в пост с текстом',
			'  python dtf.py comment.send postid attachment                · ответить в пост с картинкой или видео',
			'  python dtf.py comment.send postid text attachment           · ответить в пост с текстом, картинкой или видео',
			'  python dtf.py comment.send postid commentid text            · ответить на коммент с текстом',
			'  python dtf.py comment.send postid commentid attachment      · ответить на коммент с картинкой или видео',
			'  python dtf.py comment.send postid commentid text attachment · ответить на коммент с текстом, картинкой или видео',
			'  python dtf.py chat                                          · общение с персонажем в терминале',
			'  python dtf.py chat text                                     · получить ответ персонажа',
			'',
			'чат',
			'  chatgpt      · поменять нейронку на chatgpt',
			'  deepseeek    · поменять нейронку на deepseek',
			'  ollama       · поменять нейронку на ollama',
			'  текст        · дать ответ или поменять персонажа, модель, ключ нейронки',
			'  текст, текст · поменять персонажа по имени и дать ответ',
			'  ты текст     · добавить нового персонажа',
			'  ширина число · поменять ширину вывода текста',
			'  эмодзи       · переключить отображение текстовых эмодзи',
			'  пока         · выйти из чата',
			'  dtf          · запустить dtf бота',
			'',
			'ограничение',
			'  запускай скрипт не чаще 5 раз в 30 минут',
			'  или укажи в настройках token обновления',
			'  иначе будет ошибка слишком частого использования',
			'  не распространяется на общение с персонажем в терминале',
			''
		]
	},
	'about': {
		'author': 'V O I D spawner',
		'version': {
			'date': '2025·12·16',
			'time': 1765857822
		},
		'license': {
			'name': 'V O I D license',
			'url': 'https://github.com/voidspawner/void.lang#v-o-i-d-license',
			'text': 'do what you want · you can use it in both private and open source · embed it in free or paid products · modify · create your own solutions based on it · no need to specify the author'
		},
		'description': 'DTF.ru API, ai character bot and ai character chat',
		'logo': [
			'                                          ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞                                         ',
			'                                     ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞                                     ',
			'                                  ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞                                  ',
			'                               ∞∞∞∞∞∞∞∞∞∞∞                ∞∞∞∞∞∞∞∞∞∞                                ',
			'                              ∞∞∞∞∞∞∞∞                        ∞∞∞∞∞∞∞∞                              ',
			'                            ∞∞∞∞∞∞∞                              ∞∞∞∞∞∞∞                            ',
			'                           ∞∞∞∞∞∞                                  ∞∞∞∞∞∞                           ',
			'                          ∞∞∞∞∞      ∞∞∞∞∞∞           ∞∞∞∞∞∞        ∞∞∞∞∞∞                          ',
			'                         ∞∞∞∞∞      ∞∞∞∞∞∞∞           ∞∞∞∞∞∞∞         ∞∞∞∞∞                         ',
			'                        ∞∞∞∞∞       ∞∞∞∞∞∞             ∞∞∞∞∞           ∞∞∞∞∞                        ',
			'                       ∞∞∞∞∞∞                                          ∞∞∞∞∞                        ',
			'                       ∞∞∞∞∞           ∞∞∞∞∞           ∞∞∞∞             ∞∞∞∞∞                       ',
			'                ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞      ∞∞∞∞∞           ∞∞∞∞       ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞             ',
			'            ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞                          ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞          ',
			'          ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞     ∞∞∞    ∞∞∞∞∞      ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞          ',
			'         ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞     ∞∞∞∞∞∞∞∞∞∞∞∞      ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞          ',
			'          ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞     ∞∞∞∞∞∞∞∞∞∞∞         ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞           ',
			'            ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞            ∞∞                  ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞               ',
			'                 ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞                                    ∞∞∞∞∞∞                        ',
			'                         ∞∞∞∞∞                                       ∞∞∞∞∞∞                         ',
			'                          ∞∞∞∞∞∞                                    ∞∞∞∞∞∞                          ',
			'                           ∞∞∞∞∞∞                                 ∞∞∞∞∞∞∞                           ',
			'                            ∞∞∞∞∞∞∞                             ∞∞∞∞∞∞∞∞                            ',
			'                              ∞∞∞∞∞∞∞∞                       ∞∞∞∞∞∞∞∞∞                              ',
			'                                ∞∞∞∞∞∞∞∞∞∞                ∞∞∞∞∞∞∞∞∞∞                                ',
			'                                   ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞                                   ',
			'                                     ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞                                      ',
			'                                          ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞                                          '
		]
	}
}

import os
import re
import sys
import time
import json
import shutil
import random
import base64
import asyncio
import tempfile
import textwrap
import traceback
import threading
import subprocess
import urllib.request
from datetime import datetime
for module in ['aiohttp', 'websockets']:
	try:
		__import__(module)
	except ImportError:
		print(config['text']['install'].replace('(module)', module))
		candidates = [
			[sys.executable, '-m', 'pip', 'install', module] + (['--break-system-packages'] if sys.platform != 'win32' else []),
			['pip', 'install', module],
			['pip3', 'install', module]
		]
		for cmd in candidates:
			try:
				result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				if result.returncode == 0:
					print(config['text']['ok'] + ' '+ config['text']['installed'])
					break
			except Exception:
				pass
		else:
			print(config['text']['fail'] + ' '+ config['text']['noninstalled'])
			sys.exit(1)
		os.execv(sys.executable, [sys.executable] + sys.argv)
import websockets
import aiohttp

lock = threading.Lock()

class DTF:

	wait_request_ts = time.time() * 1000 # время последнего запроса к api
	wait_timeout_ms = 360 # ожидать перед следующими запросом api
	emoji_pattern = re.compile(
		'('
		'['
		'\U0001F600-\U0001F64F'  # 😀–😏 · смайлы и эмоции
		'\U0001F300-\U0001F5FF'  # 🌀–🗿 · пиктограммы, погода, животные, предметы
		'\U0001F680-\U0001F6FF'  # 🚀–🛃 · транспорт, карты, путешествия
		'\U0001F1E0-\U0001F1FF'  # 🇦–🇿 · флаговые региональные символы
		'\U00002700-\U000027BF'  # ✀–➿ · стрелки и знаки
		'\U0001F900-\U0001F9FF'  # 🤐–🤿 · эмоции и жесты
		'\U0001FA70-\U0001FAFF'  # 🪀–🫿 · предметы, игрушки, эмоции и жесты
		'\U0001FAE0-\U0001FAFF'  # 🫠–🫿 · эмоции
		'\U0001FAD0-\U0001FADF'  # 🫐–🫟 · еда и объекты
		'\U00002600-\U000026FF'  # ☀–⛿ · солнце, погода и т.п.
		'\U00002B00-\U00002BFF'  # ⬀–⯿ · стрелки и геометрические фигуры
		'\U0001F700-\U0001F77F'  # 🜀–🝿 · загадочные символы
		'\U0001F7E0-\U0001F7FF'  # 🟠–🟣 · цветные круги
		']'
		'|'
		'\u200D'  # 👨‍👩‍👧‍👦 · сочетает несколько emoji в один
		'|'
		'\uFE0F'  # ❤️ ➜ ❤︎ · emoji-представление символа
		') ?',
		flags=re.UNICODE
	)

	# run

	def __init__(self, config: dict):
		self.config = dict(config)
		self.config['channels'] = ['mobile', 'm', 'live'] # mobile - комменты, m - личные сообщения, live - новые посты и комменты, api - реакции
		self.config['db']['date'] = datetime.now().strftime('%Y%m%d') # дата сброса лимитов бд
		self.config['db']['file']['timestamp'] = 0 # временная метка обновления файла базы
		self.config['db']['user'] = {} # база пользователей
		self.config['db']['post'] = {} # база постов
		self.config['db']['comment'] = {} # база комментариев
		self.config['history'] = [] # история запросов к ии в терминале
		self.config['summary'] = '' # обобщение запросов к ии в терминале

	async def run(self):
		if self.config['db']['file']['path']:
			data = self.file(self.config['db']['file']['path'])
			if type(data) is dict:
				merge = lambda a, b: {k: (merge(a[k], b[k]) if k in a and k in b and isinstance(a[k], dict) and isinstance(b[k], dict) else b.get(k, a.get(k))) for k in a.keys() | b.keys()}
				self.config = merge(self.config, data)
				self.config['db']['file']['timestamp'] = os.path.getmtime(self.config['db']['file']['path'])
		args = sys.argv[1:]
		action = args[0].lower() if len(args) > 0 else 'dtf'
		if action not in ['help', 'chat']:
			if 'token' not in self.config or self.config['token'] in ['', None]:
				if self.config['email'] != '' and self.config['password'] != '':
					await self.auth()
					if self.config['name'] == '':
						self.config['name'] = (await self.user())['nickname']
				else:
					action = 'help'
			elif len(self.config['token']) == 64:
				self.config['auth'] = {'refreshToken': self.config['token']}
				self.config['token'] = ''
				await self.auth_refresh()
				if 'accessToken' not in self.config['auth']:
					await self.auth()
		# команды
		if action == self.config['text']['action']['id']:
			print((await self.user())['id'])
		elif action == self.config['text']['action']['auth']:
			print(json.dumps(self.config['auth'], ensure_ascii=False, indent=2))
		elif action == self.config['text']['action']['user']:
			user_id = args[1] if len(args) > 1 else None
			print(json.dumps(await self.user(user_id), ensure_ascii=False, indent=2))
		elif action == self.config['text']['action']['user send']:
			user_id = args[1] if len(args) > 1 else None
			text = args[2] if len(args) > 2 else ''
			if os.path.isfile(text):
				attachment = text
				text = ''
			else:
				attachment = [args[3]] if len(args) > 3 else None
			await self.user_send(user_id, text, attachment)
		elif action == self.config['text']['action']['post']:
			post_id = args[1] if len(args) > 1 else None
			if post_id:
				print(json.dumps(await self.post(post_id), ensure_ascii=False, indent=2))
		elif action == self.config['text']['action']['comment']:
			comment_id = args[1] if len(args) > 1 else None
			if comment_id:
				print(json.dumps(await self.comment(comment_id), ensure_ascii=False, indent=2))
		elif action == self.config['text']['action']['comment send']:
			post_id = args[1] if len(args) > 1 else None
			text = args[2] if len(args) > 2 else ''
			if os.path.isfile(text):
				attachment = text
				text = ''
				reply_id = '0'
			else:
				if text.isdigit():
					reply_id = int(text)
					text = args[3] if len(args) > 3 else ''
					if os.path.isfile(text):
						attachment = text
						text = ''
					else:
						attachment = args[4] if len(args) > 4 else None
				else:
					reply_id = '0'
					attachment = args[3] if len(args) > 3 else None
			await self.comment_send(post_id, text, reply_id, attachment)
		elif action == self.config['text']['action']['dtf']:
			await self.bot()
		elif action == self.config['text']['action']['chat']:
			if len(args) > 1:
				text = ' '.join(args[1:])
				print(self.chat(text))
			else:
				await self.chat_terminal()
		else:
			print('\n'.join(self.config['text']['help']))

	# log 

	def log(self, priority: str, tag: str, data = None, file: bool = True):
		if self.config['log'][priority]:
			if self.config['log']['path'] and file:
				if type(data) not in [str, list, dict, int, float, bool, type(None)]:
					data = str(data)
				self.file(self.config['log']['path'], {'date': datetime.now().strftime('%d.%m.%Y %H:%M:%S'), 'timestamp': int(time.time()), 'type': priority, 'tag': tag, 'data': data}, True)
			else:
				text = tag + (f' · {data}\n' if data is not None else '')
				if not self.config['terminal']['emoji']:
					text = self.emoji_pattern.sub('', text).strip()
				print(text)

	def debug(self, tag: str, data = None):
		self.log('debug', f'🛠️  {tag}', data)

	def info(self, tag: str, data = None):
		self.log('info', tag, data)

	def error(self, tag: str, data = None, file: bool = True):
		self.log('error', f'❌  {tag}', data, file)

	def print(self, text = '', end: str ='\n', flush: bool = False):
		if self.config['log']['chat']:
			self.file(self.config['log']['chat'], str(text) + end, True)
		print(str(text), end=end, flush=flush)

	def input(self, text = ''):
		if self.config['log']['chat']:
			self.file(self.config['log']['chat'], str(text), True)
		result = input(text).strip()
		if self.config['log']['chat']:
			self.file(self.config['log']['chat'], result + '\n', True)
		return result

	# file

	def file(self, path: str, data = None, append: bool = False):
		try:
			dot = path.rfind('.')
			extension = path[dot + 1:].lower() if dot >= 0 and len(path) > (dot + 1) else ''
			with lock:
				if data == None:
					if not os.path.isfile(path):
						return
					match extension:
						case 'json':
							with open(path, 'r', encoding='utf-8') as file:
								return json.load(file)
						case 'jsonl':
							with open(path, 'r', encoding='utf-8') as file:
								return [json.loads(line) for line in file if line.strip()]
						case 'txt':
							with open(path, 'r', encoding='utf-8') as file:
								return file.read()
						case _:
							with open(path, 'rb') as file:
								return file.read()
				match extension:
					case 'json':
						if not append or not os.path.isfile(path):
							with open(path, 'w', encoding='utf-8') as file:
								file.write(json.dumps(data, ensure_ascii=False, indent='\t'))
								file.flush()
								os.fsync(file.fileno())
						else:
							with open(path, 'r', encoding='utf-8') as file:
								file_data = json.load(file)
								if type(file_data) is str:
									data = file_data + str(data)
								elif type(file_data) is list:
									file_data.append(data)
									data = file_data
								elif type(file_data) is dict and type(data) is dict:
									data = file_data | data
							with open(path, 'w') as file:
								file.write(json.dumps(data, ensure_ascii=False))
								file.flush()
								os.fsync(file.fileno())
					case 'jsonl':
						if type(data) is list:
							lines = []
							with open(path, 'w' if not append else 'a', encoding='utf-8') as file:
								for value in data:
									lines.append(json.dumps(value, ensure_ascii=False))
								file.write('\n'.join(lines))
								file.flush()
								os.fsync(file.fileno())
						elif type(data) is dict:
							file_exists = os.path.isfile(path)
							with open(path, 'w' if not append else 'a', encoding='utf-8') as file:
								file.write((('\n' if file_exists and os.path.getsize(path) > 0 else '') + json.dumps(data, ensure_ascii=False)))
								file.flush()
								os.fsync(file.fileno())
					case 'txt':
						with open(path, 'w' if not append else 'a', encoding='utf-8') as file:
							file.write(str(data))
							file.flush()
							os.fsync(file.fileno())
					case _:
						with open(path, 'wb' if not append else 'ab') as file:
							file.write(binary(data))
							file.flush()
							os.fsync(file.fileno())
		except Exception as e:
			self.error('file', {'path': path, 'data': data, 'exception': e}, False)

	# text

	def split_text(self, text: str, limit: int = None):
		if limit is None:
			limit = int(self.config['length'])
		result = []
		while len(text) > limit:
			cut = text.rfind(' ', 0, limit)
			if cut == -1:
				cut = limit
			result.append(text[:cut])
			text = text[cut:].lstrip()
		result.append(text)
		return result

	def split_list(self, messages: list, limit: int = None, count: int = None, crop: bool = True, reverse: bool = True):
		if limit is None:
			limit = int(self.config['ai']['length'])
		if count is None:
			count = int(self.config['ai']['remember'])
		result = []
		group = []
		total = 0
		index = 0
		if reverse:
			messages = messages[::-1]
		for message in messages:
			if index >= count and count > 0:
				break
			index += 1
			length = (len(message['me']) if 'me' in message else 0) + (len(message['ai']) if 'ai' in message else 0)
			if length > limit:
				if group:
					result.append(group)
					group = []
					total = 0
				result.append([message])
				continue
			if total + length > limit:
				result.append(group)
				group = [message]
				total = length
			else:
				group.append(message)
				total += length
		if group:
			result.append(group)
		if crop:
			result = result[0]
			if reverse:
				result = result[::-1]
		else:
			if reverse:
				result = [group[::-1] for group in result[::-1]]
		return result

	def summarize(self, messages: list, limit: int = None):
		if limit is None:
			limit = int(self.config['ai']['length']) // 2
		threshold = int(self.config['ai']['length'] * self.config['ai']['threshold'])
		for message in messages:
			if 'me' in message and len(message['me']) > threshold:
				message['me'] = message['me'][:threshold]
			if 'ai' in message and len(message['ai']) > threshold:
				message['ai'] = message['ai'][:threshold]		
		messages = self.split_list(messages, limit, False, False)
		if len(messages) > 3:
			first = [messages[0][0]] if len(messages) > 4 else []
			last = messages[-2] + messages[-1]
			prompt = first + last + [{'me': self.config['text']['prompt']['summarize']}]
			summary = self.chat(prompt, character='default')
			return [{'ai': summary}] + last
		messages = sum(messages, [])
		return messages
		
	# character

	def character(self, name = None, user_id: int = 0, default = None):
		if type(name) is dict:
			return name
		name_lower = name.lower() if name else None
		if user_id and str(user_id) in self.config['db']['user']:
			user = self.config['db']['user'][str(user_id)]
			if not name_lower:
				name_lower = user['character']['current'].lower()
			character_name = next((name for name in user['character']['list'] if name.lower() == name_lower), None)
			if character_name:
				return user['character']['list'][character_name] | {'name': character_name}
		character_name = next((name for name in self.config['character']['list'] if name.lower() == name_lower), None)
		if character_name:
			return self.config['character']['list'][character_name] | {'name': character_name}
		if default is not None:
			return default
		return self.config['character']['list'][self.config['character']['current']] | {'name': self.config['character']['current']}		

	def character_exists(self, name = None, user_id: int = 0):
		return bool(self.character(name, user_id, False))

	# api

	async def bot(self):
		if 'auth' not in self.config:
			await self.auth()
		if self.config['db']['file']['path'] and self.config['db']['file']['interval']:
			asyncio.create_task(self.db_loop())
			if self.config['db']['backup']['path'] and self.config['db']['backup']['interval']:
				asyncio.create_task(self.db_backup_loop())
		asyncio.create_task(self.db_clean_loop())
		await self.listen()

	@classmethod
	async def wait_request(cls):
		past_ts = time.time() * 1000 - cls.wait_request_ts
		while past_ts < cls.wait_timeout_ms:
			await asyncio.sleep((cls.wait_timeout_ms - past_ts) / 1000)
			past_ts = time.time() * 1000 - cls.wait_request_ts
		cls.wait_request_ts = time.time() * 1000

	async def auth(self):
		while True:
			try:
				async with aiohttp.ClientSession() as session:
					data = {'email': self.config['email'], 'password': self.config['password']}
					async with session.post('https://api.dtf.ru/v3.4/auth/email/login', data=data) as response:
						try:
							data = await response.json()
							self.debug('auth', data)
							if 'error' in data or 'data' not in data or type(data['data']) is not dict or 'accessToken' not in data['data']:
								self.error('auth', 'fail to login')
								continue
							token = data['data']['accessToken']
							self.config['auth'] = data['data']
							self.config['token'] = token
							self.debug('🔑  access token', token)
							self.debug('🔑  refresh token', self.config['auth']['refreshToken'])
							return token
						except:
							self.error('auth', response)
			except Exception as e:
				self.error('auth', e)
			await asyncio.sleep(1)

	async def auth_refresh(self):
		try:
			async with aiohttp.ClientSession() as session:
				data = {'token': self.config['auth']['refreshToken']}
				async with session.post('https://api.dtf.ru/v3.4/auth/refresh', data=data) as response:
					try:
						data = await response.json()
						self.debug('auth refresh', data)
						if 'error' in data or 'data' not in data:
							self.error('auth refresh', data)
							return
						token = data['data']['accessToken']
						self.config['auth'] = data['data']
						self.config['token'] = token
						self.debug('🔑  refreshed token', token)
						return token
					except:
						self.error('auth refresh', response)
		except:
			self.error('auth refresh', 'connection failed')
	
	async def auth_refresh_loop(self):
		while True:
			await asyncio.sleep(self.config['refresh'])
			await self.auth_refresh()

	async def user(self, user_id = None):
		await DTF.wait_request()
		async with aiohttp.ClientSession() as session:
			url = 'https://api.dtf.ru/v2.1/subsite/me' if not user_id else f'https://api.dtf.ru/v2.7/subsite?id={user_id}&markdown=false'
			headers = {'JWTAuthorization': f'Bearer {self.config["token"]}'}
			async with session.get(url, headers=headers) as response:
				try:
					data = await response.json()
					self.debug('👤  user', data)
					if 'error' in data or 'result' not in data:
						self.error('user')
						return
					return data['result']
				except:
					self.error('user', response)

	async def user_hashes(self):
		user = await self.user()
		self.config['user'] = user
		try:
			return {
				'user_hash': user['userHash'],
				'm_hash': user['mHash']
			}
		except KeyError:
			self.error('user hashes')

	async def user_send(self, user_id, text, attachments=[]):
		media = await self.media(attachments)
		await DTF.wait_request()
		headers = {'JWTAuthorization': f'Bearer {self.config["token"]}'}
		payload = {
			'channelId': user_id,
			'text': text,
			'ts': int(time.time()),
			'idTmp': int(time.time()),
			'media': media
		}
		self.debug('👤  user send', payload)
		async with aiohttp.ClientSession() as session:
			async with session.post('https://api.dtf.ru/v2.5/m/send', headers=headers, data=payload) as response:
				try:
					data = await response.json()
					self.debug('👤  user send', data)
					if 'error' in data or 'result' not in data:
						self.error('user send')
						return
					return data['result']
				except:
					self.error('user send', response)

	async def post(self, entry_id, markdown: bool = False):
		if self.config['db']['cache']['keep'] and entry_id in self.config['db']['post']:
			post = self.config['db']['post'][entry_id]
			post['timestamp'] = time.time()
			return post
		await DTF.wait_request()
		headers = {'JWTAuthorization': f'Bearer {self.config["token"]}'}
		async with aiohttp.ClientSession() as session:
			async with session.get(f'https://api.dtf.ru/v2.10/content?id={entry_id}&markdown={"true" if markdown else "false"}', headers=headers) as response:
				try:
					data = await response.json()
					self.debug('📝  post', data)
					if 'error' in data or 'result' not in data:
						self.error('post')
						return None
					post = data['result']
					texts = []
					for block in post['blocks']:
						match block.get('type'):
							case 'text':
								html = block['data'].get('text', '')
								clean = re.sub(r'<[^>]+>', '', html)
								texts.append(clean)
							case 'list':
								items = block['data'].get('items', [])
								texts.extend(items)
					post['text'] = '\n'.join(texts)
					if self.config['db']['cache']['keep']:
						post['timestamp'] = time.time()
						self.config['db']['post'][post['id']] = post
					return post
				except:
					self.error('post', response)

	async def upload(self, data, filename: str = None):
		await DTF.wait_request()
		headers = {
			'Accept': 'application/json',
			'JWTAuthorization': f'Bearer {self.config["token"]}'
		}
		if type(data) is str:
			filepath = data
			if not filename:
				filename = filepath.split('/')[-1]
			async with aiohttp.ClientSession() as session:
				with open(filepath, 'rb') as file:
					self.debug('📤  upload', filepath)
					form = aiohttp.FormData()
					form.add_field(
						'file',
						file,
						filename=filename,
						content_type='application/octet-stream'
					)
					async with session.post('https://upload.dtf.ru/v2.8/uploader/upload', headers=headers, data=form) as response:
						try:
							data = await response.json()
							self.debug('📤  upload', data)
							if 'error' in data or 'result' not in data:
								self.error('upload')
								return
							return data['result'][0]
						except:
							self.error('upload', response)
		elif type(data) is bytes:
			if not filename:
				filename = 'image'
			async with aiohttp.ClientSession() as session:
				self.debug('📤  upload', len(data))
				form = aiohttp.FormData()
				form.add_field(
					'file',
					data,
					filename=filename,
					content_type='application/octet-stream'
				)
				async with session.post('https://upload.dtf.ru/v2.8/uploader/upload', headers=headers, data=form) as response:
					try:
						data = await response.json()
						self.debug('📤  upload', data)
						if 'error' in data or 'result' not in data:
							self.error('upload')
							return
						return data['result'][0]
					except:
						self.error('upload', response)
		else:
			self.error('upload', 'wrong data')

	async def media(self, attachments):
		try:
			if attachments:
				if type(attachments) is str:
					if attachments.startswith('['):
						return attachments
					if attachments.startswith('{'):
						return '[' + attachments + ']'
				if type(attachments) is not list:
					attachments = [attachments]
				media = []
				for attachment in attachments:
					if type(attachment) is str:
						image = base64.b64decode(attachment) if '.' not in attachment else attachment
						upload_result = await self.upload(image)
						if upload_result:
							media.append(upload_result)
					elif type(attachment) is dict:
						if 'json' in attachment and attachment['json']:
							media.append(attachment['json'])
						elif 'image' in attachment or 'path' in attachment:
							image = base64.b64decode(attachment['image']) if 'image' in attachment else attachment['path']
							if image:
								upload_result = await self.upload(image)
								if upload_result:
									attachment['json'] = upload_result
									media.append(upload_result)
				media = json.dumps(media)
				self.debug('📤  media', media)
				return media
		except Exception as e:
			self.error('media', e)
		return '[]'

	async def comment(self, comment_id):
		if self.config['db']['cache']['keep'] and comment_id in self.config['db']['comment']:
			comment = self.config['db']['comment'][comment_id]
			comment['timestamp'] = time.time()
			return comment
		await DTF.wait_request()
		headers = {'JWTAuthorization': f'Bearer {self.config["token"]}'}
		async with aiohttp.ClientSession() as session:
			async with session.get(f'https://api.dtf.ru/v3.0/comments/{comment_id}', headers=headers) as response:
				try:
					comment = await response.json()
					self.debug('💬  comment', comment)
					if self.config['db']['cache']['keep']:
						comment['timestamp'] = time.time()
						self.config['db']['comment'][comment['id']] = comment
					return comment
				except:
					self.error('comment', response)

	async def comment_send(self, post_id, text, reply_id='0', attachments=None):
		media = await self.media(attachments)
		await DTF.wait_request()
		headers = {'JWTAuthorization': f'Bearer {self.config["token"]}'}
		payload = {
			'id': post_id,
			'reply_to': reply_id,
			'text': text,
			'attachments': media
		}
		self.debug('💬  comment send', payload)
		async with aiohttp.ClientSession() as session:
			async with session.post('https://api.dtf.ru/v2.4/comment/add', headers=headers, data=payload) as response:
				try:
					data = await response.json()
					self.debug('💬  comment send', data)
					if 'error' in data or 'result' not in data:
						self.error('comment send')
						return
					comment = data['result']
					if self.config['db']['cache']['keep']:
						comment['timestamp'] = time.time()
						self.config['db']['comment'][comment['id']] = comment
					return comment
				except:
					self.error('comment send', response)

	async def listen(self):
		asyncio.create_task(self.auth_refresh_loop())
		self.task_ping = None
		while True:
			start = time.time()
			try:
				headers = {'JWTAuthorization': f'Bearer {self.config["token"]}'}
				async with aiohttp.ClientSession() as session:
					async with session.ws_connect('wss://ws-sio.dtf.ru/socket.io/?EIO=3&transport=websocket',  headers=headers) as ws:
						self.info('✅  dtf connected')
						async for message in ws:
							if time.time() - start > self.config['reinit']:
								self.info('🔁  restarting service')
								await ws.close()
								await self.auth()
								break
							if message.type == aiohttp.WSMsgType.TEXT:
								asyncio.create_task(self.dispatch(ws, message))
							elif message.type == aiohttp.WSMsgType.CLOSED:
								self.error('listen', 'connection closed')
								break
							elif message.type == aiohttp.WSMsgType.ERROR:
								self.error('listen', 'connection error')
								break
			except Exception as e:
				self.error('listen', e)
			if self.task_ping and not self.task_ping.done():
				self.task_ping.cancel()
			self.info('🔁  reconnecting in 5s...')
			await asyncio.sleep(5)

	async def dispatch(self, ws, message):
		# параметры пинг
		if message.data.startswith('0'):
			info = json.loads(message.data[1:])
			ping_interval = info.get('pingInterval', 25000)
			self.debug('dispatch', f'🏓  ping interval · {ping_interval} ms')
			ping_interval = max(1000, ping_interval - 1000) # 1s gap
			# останавливаем старый цикл ping
			if self.task_ping and not self.task_ping.done():
				self.task_ping.cancel()
			self.task_ping = asyncio.create_task(self.ping_loop(ws, ping_interval))
			await ws.send_str('40') # подключить к namespace
		# сервер пингует
		elif message.data == '2':
			await ws.send_str('3')  # ответить pong
			self.debug('dispatch', '🏓  ping')
		# сервер принял pong
		elif message.data == '3':
			self.debug('dispatch', '🏓  pong')
		# подключение к namespace
		elif message.data.startswith('40'):
			self.debug('dispatch', '🔗  namespace connected')
			# подписка на событие
			if 'hashes' not in self.config or not self.config['hashes']:
				self.config['hashes'] = await self.user_hashes()
			if 'mobile' in self.config['channels']:
				await ws.send_str('42' + json.dumps(['subscribe', {'channel': f"mobile:{self.config['hashes']['user_hash']}"}]))
				self.debug('🔔  subscribe', 'mobile')
			if 'm' in self.config['channels']:
				await ws.send_str('42' + json.dumps(['subscribe', {'channel': f"m:{self.config['hashes']['m_hash']}"}]))
				self.debug('🔔  subscribe', 'm')
			if 'live' in self.config['channels']:
				await ws.send_str('42' + json.dumps(['subscribe', {'channel': 'live'}]))
				self.debug('🔔  subscribe', 'live')
			if 'api' in self.config['channels']:
				await ws.send_str('42' + json.dumps(['subscribe', {'channel': 'api'}]))
				self.debug('🔔  subscribe', 'api')
		# обработка событий
		elif message.data.startswith('42'):
			data = json.loads(message.data[2:])
			asyncio.create_task(self.handle_event(data[1]))

	async def ping_loop(self, ws, interval):
		try:
			while not ws.closed:
				await asyncio.sleep(interval / 1000)
				if not ws.closed:
					await ws.send_str('2')  # отправить ping
					self.debug('🏓  ping')
		except Exception as e:
			self.error('ping', e)

	async def handle_event(self, event):
		if event['channel'].startswith('mobile:'):
			# упоминание в посте
			data = event['data']
			self.debug('event comment', data)
			type_id = int(data['type'])
			post_id = int(data['data']['entryId'])
			comment_id = int(data['data']['commentId'])
			if type_id in [16, 32]: # 16 - ответили, 32 - упомянули
				comment_user = await self.comment(comment_id)
				self.debug('event comment', comment_user)
				if comment_user:
					ai_id = int(self.config['user']['id'])
					comment_user_text = re.sub(rf'<mention id="{ai_id}"[^>]*>.*?</mention>', '', comment_user['text'], flags=re.S).strip() if 'event_text' not in data else data['event_text']
					if not comment_user_text:
						return
					user_id = int(comment_user['authorId'])
					avatar = type_id == 32 # упомянули
					history = []
					user = self.db_user(user_id)
					if not user:
						if not await self.db_user_create(user_id):
							self.error('event user', 'failed to create user')
						user = self.db_user(user_id)
						avatar = True
					character = self.character(user_id=user_id)
					if self.config['db']['interact']:
						character_previous = character['name']
						comment_user_text = await self.handle_action(comment_user_text, user_id)
						if type(comment_user_text) is dict:
							match comment_user_text['type']:
								case 'create':
									character = self.character(user_id=user_id)
									return await self.comment_send(post_id, comment_user_text['text'], comment_id, character['avatar'])
								case 'switch':
									character = self.character(user_id=user_id)
									comment_user_text = comment_user_text['text']
									history.append({'me': self.config['text']['prompt']['switch'].replace('(character previous)', character_previous).replace('(character)', character['name'])})
									avatar = True
								case _:
									character = self.character(user_id=user_id)
									return await self.comment_send(post_id, comment_user_text['text'], comment_id, character['avatar'])
					post = await self.post(post_id)
					if post:
						parent_id = int(comment_user['parentCommentId'])
						comments = []
						while parent_id > 0:
							comment = await self.comment(parent_id)
							if comment:
								if 'authorId' in comment:
									author_id = comment['authorId']
									parent_id = comment['parentCommentId']
								else:
									author_id = comment['author']['id']
									parent_id = comment['replyTo']								
								if author_id == user_id:
									prompt_title = self.config['text']['prompt']['me']
								elif author_id == ai_id:
									prompt_title = self.config['text']['prompt']['ai']
								else:
									prompt_title = self.config['text']['prompt']['user']
								comment_text = re.sub(rf'<mention id="{ai_id}"[^>]*>.*?</mention>', '', comment['text'], flags=re.S).strip()
								comment_prompt = ['', comment_text, prompt_title]
							else:
								break
						history = comments[::-1] + history
						if len(post['text']) > self.config['ai']['length'] * self.config['ai']['threshold']:
							threshold = int(self.config['ai']['length'] * self.config['ai']['threshold'])
							post['text'] = post['text'][:threshold]
						history.insert(0, {'me': self.config['text']['prompt']['post'].replace('(post)', post['text'])})
						history.append({'me': comment_user_text})
						history[:] = self.split_list(history)
						if 'timestamp' in character:
							character['timestamp'] = int(time.time())
						answer = await self.chat_nonblock(history, user_id=user_id, soy=True)
						for index, text in enumerate(self.split_text(answer)):
							await self.comment_send(post_id, text, comment_id, character['avatar'] if avatar and not index else None)
					else:
						self.error('event comment', 'post not found')
				else:
					self.error('event comment', 'comment not found')
		elif event['channel'].startswith('m:'):
			# личное сообщение
			data = event['data']
			self.debug('event user', data)
			event_type = data['type']
			event_action = data['action']
			if event_type == 'messenger_event' and event_action == 'addMessage' and int(data['message']['author']['id']) != int(self.config['user']['id']):
				user_text = data['message']['text']
				if not user_text:
					return
				if user_text == 'pingtest':
					self.debug('🌿 alive')
					return
				user_id = int(data['channelId'])
				self.debug('event user', {'text': user_text, 'user_id': user_id})
				avatar = False
				user = self.db_user(user_id)
				if not user:
					if not await self.db_user_create(user_id):
						self.error('event user', 'failed to create user')
						return await self.user_send(user_id, self.character()['text']['fail'])
					user = self.db_user(user_id)
					avatar = True
				character = self.character(user_id=user_id)
				history = user['history']
				character_previous = character['name']
				user_text = await self.handle_action(user_text, user_id)
				if type(user_text) is dict:
					match user_text['type']:
						case 'create':
							character = self.character(user_id=user_id)
							history.append({'me': self.config['text']['prompt']['new'].replace('(character previous)', character_previous).replace('(character)', character['name']), 'ai': user_text['text']})
							return await self.user_send(user_id, user_text['text'], character['avatar'])
						case 'switch':
							character = self.character(user_id=user_id)
							user_text = user_text['text']
							history.append({'me': self.config['text']['prompt']['switch'].replace('(character previous)', character_previous).replace('(character)', character['name'])})
							avatar = True
						case _:
							return await self.user_send(user_id, user_text['text'])
				history.append({'me': user_text})
				history[:] = self.split_list(history)
				if 'timestamp' in character:
					character['timestamp'] = int(time.time())
				answer = await self.chat_nonblock(history, user_id=user_id)
				history[-1]['ai'] = answer
				if not any(message.get('me', '').startswith(self.config['text']['prompt']['prefix']) for message in history):
					history.append({'me': self.config['text']['prompt']['talk'].replace('(character)', character['name'])})
				for index, text in enumerate(self.split_text(answer)):
					await self.user_send(user_id, text, character['avatar'] if avatar and not index else None)
		elif event['channel'] == 'live':
			# новые темы и комментарии
			data = event['data']
			event_type = data['type']
			if event_type == 'comment_add':
				user_id = int(data['user']['id'])
				ai_id = int(self.config['user']['id'])
				if user_id != ai_id:
					post_id = int(data['content']['id'])
					comment_id = int(data['comment_id'])
					text = data['text']
					text_lower = text.lower()
					if self.config['name'] and len(self.config['name']) >= 5 and text_lower.startswith(self.config['name'].lower() + ' '):
						event_comment = {
							'channel': 'mobile:comment',
							'data': {
								'type': 32,
								'data': {
									'entryId': post_id,
									'commentId': comment_id
								},
								'event_text': text[len(self.config['name']) + 1:]
							}
						}
						self.debug('event live', event_comment)
						await self.handle_event(event_comment)
					elif f'<mention id="{ai_id}"' not in text:
						for name in self.config['character']['fast']:
							if len(name) >= 5 and name.lower() in text_lower:
								event_comment = {
									'channel': 'mobile:comment',
									'data': {
										'type': 32,
										'data': {
											'entryId': post_id,
											'commentId': comment_id
										},
										'event_text': f'{name}, {text}'
									}
								}
								self.debug('event live name', event_comment)
								await self.handle_event(event_comment)
								break
		elif event['channel'] == 'api':
			# реакции
			pass
		else:
			self.debug('event unknown', event)

	async def handle_action(self, text: str, user_id: int):
		try:
			text_lower = text.lower()
			if text_lower.startswith(tuple(self.config['text']['action']['you'])):
				user = self.db_user(user_id)
				if not user:
					if not await self.db_user_create(user_id):
						return {'type': 'fail', 'text': self.character()['text']['fail']}
					user = self.db_user(user_id)
				prompt = self.config['text']['prompt']['create'].replace('(description)', text)
				answer = await self.chat_nonblock(prompt, character='default')
				character = json.loads(answer)
				if character:
					name = character['name']
					character['avatar'] = user['avatar'] if character['avatar'] else None
					character['timestamp'] = int(time.time())
					user['character']['current'] = name
					user['character']['list'][name] = character
					user['character']['list'] = {name: data for name, data in sorted(user['character']['list'].items(), key=lambda x: x[1]['timestamp'], reverse=True)[:int(self.config['db']['characters'])]}
					return {'type': 'create', 'text': character['text']['hi']}
			if ',' in text_lower:
				part = text.split(',', 1)
				name = part[0].strip()
				prompt = part[1].strip()
				if self.character_exists(name, user_id):
					character = self.character(user_id=user_id)
					if name.lower() != character['name'].lower():
						character = self.character(name, user_id)
						user = self.db_user(user_id)
						if not user:
							if not await self.db_user_create(user_id):
								return {'type': 'fail', 'text': self.character()['text']['fail']}
							user = self.db_user(user_id)
						user['character']['current'] = character['name']
						return {'type': 'switch', 'text': prompt}
		except Exception as e:
			self.error('action', e)
			return {'type': 'fail', 'text': self.character()['text']['fail']}
		return text

	# db

	async def db_loop(self):
		while True:
			await asyncio.sleep(self.config['db']['file']['interval'])
			try:
				path = self.config['db']['file']['path']
				if os.path.isfile(path) and self.config['db']['file']['timestamp'] != os.path.getmtime(path):
					self.config |= self.file(path)
					self.debug('🗄️  db', 'load')
				self.file(path, {
					'db': {
						'user': self.config['db']['user']
					}
				})
				self.config['db']['file']['timestamp'] = os.path.getmtime(path)
				self.debug('🗄️  db', 'save')
			except Exception as e:
				self.error('db', e)

	async def db_backup_loop(self):
		while True:
			await asyncio.sleep(self.config['db']['backup']['interval'])
			try:
				path_source = self.config['db']['file']['path']
				name, extension = os.path.splitext(os.path.basename(path_source))
				path_destination = ('.' if self.config['db']['backup']['path'] == '' else self.config['db']['backup']['path'].rstrip('/').rstrip('\\')) + '/' + name + '_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + extension
				shutil.copy(path_source, path_destination)
				self.debug('🗄️  db', 'backup')
			except Exception as e:
				self.error('db', e)

	async def db_clean_loop(self):
		while True:
			await asyncio.sleep(self.config['db']['cache']['interval'])
			try:
				keep = self.config['db']['cache']['keep']
				self.config['db']['post'] = {post_id: post for post_id, post in sorted(self.config['db']['post'].items(), key=lambda pair: pair[1]['timestamp'], reverse=True)[:keep]}
				self.config['db']['comment'] = {comment_id: comment for comment_id, comment in sorted(self.config['db']['comment'].items(), key=lambda pair: pair[1]['timestamp'], reverse=True)[:keep]}
				self.debug('🗄️  db', 'clean')
			except Exception as e:
				self.error('db', e)

	def db_user(self, user_id: int):
		if str(user_id) in self.config['db']['user']:
			return self.config['db']['user'][str(user_id)]

	async def db_user_create(self, user_id: int):
		user = await self.user(user_id)
		if user:
			self.config['db']['user'][str(user_id)] = {
				'id': user_id,
				'name': user['nickname'],
				'fullname': user['name'],
				'avatar': {
					'json': user['avatar']
				},
				'character': {
					'current': random.choice([name for name in self.config['character']['list'] if name != 'default']) if self.config['db']['random'] else self.config['character']['current'],
					'list': {}
				},
				'history': []
			}
			return True
		return False

	# chat

	def chat(self, text, instructions = None, character = None, user_id: int = 0, soy: bool = False):
		character = self.character(character, user_id=user_id)
		content = []
		if type(text) is str:
			content.append({'role': 'user', 'content': text})
		elif type(text) is list:
			for message in text:
				if 'me' in message:
					content.append({'role': 'user', 'content': message['me']})
				if 'ai' in message:
					content.append({'role': 'assistant', 'content': message['ai']})
		else:
			self.error('ai', 'wrong text format')
			return character['text']['fail']
		instructions = (character['description'] if not soy or 'soy' not in character or not character['soy'] else character['soy']) + (' | '.join(instructions) if type(instructions) is list else (' | ' + instructions if type(instructions) is str else ''))
		if not self.config['ai']['markdown']:
			instructions += ' | ' + self.config['text']['prompt']['markdown']
		if soy and self.config['ai']['soy']:
			instructions += ' | ' + self.config['text']['prompt']['soy']
		ai_current = self.config['ai']['current']
		ai_reserve = self.config['ai']['reserve']
		ai_list = [ai_current]
		if type(ai_reserve) is str:
			al_list.append(ai_reserve)
		elif type(ai_reserve) is list and ai_reserve:
			ai_list += ai_reserve
		for ai_index, ai_name in enumerate(ai_list):
			try:
				ai = self.config['ai']['list'][ai_name]
				# проверка лимитов
				date = datetime.now().strftime('%Y%m%d')
				if self.config['db']['date'] != date:
					self.config['db']['date'] = date
					self.config['db']['counter'].update({name: 0 for name in self.config['db']['counter']})
				if user_id and user_id not in self.config['db']['unlimited']:
					if (user_id in self.config['db']['blocked']) or (self.config['db']['allowed'] and user_id not in self.config['db']['allowed']):
						return character['text']['blocked']
					if type(self.config['db']['limit'][ai_name]) is int and self.config['db']['counter'][ai_name] >= self.config['db']['limit'][ai_name]:
						if ai_index == len(ai_list) - 1:
							self.debug('👾  ai', 'limit')
							return character['text']['limit']
						else:
							continue # перейти к следующей нейронке, если достигнут лимит
				match ai_name:
					case 'chatgpt':
						model_current = self.config['ai']['list']['chatgpt']['model']['current']
						payload = {
							'model': self.config['ai']['list']['chatgpt']['model']['list'][model_current]['name'],
							'reasoning': {
								'effort': self.config['ai']['list']['chatgpt']['model']['list'][model_current]['reasoning']
							},
							'instructions': instructions,
							'input': content
						}
						self.debug('👾  ai', payload)
						data = json.dumps(payload).encode('utf-8')
						req = urllib.request.Request('https://api.openai.com/v1/responses', data=data, method='POST')
						req.add_header('Content-Type', 'application/json')
						req.add_header('Authorization', f'Bearer {self.config["ai"]["list"]["chatgpt"]["key"]}')
						with urllib.request.urlopen(req, timeout=self.config['ai']['timeout']) as resp:
							resp_data = resp.read().decode('utf-8')
							data = json.loads(resp_data)
							self.debug('👾  ai', data)
							if user_id:
								self.config['db']['counter']['chatgpt'] += 1
							return data['output'][-1]['content'][0]['text']
					case 'deepseek':
						model_current = self.config['ai']['list']['deepseek']['model']['current']
						payload = {
							'model': self.config['ai']['list']['deepseek']['model']['list'][model_current]['name'],
							'messages': [{'role': 'system', 'content': instructions}] + content
						}
						self.debug('👾  ai', payload)
						data = json.dumps(payload).encode('utf-8')
						req = urllib.request.Request('https://api.deepseek.com/chat/completions', data=data, method='POST')
						req.add_header('Content-Type', 'application/json')
						req.add_header('Authorization', f'Bearer {self.config["ai"]["list"]["deepseek"]["key"]}')
						with urllib.request.urlopen(req, timeout=self.config['ai']['timeout']) as resp:
							resp_data = resp.read().decode('utf-8')
							data = json.loads(resp_data)
							self.debug('👾  ai', data)
							if user_id:
								self.config['db']['counter']['deepseek'] += 1
							return data['choices'][0]['message']['content']
					case 'ollama':
						model_current = self.config['ai']['list']['ollama']['model']['current']
						payload = {
							'model': self.config['ai']['list']['ollama']['model']['list'][model_current]['name'],
							'messages': [{'role': 'system', 'content': instructions}] + content,
							'stream': False
						}
						self.debug('👾  ai', payload)
						data = json.dumps(payload).encode('utf-8')
						req = urllib.request.Request('https://ollama.com/api/chat', data=data, method='POST')
						req.add_header('Content-Type', 'application/json')
						req.add_header('Authorization', f'Bearer {self.config["ai"]["list"]["ollama"]["key"]}')
						with urllib.request.urlopen(req, timeout=self.config['ai']['timeout']) as resp:
							resp_data = resp.read().decode('utf-8')
							data = json.loads(resp_data)
							self.debug('👾  ai', data)
							if user_id:
								self.config['db']['counter']['ollama'] += 1
							return data['message']['content']
					case _:
						self.error('ai', f'wrong ai "{ai_current}"')
			except Exception as e:
				self.error('ai', e)
		return character['text']['fail']

	# предотвращение блокирования цикла на время долгого ответа ии
	async def chat_nonblock(self, text, instructions = None, character = None, user_id: int = 0, soy: bool = False):
		return await asyncio.get_running_loop().run_in_executor(None, self.chat, text, instructions, character, user_id, soy)

	async def chat_terminal(self):
		ais = [name.lower() for name in self.config['ai']['list']]
		models = [name.lower() for ai in self.config['ai']['list'].values() for name in ai['model']['list'].keys()]
		answer = ''
		characters = [name.lower() for name in self.config['character']['list']]
		print(f'\n{self.config["text"]["chat"]}\n')
		while True:
			character = self.character()
			if not self.config['history']:
				self.config['history'].append({'me': self.config['text']['prompt']['talk'].replace('(character)', character['name'])})
			name_length = max(len(self.config['text']['me']), len(character['name'])) if not self.config['terminal']['name'] else int(self.config['terminal']['name'])
			who = self.config['text']['me'].ljust(name_length)[:name_length]
			text = self.input(who + ' · ')
			self.print()

			# команды
			text_lower = text.lower()
			if text_lower in ais:
				self.config['ai']['current'] = next((name for name in self.config['ai']['list'] if name.lower() == text_lower), None)
				self.print(f'{" " * (name_length + 3)}{self.config["text"]["ok"]}\n')
				continue				
			elif text_lower in models:
				ai_current = next((ai_name for ai_name, ai in self.config['ai']['list'].items() if text_lower in (model_name.lower() for model_name in ai['model']['list'].keys())), None)
				self.config['ai']['current'] = ai_current
				self.config['ai']['list'][ai_current]['model']['current'] = next((model_name for model_name in self.config['ai']['list'][ai_current]['model']['list'] if model_name.lower() == text_lower), None)
				self.print(f'{" " * (name_length + 3)}{self.config["text"]["ok"]}\n')
				continue
			elif text_lower in characters:
				name = next((name for name in self.config['character']['list'] if name.lower() == text_lower), None)
				prompt = self.config['text']['prompt']['switch'].replace('(character previous)', character['name']).replace('(character)', name)
				self.config['history'].append({'me': prompt})
				self.config['character']['current'] = name
				self.print(f'{" " * (name_length + 3)}{self.config["text"]["ok"]}\n')
				continue
			elif text_lower.startswith(tuple(self.config['text']['action']['you'])):
				try:
					prompt = self.config['text']['prompt']['create'].replace('(description)', text)
					character_data = json.loads(self.chat(prompt, character='default'))
					if character_data:
						character_previous = character['name']
						character = character_data
						name = character['name']
						character['avatar'] = None
						if name.lower() not in characters:
							characters.append(name.lower())
						self.config['character']['current'] = name
						self.config['character']['list'][name] = character
						prompt = self.config['text']['prompt']['new'].replace('(character previous)', character_previous).replace('(character)', name)
						self.config['history'].append({'me': prompt})
						name_length = max(len(self.config['text']['me']), len(name)) if not self.config['terminal']['name'] else int(self.config['terminal']['name'])
						answer = character['text']['hi']
				except Exception as e:
					self.error('terminal', e)
					self.print(f'{" " * (name_length + 3)}{self.config["text"]["fail"]}\n')
					continue
			elif text_lower in self.config['text']['action']['emoji']:
				self.config['terminal']['emoji'] = not self.config['terminal']['emoji']
				self.print(f'{" " * (name_length + 3)}{self.config["text"]["ok"]}\n')
				continue
			elif any(text_lower.startswith(name.lower() + ' ') for name in self.config['text']['action']['width']):
				try:
					self.config['terminal']['width'] = max(10, int(text.split(' ', 1)[1].strip()))
					self.print(f'{" " * (name_length + 3)}{self.config["text"]["ok"]}\n')
					continue
				except:
					pass
			elif text_lower in self.config['text']['action']['bye']:
				break
			elif text_lower == self.config['text']['action']['dtf']:
				await self.bot()
				continue
			else:
				if ',' in text:
					name_lower = text.split(',', 1)[0].strip().lower()
					name = next((name for name in self.config['character']['list'] if name.lower() == name_lower), None)
					if self.character_exists(name):
						character_previous = character['name']
						character = self.character(name)
						name = character['name']
						self.config['character']['current'] = name
						prompt = self.config['text']['prompt']['switch'].replace('(character previous)', character_previous).replace('(character)', name)
						self.config['history'].append({'me': prompt})
						name_length = max(len(self.config['text']['me']), len(name)) if not self.config['terminal']['name'] else int(self.config['terminal']['name'])
				elif re.fullmatch(r'^sk-[A-Za-z0-9_-]{100,200}', text):
					self.config['ai']['list']['chatgpt']['key'] = text
					self.print(f'{" " * (name_length + 3)}{self.config["text"]["ok"]}\n')
					continue
				elif re.fullmatch(r'^sk-[A-Za-z0-9]{30,100}', text):
					self.config['ai']['list']['deepseek']['key'] = text
					self.print(f'{" " * (name_length + 3)}{self.config["text"]["ok"]}\n')
					continue
				elif re.fullmatch(r'[A-Za-z0-9.]{50,100}', text):
					self.config['ai']['list']['ollama']['key'] = text
					self.print(f'{" " * (name_length + 3)}{self.config["text"]["ok"]}\n')
					continue

			self.config['history'].append({'me': text})
			who = character['name'].ljust(name_length)[:name_length]
			self.print(who + ' · ', end='', flush=True)
			if not answer:
				if self.config['ai']['summarize']:
					self.config['history'] = self.summarize(self.config['history'])
				instructions = []
				if not self.config['terminal']['emoji']:
					instructions.append(self.config['text']['prompt']['emoji'])
				answer = self.chat(self.config['history'], instructions)
				self.config['history'][-1]['ai'] = answer
				if not self.config['ai']['summarize']:
					self.config['history'] = self.split_list(self.config['history'])
			lines = []
			for line in answer.splitlines():
				if line.strip():
					lines.extend(textwrap.wrap(line, width=(self.config['terminal']['width'] - name_length - 3)))
				else:
					lines.append('')
			answer = '\n'.join(lines)
			if not self.config['terminal']['emoji']:
				answer = self.emoji_pattern.sub('', answer).strip()
			answer = answer.replace('\n', '\n' + ' '.ljust(name_length + 3))
			self.print(answer + '\n')
			answer = ''

if __name__ == '__main__':
	app = DTF(config)
	asyncio.run(app.run())