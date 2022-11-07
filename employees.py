import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")


st.title('Employees app')

DATA_URL = ('Employees.csv')


@st.cache

# Carga de datos

def load_data(nrows,val):
    if val == 1:
      data = pd.read_csv(DATA_URL)
    else:
      data = pd.read_csv(DATA_URL, nrows=nrows)
    return data


# Filtro por ID de Empleado

def filter_data_by_employee(employee_id):
    filtered_data_employee = data[data['Employee_ID'].str.upper() == employee_id]
    return filtered_data_employee

# Filtro por Hometown

def filter_data_by_hometown(hometownF):
    filtered_data_hometown = data[data['Hometown'].str.upper() == hometownF]
    return filtered_data_hometown

# Filtro por Unit

def filter_data_by_unit(UnitF):
    filtered_data_unit = data[data['Unit'].str.upper() == UnitF]
    return filtered_data_unit

# Filtro por educacion Level botón

def filter_data_by_education(educacionLevel):
    filtered_data_educationL = data[data['Education_Level'] == educacionLevel]
    return filtered_data_educationL

# Filtro por hometown botón

def filter_data_by_hometownB(HometownB):
    filtered_data_hometownB = data[data['Hometown'] == HometownB]
    return filtered_data_hometownB

# Filtro por unidad botón

def filter_data_by_unitB(UnitB):
    filtered_data_unitB = data[data['Unit'] == UnitB]
    return filtered_data_unitB


# ==============================================================================
# Carga de datos
# ==============================================================================

data_load_state = st.text('Loading cicle Employees data...')
data = load_data(500,1)
data_load_state.text("Done! (using st.cache)")

if st.sidebar.checkbox('Mostrar todos los empleados'):
    st.subheader('Todos los empleados')
    data = load_data(1,1)
    st.write(data)

# ==============================================================================
# Filtro por ID de Empleado
# ==============================================================================
employee_id = st.sidebar.text_input('ID Empleado :')
btnEmployee = st.sidebar.button('Buscar empleado')

if (btnEmployee):
   data_employee = filter_data_by_employee(employee_id.upper())
   count_row = data_employee.shape[0]  # Gives number of rows
   st.write(f"Total empleados mostrados : {count_row}")
   st.write(data_employee)

# ==============================================================================
# Filtro por Hometown
# ==============================================================================

hometownF = st.sidebar.text_input('Ciudad :')
btnHometown = st.sidebar.button('Buscar por ciudad')
if (btnHometown):
   data_Hometown = filter_data_by_hometown(hometownF.upper())
   count_row = data_Hometown.shape[0]  # Gives number of rows
   st.write(f"Total empleados mostrados : {count_row}")
   st.write(data_Hometown)

# ==============================================================================
# Filtro por Unit
# ==============================================================================

UnitF = st.sidebar.text_input('Unidad :')
btnUnit = st.sidebar.button('Buscar por unidad')
if (btnUnit):
   data_Unit = filter_data_by_unit(UnitF.upper())
   count_row = data_Unit.shape[0]  # Gives number of rows
   st.write(f"Total empleados mostrados : {count_row}")
   st.write(data_Unit)

# ==============================================================================
# Selectbox por Education_Level
# ==============================================================================

selected_education = st.sidebar.selectbox("Seleccionar nivel de educación : ", data['Education_Level'].drop_duplicates().sort_values())
btnFilterbyEducation = st.sidebar.button('Filtrar por nivel de educación ')

if (btnFilterbyEducation):
   filterbyeducation = filter_data_by_education(selected_education)
   count_row = filterbyeducation.shape[0]  # Gives number of rows
   st.write(f"Total empleados mostrados : {count_row}")
   st.write(filterbyeducation)

# ==============================================================================
#  Selectbox por Hometown
# ==============================================================================

selected_hometown = st.sidebar.selectbox("Seleccionar ciudad : ", data['Hometown'].drop_duplicates().sort_values())
btnFilterbyHometown = st.sidebar.button('Filtrar por ciudad ')

if (btnFilterbyHometown):
   filterbyhometown = filter_data_by_hometownB(selected_hometown)
   count_row = filterbyhometown.shape[0]  # Gives number of rows
   st.write(f"Total empleados mostrados : {count_row}")
   st.write(filterbyhometown)

# ==============================================================================
# Selectbox por Unit
# ==============================================================================

selected_unit = st.sidebar.selectbox("Seleccionar unidad : ", data['Unit'].drop_duplicates().sort_values())
btnFilterbyUnidad = st.sidebar.button('Filtrar por unidad ')

if (btnFilterbyUnidad):
   filterbyunit = filter_data_by_unitB(selected_unit)
   count_row = filterbyunit.shape[0]  # Gives number of rows
   st.write(f"Total empleados mostrados : {count_row}")

   st.write(filterbyunit)

# ==============================================================================
# Histograma de los empleados agrupados por edad. 
# ==============================================================================

fig, ax = plt.subplots()
ax.hist(data.Age)
plt.xlabel('Rango de edad')
plt.ylabel('Número de empleados')
st.header("Histograma por rango de edad")
st.pyplot(fig)
st.markdown("___")


# ==============================================================================
# Gráfica de frecuencias para las unidades funcionales
# ==============================================================================

employees_by_unit = data[['Employee_ID','Unit']].groupby('Unit').count()
sns.set(font_scale = 3)
fig1 = plt.figure(figsize=(16,8))
plt.style.use("seaborn")
palette = sns.color_palette("inferno", 7)
plt.bar(employees_by_unit.index,employees_by_unit['Employee_ID'], color=palette)
plt.xticks(rotation = 90)
plt.title("Número de empleados por unidad", color="darkblue", fontsize=25 )
plt.xlabel('Unidad')
plt.ylabel('Número de empleados')

st.header("Gráfica de frecuencias para las unidades funcionales")
st.pyplot(fig1)
st.markdown("___")


# ==============================================================================
# Ciudades con mayor índice de decersión
# ==============================================================================

fig2 = plt.figure(figsize=(16,8))
sns.boxplot(x='Hometown', y="Attrition_rate", data=data,palette="Blues");
sns.set(font_scale = 2)
plt.xlabel('Ciudad')
plt.ylabel('Índice de deserción')

st.header("Índice de deserción por ciudad")
st.pyplot(fig2)
st.markdown("___")


# ==============================================================================
# Gráfico edad y la tasa de deserción 
# ==============================================================================

fig3, ax = plt.subplots(1, 1, figsize=(16,8))
ax.scatter(x=data.Age, y=data.Attrition_rate, alpha= 0.8)
ax.set_xlabel('Edad')
ax.set_ylabel('Tasa de deserción');


st.header("Edad y tasa de deserción")
st.pyplot(fig3)
st.markdown("___")

# ==============================================================================
# Gráfico tiempo de servicio y la tasa de deserción 
# ==============================================================================

fig4, ax = plt.subplots(1, 1, figsize=(16,8))
ax.scatter(x = data.Time_of_service, y = data.Attrition_rate, alpha= 0.8)
ax.set_xlabel('Tiempo de servicio')
ax.set_ylabel('Tasa de deserción');


st.header("Tiempo de servicio y tasa de deserción")
st.pyplot(fig4)
st.markdown("___")


