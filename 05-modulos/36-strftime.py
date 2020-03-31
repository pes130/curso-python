from time import gmtime,localtime,strftime

print('Formato %d/%m/%y')
f_corto=strftime('%d/%m/%y',localtime())
print('Formato %d/%m/%y %H:%M:%S:',f_corto)
fh_corto=strftime('%d/%m/%y %H:%M:%S',localtime())
print('Fecha y Hora (%Y-%m-%d):',fh_corto)
f_sql=strftime('%Y-%m-%d',localtime())
print('Fecha formato SQL (%Y-%m-%d):',f_sql)
fh_sql=strftime('%Y-%m-%d %H:%M:%S',localtime())
print('Fecha y Hora formato SQL (%Y-%m-%d %H:%M:%S):',fh_sql)