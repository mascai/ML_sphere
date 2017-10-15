#35

import codecs

# объявим где хранятся исходные данные
PATH_TRAIN = '../input/train.csv'
PATH_TRAIN = 'C:\\ML\\hw\\1\\data\\train.csv'
PATH_TEST = 'C:\\ML\\hw\\1\\data\\test.csv'
# объявим куда сохраним результат
PATH_PRED = 'pred.csv'


## Из тренировочного набора собираем статистику о встречаемости слов

# создаем словарь для хранения статистики
word_stat_dict = {}
word_stat_dict3 = {}
word_stat_dict4 = {}
word_stat_dict5 = {}
# открываем файл на чтение в режиме текста
fl = codecs.open(PATH_TRAIN, 'r', encoding='utf-8')

# считываем первую строчку - заголовок (она нам не нужна)
fl.readline()

# в цикле читаем строчки из файла
for line in fl:
    # разбиваем строчку на три строковые переменные
    Id, Sample, Prediction = line.strip().split(',')
    # строковая переменная Prediction - содержит в себе словосочетание из 2 слов, разделим их
    word1, word2 = Prediction.split(' ')
    # возьмем в качестве ключа 2 первые буквы, т.к. их наличие гарантировано
    #mycode
    if len(word2) > 4:
        key = word2[:5]
        # если такого ключа еще нет в словаре, то создадим пустой словарь для этого ключа
        if key not in word_stat_dict5:
            word_stat_dict5[key] = {}
        # если текущее слово еще не встречалось, то добавим его в словарь и установим счетчик этого слова в 0
        if word2 not in word_stat_dict5[key]:
            word_stat_dict5[key][word2] = 0
        # увеличим значение счетчика по текущему слову на 1
        word_stat_dict5[key][word2] += 1
    if len(word2) > 3:
        key = word2[:4]
        # если такого ключа еще нет в словаре, то создадим пустой словарь для этого ключа
        if key not in word_stat_dict4:
            word_stat_dict4[key] = {}
        # если текущее слово еще не встречалось, то добавим его в словарь и установим счетчик этого слова в 0
        if word2 not in word_stat_dict4[key]:
            word_stat_dict4[key][word2] = 0
        # увеличим значение счетчика по текущему слову на 1
        word_stat_dict4[key][word2] += 1
    if len(word2) > 2:
        key = word2[:3]
        if key not in word_stat_dict3:
            word_stat_dict3[key] = {}
        # если текущее слово еще не встречалось, то добавим его в словарь и установим счетчик этого слова в 0
        if word2 not in word_stat_dict3[key]:
            word_stat_dict3[key][word2] = 0
        # увеличим значение счетчика по текущему слову на 1
        word_stat_dict3[key][word2] += 1

    #</mycode
    key = word2[:2]
    # если такого ключа еще нет в словаре, то создадим пустой словарь для этого ключа
    if key not in word_stat_dict:
        word_stat_dict[key] = {}
    # если текущее слово еще не встречалось, то добавим его в словарь и установим счетчик этого слова в 0
    if word2 not in word_stat_dict[key]:
        word_stat_dict[key][word2] = 0
    # увеличим значение счетчика по текущему слову на 1
    word_stat_dict[key][word2] += 1

# закрываем файл
fl.close()

## Строим модель

# создаем словарь для хранения статистики
most_freq_dict = {}
most_freq_dict3 = {}
most_freq_dict4 = {}
most_freq_dict5 = {}
# проходим по словарю word_stat_dict

#mycode
for key in word_stat_dict5:
    # для каждого ключа получаем наиболее часто встречающееся (наиболее вероятное) слово и записываем его в словарь most_freq_dict
    most_freq_dict5[key] = max(word_stat_dict5[key], key=word_stat_dict5[key].get)
for key in word_stat_dict4:
    # для каждого ключа получаем наиболее часто встречающееся (наиболее вероятное) слово и записываем его в словарь most_freq_dict
    most_freq_dict4[key] = max(word_stat_dict4[key], key=word_stat_dict4[key].get)
for key in word_stat_dict3:
    # для каждого ключа получаем наиболее часто встречающееся (наиболее вероятное) слово и записываем его в словарь most_freq_dict
    most_freq_dict3[key] = max(word_stat_dict3[key], key=word_stat_dict3[key].get)
# </mycode
for key in word_stat_dict:
    # для каждого ключа получаем наиболее часто встречающееся (наиболее вероятное) слово и записываем его в словарь most_freq_dict
    most_freq_dict[key] = max(word_stat_dict[key], key=word_stat_dict[key].get)


## Выполняем предсказание

# открываем файл на чтение в режиме текста
fl = open(PATH_TEST, 'r', encoding='utf-8')

# считываем первую строчку - заголовок (она нам не нужна)
fl.readline()

# открываем файл на запись в режиме текста
out_fl = open(PATH_PRED, 'w', encoding='utf-8')

# записываем заголовок таблицы
out_fl.write('Id,Prediction\n')

# в цикле читаем строчки из тестового файла
for line in fl:
    # разбиваем строчку на две строковые переменные
    Id, Sample = line.strip().split(',')
    # строковая переменная Sample содержит в себе полностью первое слово и кусок второго слова, разделим их
    word1, word2_chunk = Sample.split(' ')
    # вычислим ключ для заданного фрагмента второго слова
    #mycode
    if len(word2) > 4:
        key = word2_chunk[:5]
        if key in most_freq_dict5:
            # если ключ есть в нашем словаре, пишем в файл предсказаний: Id, первое слово, наиболее вероятное второе слово
            out_fl.write('%s,%s %s\n' % (Id, word1, most_freq_dict5[key]))
            continue
    if len(word2) > 3:
        key = word2_chunk[:4]
        if key in most_freq_dict4:
            # если ключ есть в нашем словаре, пишем в файл предсказаний: Id, первое слово, наиболее вероятное второе слово
            out_fl.write('%s,%s %s\n' % (Id, word1, most_freq_dict4[key]))
            continue
    if len(word2) > 2:
        key = word2_chunk[:3]
        if key in most_freq_dict3:
            # если ключ есть в нашем словаре, пишем в файл предсказаний: Id, первое слово, наиболее вероятное второе слово
            out_fl.write('%s,%s %s\n' % (Id, word1, most_freq_dict3[key]))
            continue

    #</mycode
    key = word2_chunk[:2]
    if key in most_freq_dict:
        # если ключ есть в нашем словаре, пишем в файл предсказаний: Id, первое слово, наиболее вероятное второе слово
        out_fl.write('%s,%s %s\n' % (Id, word1, most_freq_dict[key]) )
    else:
        # иначе пишем наиболее часто встречающееся словосочетание в целом
        out_fl.write('%s,%s\n' % (Id, 'что она') )

# закрываем файлы
fl.close()
out_fl.close()
