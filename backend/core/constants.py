# Максимальная длина полей
MAX_NAME_LENGTH = 150
MAX_EMAIL_LENGTH = 254
MAX_RESOURCE_LENGTH = 255
MAX_ACTION_LENGTH = 50

# Максимальный размер загружаемого изображения (в байтах)
MAX_AVATAR_SIZE = 4 * 1024 * 1024  # 4 MB

# Варианты действий для AuditLog
ACTION_CREATE = 'create'
ACTION_UPDATE = 'update'
ACTION_DELETE = 'delete'

ACTION_CHOICES = [
    (ACTION_CREATE, 'Создание'),
    (ACTION_UPDATE, 'Обновление'),
    (ACTION_DELETE, 'Удаление'),
]
