# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-19 16:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad_Gestacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.SmallIntegerField(choices=[(1, b'1er Trimestre'), (2, b'2do Trimestre'), (3, b'3er Trimestre')])),
                ('nombre_actividad', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AlimentacionCostumbres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo_leche_materna', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('motivo_suspencion_lactancia', models.CharField(blank=True, max_length=100, null=True)),
                ('afecciones', models.CharField(blank=True, max_length=100)),
                ('enfermedades', models.CharField(blank=True, max_length=256)),
                ('edad_alimentacion_complementaria', models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfA qu\xc3\xa9 edad inici\xc3\xb3 la alimentaci\xc3\xb3n complementaria? (meses)')),
                ('forma_alimento', models.CharField(max_length=100)),
                ('lugar_desayuno', models.CharField(max_length=50, verbose_name=b'desayuno')),
                ('lugar_comida_media_manana', models.CharField(blank=True, max_length=50, verbose_name=b'media ma\xc3\xb1ana')),
                ('lugar_almuerzo', models.CharField(max_length=50, verbose_name=b'almuerzo')),
                ('lugar_comida_media_tarde', models.CharField(blank=True, max_length=50, verbose_name=b'media tarde')),
                ('lugar_cena', models.CharField(max_length=50, verbose_name=b'cena')),
                ('lugar_comida_otro', models.CharField(blank=True, max_length=50, verbose_name=b'otro')),
                ('alimento_preferido', models.CharField(max_length=20, verbose_name=b'\xc2\xbfCu\xc3\xa1l es el alimento preferido por el ni\xc3\xb1o(a)?')),
                ('alimento_rechazado', models.CharField(max_length=20, verbose_name=b'\xc2\xbfCu\xc3\xa1l es el alimento que rechaza el ni\xc3\xb1o(a)?')),
                ('apetito', models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfC\xc3\xb3mo es el apetito del ni\xc3\xb1o?')),
                ('motivo_cambios_alimentacion', models.CharField(blank=True, max_length=256, verbose_name=b'Describa los principales cambios de la alimentaci\xc3\xb3n del fin de semana de los dem\xc3\xa1s d\xc3\xadas')),
            ],
        ),
        migrations.CreateModel(
            name='DatosFamiliaresOtros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_hermanos', models.PositiveSmallIntegerField(verbose_name=b'N\xc3\xbamero de hermanos')),
                ('transtorno_hermanos', models.NullBooleanField(verbose_name=b'\xc2\xbfAlguno de los hermanos tiene alg\xc3\xban tipo de transtorno?')),
                ('hermano_transtorno', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'\xc2\xbfCu\xc3\xa1l de los hermanos? (Orden en que naci\xc3\xb3)')),
                ('transtorno', models.CharField(blank=True, max_length=50, verbose_name=b'Qu\xc3\xa9 transtorno?')),
                ('alteracion_desarrollo', models.NullBooleanField(verbose_name=b'\xc2\xbfHa existido alg\xc3\xban tipo de alteraci\xc3\xb3n en su desarrollo?')),
                ('tipo_enfermedad_parientes', models.CharField(blank=True, max_length=256, verbose_name=b'Detallar el tipo de enfermedad que se ha presentado en los parientes')),
                ('orientacion_a_institucion', models.CharField(max_length=100, verbose_name=b'Qui\xc3\xa9n los orient\xc3\xb3 a \xc3\xa9sta instituci\xc3\xb3n?')),
            ],
        ),
        migrations.CreateModel(
            name='Descripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preocupacion', models.CharField(max_length=500, verbose_name=b'\xc2\xbfQu\xc3\xa9 le preocupa de su hijo? Algo especial que le llame la atenci\xc3\xb3n')),
                ('disc_molestias', models.CharField(blank=True, max_length=256, verbose_name=b'\xc2\xbfQui\xc3\xa9n descubri\xc3\xb3 estas molestias?')),
                ('edad_disc_molestia', models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfA qu\xc3\xa9 edad notaron estas molestias?')),
                ('tratamiento', models.BooleanField(verbose_name=b'\xc2\xbfSe encuentra en alg\xc3\xban tratamiento?')),
                ('lugar_tratamiento', models.CharField(blank=True, max_length=256, verbose_name=b'\xc2\xbfD\xc3\xb3nde realiza el tratamiento?')),
                ('limitaciones_movimiento', models.IntegerField(choices=[(1, b'SI'), (2, b'NO'), (3, b'DESCONOCE')], verbose_name=b'\xc2\xbfExiste alguna limitaci\xc3\xb3n con sus movimientos?')),
                ('areas_dificultad', models.CharField(blank=True, max_length=256, verbose_name=b'\xc2\xbfHa presentado su hijo(a) alg\xc3\xban tipo de dificultad en \xc3\xa9stas \xc3\xa1reas?')),
                ('had_convulsion', models.SmallIntegerField(choices=[(1, b'SI'), (2, b'NO'), (3, b'DESCONOCE')], verbose_name=b'\xc2\xbfHa sentido convulsiones?')),
                ('tipo_crisis', models.CharField(blank=True, max_length=256, verbose_name=b'\xc2\xbfQu\xc3\xa9 tipo de crisis tuvo durante la convulsi\xc3\xb3n?')),
                ('edad_crisis', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'\xc2\xbfA qu\xc3\xa9 edad fue la primera crisis?')),
            ],
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentesco', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=256)),
                ('apellidos', models.CharField(max_length=256)),
                ('nivel_estudio', models.PositiveSmallIntegerField(choices=[(0, b'Primaria'), (1, b'Secundaria'), (2, b'Universidad'), (3, b'Superior')], verbose_name=b'nivel de estudio')),
                ('direccion', models.CharField(max_length=256, verbose_name=b'direcci\xc3\xb3n')),
                ('telefonos', models.CharField(max_length=50, verbose_name=b'tel\xc3\xa9fono')),
                ('empresa', models.CharField(blank=True, max_length=256, verbose_name=b'lugar de trabajo')),
                ('direccion_empresa', models.CharField(blank=True, max_length=256, verbose_name=b'direcci\xc3\xb3n de empresa')),
                ('jornada', models.PositiveSmallIntegerField(choices=[(0, b'No Trabaja'), (1, b'Tiempo completo'), (2, b'Medio tiempo'), (3, b'Por horas')], verbose_name=b'jornada de trabajo')),
            ],
        ),
        migrations.CreateModel(
            name='Gestacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentimientos', models.CharField(blank=True, max_length=200, verbose_name=b'\xc2\xbfQu\xc3\xa9 sinti\xc3\xb3 cuando se enter\xc3\xb3 que estaba embarazada? Marque todas las opciones que desee')),
                ('num_embarazo', models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfQu\xc3\xa9 n\xc3\xbamero de embarazo es este?')),
                ('momento_desc_embarazo', models.CharField(max_length=250, verbose_name=b'\xc2\xbfEn qu\xc3\xa9 momento se enter\xc3\xb3 que estaba embarazada?')),
                ('lugar_curso_prenatal', models.CharField(blank=True, max_length=100, verbose_name=b'\xc2\xbfEn qu\xc3\xa9 lugar fue el curso prenatal?')),
                ('carga_horaria', models.CharField(blank=True, max_length=100, verbose_name=b'\xc2\xbfCu\xc3\xa1nta fue la carga del curso prenatal?')),
                ('vacuna_tetano', models.BooleanField(verbose_name=b'\xc2\xbfSe vacun\xc3\xb3 usted contra el t\xc3\xa9tano durante el embarazo?')),
                ('comunicacion_bebe', models.CharField(max_length=500, verbose_name=b'\xc2\xbfC\xc3\xb3mo se comunicaba con el bebe? Marque todas las opciones que desee.')),
            ],
        ),
        migrations.CreateModel(
            name='Hermano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(verbose_name=b'Fecha de nacimiento')),
                ('datos_familiares', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hermanos_set', to='registro.DatosFamiliaresOtros')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialMadre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enfermedades_previas', models.CharField(blank=True, max_length=200, verbose_name=b'Indique si antes del embarazo ha sufrido algunas de las siguientes enfermedades')),
                ('enfermedades_durante_embarazo', models.CharField(blank=True, max_length=256, verbose_name=b'Indique si durante el embarazo sufri\xc3\xb3 algunas de las siguientes enfermedades')),
                ('enfermedad_cronica', models.CharField(blank=True, max_length=100, verbose_name=b'Indique alg\xc3\xban tipo de enfermedad cr\xc3\xb3nica')),
                ('defunciones_fetales', models.PositiveSmallIntegerField(default=0, verbose_name=b'\xc2\xbfCu\xc3\xa1ntas defunciones fetales ha tenido durante su vida?')),
                ('hijos_nacidos_muertos', models.PositiveSmallIntegerField(default=0, verbose_name=b'N\xc3\xbamero de hijos nacidos muertos')),
                ('hijos_nacidos_vivos', models.PositiveSmallIntegerField(default=0, verbose_name=b'N\xc3\xbamero de hijos nacidos vivos')),
                ('embarazos', models.PositiveSmallIntegerField(default=1, verbose_name=b'n\xc3\xbamero de embarazos')),
                ('anticonceptivos', models.CharField(blank=True, max_length=100)),
                ('enfermedades_antes_concepcion', models.CharField(blank=True, max_length=256, verbose_name=b'\xc2\xbfTuvo usted alguna enfermedad grave, dolencia, accidente o infecci\xc3\xb3n, antes de concebir a \xc3\xa9ste beb\xc3\xa9?')),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name=b'nombre del medicamento')),
                ('dosis_diaria', models.IntegerField()),
                ('descripcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicamentos', to='registro.Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=256)),
                ('apellidos', models.CharField(max_length=256)),
                ('direccion', models.CharField(max_length=256)),
                ('telefonos', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Nacimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_lugar_nacimiento', models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfD\xc3\xb3nde ocurri\xc3\xb3 el nacimiento?')),
                ('nombre_lugar_nacimiento', models.CharField(blank=True, max_length=500, verbose_name=b'Nombre de instituci\xc3\xb3n')),
                ('semana_gestacion', models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfEn qu\xc3\xa9 semana de gestaci\xc3\xb3n naci\xc3\xb3 el beb\xc3\xa9?')),
                ('metodo_nacimiento', models.CharField(max_length=100, verbose_name=b'\xc2\xbfC\xc3\xb3mo naci\xc3\xb3n el beb\xc3\xa9? Marque todas las opciones que necesite')),
                ('manera_inicio_parto', models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfCu\xc3\xa1l fue la manera en que inici\xc3\xb3 su labor de parto?')),
                ('tipo_ruptura_fuente', models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfC\xc3\xb3mo fue la ruptura del agua fuente?')),
                ('sentimientos_parto', models.CharField(max_length=500, verbose_name=b'\xc2\xbfC\xc3\xb3mo se sinti\xc3\xb3 durante su labor de parto?')),
                ('sentimientos_nacimiento', models.CharField(max_length=500, verbose_name=b'\xc2\xbfC\xc3\xb3mo se sinti\xc3\xb3 durante el nacimiento de su hijo?')),
                ('duracion_nacimiento', models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfCu\xc3\xa1nto fue la duraci\xc3\xb3n del nacimiento? (Horas/minutos)')),
                ('gemelar', models.BooleanField(verbose_name=b'\xc2\xbfFue embarazo gemelar?')),
                ('primera_parte_cuerpo', models.PositiveSmallIntegerField(verbose_name=b'Seleccione qu\xc3\xa9 parte del cuerpo sali\xc3\xb3 primero')),
                ('complicaciones', models.CharField(blank=True, max_length=200, verbose_name=b'\xc2\xbfTuvo usted complicaciones?')),
                ('medicamentos_parto', models.NullBooleanField(verbose_name=b'\xc2\xbfSe le administraron medicamentos o inyecci\xc3\xb3n durante el embarazo?')),
                ('complicaciones_cordon', models.NullBooleanField(verbose_name=b'\xc2\xbfHubieron complicaciones con el cord\xc3\xb3n umbilical?')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=256)),
                ('apellidos', models.CharField(max_length=256)),
                ('lugar_nacimiento', models.CharField(max_length=30, verbose_name='lugar de nacimiento')),
                ('fecha_nacimiento', models.DateField(verbose_name='fecha de nacimiento')),
                ('fecha_registro', models.DateField(auto_now_add=True, verbose_name='fecha de registro')),
                ('nacionalidad', models.CharField(max_length=30)),
                ('grupo_sanguineo', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('O+', 'O+'), ('O-', 'O-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], default='O+', max_length=4, verbose_name='grupo sanguineo')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='--', max_length=1)),
                ('alimentacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.AlimentacionCostumbres')),
                ('datos_familiares', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.DatosFamiliaresOtros')),
                ('descripcion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.Descripcion')),
                ('gestacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.Gestacion')),
                ('historial_madre', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.HistorialMadre')),
                ('nacimiento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.Nacimiento')),
            ],
        ),
        migrations.CreateModel(
            name='PrimerosDias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinica_permanencia', models.CharField(blank=True, max_length=100, verbose_name=b'\xc2\xbfCu\xc3\xa1l fue la cl\xc3\xadnica u hospital en la que permaneci\xc3\xb3 el ni\xc3\xb1o(a)?')),
                ('dias_permanencia', models.PositiveIntegerField(blank=True, null=True, verbose_name=b'Indique los d\xc3\xadas de permanencia')),
                ('situaciones_despues_nacimiento', models.CharField(blank=True, max_length=256, verbose_name=b'\xc2\xbfPresent\xc3\xb3 su beb\xc3\xa9 alguna de \xc3\xa9stas situaciones despu\xc3\xa9s del nacimiento?')),
                ('icteria', models.NullBooleanField(verbose_name=b'\xc2\xbfHubo alg\xc3\xban tratamiento por icteria')),
                ('tratamiento_icteria', models.CharField(blank=True, max_length=256, verbose_name=b'\xc2\xbfCu\xc3\xa1l fue el tratamiento por icteria?')),
                ('examenes', models.CharField(blank=True, max_length=100, verbose_name=b'\xc2\xbfLe realizaron al reci\xc3\xa9n nacido alg\xc3\xban tipo de ex\xc3\xa1men?')),
                ('veces_despertar_noche', models.PositiveSmallIntegerField(default=0, verbose_name=b'\xc2\xbfCu\xc3\xa1ntas veces se despertaba el reci\xc3\xa9n nacido?')),
                ('lugar_dormir', models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfD\xc3\xb3nde dorm\xc3\xada el beb\xc3\xa9?')),
                ('descripcion_bebe', models.CharField(max_length=256, verbose_name=b'Describa a su beb\xc3\xa9 los 3 primeros meses de vida')),
                ('descripcion_madre', models.CharField(max_length=256, verbose_name=b'\xc2\xbfC\xc3\xb3mo se sent\xc3\xada usted esos 3 primeros meses?')),
            ],
        ),
        migrations.CreateModel(
            name='RecienNacido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad_madre', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Edad de la madre cuando naci\xc3\xb3 el beb\xc3\xa9')),
                ('edad_padre', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Edad del padre cuando naci\xc3\xb3 el beb\xc3\xa9')),
                ('peso', models.FloatField(verbose_name=b'peso(gr)')),
                ('tamanio', models.FloatField(verbose_name=b'tama\xc3\xb1o(cm)')),
                ('diametro_encefalico', models.FloatField(verbose_name=b'di\xc3\xa1metro encef\xc3\xa1lico(cm)')),
                ('apgar_score', models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfCu\xc3\xa1l fue la puntuaci\xc3\xb3n del apgar? Si no lo sabe podr\xc3\xada ayudarnos con la historia cl\xc3\xadnica de su hijo(a)')),
                ('complicaciones_nacimiento', models.CharField(blank=True, max_length=256, verbose_name=b'\xc2\xbfEl ni\xc3\xb1o(a) tuvo alguna de \xc3\xa9stas complicaciones al nacer?')),
                ('tiempo_apego_precoz', models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfCu\xc3\xa1nto tiempo dur\xc3\xb3 el apego precoz?')),
                ('tiempo_sostener_bebe', models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfCu\xc3\xa1nto tiempo pas\xc3\xb3 hasta que usted pudo sostener a su beb\xc3\xa9?')),
                ('tiempo_internado', models.DurationField(blank=True, default=datetime.timedelta(0), verbose_name=b'\xc2\xbfCu\xc3\xa1nto tiempo permaneci\xc3\xb3 internado(a)?')),
                ('tipo_contacto', models.PositiveSmallIntegerField(blank=True, verbose_name=b'\xc2\xbfQu\xc3\xa9 tipo de contacto tuvo con su beb\xc3\xa9 mientras estuvo internado?')),
                ('primera_lactancia', models.PositiveSmallIntegerField(verbose_name=b'La primera vez que el beb\xc3\xa9 tom\xc3\xb3 leche fue con')),
            ],
        ),
        migrations.CreateModel(
            name='Situacion_Gestacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.SmallIntegerField(choices=[(1, b'1er Trimestre'), (2, b'2do Trimestre'), (3, b'3er Trimestre')])),
                ('nombre_situacion', models.CharField(blank=True, max_length=100)),
                ('gestacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Gestacion')),
            ],
        ),
        migrations.CreateModel(
            name='SuplementoAlimenticio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frecuencia', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('cantidad', models.PositiveSmallIntegerField()),
                ('alimentacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suplementos', to='registro.AlimentacionCostumbres')),
            ],
        ),
        migrations.CreateModel(
            name='Terapia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.SmallIntegerField(choices=[(1, b'Rehabilitaci\xc3\xb3n F\xc3\xadsica'), (2, b'Estimulaci\xc3\xb3n Temprana'), (3, b'Ninguna')], verbose_name=b'Tipo de terapia')),
                ('tiempo_terapia', models.CharField(max_length=50, verbose_name=b'\xc2\xbfCu\xc3\xa1nto tiempo lleva realizando la terapia')),
                ('descripcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terapias', to='registro.Descripcion')),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='primeros_dias',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.PrimerosDias'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='recien_nacido',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.RecienNacido'),
        ),
        migrations.AddField(
            model_name='medico',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Paciente'),
        ),
        migrations.AddField(
            model_name='familiar',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Paciente'),
        ),
        migrations.AddField(
            model_name='actividad_gestacion',
            name='gestacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Gestacion'),
        ),
    ]