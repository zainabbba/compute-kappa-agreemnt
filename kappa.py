

# import pandas lib as pd
import pandas as pd

# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('first-second.xlsx')

print(dataframe1)

first_annonter='احمد'

second_annonter='يارا'

counterneutral=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]=="خبر محايد"  and row[second_annonter]=="خبر محايد"  ):
        counterneutral+=1


print('counterneutral', counterneutral)

counterPoisitive=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]=="خبر إيجابي"  and row[second_annonter]=="خبر إيجابي"  ):
        counterPoisitive+=1
 
print('counterPoisitive', counterPoisitive)


counterNegative=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]==" خبر سلبي"  and row[second_annonter]==" خبر سلبي"  ):
        counterNegative+=1

print('counterNegative',counterNegative)



# .................

counter_neutral_positive=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]=="خبر محايد"  and row[second_annonter]=="خبر إيجابي"  ):
        counter_neutral_positive+=1

print('counter_neutral_positive',counter_neutral_positive)


counter_positive_neutral=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]=="خبر إيجابي"  and row[second_annonter]=="خبر محايد"  ):
        counter_positive_neutral+=1

print('counter_positive_neutral',counter_positive_neutral)

# .................
counter_positive_Negative=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]=="خبر إيجابي"  and row[second_annonter]==" خبر سلبي"  ):
        counter_positive_Negative+=1

print('counter_positive_Negative',counter_positive_Negative)

counter_Negative_positive=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]==" خبر سلبي"  and row[second_annonter]=="خبر إيجابي"   ):
        counter_Negative_positive+=1

print('counter_Negative_positive',counter_Negative_positive)

# .................

counter_Negative_neutral=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]==" خبر سلبي"  and row[second_annonter]=="خبر محايد"  ):
        counter_Negative_neutral+=1

print('counter_Negative_neutral',counter_Negative_neutral)


counter_neutral_Negative=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]=="خبر محايد"  and row[second_annonter]== " خبر سلبي"  ):
        counter_neutral_Negative+=1

print('counter_neutral_Negative',counter_neutral_Negative)

pa=(counterneutral+counterPoisitive+counterNegative)/500
total1=counterPoisitive+counter_Negative_positive+counter_neutral_positive
total2=counterNegative+counter_positive_Negative+counter_neutral_Negative
total3=counterneutral+counter_positive_neutral+counter_Negative_neutral

total1_column=counterPoisitive+counter_positive_Negative+counter_positive_neutral
total2_column=counterNegative+counter_Negative_positive+counter_Negative_neutral
total3_column=counterneutral+counter_neutral_positive+counter_neutral_Negative



pe=(total1/500*total1_column/500)+(total2/500*total2_column/500)+(total3/500*total3_column/500)

resultkappa=(pa-pe)/(1-pe)
print('تقييم الخبر')
print(' المنصف الاول(احمد) :المصنف الثاني (يارا ) ', resultkappa)

# import pandas lib as pd
import pandas as pd

# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('first-third.xlsx')

print(dataframe1)

first_annonter='احمد'

second_annonter='احمد قطب'

counterneutral=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]=="خبر محايد"  and row[second_annonter]=="خبر محايد"  ):
        counterneutral+=1


print('counterneutral', counterneutral)

counterPoisitive=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]=="خبر إيجابي"  and row[second_annonter]=="خبر إيجابي"  ):
        counterPoisitive+=1
 
print('counterPoisitive', counterPoisitive)


counterNegative=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]==" خبر سلبي"  and row[second_annonter]==" خبر سلبي"  ):
        counterNegative+=1

print('counterNegative',counterNegative)



# .................

counter_neutral_positive=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]=="خبر محايد"  and row[second_annonter]=="خبر إيجابي"  ):
        counter_neutral_positive+=1

print('counter_neutral_positive',counter_neutral_positive)


counter_positive_neutral=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]=="خبر إيجابي"  and row[second_annonter]=="خبر محايد"  ):
        counter_positive_neutral+=1

print('counter_positive_neutral',counter_positive_neutral)

# .................
counter_positive_Negative=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]=="خبر إيجابي"  and row[second_annonter]==" خبر سلبي"  ):
        counter_positive_Negative+=1

print('counter_positive_Negative',counter_positive_Negative)

counter_Negative_positive=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]==" خبر سلبي"  and row[second_annonter]=="خبر محايد"  ):
        counter_Negative_positive+=1

print('counter_Negative_positive',counter_Negative_positive)

# .................

counter_Negative_neutral=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]==" خبر سلبي"  and row[second_annonter]=="خبر محايد"  ):
        counter_Negative_neutral+=1

print('counter_Negative_neutral',counter_Negative_neutral)


counter_neutral_Negative=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]=="خبر محايد"  and row[second_annonter]== " خبر سلبي"  ):
        counter_neutral_Negative+=1

print('counter_neutral_Negative',counter_neutral_Negative)

pa=(counterneutral+counterPoisitive+counterNegative)/500
total1=counterPoisitive+counter_Negative_positive+counter_neutral_positive
total2=counterNegative+counter_positive_Negative+counter_Negative_neutral
total3=counterneutral+counter_positive_neutral+counter_Negative_neutral

total1_column=counterPoisitive+counter_positive_Negative+counter_positive_neutral
total2_column=counterNegative+counter_Negative_positive+counter_Negative_neutral
total3_column=counterneutral+counter_neutral_positive+counter_neutral_Negative



pe=(total1/500*total1_column/500)+(total2/500*total2_column/500)+(total3/500*total3_column/500)

resultkappa=(pa-pe)/(1-pe)
print('تقييم الخبر')
print(' المنصف الاول(احمد) :المصنف الثالث(احمد قطب ) ', resultkappa)

# import pandas lib as pd
import pandas as pd

# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('second-third.xlsx')

print(dataframe1)

first_annonter='يارا'

second_annonter='احمد قطب'

counterneutral=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]=="خبر محايد"  and row[second_annonter]=="خبر محايد"  ):
        counterneutral+=1


print('counterneutral', counterneutral)

counterPoisitive=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]=="خبر إيجابي"  and row[second_annonter]=="خبر إيجابي"  ):
        counterPoisitive+=1
 
print('counterPoisitive', counterPoisitive)


counterNegative=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]==" خبر سلبي"  and row[second_annonter]==" خبر سلبي"  ):
        counterNegative+=1

print('counterNegative',counterNegative)



# .................

counter_neutral_positive=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]=="خبر محايد"  and row[second_annonter]=="خبر إيجابي"  ):
        counter_neutral_positive+=1

print('counter_neutral_positive',counter_neutral_positive)


counter_positive_neutral=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]=="خبر إيجابي"  and row[second_annonter]=="خبر محايد"  ):
        counter_positive_neutral+=1

print('counter_positive_neutral',counter_positive_neutral)

# .................
counter_positive_Negative=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]=="خبر إيجابي"  and row[second_annonter]==" خبر سلبي"  ):
        counter_positive_Negative+=1

print('counter_positive_Negative',counter_positive_Negative)

counter_Negative_positive=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]==" خبر سلبي"   and row[second_annonter]=="خبر إيجابي"  ):
        counter_Negative_positive+=1

print('counter_Negative_positive',counter_Negative_positive)

# .................

counter_Negative_neutral=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]==" خبر سلبي"  and row[second_annonter]=="خبر محايد"  ):
        counter_Negative_neutral+=1

print('counter_Negative_neutral',counter_Negative_neutral)


counter_neutral_Negative=0
for index, row in dataframe1.iterrows():
    if (row[first_annonter]=="خبر محايد"  and row[second_annonter]== " خبر سلبي"  ):
        counter_neutral_Negative+=1

print('counter_neutral_Negative',counter_neutral_Negative)

pa=(counterneutral+counterPoisitive+counterNegative)/500
total1=counterPoisitive+counter_Negative_positive+counter_neutral_positive
total2=counterNegative+counter_positive_Negative+counter_neutral_Negative
total3=counterneutral+counter_positive_neutral+counter_Negative_neutral

total1_column=counterPoisitive+counter_positive_Negative+counter_positive_neutral
total2_column=counterNegative+counter_Negative_positive+counter_Negative_neutral
total3_column=counterneutral+counter_neutral_positive+counter_neutral_Negative



pe=(total1/500*total1_column/500)+(total2/500*total2_column/500)+(total3/500*total3_column/500)

resultkappa=(pa-pe)/(1-pe)

print('تقييم الخبر')
print(' المنصف الاول(يارا) :المصنف الثالث(احمد قطب ) ', resultkappa)