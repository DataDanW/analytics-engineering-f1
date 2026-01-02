
With so many tables, it can be difficult to visualise the entire schema. This is where database diagrams come in. 

DBDiagram.io is a free tool to visualise your tables. It used a dbml text editor to type out your tables and column names. However, again with 14 tables this takes time. We can save us some time by pasting our SQL script of each table and column header into chatgpt. In the required format and here's what's generated:
<img width="1460" height="1444" alt="formula_1_diagram" src="https://github.com/user-attachments/assets/c7781399-4bee-4f04-aa22-e93e8a3448ad" />

This makes it really useful for then identifying and assigning our primary and foreign keys. 
You can do this by adding [Primary Key] and [Foreign Key] next to the relevant fields and you'll get something like this:


You'll notice that our datatypes are assigned as varchar here. You can update these if you know them or we can go ahead and do that after we asign them in our staging layer. 
