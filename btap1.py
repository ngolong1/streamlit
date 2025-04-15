import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Ngô Văn Long - 2221050187
# Nguyễn văn Sửa -2221050020
# Trần Anh Duẩn - 2221050541
# Đọc dữ liệu
movies_data = pd.read_csv("https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/Dataset%20for%20Practice/movies.csv")

# Hiển thị dữ liệu mẫu
st.write("Dữ liệu có dạng:")
st.dataframe(movies_data.head())

# Tiêu đề
st.write("🎬 Average Movie Budget, Grouped by Genre")

# Tính toán ngân sách trung bình theo thể loại
avg_budget = movies_data.groupby('genre')['budget'].mean().round()
avg_budget = avg_budget.reset_index()

# Vẽ biểu đồ
fig = plt.figure(figsize=(19, 10))
plt.bar(avg_budget['genre'], avg_budget['budget'], color='maroon')
plt.xlabel('Genre')
plt.ylabel('Budget')
plt.title('Average Movie Budget by Genre')

# Hiển thị biểu đồ trong Streamlit
st.pyplot(fig)
