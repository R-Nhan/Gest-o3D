from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestaofilamento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='peso',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]