import numpy as np #imports numpy and names as np
import pandas as pd #imports pandas and names as pd
import matplotlib.pyplot as plt #imports matplot and names as plt

def combine_rows(data_frame, row_labels, name, drop=True): #function to combine rows, takes fram, labels, name as parameters, sets drop=T
    """
    Add rows together, drop them, return a new data frame
    """
    series = data_frame.loc[row_labels[0]]
    for row_label in row_labels[1:]:
        series = series + data_frame.loc[row_label]
    series.name = name
    if drop:
        for row_label in row_labels:
            data_frame = data_frame.drop(row_label)
    data_frame = data_frame.append(series)
    return data_frame

x=pd.read_excel('2016_11_30/monthly_by_product.xls','Sheet1')
pd.options.display.width=None
z=x[x.columns[::2]]
z.fillna('')
rows = []
headings = []
for row_index in range(z.shape[0]):
    for multi_index in range(len(z.index.labels)):
        label_index = z.index.labels[multi_index][row_index]
        if label_index != -1:
            if np.isnan(z.values[row_index]).sum() == 0:
                heading = z.index.levels[multi_index][label_index]
                if heading.startswith('Net') or heading.startswith('Total') or heading.startswith('Gross'):
                    continue
                #print z.index.levels[multi_index][label_index], row_index
                headings.append(heading)
                rows.append(row_index)

x = pd.DataFrame(z.values[rows,:-1],columns=z.columns[:-1],index=headings)

print(x)

x = combine_rows(x, ['Sidekiq MiniPCIe Sales', 'Sidekiq Sales - Other'], 'Sidekiq MiniPCIe Sales')
x = combine_rows(x, x.index, 'Total', drop=False)

# get rid of "Sales"
new_headings = []
for heading in x.index:
    new_heading = heading.split(' Sales')[0]
    new_headings.append(new_heading)
x.index = new_headings

report_description = [
 ('Sidekiq MiniPCIe',['Sidekiq MiniPCIe']),
 ('Sidekiq M.2',['Sidekiq M.2']),
 ('Matchstiq',['Matchstiq S1', 'Matchstiq S10', 'Matchstiq SX0 Software', 'Matchstiq Z1', 'Matchstiq']),
 ('Maveriq',['Maveriq']),
 ('Quadratiq',['Quadratiq']),
 ('Skylight',['Skylight']),
 ('Total',['Total']),
]
report_set = set()
for new_row_label, row_labels_to_combine in report_description:
    x = combine_rows(x, row_labels_to_combine, new_row_label)
    report_set.add(new_row_label)

for row_label in x.index:
    if row_label not in report_set:
        x = x.drop(row_label)

print(x)
x[:-1].T.plot.bar(stacked=True)  # use [:-1] to omit "Total" column from stacked bar chart
plt.grid()
savefig.format('dec15_through_nov16_sales.png')
x.to_excel('dec15_through_nov16_sales.xls')

