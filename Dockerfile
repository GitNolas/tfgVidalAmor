FROM php:7.3-apache
COPY tfgAPI/ /var/www/html/
RUN mkdir /var/www/tfgObtencionDatos/
COPY tfgObtencionDatos/ /var/www/tfgObtencionDatos/

RUN rm /etc/apache2/sites-available/000-default.conf
RUN rm /etc/apache2/sites-enabled/000-default.conf
RUN rm /etc/apache2/apache2.conf

COPY apache2.conf /etc/apache2/apache2.conf
#install some base extensions
RUN apt-get update
RUN apt-get install -y \
        libzip-dev \
        zip \
  && docker-php-ext-install zip pdo pdo_mysql

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid


RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN composer global require "laravel/lumen-installer"
RUN composer install --no-interaction --optimize-autoloader --no-scripts

ENV PATH=/var/www/html/vendor/bin:${PATH}

RUN a2enmod rewrite
RUN service apache2 restart


RUN apt-get install -y \
        python3 \
        python3-pip
RUN pip3 install scrapy

ENV PYTHONPATH=/var/www/tfgObtencionDatos/tfgObtencionDatos:${PYTHONPATH}
