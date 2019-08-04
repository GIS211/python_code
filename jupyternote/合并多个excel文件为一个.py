
#%%
import xlrd
import xlsxwriter
import os


#%%
#要融合的文件所在目录
files_path = r'C:\Users\lenovo\Desktop\采集表'

#获取目录下的文件名
File_Name_List = os.walk(files_path)
for root,dirs,source_xlsx in File_Name_List:
    print(len(source_xlsx))

#文件绝对路径
files_dirname = []
for files_dir in source_xlsx:
    files_dirname.append(files_path + '\\' + files_dir)
                         
print(files_dirname)


#%%
#输出excel的路径
target_xlsx = r'C:\Users\lenovo\Desktop\merge.xlsx'

numx = -1
sheets_1 = []

#创建一个[38,20]的数组，因为sheet有20个，文件有38个
for i in range(38):
    sheets_1.append([])

    for j in range(20):
        sheets_1[i].append(0)

#读取所有文件的sheet并保存到二维数组中
for i in files_dirname:
    print(len(files_dirname))
    wb = xlrd.open_workbook(i)
    numx = numx + 1
    numy = -1
    for sheet in wb.sheets():
        numy = numy + 1
        #print(numx,numy)
        sheets_1[numx][numy] = sheet
            
            
print('done')


#%%
print(numx,numy)


#%%
workbook = xlsxwriter.Workbook(target_xlsx)
worksheet = []
font = workbook.add_format({'font_size':14})

#先循环sheet，再循环文件实现拼接，再循环行列获取数据
for sheet_num in range(numy):
    data = []
    worksheet=workbook.add_worksheet()
    for file_num in range(numx+1):
        sheet = sheets_1[file_num][sheet_num]
        for rownum in range(sheet.nrows):
            data.append(sheet.row_values(rownum))
  #每循环完一个sheet则输出一个sheet          
    for i in range(len(data)):
        for j in range(len(data[i])):
            worksheet.write(i,j,data[i][j],font)

workbook.close()
print('all done')


#%%
print(len(worksheet))


