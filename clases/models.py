from django.db import models

class ClaseKitesurf(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Escuela de Entrenamiento Kitesurf")
    descripcion = models.TextField(verbose_name="La pasión por el kitesurf no se explica, se vive. En nuestra escuela, este deporte es parte de nuestra identidad familiar desde hace años. Diego, instructor con años de trayectoria, combina el conocimiento técnico profundo con la experiencia de quien ha dedicado su vida a entender el viento y el agua. No te enseñamos solo a navegar; te transmitimos el respeto por el mar, la seguridad necesaria para disfrutar cada sesión y la técnica precisa para progresar con confianza. Somos una familia apasionada compartiendo lo que amamos, con todo el equipamiento profesional necesario para que tu aprendizaje sea seguro, constante y, sobre todo, inolvidable.")
    duracion_horas = models.IntegerField(verbose_name="Duración 3 horas, 1:30 teorico/practiro y otra 1:30 pero todo practico  ")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio 200.000")
    imagen = models.ImageField(upload_to='clases_fotos/', blank=True, null=True, verbose_name="Foto del Curso")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Clase de Kitesurf"
        verbose_name_plural = "Clases de Kitesurf"
    
    