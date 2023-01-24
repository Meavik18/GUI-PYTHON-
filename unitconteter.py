import tkinter as tk
import tkinter.font  as font
from functools import partial
from tkinter import StringVar, messagebox
from  tkinter import ttk

#from django.forms import SelectDateWidget


window =tk.Tk()
window.geometry('500x600')
window.title('UNIT CONVETER')
window.configure(bg='peach puff2')


#create font
font1=font.Font(family='helvetica',size='30')
font2=font.Font(family='helvetica',size='10')
font3=font.Font(family='helvetica',size='20')

#textvariable

number_from=StringVar()
#all the funs



#frmfuntion
def fromfunc(event):
    global result_from
    result_from = event.widget.get()
    
    
#to function

def tofunc(event):
   global result_to
   result_to = event.widget.get()
   
#the ans func
def answer(n1):
    num1=n1.get()
    try:
        number1 = int(num1)
    except:
        messagebox.showerror('Error','Term not registered')
    if result_from == 'RUPPEE' and result_to=='RUPPEE':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'RUPPEE' and result_to=='POUND':
        calculate = number1*0.010
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'RUPPEE' and result_to=='EURO':
        calculate = number1*0.012
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif  result_from == 'POUND' and result_to=='RUPPEE':
        calculate = number1 * 98.44
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'POUND' and result_to=='POUND':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'POUND' and result_to=='EURO':
        calculate = number1 *1.13
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'EURO' and result_to=='RUPPEE':
        calculate = number1* 86.94
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'EURO' and result_to=='POUND':
        calculate = number1*0.88
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'EURO' and result_to=='EURO':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'FAHRENHEIT' and result_to=='FAHRENHEIT':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'FAHRENHEIT' and result_to=='CELSIUS':
        calculate = (number1 -32)*(5/9)
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'FAHRENHEIT' and result_to=='KELVIN':
        calculate = (number1 -32)*(5/9)+273.15
        result.cget('text')
        result.configure(text=(calculate,result_to))
    
    elif result_from == 'CELSIUS' and result_to=='FAHRENHEIT':
        calculate = number1 *(9/5) +32
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'CELSIUS' and result_to=='CELSIUS':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'CELSIUS' and result_to=='KELVIN':
        calculate = number1 +273.15
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'KELVIN' and result_to=='FAHRENHEIT':
        calculate = (number1 -273.15) *(9/5) +32
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'KELVIN' and result_to=='CELSIUS':
        calculate = number1-273.15
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'KELVIN' and result_to=='KELVIN':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'HOUR' and result_to=='HOUR':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'HOUR' and result_to=='MINIUTE':
        calculate = number1 *60
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'HOUR' and result_to=='SECOND':
        calculate = number1 *3600
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'MINIUTE' and result_to=='HOUR':
        calculate = number1 /60
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'MINIUTE' and result_to=='MINIUTE':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'MINIUTE' and result_to=='SECOND':
        calculate = number1 *60
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'SECOND' and result_to=='HOUR':
        calculate = number1 /3600
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'SECOND' and result_to=='MINIUTE':
        calculate = number1 /60
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'SECOND' and result_to=='SECOND':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'MILIGRAMS' and result_to=='MILIGRAMS':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'MILIGRAMS' and result_to=='CENTIGRAMS':
        calculate = number1 /10
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'MILIGRAMS' and result_to=='GRAMS':
        calculate = number1 /1000
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'MILIGRAMS' and result_to=='DECIGRAMS':
        calculate = number1 /100
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'MILIGRAMS' and result_to=='KILOGRAMS':
        calculate = number1 /1000000
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'CENTIGRAMS' and result_to=='MILIGRAMS':
        calculate = number1 *10
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'CENTIGRAMS' and result_to=='CENTIGRAMS':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'CENTIGRAMS' and result_to=='GRAMS':
        calculate = number1 /100
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'CENTIGRAMS' and result_to=='DECIGRAMS':
        calculate = number1 /10
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'CENTIGRAMS' and result_to=='KILOGRAMS':
        calculate = number1 /100000
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'GRAMS' and result_to=='MILIGRAMS':
        calculate = number1 *1000
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'GRAMS' and result_to=='CENTIGRAMS':
        calculate = number1 *100
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'GRAMS' and result_to=='GRAMS':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'GRAMS' and result_to=='DECIGRAMS':
        calculate = number1 *10
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'GRAMS' and result_to=='KILOGRAMS':
        calculate = number1 /1000
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'DECIGRAMS' and result_to=='MILIGRAMS':
        calculate = number1 *100
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'DECIGRAMS' and result_to=='CENTIGRAMS':
        calculate = number1 *10
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'DECIGRAMS' and result_to=='GRAMS':
        calculate = number1 /10
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'DECIGRAMS' and result_to=='DECIGRAMS':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'DECIGRAMS' and result_to=='KILOGRAMS':
        calculate = number1 /10000
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'KILOGRAMS' and result_to=='MILIGRAMS':
        calculate = number1 *1000000
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'KILOGRAMS' and result_to=='CENIGRAMS':
        calculate = number1 *100000
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'KILOGRAMS' and result_to=='GRAMS':
        calculate = number1 *1000
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'KILOGRAMS' and result_to=='DECIGRAMS':
        calculate = number1 *10000
        result.cget('text')
        result.configure(text=(calculate,result_to))
    elif result_from == 'KILOGRAMS' and result_to=='KILOGRAMS':
        calculate = number1 
        result.cget('text')
        result.configure(text=(calculate,result_to))
    
    
       
#all the selectedfuntion
def selected(event):
    unit= event.widget.get()
    if unit =='Currency':
        fromdd['values']=('RUPPEE',
                          'POUND',
                          'EURO')
        todd['values']=('RUPPEE',
                        'POUND',
                        'EURO')
    elif unit =='Temperature':
        fromdd['values']= ('FAHRENHEIT',
                           'CELSIUS',
                           'KELVIN')
        todd['values']=('FAHRENHEIT',
                        'CELSIUS',
                        'KELVIN')
    elif unit =='Time':
        fromdd['values']= ('HOUR',
                           'MINIUTE',
                           'SECOND')
        todd['values']=('HOUR',
                        'MINIUTE',
                        'SECOND')
    elif unit =='Weight':
        fromdd['values']= ('MILIGRAMS',
                           'CENTIGRAMS',
                           'GRAMS',
                           'DECIGRAMS',
                           'KILOGRAMS')
        todd['values']=('MILIGRAMS',
                           'CENTIGRAMS',
                           'GRAMS',
                           'DECIGRAMS',
                           'KILOGRAMS')

#create the unit coveter table



main = tk.Label(window,text='UNIT CONVETER', bg='peach puff2')




main['font'] =font1
main.place(relx='0.48',rely='0.1',anchor='center')
#CREATING UNIT LABEL
unit=tk.Label(window,text='Unit--:',bg='peach puff2')
unit['font']=font2
unit.place(relx='0.25',rely='0.28')
label_unit = tk.Label(window,text='Unit--:', bg='peach puff2')
n=StringVar()
unitdd=ttk.Combobox(window,width='35', textvariable=n)

#values
unitdd['values'] =('Currency',
                    'Temperature',
                    'Time',
                    'Weight')
unitdd.place(relx='0.57',rely='0.3',anchor ='center')

label_from=tk.Label(window)
unitdd.current()
unitdd.bind('<<ComboboxSelected>>',selected)

#creating frm label

label_from=tk.Label(window,text='From--:',bg='peach puff2')
label_from['font']=font2
label_from.place(relx='0.238',rely='0.37')
#creating thr fromdd

f=StringVar()
fromdd=ttk.Combobox(window,width='35',textvariable=f)

fromdd.place(relx='0.57',rely='0.39',anchor ='center')
fromdd.current()
fromdd.bind('<<ComboboxSelected>>',fromfunc)
#creating the NUM FRM
num_from=tk.Entry(window,width=10,textvariable=number_from)
num_from.place(relx='0.82',rely='0.37')
answer =partial(answer,num_from)
#creating to the label
to = tk.Label(window,text='To--:', bg='peach puff2')
to['font']=font2
to.place(relx='0.268',rely='0.45')
#creating to drop down
t=StringVar()
todd=ttk.Combobox(window,width=35,textvariable=t)
todd.place(relx='0.57',rely='0.47',anchor='center')
todd.current()
todd.bind('<<ComboboxSelected>>',tofunc)


#creating result level
result=tk.Label(window,text='',bg='white',width=23)
result['font']=font3
result.place(relx='0.21',rely='0.6')
#creating the get ans button
get_answer=tk.Button(window,text='GET ANSWER',bg='cyan2',command=answer)
get_answer['font']=font2
get_answer.place(relx='0.46',rely='0.7')

#creating art label 
art=tk.Label(window,text='GUI PYTHON APPLICATION',bg='peach puff2',fg='blue')
art['font']=font3
art.place(relx='0.21',rely='0.9')



window.mainloop()