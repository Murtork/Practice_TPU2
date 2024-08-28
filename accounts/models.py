from django.db import models

# energy/models.py
from django.db import models
from django.contrib.auth.models import User


class Consumer(models.Model):
    CONSUMER_TYPE_CHOICES = [
        ('Физическое', 'Физическое лицо'),
        ('Юридическое', 'Юридическое лицо'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    consumer_type = models.CharField(max_length=15, choices=CONSUMER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.consumer_type})"


class Tariff(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"Название тарифа")
    rate_per_kwh = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u"Тариф в руб./кВтч")

    def __str__(self):
        return self.name


class ConsumptionRecord(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    date = models.DateField(verbose_name=u"Дата показаний")
    kwh_consumed = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u"кВт использовано")
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE, verbose_name=u"Тариф")
    paid = models.BooleanField(default=False, verbose_name=u"Оплачео?")

    def total_cost(self):
        return self.kwh_consumed * self.tariff.rate_per_kwh

    def __str__(self):
        return f"Запись для {self.consumer} на {self.date}"


class ContractPhys(models.Model):
    contract_phys_id = models.AutoField(primary_key=True, verbose_name=u"ID физ. лица")
    phys_login = models.CharField(max_length=25, verbose_name=u"Логин")
    second_name = models.CharField(max_length=25, verbose_name=u"Фамилия")
    first_name = models.CharField(max_length=25, verbose_name=u"Имя")
    third_name = models.CharField(max_length=25, verbose_name=u"Отчество")
    phone_number = models.CharField(max_length=15, verbose_name=u"Номер телефона")
    date_of_birth = models.DateField(max_length=15, verbose_name=u"Дата рождения")

    class Meta:
        verbose_name = "Физическое лицо"
        verbose_name_plural = "Физические лица"

    def __str__(self):
        return f"{self.second_name} {self.first_name} {self.third_name}"


class ContractLegal(models.Model):
    contract_legal_id = models.AutoField(primary_key=True, verbose_name=u"ID физ. лица")
    legal_login = models.CharField(max_length=25, verbose_name=u"Логин юр. лица")
    name = models.CharField(max_length=25, verbose_name=u"Наименование организации")
    type = models.CharField(max_length=25, verbose_name=u"Тип")
    phone_number = models.CharField(max_length=15, verbose_name=u"Номер телефона")
    legal_adress = models.CharField(max_length=60, verbose_name=u"Адрес юр. лица")
    inn = models.CharField(max_length=15, verbose_name=u"ИНН")

    class Meta:
        verbose_name = "Юридическое лицо"
        verbose_name_plural = "Юридические лица"

    def __str__(self):
        return f"{self.name}"
