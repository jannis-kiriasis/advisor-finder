from django.core.management.base import BaseCommand
from advisors.models import Location


class Command(BaseCommand):
    help = 'Imports a list of cities into the City model'

    def handle(self, *args, **options):
        cities = [
            "London",
            "Paris",
            "New York",
            "Berlin",
            "Tokyo"
        ]
        
        for city_name in cities:
            city = City(name=city_name)
            city.save()
        
        self.stdout.write(self.style.SUCCESS('Successfully imported cities.'))
