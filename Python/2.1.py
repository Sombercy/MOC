import pandas as pd
#frame = pd.DataFrame({"numbers":range(10),'chars':['a']*10 })
frame = pd.read_csv("dataset.tsv", '\t', header=0)
print(frame)
new_line = {'Name':'Petrov', 'Birth':'22.03.1990','City':'Penza'}
frame.append(new_line,True) # не изменяет саму таблицу, а лишь возвращает модифицированную ее копию
frame = frame.append(new_line,True) # изменяет
frame['IsStudent'] = [False]*5 + [True]*2 # создает новый столбец
frame.drop([5,6], axis=0) # удаляем последние 2 строчки, нулевая ось, копия
frame.drop([5,6],inplace=True) # изменяем сам фрейм
frame.drop('IsStudent',1,inplace=True) # удаляем недавно созданный столбик
frame.to_csv('updated_dataset.csv',header=True, index=None)

frame.dtypes # выводит типы данных
frame.Birth = frame.Birth.apply(pd.to_datetime) # меняем тип данных столбца 'Birth'
frame.info() # общая информация о таблице
frame.fillna('разнорабочий', inplace=True) # заменяем все пропуски в данных на 'разнорабочий'
print(frame.Possition) # выводит содержимое столбца
print(frame[['Possition']]) # выводит содержимое столбца в виде таблицы
frame.head(3) # выводит первые 3 строки
frame[:3] # аналогично
frame[-3:] # выводит последние 3 строки
print (frame.loc[[1,3,5], ['Name', 'City']]) # выводит 1, 3 и 5 строки по столбцам 'Name' и 'City'
# iloc - обращение по номерам, ix - поддерживает обращение и по имени, и по номерам
frame[frame.Birth >= pd.datetime(1985, 1, 1)] # фильтрует по дате рождения

