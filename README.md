## Создание виртуального окружения

```shell
python3 -m venv venv
```

## Установка зависимостей

Необходимо войти в виртуальное окружение (зависит от платформы) и выполнить

```shell
pip3 install -r requirements.txt   
```

для установки продуктового окружения или

```shell
pip3 install -r dev_requirements.txt   
```

для установки окружения для разработки.

Отличаются они тем, что в окружении для разработки есть линтер `pylint`, `snakeviz` для визуализации измерений
профайлера, `twine` для создания и обновления пакета

## Создание пакета и публикация в pypi-test

Создаём пакет

```shell
python3 -m build
```

Загружаем в pypi-test

```shell
twine upload -r testpypi dist/*
```

Получаем ссылку
[https://test.pypi.org/project/homework-test-package-2/1.0/](https://test.pypi.org/project/homework-test-package-2/1.0/)

## Установка пакета

```shell
pip3 install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple homework-test-package-2==1.0
```

Объясню зачем здесь `--extra-index-url`: мне уже приходилось устанавливать пакет из pypi-test и вот оказывается, что
если сделать просто `pip install -i https://test.pypi.org/simple/ homework-test-package-2==1.0`, то зависимости устанавливаемого
пакета будут также тянутся из pypi-test, что плохо -- там нет некоторых распространённых пакетов, соответственно установка
может завершиться неудачно. Поэтому командой приведённой выше мы устанавливаем наш пакет из pypi-test, а его зависимости из
дефолтного pypi.