FROM php:8.2-apache
RUN apt-get update && apt-get install -y libpng-dev && docker-php-ext-install gd
COPY index.html img.php /var/www/html/