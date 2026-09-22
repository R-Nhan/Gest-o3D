from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestaofilamento', '0002_venda_peso'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='valor_esperado',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]