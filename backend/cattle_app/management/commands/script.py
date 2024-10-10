import random
from datetime import datetime, timedelta
from cattle_app.models import Cattle  # Импортируйте вашу модель


from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Генерация случайных данных
        names = [
            'Зорька', 'Рябинка', 'Грета', 'Златка', 'Мелисса', 'Бурка', 'Роза', 
            'Луна', 'Снежка', 'Ночка', 'Пегги', 'Карамелька', 
            'Тучка', 'Патриция', 'Слива', 'Фиалка', 'Снежинка', 
            'Яблонька', 'Капуста', 'Чернушка', 'Алёнка', 'Грация', 
            'Ласка', 'Зефирка', 'Умка', 'Фея', 'Тюльпан'
        ]
        colors = [
            'черная', 'черная', 'черная',
            'рябая', 'рябая', 'рябая', 'рябая',
            'белая', 'рябая', 'коричневая', 'серебристая', 'пегая'
        ]
        
        birth_dates = [datetime.now() - timedelta(days=random.randint(10, 365 * 5)) for _ in range(50)]         
        weights = [random.randint(25, 35) for _ in range(50)]         

        # Создание и сохранение 50 голов КРС
        for i in range(50):
            cattle = Cattle(
                id=i + 4,  # Начинаем с ID 4
                name=random.choice(names),
                color=random.choice(colors),
                birth=birth_dates[i],
                weight=weights[i],
            )
            cattle.save()  # Сохранение в базе данных
