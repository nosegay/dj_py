from datetime import datetime
import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.DictReader(csvfile, delimiter=';')

            for ph in phone_reader:
                current_phone = Phone(id=ph.get("id"),
                                      name=ph.get("name"),
                                      price=float(ph.get("price")),
                                      image=ph.get("image"),
                                      release_date=datetime.strptime(ph.get("release_date"), "%Y-%m-%d"),
                                      lte_exists=bool(ph.get("lte_exists")),
                                      slug=slugify(ph.get("name")))
                current_phone.save()
