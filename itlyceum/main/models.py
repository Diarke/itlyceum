from django.db import models

# Модель для слайдера (Swiper)
class Slider(models.Model):
    image = models.ImageField(upload_to='slider_images/', blank=True, null=True)
    main_title = models.CharField(max_length=200, verbose_name="Основной заголовок")
    subtitle = models.CharField(max_length=200, verbose_name="Подзаголовок")
    description = models.CharField(max_length=200, verbose_name="Описание")
    button_text = models.CharField(max_length=100, verbose_name="Текст кнопки")
    button_url = models.URLField(blank=True, null=True, verbose_name="Ссылка кнопки")

    def __str__(self):
        return self.main_title

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"

# Модель для объявлений (Announcements)
class Announcement(models.Model):
    image = models.ImageField(upload_to='announcement_images/', blank=True, null=True)
    image1 = models.ImageField(upload_to='announcement_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='announcement_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='announcement_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='announcement_images/', blank=True, null=True)
    image5 = models.ImageField(upload_to='announcement_images/', blank=True, null=True)
    image6 = models.ImageField(upload_to='announcement_images/', blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Краткое описание")
    full_description = models.TextField(blank=True, verbose_name="Полное описание")
    button_text = models.CharField(max_length=100, default="Толығырақ", verbose_name="Текст кнопки")
    button_url = models.URLField(blank=True, null=True, verbose_name="Ссылка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

# Модель для блока "Біз туралы" (About Us)
class AboutUs(models.Model):
    image = models.ImageField(upload_to='about_us_images/', blank=True, null=True)
    image1 = models.ImageField(upload_to='about_us_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='about_us_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='about_us_images/', blank=True, null=True)
    title = models.CharField(max_length=200, default="Біз туралы", verbose_name="Заголовок")
    subtitle = models.CharField(max_length=300, verbose_name="Подзаголовок")
    description = models.TextField(verbose_name="Краткое описание")
    full_description = models.TextField(blank=True, verbose_name="Полное описание")
    button_text = models.CharField(max_length=100, default="Толығырақ хабарлығы", verbose_name="Текст кнопки")
    button_url = models.URLField(blank=True, null=True, verbose_name="Ссылка кнопки")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

# Модель для блока "IT бағыты" (IT Direction)
class ITDirection(models.Model):
    title = models.CharField(max_length=200, default="IT бағыты", verbose_name="Заголовок")
    subtitle = models.CharField(max_length=200, verbose_name="Подзаголовок")
    description = models.TextField(verbose_name="Краткое описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "IT направление"
        verbose_name_plural = "IT направления"

# Модель для IT курсов (IT Courses)
class ITCourse(models.Model):
    image = models.ImageField(upload_to='it_course_images/', blank=True, null=True)
    image1 = models.ImageField(upload_to='it_course_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='it_course_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='it_course_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='it_course_images/', blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name="Название курса")
    description = models.TextField(verbose_name="Краткое описание")
    full_description = models.TextField(blank=True, verbose_name="Полное описание")
    button_text = models.CharField(max_length=100, default="Толығырақ", verbose_name="Текст кнопки")
    button_url = models.URLField(blank=True, null=True, verbose_name="Ссылка")
    technologies = models.ManyToManyField('Technology', verbose_name="Технологии")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "IT курс"
        verbose_name_plural = "IT курсы"

# Модель для технологий в IT курсах
class Technology(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название технологии")
    css_class = models.CharField(max_length=50, verbose_name="CSS класс", help_text="Например, 'html', 'css', 'python'")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Технология"
        verbose_name_plural = "Технологии"

# Модель для клубов (Clubs)
class Club(models.Model):
    image = models.ImageField(upload_to='club_images/', blank=True, null=True)
    image1 = models.ImageField(upload_to='club_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='club_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='club_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='club_images/', blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name="Название клуба")
    description = models.TextField(verbose_name="Краткое описание")
    full_description = models.TextField(blank=True, verbose_name="Полное описание")
    button_text = models.CharField(max_length=100, default="Толығырақ", verbose_name="Текст кнопки")
    button_url = models.URLField(blank=True, null=True, verbose_name="Ссылка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Клуб"
        verbose_name_plural = "Клубы"

# Модель для системы управления (Management System)
class ManagementMember(models.Model):
    image = models.ImageField(upload_to='management_images/', blank=True, null=True)
    image1 = models.ImageField(upload_to='management_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='management_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='management_images/', blank=True, null=True)
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    position = models.CharField(max_length=200, verbose_name="Должность")
    description = models.TextField(verbose_name="Краткое описание")
    full_description = models.TextField(blank=True, verbose_name="Полное описание")

    def __str__(self):
        return f"{self.full_name} - {self.position}"

    class Meta:
        verbose_name = "Член управления"
        verbose_name_plural = "Члены управления"

# Модель для блока "Байланыс" (Contact)
class Contact(models.Model):
    address = models.CharField(max_length=300, verbose_name="Адрес")
    working_hours = models.CharField(blank=True, null=True, max_length=200, verbose_name="Часы работы")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    instagram_url = models.URLField(blank=True, null=True, verbose_name="Instagram")
    telegram_url = models.URLField(blank=True, null=True, verbose_name="Telegram")
    whatsapp_url = models.URLField(blank=True, null=True, verbose_name="WhatsApp")
    map_iframe = models.TextField(verbose_name="Iframe код карты")

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

# Модель для футера (Footer)
class Footer(models.Model):
    copyright_text = models.CharField(max_length=200, verbose_name="Текст копирайта")

    def __str__(self):
        return self.copyright_text

    class Meta:
        verbose_name = "Футер"
        verbose_name_plural = "Футеры"