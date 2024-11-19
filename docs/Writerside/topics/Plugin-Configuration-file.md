# Plugin Configuration file

Конфигурационный файл **config.py** содрежит всю информацию о плагине. Разделы ниже описывают все элементы конфигурации подробнее.

## Введение
Конфигурация плагина S3 Platform - это базовый объект [PluginConfig](../src/s3p_sdk/plugin/config/__init__.py?plain=24).

Все объекты, включая `PluginConfig`, наследуются от абстрактного класса [AbcObject](../src/s3p_sdk/plugin/config/abc_object.py).

Главный метод всех объектов конфигурации `dict() -> dict`, который генерирует словарь определенной структуры каждого объекта.

## Структура плагина
Основной объект конфигурации [PluginConfig](../src/s3p_sdk/plugin/config/__init__.py?plain=24) содержит 4 свойства:
- [plugin](#свойство-coreconfigplugin)
- [task](#свойство-taskconfigtask)
- [middleware](#свойство-middlewareconfigmiddleware)
- [payload](#свойство-payloadconfigpaylad)

### Свойство CoreConfig(plugin)
Основные свойства плагина определяются в объекте [CoreConfig](../src/s3p_sdk/plugin/config/coreconfig.py):
- `reference`: **string** - уникальное название сущности, к которой относится плагин (уникальное имя источника).
- `type`: **string** - тип источника, который обрабатываем плагин ([подробнее](#тип-плагина)).
- `files`: **list[string]** - список файлов, которые необходимы для работы плагина (они будут сохранены в архив).
- `is_localstorage`: **boolean** - флаг определяет параметр: нужно ли плагину при работе локальное хранилище (локальный каталог этого плагина). Локальное хранилище может понадобиться в ситуациях, когда есть необходимость сохранить или скачать файл для обработки источника, но его не получается получить в байтовом формате.

#### Тип плагина
Типы плагинов определены [здесь](../src/s3p_sdk/plugin/config/type.py).
Типы плагина:
- `SOURCE` - плагин, который собирает информацию источника (плагин-источник)
- `ML` - плагин, который занимается обработкой (плагин-обработчик)

### Свойство TaskConfig(task)
Свойства задачи определяются в объекте [TaskConfig](../src/s3p_sdk/plugin/config/taskconfig.py), в рамках которой исполняется логика плагина.
- `trigger`: [**TriggerConfig**](#объект-triggerconfig)

#### Объект TriggerConfig
Объект TriggerConfig расположен [здесь](../src/s3p_sdk/plugin/config/trigger.py). Он обладает следующими свойствами:
- `type`: **string** - [тип триггера](#тип-триггера)
- `interval`: **timedelta** - Python timedelta тип, определяющий интервал

##### Тип триггера
Тип триггера определен [здесь](../src/s3p_sdk/plugin/config/trigger.py).
- `SCHEDULE` - означает тип триггера, срабатывающий по расписанию.

### Свойство MiddlewareConfig(middleware)
Свойства постобработки определяются в объекте [MiddlewareConfig](../src/s3p_sdk/plugin/config/middlewareconfig.py). Это тот путь, который должен пройти материал, после того, как он будет получен платформой. Для этого нужно указать последовательность модулей **обработки**:
- `modules`: list[[AbcModuleConfig](#объект-модуля-постобработки)] - список определяет последовательность модулей постобработки, которые запускаются по очереди и исполняют свою логику.

#### Объект модуля постобработки
Все объекты модулей постобработки наследуются от [абстрактного класса модуля](../src/s3p_sdk/plugin/config/modules/abc_module.py).

Базовые свойство модуля определенны в абстрактном классе:
- `order`: **integer** - номер последовательности запуска модуля
- `name`: **string** - уникальное имя модуля
- `is_critical`: **boolean** - параметр критичности модуля, означает: можно ли продолжать обработку другими модулями, если этот модуль завершил работу с ошибкой. TRUE - нельзя (критично), FALSE - можно (некритично).
- `parameters`: **dict** - словарь параметров, которые необходимы модулю для работы.

### Свойство PayloadConfig(payload)
Свойства запуска логики определены в объекте [PayloadConfig](../src/s3p_sdk/plugin/config/payload/__init__.py?plain=10):
- `file`: string - название python файла (название этого файла должно быть указано в свойстве [files](#свойство-coreconfigplugin)).
- `classname`: string - название основного python класса логики в файле.
- `entry`: [EntryConfig](#свойства-начальных-параметров) -

#### Свойства начальных параметров
Свойства начальных параметров логики плагина определяются в объекте [EntryConfig](../src/s3p_sdk/plugin/config/payload/entry/__init__.py):
- `method`: string - название метода класса, который вызовет S3 Platform для получения материалов.
- `params`: list[[AbcParamConfig](#свойства-объекта-начальных-параметров)] - список начальных параметров

#### Свойства объекта начальных параметров
Все объекты начальных параметров наследуются от [абстрактного класса параметра](../src/s3p_sdk/plugin/config/payload/entry/abc_param.py).

Начальный параметр - это тот параметр, который необходимо передать в конструктор класса логики (парсера). На примере, имеем класс `MyParser`.

```python
from s3p_sdk.types import S3PRefer, S3PDocument
from selenium.webdriver.chrome.webdriver import WebDriver

class MyParser:
    def __init__(self, refer: S3PRefer, web_driver: WebDriver, url: str, max_count_documents: int = None, last_document: S3PDocument = None):
        super().__init__(refer, max_count_documents, last_document)
        
        # Other code
        ...
```
В конструктор передаются параметры обязательные и необязательные. Обязательные параметры необходимы для работы базового класса логики плагина. Обязательные параметры передаются платформой и не требуют действий разработчика:
- `refer: S3PRefer` - объект источника

Необязательные параметры нужны для параметризации логики плагина. Плагин должен быть настраиваемым и любая логика, которая подразумевает использование какой-нибудь переменной или константы должна быть получена из начального параметра.

Платформенные необязательные параметры:
- `max_count_documents: int` - максимальное количество материалов, после сбора которых сборщик остановит свою работу (по умолчанию, None).
- `last_document: S3PDocument` - объект _последнего_ материала, который был получен плагином. Это нужно для остановки сборщика при совпадении полученного и последнего документа.

Пользовательские необязательные параметры - это те параметры, которые уникальны и нужны только в рамках конкретного плагина.


##### Базовые свойства начальных параметров
Базовые свойства параметра, определены в абстрактном классе:
- `key`: string - ключ параметра (должен совпадать с параметром инициализации класса).
- `typeof`: string - тип начального параметра.
- `value`: object - значение параметра.

##### Начальный параметр: константа
Объект начального параметра константы определен [здесь](../src/s3p_sdk/plugin/config/payload/entry/const_param_config.py).

[ConstParamConfig](../src/s3p_sdk/plugin/config/payload/entry/const_param_config.py) требует при инициализации следующие параметры:
- `key`
- `value`

Пример: константа, определяющая максимальное количество материалов.
```python
from s3p_sdk.plugin.config import payload

payload.entry.ConstParamConfig(key='max_count_documents', value=50)
```
После генерации словаря, получается следующее.
```json
{
  "key": "max_count_documents",
  "value": {
    "type": "const",
    "value": 50
  }
}
```

##### Начальный параметр: файл
Объект начального параметра файла определен [здесь](../src/s3p_sdk/plugin/config/payload/entry/file_param_config.py).

(#TODO)

##### Начальный параметр: модуль
Объект начального параметра модуля определен [здесь](../src/s3p_sdk/plugin/config/payload/entry/module_param_config.py).

[ModuleParamConfig](../src/s3p_sdk/plugin/config/payload/entry/module_param_config.py) требует при инициализации следующие параметры:
- `key`: string
- `module_name`: string - уникальное название модуля. Подробнее [тут](#модули-s3-platform).
- `bus`: boolean - параметр необходимости шины S3 Platform.

Пример: модуль WebDriver, передающийся в логику плагина для работы selenium.

```python
from s3p_sdk.plugin.config import payload
from s3p_sdk.module import WebDriver

payload.entry.ModuleParamConfig(key='driver', module_name=WebDriver, bus=True),
```
После генерации словаря, получается следующее.
```json
{
  "key": "driver",
  "value": {
    "type": "module",
    "name": "WebDriver",
    "bus": true
  }
}
```

## Модули S3 Platform
Уникальные имена модулей определены [здесь](../src/s3p_sdk/module/__init__.py).

- `WebDriver` - основной web-драйвер selenium, предназначенный для работы парсера.
- `TimezoneSafeControl` - модуль защищенного добавления UTC к полям даты и времени материала.
- `CutJunkCharactersFromDocumentText` - модуль очистки текстовых полей материала.
- `FilterOnlyNewDocumentWithDB` - модуль фильтрации новых материалов.
- `SaveDocumentToDB` - модуль сохранения материалов в базу данных S3 Platform.

